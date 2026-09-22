"""classify_write_candidate -- telling a filter-shaped POST from a real write.

The write-guard blocks every POST/PUT/PATCH/DELETE by default, which is the
right default -- but on one real target that also blocked two endpoints that
read like list/search calls (`.../resources`, `.../places`), because they use
a POST body to carry a filter too complex for a GET query string.

This classifier is deliberately conservative: PUT/PATCH/DELETE and any path
naming an explicit action are never reclassified, whatever their body looks
like. Only a plain POST whose body reads as a filter/pagination object, with
no competing write-shaped field, is called a likely read -- and even then,
only `browser.classify_ambiguous_writes` opting in changes live behaviour.
"""

from __future__ import annotations

from qagen.browser.session import classify_write_candidate


class TestMethodAlwaysWins:
    """PUT/PATCH/DELETE are never reclassified, regardless of body."""

    def test_put_is_always_a_write(self):
        label, _ = classify_write_candidate("PUT", "/api/dms/x/screens/1", None)
        assert label == "likely_write"

    def test_patch_is_always_a_write(self):
        label, _ = classify_write_candidate("PATCH", "/api/x/y", '{"page": 1}')
        assert label == "likely_write"

    def test_delete_is_always_a_write_even_with_a_filter_shaped_body(self):
        """The one method where a body would be most likely to mislead."""
        label, _ = classify_write_candidate(
            "DELETE", "/api/x/y", '{"filter": {}, "sort": "name"}'
        )
        assert label == "likely_write"


class TestActionWordsInThePathAlwaysWin:
    """A path naming an action stays a write however its body looks --
    this is what stops a write endpoint being fooled by a coincidentally
    filter-shaped body."""

    def test_create_in_the_path(self):
        label, _ = classify_write_candidate("POST", "/api/x/create", '{"page": 1}')
        assert label == "likely_write"

    def test_chat_start_in_the_path(self):
        label, _ = classify_write_candidate(
            "POST", "/api/ums/x/x/chat/start", '{"page": 1, "keyword": "hi"}'
        )
        assert label == "likely_write"

    def test_screens_wall_in_the_path(self):
        label, _ = classify_write_candidate("POST", "/api/dms/x/x/screens/wall", None)
        assert label == "likely_write"

    def test_signout_in_the_path(self):
        label, _ = classify_write_candidate("POST", "/api/auth/signout", None)
        assert label == "likely_write"


class TestBodyShapeForPlainPost:
    """The actual rescue: a plain POST with a filter/pagination body."""

    def test_pagination_and_filter_keys_read_as_a_list_call(self):
        label, reason = classify_write_candidate(
            "POST", "/api/cms/x/x/resources", '{"page": 1, "pageSize": 20, "keyword": ""}'
        )
        assert label == "likely_read"
        assert "page" in reason

    def test_camelcase_and_snake_case_filter_keys_both_match(self):
        label, _ = classify_write_candidate(
            "POST", "/api/ums/x/places", '{"sortBy": "name", "page_size": 10}'
        )
        assert label == "likely_read"

    def test_a_write_shaped_field_outweighs_a_filter_shaped_one(self):
        """A request can carry pagination AND a field to persist in the same
        payload -- the write signal must win."""
        label, reason = classify_write_candidate(
            "POST", "/api/ums/x/places", '{"page": 1, "name": "New Place"}'
        )
        assert label == "likely_write"
        assert "name" in reason

    def test_a_pure_write_body_is_a_write(self):
        label, _ = classify_write_candidate(
            "POST", "/api/ums/x/places", '{"name": "New Place", "email": "a@b.com"}'
        )
        assert label == "likely_write"

    def test_empty_body_is_unclear_not_a_read(self):
        """No signal either way -- must not default to allowing it through."""
        label, _ = classify_write_candidate("POST", "/api/misc/x", None)
        assert label == "unclear"

    def test_empty_string_body_is_unclear(self):
        label, _ = classify_write_candidate("POST", "/api/misc/x", "")
        assert label == "unclear"

    def test_non_json_body_is_unclear(self):
        label, _ = classify_write_candidate("POST", "/api/misc/x", "not json at all")
        assert label == "unclear"

    def test_json_array_body_is_unclear(self):
        """A JSON body that parses but is not an object -- nothing to inspect
        keys on."""
        label, _ = classify_write_candidate("POST", "/api/misc/x", "[1, 2, 3]")
        assert label == "unclear"

    def test_body_with_no_recognised_keys_is_unclear(self):
        label, _ = classify_write_candidate(
            "POST", "/api/misc/x", '{"foo": "bar", "baz": 1}'
        )
        assert label == "unclear"


class TestRealEndpointsFromTheActualCrawl:
    """The exact evidence this classifier was built from."""

    def test_resources_call_with_a_filter_body_is_a_read(self):
        label, _ = classify_write_candidate(
            "POST", "/api/cms/E601D846/8AD89E5C/resources",
            '{"page": 0, "pageSize": 50, "keyword": "", "sort": "name"}',
        )
        assert label == "likely_read"

    def test_places_call_with_a_filter_body_is_a_read(self):
        label, _ = classify_write_candidate(
            "POST", "/api/ums/E601D846/places", '{"filters": {}, "limit": 100}'
        )
        assert label == "likely_read"

    def test_screens_edit_stays_a_write(self):
        label, _ = classify_write_candidate(
            "PUT", "/api/dms/E601D846/8AD89E5C/screens/3a-a0-d9-b3-43-dd", None
        )
        assert label == "likely_write"

    def test_organizations_update_stays_a_write(self):
        label, _ = classify_write_candidate(
            "PUT", "/api/ums/E601D846/8AD89E5C/organizations/E601D846", None
        )
        assert label == "likely_write"

    def test_cases_create_stays_a_write(self):
        label, _ = classify_write_candidate("POST", "/api/ums/E601D846/cases", None)
        assert label == "likely_write"


class TestQueryStringPagination:
    """Some APIs put the filter in the body and the pagination in the query
    string -- found live on five endpoints (screens/search, contents/search,
    playlist/search, programs/search, channels/search), each with a body of
    just {"advancedSearch": []} and the real signal (orderBy, order, start,
    rowsPerPage) sitting in the URL. Confirmed by inspecting the real
    response: each returned a populated list of real entities at status 200.
    """

    def test_the_exact_screens_search_call_is_a_read(self):
        """Two independent signals agree here -- the body's own
        "advancedSearch" key and the query string's pagination -- either one
        on its own would be enough; both firing is the strongest case."""
        label, _ = classify_write_candidate(
            "POST",
            "/api/dms/2086D82A/71BDE223/screens/search",
            '{"advancedSearch":[]}',
            query_string="orderBy=created_time&order=desc&tz=Asia%2FCalcutta&all=false&start=0&rowsPerPage=50",
        )
        assert label == "likely_read"

    def test_the_exact_channels_search_call_is_a_read(self):
        label, _ = classify_write_candidate(
            "POST",
            "/api/cms/2086D82A/71BDE223/channels/search",
            '{"advancedSearch":[]}',
            query_string="orderBy=updated_time&order=desc&start=0&rowsPerPage=50",
        )
        assert label == "likely_read"

    def test_query_string_alone_is_enough_without_a_helpful_body(self):
        """The body here has no key from _READ_BODY_KEYS at all -- only the
        query string carries the signal."""
        label, reason = classify_write_candidate(
            "POST", "/api/x/y", '{"unrelatedKey": true}', query_string="start=0&rowsPerPage=50"
        )
        assert label == "likely_read"
        assert "query string" in reason

    def test_a_mutation_word_in_the_path_still_wins_over_query_pagination(self):
        label, _ = classify_write_candidate(
            "POST", "/api/x/create", '{"advancedSearch":[]}', query_string="start=0&rowsPerPage=50"
        )
        assert label == "likely_write"

    def test_a_write_shaped_body_still_wins_over_query_pagination(self):
        label, _ = classify_write_candidate(
            "POST", "/api/x/y", '{"name": "New Thing"}', query_string="start=0&rowsPerPage=50"
        )
        assert label == "likely_write"

    def test_no_query_string_falls_through_as_before(self):
        """Passing no query_string at all must not change existing callers'
        behaviour -- this is an additive signal, not a required one."""
        label, _ = classify_write_candidate("POST", "/api/x/y", '{"advancedSearch":[]}')
        assert label == "likely_read"  # advancedsearch is in _READ_BODY_KEYS


class TestExplicitSearchPathWord:
    """A path unambiguously naming a read action ("/search") is a fallback
    signal when neither the body nor the query string say anything -- but it
    never overrides a write signal."""

    def test_bare_search_path_with_no_other_signal_is_a_read(self):
        label, reason = classify_write_candidate("POST", "/api/x/search", None)
        assert label == "likely_read"
        assert "search" in reason

    def test_list_and_query_path_words_also_count(self):
        assert classify_write_candidate("POST", "/api/x/list", None)[0] == "likely_read"
        assert classify_write_candidate("POST", "/api/x/query", None)[0] == "likely_read"

    def test_a_write_shaped_body_still_wins_over_a_search_path(self):
        label, _ = classify_write_candidate(
            "POST", "/api/x/search", '{"name": "New Thing"}'
        )
        assert label == "likely_write"

    def test_an_unrelated_word_containing_search_does_not_match(self):
        """"researched" or similar must not accidentally trip the /search
        path check -- it requires the literal path segment."""
        label, _ = classify_write_candidate("POST", "/api/researched/x", None)
        assert label == "unclear"
