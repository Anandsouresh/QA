# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T01:55:02+00:00  
**States:** 34 · **Transitions:** 80 · **Actionable elements:** 864 of 864 extracted

## N001 — HOME | Samsung VXT CMS *(entry)*

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 425 · **Visits:** 1
- **Reached by:** entry point
- **Screenshot:** [artifacts/N001_b7584813.png](artifacts/N001_b7584813.png)
- **DOM:** [artifacts/N001_b7584813.html](artifacts/N001_b7584813.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Buy Now' | no_change | (self) | inert |
| Click '.st0{opacity:0.8;}' | in_page_state | N003 HOME | Samsung VXT CMS — .st | — |
| Click 'New' | in_page_state | N004 HOME | Samsung VXT CMS — New | — |
| Click 'New' | in_page_state | N007 HOME | Samsung VXT CMS — New | — |
| Click 'New' | in_page_state | (self) | state-cap |
| Click 'New' | no_change | (self) | inert |
| Click 'screen' | navigation | N008 Screen | Samsung VXT CMS | — |
| Click 'content' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'playlist' | navigation | N010 Playlist | Samsung VXT CMS | — |
| Click 'schedule' | navigation | N011 Schedule | Samsung VXT CMS | — |
| Click 'Terms and Conditions' | navigation | N012 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N015 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N016 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N017 Samsung VXT CMS | — |
| Click 'screen' | navigation | N008 Screen | Samsung VXT CMS | — |
| Click 'content' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'playlist' | navigation | N010 Playlist | Samsung VXT CMS | — |
| Click 'schedule' | navigation | N011 Schedule | Samsung VXT CMS | — |

## N002 — vxt.samsung.com

- **URL:** https://vxt.samsung.com/contact-us
- **Type:** boundary · **Depth:** 0 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** n/a · **Visits:** 5
- **Reached by:** Click 'Contact Us'

_No actionable elements extracted._

## N003 — HOME | Samsung VXT CMS — .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 429 · **Visits:** 1
- **Reached by:** Click '.st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N003_5780f48c.png](artifacts/N003_5780f48c.png)
- **DOM:** [artifacts/N003_5780f48c.html](artifacts/N003_5780f48c.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace [[data-testid="dashboardPlaces_liPlaces_Item0"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N004 — HOME | Samsung VXT CMS — New

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 432 · **Visits:** 1
- **Reached by:** Click 'New'
- **Screenshot:** [artifacts/N004_8d7af56f.png](artifacts/N004_8d7af56f.png)
- **DOM:** [artifacts/N004_8d7af56f.html](artifacts/N004_8d7af56f.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Add Screen [[data-testid="dashboard_screen_addbtn_addscreen"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Screen Wall [[data-testid="dashboard_screen_addbtn_newscreenwall"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N005 HOME | Samsung VXT CMS — New | — |
| Click 'Add Screen' | in_page_state | N006 HOME | Samsung VXT CMS — New | — |
| Click 'New Screen Wall' | in_page_state | N005 HOME | Samsung VXT CMS — New | — |

## N005 — HOME | Samsung VXT CMS — New — span

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 519 · **Visits:** 1
- **Reached by:** Click 'New' → Click 'span'
- **Screenshot:** [artifacts/N005_3226f779.png](artifacts/N005_3226f779.png)
- **DOM:** [artifacts/N005_3226f779.html](artifacts/N005_3226f779.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Later [[data-testid="plan_dialog_later"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: Upgrade Now [[data-testid="plan_dialog_upgrade_now"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

## N006 — HOME | Samsung VXT CMS — New — Add Screen

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 453 · **Visits:** 1
- **Reached by:** Click 'New' → Click 'Add Screen'
- **Screenshot:** [artifacts/N006_b1d552cc.png](artifacts/N006_b1d552cc.png)
- **DOM:** [artifacts/N006_b1d552cc.html](artifacts/N006_b1d552cc.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

## N007 — HOME | Samsung VXT CMS — New

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 436 · **Visits:** 1
- **Reached by:** Click 'New'
- **Screenshot:** [artifacts/N007_d7ef7a88.png](artifacts/N007_d7ef7a88.png)
- **DOM:** [artifacts/N007_d7ef7a88.html](artifacts/N007_d7ef7a88.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Add Content [[data-testid="dashboard_content_addbtn_addcontent"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Create Content [[data-testid="dashboard_content_addbtn_createcontent"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Content' | in_page_state | (self) | state-cap |
| Click 'Create Content' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N008 — Screen | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 0 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 551 · **Visits:** 2
- **Reached by:** Click 'screen'
- **Screenshot:** [artifacts/N008_6429ff82.png](artifacts/N008_6429ff82.png)
- **DOM:** [artifacts/N008_6429ff82.html](artifacts/N008_6429ff82.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Screen' | in_page_state | N018 Screen | Samsung VXT CMS — A | — |
| Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' | in_page_state | N019 Screen | Samsung VXT CMS — C | — |
| Click 'Screen' | no_change | (self) | inert |
| Click 'Content' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'Content' | navigation | N009 Content | Samsung VXT CMS | — |

## N009 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 6 · **Interactive extracted:** 6 · **DOM nodes:** 526 · **Visits:** 3
- **Reached by:** Click 'content'
- **Screenshot:** [artifacts/N009_9dfb1c0f.png](artifacts/N009_9dfb1c0f.png)
- **DOM:** [artifacts/N009_9dfb1c0f.html](artifacts/N009_9dfb1c0f.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo' | no_change | (self) | inert |
| Click 'Create Content' | no_change | (self) | inert |
| Click 'Add Content' | in_page_state | N020 Content | Samsung VXT CMS —  | — |

## N010 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 0 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 529 · **Visits:** 2
- **Reached by:** Click 'playlist'
- **Screenshot:** [artifacts/N010_d514382c.png](artifacts/N010_d514382c.png)
- **DOM:** [artifacts/N010_d514382c.html](artifacts/N010_d514382c.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Playlist' | in_page_state | N024 Playlist | Samsung VXT CMS — | — |

## N011 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 0 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 503 · **Visits:** 2
- **Reached by:** Click 'schedule'
- **Screenshot:** [artifacts/N011_a21aaaae.png](artifacts/N011_a21aaaae.png)
- **DOM:** [artifacts/N011_a21aaaae.html](artifacts/N011_a21aaaae.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Schedule' | in_page_state | N028 Schedule | Samsung VXT CMS — | — |

## N012 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N012_5d156f05.png](artifacts/N012_5d156f05.png)
- **DOM:** [artifacts/N012_5d156f05.html](artifacts/N012_5d156f05.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'logo' | navigation | N001 HOME | Samsung VXT CMS | mutating |
| Click 'Notification' | in_page_state | N013 Terms and Conditions | Samsu | mutating |
| Click 'chatbot' | in_page_state | N014 Terms and Conditions | Samsu | mutating |

## N013 — Terms and Conditions | Samsung VXT CMS — Notification

- **URL:** https://www.samsungvx.com/terms
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 1036 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions' → Click 'Notification'
- **Screenshot:** [artifacts/N013_5a1ebc6c.png](artifacts/N013_5a1ebc6c.png)
- **DOM:** [artifacts/N013_5a1ebc6c.html](artifacts/N013_5a1ebc6c.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
generic_button: Export All [#notiFilterStateId > button.btn_icon]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: (unnamed) [[data-testid="icon_notification_all"]] (app frame)
inferred_clickable: All [#pc_filterRMStateId > div.select.select_btn]
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
text_input: Search Functions or Screens [role=textbox[name="Search Functions or Screens"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Close' | in_page_state | N012 Terms and Conditions | Samsu | mutating |
| Click 'Export All' | blocked_mutation | (self) | mutating |

## N014 — Terms and Conditions | Samsung VXT CMS — chatbot

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 358 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions' → Click 'chatbot'
- **Screenshot:** [artifacts/N014_37254bb7.png](artifacts/N014_37254bb7.png)
- **DOM:** [artifacts/N014_37254bb7.html](artifacts/N014_37254bb7.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: Minimize [#closeChatBtn]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Minimize' | in_page_state | N012 Terms and Conditions | Samsu | — |

## N015 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 10 · **Interactive extracted:** 10 · **DOM nodes:** 169 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy'
- **Screenshot:** [artifacts/N015_73bf039d.png](artifacts/N015_73bf039d.png)
- **DOM:** [artifacts/N015_73bf039d.html](artifacts/N015_73bf039d.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Version 1.3 [#select]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Version 1.3' | no_change | (self) | inert |

## N016 — Cookie Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/cookie
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N016_cdd051e5.png](artifacts/N016_cdd051e5.png)
- **DOM:** [artifacts/N016_cdd051e5.html](artifacts/N016_cdd051e5.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N017 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N017_b9728938.png](artifacts/N017_b9728938.png)
- **DOM:** [artifacts/N017_b9728938.html](artifacts/N017_b9728938.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N018 — Screen | Samsung VXT CMS — Add Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 484 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Add Screen'
- **Screenshot:** [artifacts/N018_90004d10.png](artifacts/N018_90004d10.png)
- **DOM:** [artifacts/N018_90004d10.html](artifacts/N018_90004d10.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N019 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 25 · **Interactive extracted:** 25 · **DOM nodes:** 469 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N019_7f063ef9.png](artifacts/N019_7f063ef9.png)
- **DOM:** [artifacts/N019_7f063ef9.html](artifacts/N019_7f063ef9.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [#place_list > li.ga-button-action-class.selected > span.check_off:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Default Workspace [role=listitem[name="Default Workspace"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N008 Screen | Samsung VXT CMS | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N008 Screen | Samsung VXT CMS | — |

## N020 — Content | Samsung VXT CMS — Add Content

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 472 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content'
- **Screenshot:** [artifacts/N020_ea05bf14.png](artifacts/N020_ea05bf14.png)
- **DOM:** [artifacts/N020_ea05bf14.html](artifacts/N020_ea05bf14.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [role=button[name="Close"]]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Drop the image, video and document files here.OpenClose [role=button[name="Drop the image, video and document files here.OpenClose"]]
generic_button: Open [#non_add]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Close' | in_page_state | N009 Content | Samsung VXT CMS | — |
| Click 'Open' | file_chooser | (self) | upload |
| Click 'My Device' | no_change | (self) | inert |
| Click 'Ticker' | in_page_state | N021 Content | Samsung VXT CMS —  | — |
| Click 'Web(HTML)' | in_page_state | N022 Content | Samsung VXT CMS —  | — |
| Click 'Web(URL)' | in_page_state | N023 Content | Samsung VXT CMS —  | — |

## N021 — Content | Samsung VXT CMS — Add Content — Ticker

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 1268 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Ticker'
- **Screenshot:** [artifacts/N021_2d37650f.png](artifacts/N021_2d37650f.png)
- **DOM:** [artifacts/N021_2d37650f.html](artifacts/N021_2d37650f.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#url_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#doneBtn] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ani_none"] >> nth=0]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(1) > div.relative > div.\#000000FF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(2) > div.relative > div.\#FFFFFFFF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(3) > div.relative > div.\#000000FF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(4) > div.relative > div.\#FFFFFFFF.border-radius4]
inferred_clickable: 90 [[data-testid="select_default"] >> nth=0]
inferred_clickable: Add Tag [[data-testid="icon_circleplus"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: None [[data-testid="select_default"] >> nth=0]
inferred_clickable: SamsungOne 300 [[data-testid="select_default"] >> nth=0]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
radio: Bottom [#radio_bottom]
radio: Top [#radio_top]
range: (unnamed) [div.flex_col.flexChildrenGrow > div.w100:nth-of-type(3) > div.slidecontainer.flex_center_between > span.MuiSlider-root.MuiSlider-colorPrimary > span.MuiSlider-thumb.MuiSlider-thumbSizeMedium:nth-of-type(3) > input]
text_input: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100:nth-of-type(3) > div.slidecontainer.flex_center_between > div.range_text > input]
text_input: Content Name [#name]
textarea: Enter a message. [role=textbox[name="Enter a message."]]
```

## N022 — Content | Samsung VXT CMS — Add Content — Web(HTML)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 545 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(HTML)'
- **Screenshot:** [artifacts/N022_2e47d2f0.png](artifacts/N022_2e47d2f0.png)
- **DOM:** [artifacts/N022_2e47d2f0.html](artifacts/N022_2e47d2f0.html)

**Action elements**

```
generic_button: (unnamed) [#web_tab_listbox]
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#web_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#web_tab_btn_done] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: 1 hour [[data-testid="select-Refresh Interval"]]
inferred_clickable: Add Tag [[data-testid="icon_circleplus"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Select the .zip file that contains .html and resource files [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Select the .zip file that contains .html and resource files [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
text_input: Content Name [#name]
text_input: Start Page [#page]
```

## N023 — Content | Samsung VXT CMS — Add Content — Web(URL)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 17 · **Interactive extracted:** 17 · **DOM nodes:** 535 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(URL)'
- **Screenshot:** [artifacts/N023_74a5c950.png](artifacts/N023_74a5c950.png)
- **DOM:** [artifacts/N023_74a5c950.html](artifacts/N023_74a5c950.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#url_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#doneBtn] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: 1 hour [[data-testid="select-Refresh Interval"]]
inferred_clickable: Add Tag [[data-testid="icon_circleplus"]]
inferred_clickable: Enter website address. Please include "http://" or "https:// [[data-testid="icon_question"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
text_input: Address [#address]
text_input: Content Name [#name]
```

## N024 — Playlist | Samsung VXT CMS — New Playlist

- **URL:** https://www.samsungvx.com/playlist
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 443 · **Visits:** 1
- **Reached by:** Click 'playlist' → Click 'New Playlist'
- **Screenshot:** [artifacts/N024_69f55def.png](artifacts/N024_69f55def.png)
- **DOM:** [artifacts/N024_69f55def.html](artifacts/N024_69f55def.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#select-wrap > ul.select-ul.on > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [#select-wrap > ul.select-ul.on > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: General [[data-testid="playlist_newplaylist_general"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Sync Play [[data-testid="playlist_newplaylist_syncplay"]]
inferred_clickable: Takeover Sync Play [[data-testid="playlist_newplaylist_takeover_syncplay"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N025 Playlist | Samsung VXT CMS — | — |
| Click 'span' | navigation | N026 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N027 Playlist | Samsung VXT CMS | — |
| Click 'Sync Play' | in_page_state | N025 Playlist | Samsung VXT CMS — | — |
| Click 'Takeover Sync Play' | navigation | N026 Playlist | Samsung VXT CMS | — |
| Click '' | navigation | N030 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N027 Playlist | Samsung VXT CMS | — |

## N025 — Playlist | Samsung VXT CMS — New Playlist — span

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 511 · **Visits:** 1
- **Reached by:** Click 'playlist' → Click 'New Playlist' → Click 'span'
- **Screenshot:** [artifacts/N025_11a45fcc.png](artifacts/N025_11a45fcc.png)
- **DOM:** [artifacts/N025_11a45fcc.html](artifacts/N025_11a45fcc.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [[data-testid="playlist_newplaylist_syncplay_btnclose"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(1) > img]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(2) > img]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(3) > img]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Multi Playlists to Screen Wall [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(2) > div]
inferred_clickable: Multi Playlists to Screen WallUseful for playing multiple playlists simultaneously on a screen wall. [[data-testid="new-sync-multi"]]
inferred_clickable: Multi Playlists to Tagged Screens [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(3) > div]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Single Playlist to Screen Wall [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(1) > div]
inferred_clickable: Single Playlist to Screen WallUseful for playing a single playlist simultaneously on a screen wall. [[data-testid="new-sync-single"]]
inferred_clickable: Sync Play lets you play playlists simultaneously across scre [[data-testid="icon_question"]]
```

## N026 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 1 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 678 · **Visits:** 2
- **Reached by:** Click 'playlist' → Click 'New Playlist' → Click 'span'

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_takeover_syncplay_preview"]]
generic_button: Add Playlist [[data-testid="playlist_newplaylist_takeover_syncplay_addplaylist"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_takeover_syncplay_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_takeover_syncplay_set2screen"]]
generic_button: To pick up a draggable item, press the space bar. While drag [#fcms-list-ul > li.swiper-area.swiper_arrow]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: 1 [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > div.cqGZgr]
inferred_clickable: 1Settings [role=listitem[name="1Settings"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
tab: 1Takeover 1 [role=tab[name="1Takeover 1"]]
text_input: (unnamed) [[data-testid="duration-input-0"]] (disabled)
text_input: (unnamed) [#_r_0_]
```

## N027 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/create
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 443 · **Visits:** 2
- **Reached by:** Click 'playlist' → Click 'New Playlist' → Click 'General'
- **Screenshot:** [artifacts/N027_b2960846.png](artifacts/N027_b2960846.png)
- **DOM:** [artifacts/N027_b2960846.html](artifacts/N027_b2960846.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'logo' | navigation | N001 HOME | Samsung VXT CMS | — |

## N028 — Schedule | Samsung VXT CMS — New Schedule

- **URL:** https://www.samsungvx.com/schedule
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 410 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click 'New Schedule'
- **Screenshot:** [artifacts/N028_a24fcfd3.png](artifacts/N028_a24fcfd3.png)
- **DOM:** [artifacts/N028_a24fcfd3.html](artifacts/N028_a24fcfd3.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#select-wrap > ul.select-ul.on > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: General [[data-testid="schedule_genral_btn"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Sync Play [[data-testid="schedule_syncplay_btn"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'General' | navigation | N029 Schedule | Samsung VXT CMS | — |
| Click 'Sync Play' | navigation | N029 Schedule | Samsung VXT CMS | — |
| Click 'General' | navigation | N029 Schedule | Samsung VXT CMS | — |

## N029 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 1 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 667 · **Visits:** 3
- **Reached by:** Click 'schedule' → Click 'New Schedule' → Click 'General'
- **Screenshot:** [artifacts/N029_ea84ae78.png](artifacts/N029_ea84ae78.png)
- **DOM:** [artifacts/N029_ea84ae78.html](artifacts/N029_ea84ae78.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Content' | in_page_state | N031 Schedule | Samsung VXT CMS — | — |
| Click 'Set to Screens' | no_change | (self) | inert |
| Click 'Save' | no_change | (self) | inert |
| Click 'more' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'August 2026Week 34' | in_page_state | N033 Schedule | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | in_page_state | N034 Schedule | Samsung VXT CMS — | — |
| Click 'Today' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |

## N030 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 2 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 471 · **Visits:** 1
- **Reached by:** Click 'playlist' → Click 'New Playlist' → Click ''
- **Screenshot:** [artifacts/N030_e4204427.png](artifacts/N030_e4204427.png)
- **DOM:** [artifacts/N030_e4204427.html](artifacts/N030_e4204427.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Playlist [role=button[name="Playlist"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N031 — Schedule | Samsung VXT CMS — Add Content

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 783 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click 'New Schedule' → Click 'General' → Click 'Add Content'
- **Screenshot:** [artifacts/N031_733888c7.png](artifacts/N031_733888c7.png)
- **DOM:** [artifacts/N031_733888c7.html](artifacts/N031_733888c7.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: Cancel [[data-testid="schedule_content_popup_cancel_btn"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: OK [[data-testid="schedule_content_popup_ok_btn"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_content_popup_add_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Once [[data-testid="select-Repeat"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
text_input: (unnamed) [#schedule_content_popup_start_date > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: (unnamed) [#select >> nth=0]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N029 Schedule | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N032 Schedule | Samsung VXT CMS — | — |

## N032 — Schedule | Samsung VXT CMS — Add Content — div

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 900 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click 'New Schedule' → Click 'General' → Click 'Add Content' → Click 'div'
- **Screenshot:** [artifacts/N032_2f6b8fb7.png](artifacts/N032_2f6b8fb7.png)
- **DOM:** [artifacts/N032_2f6b8fb7.html](artifacts/N032_2f6b8fb7.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: Cancel [[data-testid="schedule_content_popup_cancel_btn"]]
generic_button: Cancel [[data-testid="schedule_footer_rightpart_cancelBtn"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: OK [[data-testid="schedule_content_popup_ok_btn"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Select [[data-testid="schedule_footer_rightpart_okbtn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_content_popup_add_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [#select >> nth=0]
inferred_clickable: (unnamed) [#select >> nth=0]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [[data-testid="schedule_selectcontentdialog_content"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Once [[data-testid="select-Repeat"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [[data-testid="schedule_selectcontentdialog_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
text_input: (unnamed) [#schedule_content_popup_start_date > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: (unnamed) [#select >> nth=0]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N033 — Schedule | Samsung VXT CMS — August 2026Week 34

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 2 · **Actionable:** 65 · **Interactive extracted:** 65 · **DOM nodes:** 778 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click 'New Schedule' → Click 'General' → Click 'August 2026Week 34'
- **Screenshot:** [artifacts/N033_be2f490d.png](artifacts/N033_be2f490d.png)
- **DOM:** [artifacts/N033_be2f490d.html](artifacts/N033_be2f490d.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: 1 [#day_6 >> nth=0]
inferred_clickable: 10 [#day_1 >> nth=0]
inferred_clickable: 11 [#day_2 >> nth=0]
inferred_clickable: 12 [#day_3 >> nth=0]
inferred_clickable: 13 [#day_4 >> nth=0]
inferred_clickable: 14 [#day_5 >> nth=0]
inferred_clickable: 15 [#day_6 >> nth=0]
inferred_clickable: 16 [#day_0 >> nth=0]
inferred_clickable: 17 [#day_1 >> nth=0]
inferred_clickable: 18 [#day_2 >> nth=0]
inferred_clickable: 19 [#day_3 >> nth=0]
inferred_clickable: 2 [#day_0 >> nth=0]
inferred_clickable: 20 [#day_4 >> nth=0]
inferred_clickable: 21 [#day_5 >> nth=0]
inferred_clickable: 22 [#day_6 >> nth=0]
inferred_clickable: 23 [#day_0 >> nth=0]
inferred_clickable: 24 [#day_1 >> nth=0]
inferred_clickable: 25 [#day_2 >> nth=0]
inferred_clickable: 26 [#day_3 >> nth=0]
inferred_clickable: 27 [#day_4 >> nth=0]
inferred_clickable: 28 [#day_5 >> nth=0]
inferred_clickable: 29 [#day_6 >> nth=0]
inferred_clickable: 3 [#day_1 >> nth=0]
inferred_clickable: 30 [#day_0 >> nth=0]
inferred_clickable: 31 [#day_1 >> nth=0]
inferred_clickable: 4 [#day_2 >> nth=0]
inferred_clickable: 5 [#day_3 >> nth=0]
inferred_clickable: 6 [#day_4 >> nth=0]
inferred_clickable: 7 [#day_5 >> nth=0]
inferred_clickable: 8 [#day_6 >> nth=0]
inferred_clickable: 9 [#day_0 >> nth=0]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: August 2026Week 33 [#schedule_date_sort]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1' | in_page_state | N029 Schedule | Samsung VXT CMS | — |

## N034 — Schedule | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 2 · **Actionable:** 36 · **Interactive extracted:** 36 · **DOM nodes:** 687 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click 'New Schedule' → Click 'General' → Click 'div'
- **Screenshot:** [artifacts/N034_0475bb5e.png](artifacts/N034_0475bb5e.png)
- **DOM:** [artifacts/N034_0475bb5e.html](artifacts/N034_0475bb5e.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon.width_100_percent:nth-of-type(1) > div.tag_help_class.is_first > span > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: August 2026Week 35 [#schedule_date_sort]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
text_input: Enter text. [[data-testid="FcmsEditTags_edit_new_tag"]]
```

