# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-17T16:50:50+00:00  
**States:** 69 · **Transitions:** 176 · **Actionable elements:** 2188 of 2188 extracted

## N001 — HOME | Samsung VXT CMS *(entry)*

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 425 · **Visits:** 1
- **Reached by:** entry point
- **Screenshot:** [artifacts/N001_b7584813.png](artifacts/N001_b7584813.png)
- **DOM:** [artifacts/N001_b7584813.html](artifacts/N001_b7584813.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Buy Now' | no_change | (self) | inert |
| Click 'chatbot' | in_page_state | N003 HOME | Samsung VXT CMS — cha | mutating |
| Click 'editHome' | navigation | N004 Settings | Samsung VXT CMS | — |
| Click 'refresh' | no_change | (self) | inert |
| Click 'div' | in_page_state | N005 HOME | Samsung VXT CMS — div | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click 'div' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click '.st0{opacity:0.8;}' | in_page_state | N010 HOME | Samsung VXT CMS — .st | — |
| Click 'Allocation 3Used 0Available 3' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click 'content' | navigation | N011 Content | Samsung VXT CMS | — |
| Click 'Terms and Conditions' | navigation | N012 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N014 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N017 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N018 Samsung VXT CMS | — |
| Click 'editHome' | navigation | N004 Settings | Samsung VXT CMS | — |
| Click '' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click 'Allocation 3Used 0Available 3' | navigation | N030 Settings | Samsung VXT CMS | — |
| Click 'content' | navigation | N011 Content | Samsung VXT CMS | — |

## N002 — vxt.samsung.com

- **URL:** https://vxt.samsung.com/contact-us
- **Type:** boundary · **Depth:** 0 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** n/a · **Visits:** 7
- **Reached by:** Click 'Contact Us'

_No actionable elements extracted._

## N003 — HOME | Samsung VXT CMS — chatbot

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 451 · **Visits:** 1
- **Reached by:** Click 'chatbot'
- **Screenshot:** [artifacts/N003_61bdf557.png](artifacts/N003_61bdf557.png)
- **DOM:** [artifacts/N003_61bdf557.html](artifacts/N003_61bdf557.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Minimize [#closeChatBtn]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Minimize' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N004 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 0 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 548 · **Visits:** 2
- **Reached by:** Click 'editHome'
- **Screenshot:** [artifacts/N004_294bdb11.png](artifacts/N004_294bdb11.png)
- **DOM:** [artifacts/N004_294bdb11.html](artifacts/N004_294bdb11.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Apps [role=button[name="Apps"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
generic_button: Done [role=button[name="Done"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]]
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: StorageUsed0.00KB [role=button[name="StorageUsed0.00KB"]]
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Title [role=listitem[name="Title"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Logo' | file_chooser | (self) | upload |
| Click 'Organization Name' | no_change | (self) | inert |
| Click 'button' | file_chooser | (self) | upload |
| Click 'button' | in_page_state | N019 Settings | Samsung VXT CMS — | — |
| Click 'Apps' | no_change | (self) | inert |
| Click 'Cancel' | navigation | N020 Samsung VXT CMS | — |
| Click 'Cancel' | navigation | N018 Samsung VXT CMS | — |

## N005 — HOME | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 475 · **Visits:** 1
- **Reached by:** Click 'div'
- **Screenshot:** [artifacts/N005_b457968f.png](artifacts/N005_b457968f.png)
- **DOM:** [artifacts/N005_b457968f.html](artifacts/N005_b457968f.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: General [[data-testid="dashboard_playlist_addbtn_general"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Sync Play [[data-testid="dashboard_playlist_addbtn_syncplay"]]
inferred_clickable: Takeover Sync Play [[data-testid="dashboard_playlist_addbtn_takeoversyncplay"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N006 HOME | Samsung VXT CMS — div | — |
| Click 'span' | navigation | N007 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N008 Playlist | Samsung VXT CMS | — |
| Click 'Sync Play' | in_page_state | N006 HOME | Samsung VXT CMS — div | — |
| Click 'Takeover Sync Play' | navigation | N007 Playlist | Samsung VXT CMS | — |
| Click '' | navigation | N021 Playlist | Samsung VXT CMS | — |
| Click 'General' | navigation | N008 Playlist | Samsung VXT CMS | — |

## N006 — HOME | Samsung VXT CMS — div — span

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 540 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'span'
- **Screenshot:** [artifacts/N006_b5004fa8.png](artifacts/N006_b5004fa8.png)
- **DOM:** [artifacts/N006_b5004fa8.html](artifacts/N006_b5004fa8.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [[data-testid="playlist_newplaylist_syncplay_btnclose"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(1) > img]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(2) > img]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_rightwards"] >> nth=0]
inferred_clickable: (unnamed) [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(3) > img]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: Multi Playlists to Screen Wall [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(2) > div]
inferred_clickable: Multi Playlists to Screen WallUseful for playing multiple playlists simultaneously on a screen wall. [[data-testid="new-sync-multi"]]
inferred_clickable: Multi Playlists to Tagged Screens [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(3) > div]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Single Playlist to Screen Wall [div:nth-of-type(4) > div.modalcomponent:nth-of-type(1) > div._pop_con_1e26u_207:nth-of-type(2) > ul.mt40 > li:nth-of-type(1) > div]
inferred_clickable: Single Playlist to Screen WallUseful for playing a single playlist simultaneously on a screen wall. [[data-testid="new-sync-single"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

## N007 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 0 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 789 · **Visits:** 2
- **Reached by:** Click 'div' → Click 'span'

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_takeover_syncplay_preview"]]
generic_button: Add Playlist [[data-testid="playlist_newplaylist_takeover_syncplay_addplaylist"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_takeover_syncplay_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_takeover_syncplay_set2screen"]]
generic_button: To pick up a draggable item, press the space bar. While drag [#fcms-list-ul > li.swiper-area.swiper_arrow]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: 1 [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > div.cqGZgr]
inferred_clickable: 1Settings [role=listitem[name="1Settings"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
tab: 1Takeover 1 [role=tab[name="1Takeover 1"]]
text_input: (unnamed) [[data-testid="duration-input-0"]] (disabled)
text_input: (unnamed) [#_r_0_]
```

## N008 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/create
- **Type:** page · **Depth:** 0 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 527 · **Visits:** 2
- **Reached by:** Click 'div' → Click 'General'
- **Screenshot:** [artifacts/N008_b2960846.png](artifacts/N008_b2960846.png)
- **DOM:** [artifacts/N008_b2960846.html](artifacts/N008_b2960846.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'AppsN' | navigation | N022 Samsung VXT CMS | — |
| Click 'GeneralGeneral' | no_change | (self) | inert |
| Click 'AppsN' | navigation | N042 Samsung VXT CMS | — |

## N009 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 0 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 564 · **Visits:** 4
- **Reached by:** Click 'div'
- **Screenshot:** [artifacts/N009_262d7cb3.png](artifacts/N009_262d7cb3.png)
- **DOM:** [artifacts/N009_262d7cb3.html](artifacts/N009_262d7cb3.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'button' | in_page_state | N023 Settings | Samsung VXT CMS — | — |
| Click 'Add Workspace' | in_page_state | N025 Settings | Samsung VXT CMS — | — |
| Click 'div' | navigation | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | navigation | N026 Settings | Samsung VXT CMS | — |
| Click 'div' | navigation | N004 Settings | Samsung VXT CMS | — |
| Click 'div' | no_change | (self) | inert |
| Click 'Activity Log' | navigation | N027 Settings | Samsung VXT CMS | — |
| Click 'Allocation' | no_change | (self) | inert |
| Click 'Edit Home' | navigation | N028 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N029 Settings | Samsung VXT CMS | — |
| Click 'Event' | navigation | N026 Settings | Samsung VXT CMS | — |
| Click 'Tech Inquiry' | navigation | N044 Settings | Samsung VXT CMS | — |
| Click '' | navigation | N026 Settings | Samsung VXT CMS | — |
| Click 'Activity Log' | navigation | N027 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N004 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N029 Settings | Samsung VXT CMS | — |

## N010 — HOME | Samsung VXT CMS — .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 497 · **Visits:** 1
- **Reached by:** Click '.st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N010_5780f48c.png](artifacts/N010_5780f48c.png)
- **DOM:** [artifacts/N010_5780f48c.html](artifacts/N010_5780f48c.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace [[data-testid="dashboard_workspace_change"]]
inferred_clickable: Default Workspace [[data-testid="dashboardPlaces_liPlaces_Item0"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: Notification [[data-testid="icon_notific_solidation"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N011 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 6 · **Interactive extracted:** 6 · **DOM nodes:** 571 · **Visits:** 2
- **Reached by:** Click 'content'
- **Screenshot:** [artifacts/N011_9dfb1c0f.png](artifacts/N011_9dfb1c0f.png)
- **DOM:** [artifacts/N011_9dfb1c0f.html](artifacts/N011_9dfb1c0f.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Content' | in_page_state | N038 Content | Samsung VXT CMS —  | — |
| Click 'ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo' | no_change | (self) | inert |
| Click 'Create Content' | no_change | (self) | inert |

## N012 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N012_5d156f05.png](artifacts/N012_5d156f05.png)
- **DOM:** [artifacts/N012_5d156f05.html](artifacts/N012_5d156f05.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: logo [#header_logo]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'div' | no_change | (self) | inert |
| Click 'logo' | navigation | N013 HOME | Samsung VXT CMS | — |
| Click 'logo' | navigation | N001 HOME | Samsung VXT CMS | — |

## N013 — HOME | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 1 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 336 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions' → Click 'logo'

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_keyboard_arrow"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocate Licenses [[data-testid="dashboard_planview0"]]
inferred_clickable: Allocation - [role=listitem[name="Allocation -"]]
inferred_clickable: Allocation -Used -Available - [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Available - [role=listitem[name="Available -"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Used - [role=listitem[name="Used -"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

## N014 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 142 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy'
- **Screenshot:** [artifacts/N014_74487e92.png](artifacts/N014_74487e92.png)
- **DOM:** [artifacts/N014_74487e92.html](artifacts/N014_74487e92.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [#alarmId > div.notific]
inferred_clickable: Version [#select]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'div' | in_page_state | N015 Privacy Policy | Samsung VXT | — |

## N015 — Privacy Policy | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 20 · **Interactive extracted:** 20 · **DOM nodes:** 937 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy' → Click 'div'
- **Screenshot:** [artifacts/N015_83af4c48.png](artifacts/N015_83af4c48.png)
- **DOM:** [artifacts/N015_83af4c48.html](artifacts/N015_83af4c48.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [#notiFilterStateId > button.btn_icon]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: (unnamed) [[data-testid="icon_notification_all"]]
inferred_clickable: All [#pc_filterRMStateId > div.select.select_btn]
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: Version 1.3 [#select]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
text_input: Search Functions or Screens [role=textbox[name="Search Functions or Screens"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'button' | in_page_state | N016 Privacy Policy | Samsung VXT | — |

## N016 — Privacy Policy | Samsung VXT CMS — div — button

- **URL:** https://www.samsungvx.com/privacy
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 1030 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy' → Click 'div' → Click 'button'
- **Screenshot:** [artifacts/N016_4d1221bf.png](artifacts/N016_4d1221bf.png)
- **DOM:** [artifacts/N016_4d1221bf.html](artifacts/N016_4d1221bf.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [#notiFilterStateId > button.btn_icon]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [#footer_rightPart_okBtn]
generic_button: Later [[data-testid="plan_dialog_later"]]
generic_button: Upgrade Now [[data-testid="plan_dialog_upgrade_now"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: (unnamed) [[data-testid="icon_notification_all"]]
inferred_clickable: All [#pc_filterRMStateId > div.select.select_btn]
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]]
inferred_clickable: logo [#header_logo]
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: Version 1.3 [#select]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
text_input: Search Functions or Screens [role=textbox[name="Search Functions or Screens"]]
```

## N017 — Cookie Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/cookie
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N017_cdd051e5.png](artifacts/N017_cdd051e5.png)
- **DOM:** [artifacts/N017_cdd051e5.html](artifacts/N017_cdd051e5.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: logo [#header_logo]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N018 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 9 · **Interactive extracted:** 9 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N018_b9728938.png](artifacts/N018_b9728938.png)
- **DOM:** [artifacts/N018_b9728938.html](artifacts/N018_b9728938.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: logo [#header_logo]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N019 — Settings | Samsung VXT CMS — button

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 43 · **Interactive extracted:** 43 · **DOM nodes:** 440 · **Visits:** 1
- **Reached by:** Click 'editHome' → Click 'button'
- **Screenshot:** [artifacts/N019_633d7bc1.png](artifacts/N019_633d7bc1.png)
- **DOM:** [artifacts/N019_633d7bc1.html](artifacts/N019_633d7bc1.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Apps [role=button[name="Apps"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
generic_button: Done [role=button[name="Done"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: No [role=button[name="No"]]
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]]
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: StorageUsed0.00KB [role=button[name="StorageUsed0.00KB"]]
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]]
generic_button: Yes [role=button[name="Yes"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Title [role=listitem[name="Title"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'No' | in_page_state | N004 Settings | Samsung VXT CMS | — |
| Click 'Yes' | in_page_state | N004 Settings | Samsung VXT CMS | — |

## N020 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'editHome' → Click 'Cancel'

_No actionable elements extracted._

## N021 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/sync/create
- **Type:** page · **Depth:** 1 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 452 · **Visits:** 1
- **Reached by:** Click 'div' → Click ''
- **Screenshot:** [artifacts/N021_b0742664.png](artifacts/N021_b0742664.png)
- **DOM:** [artifacts/N021_b0742664.html](artifacts/N021_b0742664.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Playlist [role=button[name="Playlist"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
```

## N022 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 430 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'General' → Click 'AppsN'

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
```

## N023 — Settings | Samsung VXT CMS — button

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 399 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'button'
- **Screenshot:** [artifacts/N023_f8b18d1e.png](artifacts/N023_f8b18d1e.png)
- **DOM:** [artifacts/N023_f8b18d1e.html](artifacts/N023_f8b18d1e.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Lock Plan [[data-testid="button_Lock Plan"]]
inferred_clickable: Merge Plan [[data-testid="button_Merge Plan"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Lock Plan' | in_page_state | N009 Settings | Samsung VXT CMS | mutating |
| Click 'Merge Plan' | in_page_state | N024 Settings | Samsung VXT CMS — | — |

## N024 — Settings | Samsung VXT CMS — button — Merge Plan

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 1 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 426 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'button' → Click 'Merge Plan'
- **Screenshot:** [artifacts/N024_d6dacd9a.png](artifacts/N024_d6dacd9a.png)
- **DOM:** [artifacts/N024_d6dacd9a.html](artifacts/N024_d6dacd9a.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [#footer_rightPart_cancelBtn]
generic_button: chatbot [#startChatBtn]
generic_button: Select [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

## N025 — Settings | Samsung VXT CMS — Add Workspace

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 442 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'Add Workspace'
- **Screenshot:** [artifacts/N025_2d53e1ad.png](artifacts/N025_2d53e1ad.png)
- **DOM:** [artifacts/N025_2d53e1ad.html](artifacts/N025_2d53e1ad.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add [[data-testid="undefined_apply"]]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [[data-testid="undefined_close"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [[data-testid="icon_search"]]
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
search: Search Workspaces [[data-testid="setting_screen_tv_channel_map_add_workspace_search"]]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N009 Settings | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N009 Settings | Samsung VXT CMS | — |
| Click 'div' | no_change | (self) | inert |

## N026 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 446 · **Visits:** 3
- **Reached by:** Click 'div' → Click 'div'
- **Screenshot:** [artifacts/N026_25f82ba2.png](artifacts/N026_25f82ba2.png)
- **DOM:** [artifacts/N026_25f82ba2.html](artifacts/N026_25f82ba2.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Upgrade Now' | in_page_state | N047 Settings | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Search for 'qa' | in_page_state | N050 Settings | Samsung VXT CMS | — |

## N027 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 1 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 583 · **Visits:** 2
- **Reached by:** Click 'div' → Click 'Activity Log'
- **Screenshot:** [artifacts/N027_f0b65c0e.png](artifacts/N027_f0b65c0e.png)
- **DOM:** [artifacts/N027_f0b65c0e.html](artifacts/N027_f0b65c0e.html)

**Action elements**

```
generic_button: Apply [[data-testid="setting_activity_log_apply"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Export [[data-testid="activity_btnExport"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="setting_activityLog_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: When [#sortColumn >> nth=0]
inferred_clickable: Where [#sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Logs [[data-testid="Activity Log_settingHeader_input"]]
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(1) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(2) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Apply' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'When' | no_change | (self) | inert |
| Search for 'qa' | no_change | (self) | inert |

## N028 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 558 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'Edit Home'

**Action elements**

```
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Done [role=button[name="Done"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: Title [role=listitem[name="Title"]]
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

## N029 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert
- **Type:** page · **Depth:** 1 · **Actionable:** 20 · **Interactive extracted:** 20 · **DOM nodes:** 462 · **Visits:** 2
- **Reached by:** Click 'div' → Click 'Emergency Alert'
- **Screenshot:** [artifacts/N029_b1ccf07d.png](artifacts/N029_b1ccf07d.png)
- **DOM:** [artifacts/N029_b1ccf07d.html](artifacts/N029_b1ccf07d.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

## N030 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 1 · **Actionable:** 22 · **Interactive extracted:** 22 · **DOM nodes:** 334 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3'
- **Screenshot:** [artifacts/N030_9316374e.png](artifacts/N030_9316374e.png)
- **DOM:** [artifacts/N030_9316374e.html](artifacts/N030_9316374e.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.undefined:nth-of-type(1)]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'General' | navigation | N031 Settings | Samsung VXT CMS — | — |
| Click 'Organization' | navigation | N032 Settings | Samsung VXT CMS | — |
| Click 'Plan' | navigation | N033 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N034 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N035 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N036 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N037 Settings | Samsung VXT CMS | — |
| Click 'General' | navigation | N051 Settings | Samsung VXT CMS | — |
| Click 'Organization' | navigation | N032 Settings | Samsung VXT CMS | — |
| Click 'Plan' | navigation | N033 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N034 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N035 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N036 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N037 Settings | Samsung VXT CMS | — |

## N031 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 442 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'General'
- **Screenshot:** [artifacts/N031_32974eeb.png](artifacts/N031_32974eeb.png)
- **DOM:** [artifacts/N031_32974eeb.html](artifacts/N031_32974eeb.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]]
inferred_clickable: 20:41 [[data-testid="select-Time Format"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: English [[data-testid="select-Language"]]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]]
inferred_clickable: Mon [[data-testid="select-First Day of Week"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: Phone Number [#phone_input]
text_input: Select [[data-testid="select-Country Code"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N051 Settings | Samsung VXT CMS | — |

## N032 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 1 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 547 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Organization'
- **Screenshot:** [artifacts/N032_0a52c664.png](artifacts/N032_0a52c664.png)
- **DOM:** [artifacts/N032_0a52c664.html](artifacts/N032_0a52c664.html)

**Action elements**

```
generic_button: Add [#add_phone_number]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Entertainment [[data-testid="select-Industry"]]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: Store Owner [[data-testid="select-CMS User"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: ~10 [[data-testid="select-Number of Employees"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_ORGANIZATION_NAME"]]
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_NAME"]]
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_EMAIL"]]
text_input: Register Phone Number [role=textbox[name="Register Phone Number"]]
text_input: Select [[data-testid="select-Country/Region"]]
form (inferred): submit=Add [#add_phone_number] fields=(contactName, contactEmail)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add' | in_page_state | N052 Settings | Samsung VXT CMS — | — |
| Click 'Customization' | in_page_state | N053 Settings | Samsung VXT CMS — | — |
| Click 'Entertainment' | no_change | (self) | inert |
| Click 'Information' | no_change | (self) | inert |
| Click 'Preset' | in_page_state | N054 Settings | Samsung VXT CMS — | — |

## N033 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 1 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 508 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Plan'
- **Screenshot:** [artifacts/N033_b812be49.png](artifacts/N033_b812be49.png)
- **DOM:** [artifacts/N033_b812be49.html](artifacts/N033_b812be49.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#liItemContents0 > div]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: 0 [#liItemContents2]
inferred_clickable: 2026-10-01 [#SubscriptionTable_nextPaymentDate]
inferred_clickable: 3 [#liItemContents1]
inferred_clickable: 3 [#liItemContents3]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Default Workspace [#liItemContents4]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1)]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: S Series Trial [#liItemContents0 > dl.dl-d > dt > span]
inferred_clickable: S Series TrialVX-TRIAL [#liItemContents0]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Register Activation Code' | in_page_state | N056 Settings | Samsung VXT CMS — | — |
| Click 'div' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click '2026-10-01' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N009 Settings | Samsung VXT CMS | — |
| Click 'Additional Plan' | in_page_state | N057 Settings | Samsung VXT CMS — | — |

## N034 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 1 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 464 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Screen Preset'
- **Screenshot:** [artifacts/N034_e6edbd3d.png](artifacts/N034_e6edbd3d.png)
- **DOM:** [artifacts/N034_e6edbd3d.html](artifacts/N034_e6edbd3d.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Certificate' | no_change | (self) | inert |
| Click 'Screen Profile' | no_change | (self) | inert |
| Click 'Screen Software' | no_change | (self) | inert |

## N035 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 1 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 500 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Tag'
- **Screenshot:** [artifacts/N035_5f88f3d7.png](artifacts/N035_5f88f3d7.png)
- **DOM:** [artifacts/N035_5f88f3d7.html](artifacts/N035_5f88f3d7.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Default TagsetRegion, Location, Subject, Others [#FcmsTable_liItemContents0]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents1]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N058 Settings | Samsung VXT CMS | — |
| Search for 'qa' | in_page_state | N059 Settings | Samsung VXT CMS | — |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N058 Settings | Samsung VXT CMS | — |

## N036 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 1 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 494 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User'
- **Screenshot:** [artifacts/N036_72f513cd.png](artifacts/N036_72f513cd.png)
- **DOM:** [artifacts/N036_72f513cd.html](artifacts/N036_72f513cd.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Invite User' | in_page_state | N060 Settings | Samsung VXT CMS — | mutating |
| Click 'more' | in_page_state | N061 Settings | Samsung VXT CMS — | mutating |
| Click 'div' | no_change | (self) | inert |
| Click 'Member' | blocked_mutation | (self) | mutating |
| Click 'No users.' | no_change | (self) | inert |
| Click 'Owner' | in_page_state | N063 Settings | Samsung VXT CMS — | mutating |
| Click 'Pending' | in_page_state | N064 Settings | Samsung VXT CMS — | — |
| Search for 'qa' | in_page_state | N064 Settings | Samsung VXT CMS — | — |

## N037 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 1 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 517 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Workspace'
- **Screenshot:** [artifacts/N037_1a2284f8.png](artifacts/N037_1a2284f8.png)
- **DOM:** [artifacts/N037_1a2284f8.html](artifacts/N037_1a2284f8.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: New Workspace [[data-testid="settings_workspace_new_add"]]
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: 0 [#FcmsTable_liItemContents2]
inferred_clickable: 0 [#FcmsTable_liItemContents4]
inferred_clickable: 0.00KB [#FcmsTable_liItemContents5]
inferred_clickable: 3 [#FcmsTable_liItemContents1]
inferred_clickable: 3 [#FcmsTable_liItemContents3]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Available [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Workspace' | blocked_mutation | (self) | mutating |
| Click 'div' | no_change | (self) | inert |
| Click '0' | navigation | N065 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N065 Settings | Samsung VXT CMS | — |
| Click '0.00KB' | navigation | N065 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N065 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N065 Settings | Samsung VXT CMS | — |
| Click 'Allocation' | no_change | (self) | inert |
| Click 'Default Workspace' | navigation | N065 Settings | Samsung VXT CMS | — |
| Search for 'qa' | in_page_state | N066 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N065 Settings | Samsung VXT CMS | — |

## N038 — Content | Samsung VXT CMS — Add Content

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 471 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content'
- **Screenshot:** [artifacts/N038_ea05bf14.png](artifacts/N038_ea05bf14.png)
- **DOM:** [artifacts/N038_ea05bf14.html](artifacts/N038_ea05bf14.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [role=button[name="Close"]]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Drop the image, video and document files here.OpenClose [role=button[name="Drop the image, video and document files here.OpenClose"]]
generic_button: Open [#non_add]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Close' | in_page_state | N011 Content | Samsung VXT CMS | — |
| Click 'Open' | file_chooser | (self) | upload |
| Click 'My Device' | no_change | (self) | inert |
| Click 'Ticker' | in_page_state | N039 Content | Samsung VXT CMS —  | — |
| Click 'Web(HTML)' | in_page_state | N040 Content | Samsung VXT CMS —  | — |
| Click 'Web(URL)' | in_page_state | N041 Content | Samsung VXT CMS —  | — |

## N039 — Content | Samsung VXT CMS — Add Content — Ticker

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 1267 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Ticker'
- **Screenshot:** [artifacts/N039_2d37650f.png](artifacts/N039_2d37650f.png)
- **DOM:** [artifacts/N039_2d37650f.html](artifacts/N039_2d37650f.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [#url_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#doneBtn] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [[data-testid="icon_ani_none"] >> nth=0]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(1) > div.relative > div.\#000000FF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(2) > div.relative > div.\#FFFFFFFF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(3) > div.relative > div.\#000000FF.border-radius4]
inferred_clickable: (unnamed) [div.flex.flexChildrenGrow:nth-of-type(3) > div.flex_col.flexChildrenGrow > div.w100.mb30:nth-of-type(5) > div.flex_col.flexChildrenGrow:nth-of-type(4) > div.relative > div.\#FFFFFFFF.border-radius4]
inferred_clickable: 90 [[data-testid="select_default"] >> nth=0]
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

## N040 — Content | Samsung VXT CMS — Add Content — Web(HTML)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 19 · **Interactive extracted:** 19 · **DOM nodes:** 544 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(HTML)'
- **Screenshot:** [artifacts/N040_2e47d2f0.png](artifacts/N040_2e47d2f0.png)
- **DOM:** [artifacts/N040_2e47d2f0.html](artifacts/N040_2e47d2f0.html)

**Action elements**

```
generic_button: (unnamed) [#web_tab_listbox]
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [#web_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#web_tab_btn_done] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: 1 hour [[data-testid="select-Refresh Interval"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
text_input: Content Name [#name]
text_input: Start Page [#page]
```

## N041 — Content | Samsung VXT CMS — Add Content — Web(URL)

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 17 · **Interactive extracted:** 17 · **DOM nodes:** 534 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'Add Content' → Click 'Web(URL)'
- **Screenshot:** [artifacts/N041_74a5c950.png](artifacts/N041_74a5c950.png)
- **DOM:** [artifacts/N041_74a5c950.html](artifacts/N041_74a5c950.html)

**Action elements**

```
generic_button: Add Content [[data-testid="content_noData_btnAdd"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [#url_tab_btn_close]
generic_button: ContentBuy Nowsouresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.comCHITNU TEAMDefault Workspace .st0{opacity:0.8;} ScreenCo [#container]
generic_button: Create Content [[data-testid="content_noData_btnCreate"]]
generic_button: Done [#doneBtn] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: 1 hour [[data-testid="select-Refresh Interval"]]
inferred_clickable: My Device [#content_upload_tabDevice]
inferred_clickable: Ticker [#content_upload_tabTicker]
inferred_clickable: Web(HTML) [#content_upload_tabHtml]
inferred_clickable: Web(URL) [#content_upload_tabUrl]
text_input: Address [#address]
text_input: Content Name [#name]
```

## N042 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 2 · **Actionable:** 155 · **Interactive extracted:** 155 · **DOM nodes:** 1086 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'General' → Click 'AppsN'
- **Screenshot:** [artifacts/N042_2f782785.png](artifacts/N042_2f782785.png)
- **DOM:** [artifacts/N042_2f782785.html](artifacts/N042_2f782785.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
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
inferred_clickable: AI CorpPostAI CorpPostBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI Image UpscalerAI Image UpscalerBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]]
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
inferred_clickable: CalendarCalendarProductivity [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData Sync [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: DropboxDropbox [div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: EWQ SuperQueueEWQ SuperQueue [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Google DriveGoogle Drive [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Image GeneratorImage GeneratorBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: LDSK EnterpriseLDSK Enterprise [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Link My POSLink My POS [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: logo [#header_logo]
inferred_clickable: Microsoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft OneDriveMicrosoft OneDrive [div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft PowerPoint enables you to instantly play dynamic slideshow. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
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
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
inferred_clickable: ShadowGenShadowGenBETA [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'img' | in_page_state | N043 Samsung VXT CMS — img | — |

## N043 — Samsung VXT CMS — img

- **URL:** https://www.samsungvx.com/apps
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 173 · **Interactive extracted:** 173 · **DOM nodes:** 1796 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'General' → Click 'AppsN' → Click 'img'
- **Screenshot:** [artifacts/N043_48e6e9b3.png](artifacts/N043_48e6e9b3.png)
- **DOM:** [artifacts/N043_48e6e9b3.html](artifacts/N043_48e6e9b3.html)

**Action elements**

```
disclosure: Africa [role=button[name="Africa"]]
disclosure: Asia [role=button[name="Asia"]]
disclosure: Europe [role=button[name="Europe"]]
disclosure: North America [role=button[name="North America"]]
disclosure: Oceania [role=button[name="Oceania"]]
disclosure: South America [role=button[name="South America"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Install [role=button[name="Install"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
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
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_left"] >> nth=0]
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
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI CorpPostAI CorpPostBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI Image UpscalerAI Image UpscalerBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: CalendarCalendar [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: CalendarCalendarProductivity [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap]
inferred_clickable: Content [[data-testid="navbar_li_content"]]
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData Sync [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Data SyncData Sync [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div > div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: DropboxDropbox [div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: EWQ SuperQueueEWQ SuperQueue [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Google DriveGoogle Drive [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Image GeneratorImage GeneratorBETA [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: LDSK EnterpriseLDSK Enterprise [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Link My POSLink My POS [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: logo [#header_logo]
inferred_clickable: Microsoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft ExcelMicrosoft Excel [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft OneDriveMicrosoft OneDrive [div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Microsoft PowerPoint enables you to instantly play dynamic slideshow. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft SharePoint enables you to effortlessly share and collaborate on news posts with your team. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
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
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: Ngine AutomotiveNgine Automotive [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Ngine Real EstateNgine Real Estate [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Productivity [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]]
inferred_clickable: ShadowGenShadowGenBETA [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Africa' | no_change | (self) | inert |

## N044 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** page · **Depth:** 2 · **Actionable:** 21 · **Interactive extracted:** 21 · **DOM nodes:** 290 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'Tech Inquiry'
- **Screenshot:** [artifacts/N044_4e1312b6.png](artifacts/N044_4e1312b6.png)
- **DOM:** [artifacts/N044_4e1312b6.html](artifacts/N044_4e1312b6.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: New Inquiry [role=button[name="New Inquiry"]]
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |
| Click 'Tech Inquiry Permissions' | in_page_state | N046 Settings | Samsung VXT CMS — | — |
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |

## N045 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** page · **Depth:** 2 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 448 · **Visits:** 2
- **Reached by:** Click 'div' → Click 'Tech Inquiry' → Click 'New Inquiry'
- **Screenshot:** [artifacts/N045_a64e2bb9.png](artifacts/N045_a64e2bb9.png)
- **DOM:** [artifacts/N045_a64e2bb9.html](artifacts/N045_a64e2bb9.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]]
generic_button: Open [role=button[name="Open"]]
generic_button: Request [role=button[name="Request"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: Enter a subject. [role=textbox[name="Enter a subject."]]
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Drop the files here to attach.' | no_change | (self) | inert |
| Click 'Open' | file_chooser | (self) | upload |
| Click 'Register Phone Number' | in_page_state | N067 Settings | Samsung VXT CMS — | — |
| Click 'Select' | no_change | (self) | inert |

## N046 — Settings | Samsung VXT CMS — Tech Inquiry Permissions

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 373 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'Tech Inquiry' → Click 'Tech Inquiry Permissions'
- **Screenshot:** [artifacts/N046_af93aeda.png](artifacts/N046_af93aeda.png)
- **DOM:** [artifacts/N046_af93aeda.html](artifacts/N046_af93aeda.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [#footer_rightPart_cancelBtn]
generic_button: chatbot [#startChatBtn]
generic_button: New Inquiry [role=button[name="New Inquiry"]]
generic_button: Save [#footer_rightPart_okBtn] (disabled)
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#modal_pop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: All Users [[data-testid="select_default"] >> nth=0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner and Admin [[data-testid="select_default"] >> nth=0]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N044 Settings | Samsung VXT CMS | mutating |
| Click 'div' | in_page_state | N044 Settings | Samsung VXT CMS | mutating |
| Click 'All Users' | no_change | (self) | inert |

## N047 — Settings | Samsung VXT CMS — Upgrade Now

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 394 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'div' → Click 'Upgrade Now'
- **Screenshot:** [artifacts/N047_76b0ae57.png](artifacts/N047_76b0ae57.png)
- **DOM:** [artifacts/N047_76b0ae57.html](artifacts/N047_76b0ae57.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Later [[data-testid="plan_dialog_later"]]
generic_button: Upgrade Now [[data-testid="plan_dialog_upgrade_now"]]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Later' | in_page_state | N048 Settings | Samsung VXT CMS — | — |
| Click 'Upgrade Now' | in_page_state | N049 Settings | Samsung VXT CMS — | mutating, error |

## N048 — Settings | Samsung VXT CMS — Upgrade Now — Later

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 516 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'div' → Click 'Upgrade Now' → Click 'Later'
- **Screenshot:** [artifacts/N048_fa8fd9ea.png](artifacts/N048_fa8fd9ea.png)
- **DOM:** [artifacts/N048_fa8fd9ea.html](artifacts/N048_fa8fd9ea.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Later [#plan_dialog_right_footer_btn_0]
generic_button: Try Now [#plan_dialog_right_footer_btn_1]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

## N049 — Settings | Samsung VXT CMS — Upgrade Now — Upgrade Now

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 2 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 377 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'div' → Click 'Upgrade Now' → Click 'Upgrade Now'
- **Screenshot:** [artifacts/N049_366a8083.png](artifacts/N049_366a8083.png)
- **DOM:** [artifacts/N049_366a8083.html](artifacts/N049_366a8083.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: OK [#plan_dialog_right_footer_btn_0]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

## N050 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'div' → Search for 'qa'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Date Updated [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Event [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Type [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

## N051 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings
- **Type:** page · **Depth:** 2 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 530 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'General'
- **Screenshot:** [artifacts/N051_deeee9fc.png](artifacts/N051_deeee9fc.png)
- **DOM:** [artifacts/N051_deeee9fc.html](artifacts/N051_deeee9fc.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]]
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]]
inferred_clickable: 20:41 [[data-testid="select-Time Format"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: English [[data-testid="select-Language"]]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]]
inferred_clickable: Mon [[data-testid="select-First Day of Week"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click '2022-04-19' | no_change | (self) | inert |
| Click '20:41' | no_change | (self) | inert |
| Click 'English' | no_change | (self) | inert |
| Click 'Exhibition' | no_change | (self) | inert |
| Click 'Register Phone Number' | in_page_state | N031 Settings | Samsung VXT CMS — | — |

## N052 — Settings | Samsung VXT CMS — Add

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 40 · **Interactive extracted:** 40 · **DOM nodes:** 461 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Organization' → Click 'Add'
- **Screenshot:** [artifacts/N052_a7d59e53.png](artifacts/N052_a7d59e53.png)
- **DOM:** [artifacts/N052_a7d59e53.html](artifacts/N052_a7d59e53.html)

**Action elements**

```
generic_button: Add [#add_phone_number]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Entertainment [[data-testid="select-Industry"]]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: Store Owner [[data-testid="select-CMS User"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: ~10 [[data-testid="select-Number of Employees"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_ORGANIZATION_NAME"]]
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_NAME"]]
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_EMAIL"]]
text_input: Phone Number [#phone_input]
text_input: Register Phone Number [role=textbox[name="Register Phone Number"]]
text_input: Select [[data-testid="select-Country/Region"]]
text_input: Select [[data-testid="select-Country Code"]]
form (inferred): submit=Add [#add_phone_number] fields=(contactName, contactEmail)
```

## N053 — Settings | Samsung VXT CMS — Customization

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 897 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Organization' → Click 'Customization'
- **Screenshot:** [artifacts/N053_edcba170.png](artifacts/N053_edcba170.png)
- **DOM:** [artifacts/N053_edcba170.html](artifacts/N053_edcba170.html)

**Action elements**

```
disclosure: Admin Privilege ControlUpgrade Now [role=button[name="Admin Privilege ControlUpgrade Now"]]
disclosure: App Splash Logo [role=button[name="App Splash Logo"]]
disclosure: Content Embargo & LifespanUpgrade Now [role=button[name="Content Embargo & LifespanUpgrade Now"]]
disclosure: Default Content [role=button[name="Default Content"]]
disclosure: Screen Custom FieldsUpgrade Now [role=button[name="Screen Custom FieldsUpgrade Now"]]
generic_button: Apply [role=button[name="Apply"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > div.flex_col.gap20px:nth-of-type(3) > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'App Splash Logo' | no_change | (self) | inert |
| Click 'Default Content' | no_change | (self) | inert |

## N054 — Settings | Samsung VXT CMS — Preset

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 423 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Organization' → Click 'Preset'
- **Screenshot:** [artifacts/N054_98965430.png](artifacts/N054_98965430.png)
- **DOM:** [artifacts/N054_98965430.html](artifacts/N054_98965430.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Android [role=listitem[name="Android"]]
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: E-Paper [role=listitem[name="E-Paper"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Flip [role=listitem[name="Flip"]]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Indoor LED Signage [role=listitem[name="Indoor LED Signage"]]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Legacy [role=listitem[name="Legacy"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: Signage [role=listitem[name="Signage"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Windows [role=listitem[name="Windows"]]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Upgrade Now' | in_page_state | N055 Settings | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |

## N055 — Settings | Samsung VXT CMS — Preset — Upgrade Now

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 43 · **Interactive extracted:** 43 · **DOM nodes:** 516 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Organization' → Click 'Preset' → Click 'Upgrade Now'
- **Screenshot:** [artifacts/N055_d36da5c9.png](artifacts/N055_d36da5c9.png)
- **DOM:** [artifacts/N055_d36da5c9.html](artifacts/N055_d36da5c9.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Later [[data-testid="plan_dialog_later"]]
generic_button: Upgrade Now [[data-testid="plan_dialog_upgrade_now"]]
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Android [role=listitem[name="Android"]]
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: E-Paper [role=listitem[name="E-Paper"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Flip [role=listitem[name="Flip"]]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Indoor LED Signage [role=listitem[name="Indoor LED Signage"]]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Legacy [role=listitem[name="Legacy"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: Signage [role=listitem[name="Signage"]]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Windows [role=listitem[name="Windows"]]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

## N056 — Settings | Samsung VXT CMS — Register Activation Code

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 44 · **Interactive extracted:** 44 · **DOM nodes:** 382 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Plan' → Click 'Register Activation Code'
- **Screenshot:** [artifacts/N056_962a56af.png](artifacts/N056_962a56af.png)
- **DOM:** [artifacts/N056_962a56af.html](artifacts/N056_962a56af.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [#footer_rightPart_cancelBtn]
generic_button: chatbot [#startChatBtn]
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
generic_button: Register Now [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#liItemContents0 > div]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: .st0{opacity:0.8;} How to get your activation code [role=listitem[name=".st0{opacity:0.8;} How to get your activation code"]]
inferred_clickable: 0 [#liItemContents2]
inferred_clickable: 2026-10-01 [#SubscriptionTable_nextPaymentDate]
inferred_clickable: 3 [#liItemContents1]
inferred_clickable: 3 [#liItemContents3]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Default Workspace [#liItemContents4]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1)]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: S Series Trial [#liItemContents0 > dl.dl-d > dt > span]
inferred_clickable: S Series TrialVX-TRIAL [#liItemContents0]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
textarea: (unnamed) [#modalpop_wrap > div.pop_con.pop-slide:nth-of-type(2) > div:nth-of-type(1) > div.flex_col.w100 > div:nth-of-type(2) > textarea]
```

## N057 — Settings | Samsung VXT CMS — Additional Plan

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 2 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 334 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Plan' → Click 'Additional Plan'
- **Screenshot:** [artifacts/N057_7cd1a015.png](artifacts/N057_7cd1a015.png)
- **DOM:** [artifacts/N057_7cd1a015.html](artifacts/N057_7cd1a015.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: No Plans [[data-testid="No Plans"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'No Plans' | no_change | (self) | inert |

## N058 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 2 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 740 · **Visits:** 2
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others'
- **Screenshot:** [artifacts/N058_3fb8be69.png](artifacts/N058_3fb8be69.png)
- **DOM:** [artifacts/N058_3fb8be69.html](artifacts/N058_3fb8be69.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'checkbox' | in_page_state | N068 Settings | Samsung VXT CMS — | — |

## N059 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 2 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 305 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Tag' → Search for 'qa'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: No tag. [[data-testid="No tag."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]]
```

## N060 — Settings | Samsung VXT CMS — Invite User

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 412 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User' → Click 'Invite User'
- **Screenshot:** [artifacts/N060_9d353c06.png](artifacts/N060_9d353c06.png)
- **DOM:** [artifacts/N060_9d353c06.html](artifacts/N060_9d353c06.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [[data-testid="setting_user_new_invite_cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Invite [[data-testid="setting_user_new_invite_ok"]]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Admin [#select]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
radio: As Other Roles [#radio_label2]
radio: As Owner [#radio_label]
search: Search Users [[data-testid="User_settingHeader_input"]]
text_input: Enter the email address of the Samsung account. [[data-testid="setting_user_new_invite_email"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N036 Settings | Samsung VXT CMS | mutating |

## N061 — Settings | Samsung VXT CMS — more

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 358 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User' → Click 'more'
- **Screenshot:** [artifacts/N061_cce32ed0.png](artifacts/N061_cce32ed0.png)
- **DOM:** [artifacts/N061_cce32ed0.html](artifacts/N061_cce32ed0.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: Export [#topOption_li_setting_user_more_export]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Export' | in_page_state | N062 Settings | Samsung VXT CMS — | mutating |

## N062 — Settings | Samsung VXT CMS — more — Export

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 377 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User' → Click 'more' → Click 'Export'
- **Screenshot:** [artifacts/N062_56eca44c.png](artifacts/N062_56eca44c.png)
- **DOM:** [artifacts/N062_56eca44c.html](artifacts/N062_56eca44c.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Close [[data-testid="setting_user_more_export_close"]]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

## N063 — Settings | Samsung VXT CMS — Owner

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 370 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User' → Click 'Owner'
- **Screenshot:** [artifacts/N063_ceb21b66.png](artifacts/N063_ceb21b66.png)
- **DOM:** [artifacts/N063_ceb21b66.html](artifacts/N063_ceb21b66.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_more"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |

## N064 — Settings | Samsung VXT CMS — Pending

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 344 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'User' → Click 'Pending'
- **Screenshot:** [artifacts/N064_aec17667.png](artifacts/N064_aec17667.png)
- **DOM:** [artifacts/N064_aec17667.html](artifacts/N064_aec17667.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Date Sent [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Date Sent' | no_change | (self) | inert |

## N065 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 2 · **Actionable:** 40 · **Interactive extracted:** 40 · **DOM nodes:** 442 · **Visits:** 7
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Workspace' → Click '0'
- **Screenshot:** [artifacts/N065_204df71d.png](artifacts/N065_204df71d.png)
- **DOM:** [artifacts/N065_204df71d.html](artifacts/N065_204df71d.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: 0 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_planundefined"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Learn more' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'span' | in_page_state | N069 Settings | Samsung VXT CMS — | — |

## N066 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 2 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 368 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Workspace' → Search for 'qa'

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Available [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: No workspaces. [[data-testid="No workspaces."]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]]
```

## N067 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 475 · **Visits:** 1
- **Reached by:** Click 'div' → Click 'Tech Inquiry' → Click 'New Inquiry' → Click 'Register Phone Number'
- **Screenshot:** [artifacts/N067_ddbc8469.png](artifacts/N067_ddbc8469.png)
- **DOM:** [artifacts/N067_ddbc8469.html](artifacts/N067_ddbc8469.html)

**Action elements**

```
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]]
generic_button: chatbot [#startChatBtn]
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]]
generic_button: Open [role=button[name="Open"]]
generic_button: Request [role=button[name="Request"]]
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: Enter a subject. [role=textbox[name="Enter a subject."]]
text_input: Phone Number [#phone_input]
text_input: Select [[data-testid="select-Country Code"]]
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]]
```

## N068 — Settings | Samsung VXT CMS — checkbox

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 715 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'checkbox'
- **Screenshot:** [artifacts/N068_f05a424c.png](artifacts/N068_f05a424c.png)
- **DOM:** [artifacts/N068_f05a424c.html](artifacts/N068_f05a424c.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
destructive: Remove Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: Workspace [#settingNavbar_li_place]
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

## N069 — Settings | Samsung VXT CMS — span

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 429 · **Visits:** 1
- **Reached by:** Click 'Allocation 3Used 0Available 3' → Click 'Workspace' → Click '0' → Click 'span'
- **Screenshot:** [artifacts/N069_c6920b15.png](artifacts/N069_c6920b15.png)
- **DOM:** [artifacts/N069_c6920b15.html](artifacts/N069_c6920b15.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_notific_solidation"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: 0 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Activity Log [#settingNavbar_li_activityLog]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_planundefined"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Edit Home [#settingNavbar_li_editHome]
inferred_clickable: Emergency Alert [#settingNavbar_li_alert]
inferred_clickable: Event [#settingNavbar_li_event]
inferred_clickable: General [#settingNavbar_li_general]
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: Organization [#settingNavbar_li_organization]
inferred_clickable: Plan [#settingNavbar_li_plan]
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Screen Preset [#settingNavbar_li_screenPreset]
inferred_clickable: Tag [#settingNavbar_li_tag]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: User [#settingNavbar_li_user]
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: Workspace [#settingNavbar_li_place]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: Default Workspace [[data-testid="FCMSInput"]]
```

