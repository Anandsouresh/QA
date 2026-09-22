"""Session._write_guard -- the live decision, not just the classifier.

Exercises the actual guard method with fake Route/Request objects (no real
network, no browser) so the wiring between config, the deterministic
allowlist, and the opt-in classifier is covered end to end.
"""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import AsyncMock

import pytest

from qagen.browser.session import EventSink, Session


def _session(safe_read_endpoints=None, classify=False, block_mutations=True):
    s = Session.__new__(Session)
    s.cfg = SimpleNamespace(
        browser=SimpleNamespace(
            block_mutations=block_mutations,
            safe_read_endpoints=safe_read_endpoints or [],
            classify_ambiguous_writes=classify,
        )
    )
    s.sink = EventSink()
    return s


def _request(method, url, post_data=None):
    return SimpleNamespace(method=method, url=url, post_data=post_data)


def _route():
    return SimpleNamespace(abort=AsyncMock(), continue_=AsyncMock())


class TestDefaultBehaviourUnchanged:
    """With neither new option set, every mutating call is still blocked --
    the whole point is that opting in is required, not automatic."""

    @pytest.mark.asyncio
    async def test_post_is_blocked_by_default(self):
        s = _session()
        route = _route()
        await s._write_guard(route, _request("POST", "https://x.test/api/ums/places", '{"name": "x"}'))
        route.abort.assert_awaited_once()
        route.continue_.assert_not_called()
        assert s.sink.blocked == ["POST https://x.test/api/ums/places"]

    @pytest.mark.asyncio
    async def test_a_filter_shaped_post_is_still_blocked_without_opting_in(self):
        """The classifier existing is not enough -- it must be turned on."""
        s = _session(classify=False)
        route = _route()
        await s._write_guard(
            route,
            _request("POST", "https://x.test/api/cms/x/resources", '{"page": 1, "pageSize": 20}'),
        )
        route.abort.assert_awaited_once()
        assert len(s.sink.blocked) == 1

    @pytest.mark.asyncio
    async def test_get_is_never_touched(self):
        s = _session()
        route = _route()
        await s._write_guard(route, _request("GET", "https://x.test/api/x"))
        route.continue_.assert_awaited_once()
        route.abort.assert_not_called()
        assert s.sink.blocked == []


class TestSafeReadEndpoints:
    """The deterministic allowlist -- exact, explicit, opt-in per endpoint."""

    @pytest.mark.asyncio
    async def test_a_listed_endpoint_is_let_through(self):
        s = _session(safe_read_endpoints=["/api/cms/*/resources"])
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://x.test/api/cms/abc/resources", '{"name": "x"}')
        )
        route.continue_.assert_awaited_once()
        route.abort.assert_not_called()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_an_unlisted_endpoint_stays_blocked(self):
        """Confirms the allowlist is scoped -- it does not open the guard
        wide, only the named path."""
        s = _session(safe_read_endpoints=["/api/cms/*/resources"])
        route = _route()
        await s._write_guard(route, _request("POST", "https://x.test/api/ums/places"))
        route.abort.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_substring_match_also_works_without_a_glob(self):
        s = _session(safe_read_endpoints=["/resources"])
        route = _route()
        await s._write_guard(route, _request("POST", "https://x.test/api/cms/abc/resources"))
        route.continue_.assert_awaited_once()


class TestClassifyAmbiguousWrites:
    """The opt-in shape-based classifier."""

    @pytest.mark.asyncio
    async def test_a_filter_shaped_post_is_let_through_when_enabled(self):
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route,
            _request("POST", "https://x.test/api/ums/places", '{"filter": {}, "sort": "name"}'),
        )
        route.continue_.assert_awaited_once()
        route.abort.assert_not_called()

    @pytest.mark.asyncio
    async def test_query_string_pagination_reaches_the_classifier_end_to_end(self):
        """The exact live pattern: an unhelpful body, real signal in the URL.
        Confirms the guard passes the query string through, not just the
        path."""
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route,
            _request(
                "POST",
                "https://x.test/api/dms/org/place/screens/search"
                "?orderBy=created_time&order=desc&start=0&rowsPerPage=50",
                '{"advancedSearch":[]}',
            ),
        )
        route.continue_.assert_awaited_once()
        route.abort.assert_not_called()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_put_is_never_reclassified_even_when_enabled(self):
        """The conservative guarantee: PUT/PATCH/DELETE are never rescued,
        whatever their body looks like."""
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route,
            _request("PUT", "https://x.test/api/dms/x/screens/1", '{"filter": {}}'),
        )
        route.abort.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_an_action_word_in_the_path_is_never_reclassified(self):
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route,
            _request(
                "POST", "https://x.test/api/ums/x/x/chat/start",
                '{"page": 1, "keyword": "hi"}',
            ),
        )
        route.abort.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_a_genuine_write_body_is_never_reclassified(self):
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://x.test/api/ums/places", '{"name": "New Place"}')
        )
        route.abort.assert_awaited_once()

    @pytest.mark.asyncio
    async def test_an_unclear_body_stays_blocked(self):
        """"unclear" is not "likely_read" -- only a positive read signal
        passes."""
        s = _session(classify=True)
        route = _route()
        await s._write_guard(route, _request("POST", "https://x.test/api/misc/x", None))
        route.abort.assert_awaited_once()


class TestTelemetryStillTakesPriority:
    """Analytics and ad-conversion beacons are aborted before either
    mechanism runs, and never counted as blocked -- unaffected by either new
    option."""

    @pytest.mark.asyncio
    async def test_analytics_beacon_is_not_recorded_even_with_classifier_on(self):
        s = _session(classify=True)
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://analytics.google.com/g/collect")
        )
        route.abort.assert_awaited_once()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_ad_conversion_pixel_is_not_recorded(self):
        """Found live: this fired on every click and, before this fix, still
        showed up as a blocked mutation even though the g/collect beacon was
        already excluded."""
        s = _session()
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://www.google.com/measurement/conversion")
        )
        route.abort.assert_awaited_once()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_rum_sts_call_is_not_recorded(self):
        """AWS CloudWatch RUM assuming its own monitoring role -- found live,
        fires once per navigation, carries no application data."""
        s = _session()
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://sts.us-east-1.amazonaws.com/")
        )
        route.abort.assert_awaited_once()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_rum_dataplane_call_is_not_recorded(self):
        """The other half of the pair -- RUM posting its collected metrics."""
        s = _session()
        route = _route()
        await s._write_guard(
            route,
            _request(
                "POST",
                "https://dataplane.rum.us-east-1.amazonaws.com/appmonitors/abc123",
            ),
        )
        route.abort.assert_awaited_once()
        assert s.sink.blocked == []


class TestCredentialServicesAreLetThrough:
    """Cognito issues real AWS credentials the app needs to read its own
    protected content -- not analytics, and blocking it can cause a page to
    render with real items but no thumbnails. Unlike telemetry, this is
    allowed through entirely rather than aborted-but-uncounted."""

    @pytest.mark.asyncio
    async def test_cognito_identity_post_reaches_the_network(self):
        s = _session()
        route = _route()
        await s._write_guard(
            route,
            _request(
                "POST", "https://cognito-identity.eu-central-1.amazonaws.com/",
            ),
        )
        route.continue_.assert_awaited_once()
        route.abort.assert_not_called()
        assert s.sink.blocked == []

    @pytest.mark.asyncio
    async def test_an_unrelated_amazonaws_host_is_not_affected(self):
        """Only the credential-issuing hosts are exempt -- a real API on the
        app's own AWS-hosted backend stays blocked as normal."""
        s = _session()
        route = _route()
        await s._write_guard(
            route, _request("POST", "https://api.execute-api.eu-central-1.amazonaws.com/prod/x")
        )
        route.abort.assert_awaited_once()
