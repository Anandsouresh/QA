# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T02:20:33+00:00  
**States:** 45 · **Transitions:** 91 · **Actionable elements:** 1060 of 1060 extracted

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
| Click 'New' | blocked_mutation | (self) | mutating |
| Click 'screen' | navigation | N008 Screen | Samsung VXT CMS | mutating |
| Click 'content' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'Terms and Conditions' | navigation | N010 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N013 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N014 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N015 Samsung VXT CMS | — |
| Click 'screen' | navigation | N008 Screen | Samsung VXT CMS | — |
| Click 'content' | navigation | N009 Content | Samsung VXT CMS | — |

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
| Click 'div' | no_change | (self) | inert |
| Click 'div' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'div' | navigation | N016 Playlist | Samsung VXT CMS | — |
| Click 'div' | navigation | N017 Schedule | Samsung VXT CMS | — |
| Click 'div' | navigation | N018 Channel | Samsung VXT CMS | — |
| Click 'div' | navigation | N018 Channel | Samsung VXT CMS | — |
| Click 'Open Tag Explorer' | in_page_state | N019 Screen | Samsung VXT CMS — O | — |
| Click 'div' | navigation | N020 Samsung VXT CMS | — |
| Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' | in_page_state | N026 Screen | Samsung VXT CMS — C | — |
| Click 'Screen' | no_change | (self) | inert |
| Click 'Content' | navigation | N009 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N027 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N028 Schedule | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N029 Channel | Samsung VXT CMS | — |
| Click 'AppsN' | navigation | N020 Samsung VXT CMS | — |
| Click '' | navigation | N009 Content | Samsung VXT CMS | — |
| Click '' | navigation | N027 Playlist | Samsung VXT CMS | — |
| Click '' | navigation | N038 Schedule | Samsung VXT CMS | — |
| Click '' | navigation | N039 Channel | Samsung VXT CMS | — |
| Click '' | navigation | N040 Samsung VXT CMS | — |
| Click 'Content' | navigation | N041 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N042 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N043 Schedule | Samsung VXT CMS | — |

## N009 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 6 · **Interactive extracted:** 6 · **DOM nodes:** 526 · **Visits:** 4
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
| Click 'Add Content' | in_page_state | N030 Content | Samsung VXT CMS —  | — |

## N010 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 160 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N010_5d156f05.png](artifacts/N010_5d156f05.png)
- **DOM:** [artifacts/N010_5d156f05.html](artifacts/N010_5d156f05.html)

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
| Click 'logo' | navigation | N001 HOME | Samsung VXT CMS | — |
| Click 'Notification' | in_page_state | N011 Terms and Conditions | Samsu | — |
| Click 'chatbot' | in_page_state | N012 Terms and Conditions | Samsu | mutating |

## N011 — Terms and Conditions | Samsung VXT CMS — Notification

- **URL:** https://www.samsungvx.com/terms
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 1036 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions' → Click 'Notification'
- **Screenshot:** [artifacts/N011_5a1ebc6c.png](artifacts/N011_5a1ebc6c.png)
- **DOM:** [artifacts/N011_5a1ebc6c.html](artifacts/N011_5a1ebc6c.html)

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
| Click 'Close' | in_page_state | N010 Terms and Conditions | Samsu | — |
| Click 'Export All' | no_change | (self) | inert |

## N012 — Terms and Conditions | Samsung VXT CMS — chatbot

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 358 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions' → Click 'chatbot'
- **Screenshot:** [artifacts/N012_37254bb7.png](artifacts/N012_37254bb7.png)
- **DOM:** [artifacts/N012_37254bb7.html](artifacts/N012_37254bb7.html)

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
| Click 'Minimize' | in_page_state | N010 Terms and Conditions | Samsu | — |

## N013 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 10 · **Interactive extracted:** 10 · **DOM nodes:** 169 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy'
- **Screenshot:** [artifacts/N013_73bf039d.png](artifacts/N013_73bf039d.png)
- **DOM:** [artifacts/N013_73bf039d.html](artifacts/N013_73bf039d.html)

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

## N014 — Cookie Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/cookie
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N014_cdd051e5.png](artifacts/N014_cdd051e5.png)
- **DOM:** [artifacts/N014_cdd051e5.html](artifacts/N014_cdd051e5.html)

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

## N015 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N015_b9728938.png](artifacts/N015_b9728938.png)
- **DOM:** [artifacts/N015_b9728938.html](artifacts/N015_b9728938.html)

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

## N016 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 486 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'div'

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

## N017 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 515 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'div'

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

## N018 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 1 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 521 · **Visits:** 2
- **Reached by:** Click 'screen' → Click 'div'

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
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N019 — Screen | Samsung VXT CMS — Open Tag Explorer

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 14 · **Interactive extracted:** 14 · **DOM nodes:** 513 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer'
- **Screenshot:** [artifacts/N019_421e27f1.png](artifacts/N019_421e27f1.png)
- **DOM:** [artifacts/N019_421e27f1.html](artifacts/N019_421e27f1.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [[data-testid="icon_left_controller"]]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '.st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;}' | in_page_state | N008 Screen | Samsung VXT CMS | — |
| Click 'Apps' | navigation | N020 Samsung VXT CMS | — |
| Click 'Channel' | navigation | N021 Channel | Samsung VXT CMS | — |
| Click 'Content' | navigation | N022 Content | Samsung VXT CMS | — |
| Click 'Menu' | in_page_state | N023 Screen | Samsung VXT CMS — O | — |
| Click 'Playlist' | navigation | N024 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N025 Schedule | Samsung VXT CMS | — |
| Click 'Screen' | no_change | (self) | inert |
| Click 'Apps' | navigation | N040 Samsung VXT CMS | — |
| Click 'Channel' | navigation | N039 Channel | Samsung VXT CMS | — |
| Click 'Content' | navigation | N041 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N042 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N043 Schedule | Samsung VXT CMS | — |

## N020 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 1 · **Actionable:** 156 · **Interactive extracted:** 156 · **DOM nodes:** 1231 · **Visits:** 4
- **Reached by:** Click 'screen' → Click 'div'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > img]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > img]
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_right"]]
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_left"]]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(4) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(5) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(5) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(8) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(8) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(9) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(10) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(11) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: CalendarCalendar [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData Sync [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: DropboxDropbox [div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: DropboxDropboxDropbox lets you create immersive slideshows instantly from your photos and videos. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: EWQ SuperQueueEWQ SuperQueue [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Google DriveGoogle Drive [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: LDSK EnterpriseLDSK Enterprise [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Link My POSLink My POS [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Microsoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft ExcelMicrosoft ExcelMicrosoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Microsoft OneDriveMicrosoft OneDrive [div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft OneDriveMicrosoft OneDriveMicrosoft One Drive enables you to instantly play your image and video into dynamic slideshows. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Microsoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft Power BIMicrosoft Power BIMicrosoft Power BI enables you to instantly visualize your report and dashboard on screen [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Microsoft PowerPoint enables you to instantly play dynamic slideshow. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPointMicrosoft PowerPoint enables you to instantly play dynamic slideshow. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Microsoft SharePoint enables you to effortlessly share and collaborate on news posts with your team. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: Ngine AutomotiveNgine Automotive [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Ngine Real EstateNgine Real Estate [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Productivity [div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: ShadowGenShadowGenBETASamsung VXT Canvas enables you to create the shadow effects effortlessly [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

## N021 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 1 · **Actionable:** 14 · **Interactive extracted:** 14 · **DOM nodes:** 440 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer' → Click 'Channel'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [[data-testid="icon_left_controller"]]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N022 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 7 · **Interactive extracted:** 7 · **DOM nodes:** 450 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer' → Click 'Content'

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comContentCreate content by VXT Canvas or add your media fi [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [[data-testid="icon_left_controller"]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
```

## N023 — Screen | Samsung VXT CMS — Open Tag Explorer — Menu

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 462 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer' → Click 'Menu'
- **Screenshot:** [artifacts/N023_7808b66a.png](artifacts/N023_7808b66a.png)
- **DOM:** [artifacts/N023_7808b66a.html](artifacts/N023_7808b66a.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N024 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 14 · **Interactive extracted:** 14 · **DOM nodes:** 454 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer' → Click 'Playlist'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [[data-testid="icon_left_controller"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N025 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 14 · **Interactive extracted:** 14 · **DOM nodes:** 430 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Open Tag Explorer' → Click 'Schedule'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [[data-testid="icon_left_controller"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N026 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 489 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N026_afbd3c27.png](artifacts/N026_afbd3c27.png)
- **DOM:** [artifacts/N026_afbd3c27.html](artifacts/N026_afbd3c27.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Default Workspace [role=listitem[name="Default Workspace"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N023 Screen | Samsung VXT CMS — O | — |
| Click 'Apps' | navigation | N020 Samsung VXT CMS | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N023 Screen | Samsung VXT CMS — O | — |
| Click 'Apps' | navigation | N044 Samsung VXT CMS | — |

## N027 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 507 · **Visits:** 2
- **Reached by:** Click 'screen' → Click 'Playlist'
- **Screenshot:** [artifacts/N027_5907c757.png](artifacts/N027_5907c757.png)
- **DOM:** [artifacts/N027_5907c757.html](artifacts/N027_5907c757.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Playlist' | in_page_state | N034 Playlist | Samsung VXT CMS — | — |

## N028 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 514 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Schedule'

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N029 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 521 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Channel'

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N030 — Content | Samsung VXT CMS — Add Content

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 471 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content'
- **Screenshot:** [artifacts/N030_ea05bf14.png](artifacts/N030_ea05bf14.png)
- **DOM:** [artifacts/N030_ea05bf14.html](artifacts/N030_ea05bf14.html)

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
| Click 'Ticker' | in_page_state | N031 Content | Samsung VXT CMS —  | — |
| Click 'Web(HTML)' | in_page_state | N032 Content | Samsung VXT CMS —  | — |
| Click 'Web(URL)' | in_page_state | N033 Content | Samsung VXT CMS —  | — |

## N031 — Content | Samsung VXT CMS — Add Content — Ticker

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 1267 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Ticker'
- **Screenshot:** [artifacts/N031_2d37650f.png](artifacts/N031_2d37650f.png)
- **DOM:** [artifacts/N031_2d37650f.html](artifacts/N031_2d37650f.html)

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

## N032 — Content | Samsung VXT CMS — Add Content — Web(HTML)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 544 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(HTML)'
- **Screenshot:** [artifacts/N032_2e47d2f0.png](artifacts/N032_2e47d2f0.png)
- **DOM:** [artifacts/N032_2e47d2f0.html](artifacts/N032_2e47d2f0.html)

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

## N033 — Content | Samsung VXT CMS — Add Content — Web(URL)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 17 · **Interactive extracted:** 17 · **DOM nodes:** 534 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(URL)'
- **Screenshot:** [artifacts/N033_74a5c950.png](artifacts/N033_74a5c950.png)
- **DOM:** [artifacts/N033_74a5c950.html](artifacts/N033_74a5c950.html)

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

## N034 — Playlist | Samsung VXT CMS — New Playlist

- **URL:** https://www.samsungvx.com/playlist
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 442 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Playlist' → Click 'New Playlist'
- **Screenshot:** [artifacts/N034_fbd4e1ed.png](artifacts/N034_fbd4e1ed.png)
- **DOM:** [artifacts/N034_fbd4e1ed.html](artifacts/N034_fbd4e1ed.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: General [[data-testid="playlist_newplaylist_general"]]
inferred_clickable: logo [#header_logo] (app frame)
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
| Click 'span' | in_page_state | N035 Playlist | Samsung VXT CMS — | — |
| Click 'span' | navigation | N036 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N037 Playlist | Samsung VXT CMS | — |
| Click '' | navigation | N045 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N037 Playlist | Samsung VXT CMS | — |

## N035 — Playlist | Samsung VXT CMS — New Playlist — span

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 2 · **Actionable:** 36 · **Interactive extracted:** 36 · **DOM nodes:** 510 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Playlist' → Click 'New Playlist' → Click 'span'
- **Screenshot:** [artifacts/N035_32686225.png](artifacts/N035_32686225.png)
- **DOM:** [artifacts/N035_32686225.html](artifacts/N035_32686225.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Multi Playlists to Screen Wall [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(2) > div]
inferred_clickable: Multi Playlists to Screen WallUseful for playing multiple playlists simultaneously on a screen wall. [[data-testid="new-sync-multi"]]
inferred_clickable: Multi Playlists to Tagged Screens [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(3) > div]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Single Playlist to Screen Wall [div:nth-of-type(5) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(1) > div]
inferred_clickable: Single Playlist to Screen WallUseful for playing a single playlist simultaneously on a screen wall. [[data-testid="new-sync-single"]]
inferred_clickable: Sync Play lets you play playlists simultaneously across scre [[data-testid="icon_question"]]
```

## N036 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 2 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 677 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Playlist' → Click 'New Playlist' → Click 'span'

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
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: 1 [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > div.cqGZgr]
inferred_clickable: 1Settings [role=listitem[name="1Settings"]]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
tab: 1Takeover 1 [role=tab[name="1Takeover 1"]]
text_input: (unnamed) [[data-testid="duration-input-0"]] (disabled)
text_input: (unnamed) [#_r_0_]
```

## N037 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/create
- **Type:** page · **Depth:** 2 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 448 · **Visits:** 2
- **Reached by:** Click 'screen' → Click 'Playlist' → Click 'New Playlist' → Click 'General'
- **Screenshot:** [artifacts/N037_52239882.png](artifacts/N037_52239882.png)
- **DOM:** [artifacts/N037_52239882.html](artifacts/N037_52239882.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |

## N038 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 1 · **Interactive extracted:** 1 · **DOM nodes:** 116 · **Visits:** 1
- **Reached by:** Click 'screen' → Click ''
- **Screenshot:** [artifacts/N038_14fd9173.png](artifacts/N038_14fd9173.png)
- **DOM:** [artifacts/N038_14fd9173.html](artifacts/N038_14fd9173.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
```

## N039 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 2 · **Actionable:** 21 · **Interactive extracted:** 21 · **DOM nodes:** 330 · **Visits:** 1
- **Reached by:** Click 'screen' → Click ''
- **Screenshot:** [artifacts/N039_0fd3f03e.png](artifacts/N039_0fd3f03e.png)
- **DOM:** [artifacts/N039_0fd3f03e.html](artifacts/N039_0fd3f03e.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N040 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 2 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 262 · **Visits:** 1
- **Reached by:** Click 'screen' → Click ''
- **Screenshot:** [artifacts/N040_fdb8d51b.png](artifacts/N040_fdb8d51b.png)
- **DOM:** [artifacts/N040_fdb8d51b.html](artifacts/N040_fdb8d51b.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N041 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 2 · **Actionable:** 4 · **Interactive extracted:** 4 · **DOM nodes:** 281 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Content'
- **Screenshot:** [artifacts/N041_ec3665b0.png](artifacts/N041_ec3665b0.png)
- **DOM:** [artifacts/N041_ec3665b0.html](artifacts/N041_ec3665b0.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
```

## N042 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 2 · **Actionable:** 21 · **Interactive extracted:** 21 · **DOM nodes:** 353 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Playlist'
- **Screenshot:** [artifacts/N042_41872a2f.png](artifacts/N042_41872a2f.png)
- **DOM:** [artifacts/N042_41872a2f.html](artifacts/N042_41872a2f.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N043 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 21 · **Interactive extracted:** 21 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Schedule'
- **Screenshot:** [artifacts/N043_73bb5c37.png](artifacts/N043_73bb5c37.png)
- **DOM:** [artifacts/N043_73bb5c37.html](artifacts/N043_73bb5c37.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: Open Tag Explorer [[data-testid="icon_left_controller2"]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

## N044 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 2 · **Actionable:** 63 · **Interactive extracted:** 63 · **DOM nodes:** 531 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' → Click 'Apps'
- **Screenshot:** [artifacts/N044_3bec6171.png](artifacts/N044_3bec6171.png)
- **DOM:** [artifacts/N044_3bec6171.html](artifacts/N044_3bec6171.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(1)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(2)]
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(3)]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_right"]]
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_left"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Microsoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPoint enables you to instantly play dynamic slideshow. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft SharePoint enables you to effortlessly share and collaborate on news posts with your team. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'img' | no_change | (self) | inert |

## N045 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 3 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 455 · **Visits:** 1
- **Reached by:** Click 'screen' → Click 'Playlist' → Click 'New Playlist' → Click ''
- **Screenshot:** [artifacts/N045_b0742664.png](artifacts/N045_b0742664.png)
- **DOM:** [artifacts/N045_b0742664.html](artifacts/N045_b0742664.html)

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
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
```

