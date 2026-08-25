# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T20:01:03+00:00  
**States:** 90 · **Transitions:** 248 · **Actionable elements:** 4387 of 4387 extracted

## N001 — HOME | Samsung VXT CMS *(entry)*

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 45 · **Interactive extracted:** 45 · **DOM nodes:** 430 · **Visits:** 1
- **Reached by:** entry point
- **Screenshot:** [artifacts/N001_4792e46f.png](artifacts/N001_4792e46f.png)
- **DOM:** [artifacts/N001_4792e46f.html](artifacts/N001_4792e46f.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Plan Notice [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click '.st0{opacity:0.8;}' | in_page_state | N003 HOME | Samsung VXT CMS — .st | mutating |
| Click 'Screen' | navigation | N004 Screen | Samsung VXT CMS | mutating |
| Click 'Content' | navigation | N005 Content | Samsung VXT CMS | mutating |
| Click 'Playlist' | navigation | N006 Playlist | Samsung VXT CMS | mutating |
| Click 'Schedule' | navigation | N007 Schedule | Samsung VXT CMS | mutating |
| Click 'New' | in_page_state | N008 HOME | Samsung VXT CMS — New | mutating |
| Click 'New' | in_page_state | N009 HOME | Samsung VXT CMS — New | mutating |
| Click 'New' | in_page_state | N010 HOME | Samsung VXT CMS — New | — |
| Click 'New' | no_change | (self) | inert |
| Click 'screen' | navigation | N004 Screen | Samsung VXT CMS | — |
| Click 'content' | navigation | N005 Content | Samsung VXT CMS | — |
| Click 'playlist' | navigation | N006 Playlist | Samsung VXT CMS | — |
| Click 'schedule' | navigation | N007 Schedule | Samsung VXT CMS | mutating |
| Click 'PROAllocation 3Used 0Available 3' | navigation | N011 Settings | Samsung VXT CMS | mutating |
| Click 'PRO' | navigation | N011 Settings | Samsung VXT CMS | mutating |
| Click 'PRO' | navigation | N011 Settings | Samsung VXT CMS | mutating |
| Click 'div' | navigation | N011 Settings | Samsung VXT CMS | mutating |
| Click 'Plan Notice' | in_page_state | N012 HOME | Samsung VXT CMS — Pla | mutating |
| Click 'Allocation 3Used 0Available 3' | navigation | N011 Settings | Samsung VXT CMS | mutating |
| Click 'Normal-' | blocked_mutation | (self) | mutating |
| Click 'Warning-' | blocked_mutation | (self) | mutating |
| Click 'Deactivated-' | blocked_mutation | (self) | mutating |
| Click 'div' | blocked_mutation | (self) | mutating |
| Click 'refresh' | no_change | (self) | inert |
| Click 'logo' | blocked_mutation | (self) | mutating |
| Click 'img' | blocked_mutation | (self) | mutating |
| Click 'Buy Now' | blocked_mutation | (self) | mutating |
| Click 'VXT Labs' | navigation | N013 Samsung VXT CMS | — |
| Click 'Notification' | in_page_state | (self) | mutating, state-cap |
| Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' | in_page_state | (self) | mutating, state-cap |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | (self) | mutating, state-cap |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | (self) | state-cap |
| Click 'chatbot' | in_page_state | (self) | mutating, state-cap |
| Click 'Terms and Conditions' | navigation | N014 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N015 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N016 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N017 Samsung VXT CMS | — |
| Click 'Screen' | navigation | N004 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N027 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N029 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N031 Schedule | Samsung VXT CMS | — |
| Click 'content' | navigation | N021 Content | Samsung VXT CMS | — |
| Click 'playlist' | navigation | N034 Playlist | Samsung VXT CMS | — |
| Click 'schedule' | navigation | N023 Schedule | Samsung VXT CMS | — |
| Click 'PROAllocation 3Used 0Available 3' | navigation | N011 Settings | Samsung VXT CMS | — |
| Click 'VXT Labs' | navigation | N013 Samsung VXT CMS | — |

## N002 — vxt.samsung.com

- **URL:** https://vxt.samsung.com/contact-us
- **Type:** boundary · **Depth:** 0 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** n/a · **Visits:** 6
- **Reached by:** Click 'Contact Us'

_No actionable elements extracted._

## N003 — HOME | Samsung VXT CMS — .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 46 · **Interactive extracted:** 46 · **DOM nodes:** 434 · **Visits:** 1
- **Reached by:** Click '.st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N003_0331e0df.png](artifacts/N003_0331e0df.png)
- **DOM:** [artifacts/N003_0331e0df.html](artifacts/N003_0331e0df.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace [[data-testid="dashboardPlaces_liPlaces_Item0"]] (main area, top-centre)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Plan Notice [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Not exercised by the crawler**

- inferred_clickable: Default Workspace -- queued for depth 1
- inferred_clickable: Default Workspace -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: Default Workspace -- queued for depth 1

## N004 — Screen | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 0 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 552 · **Visits:** 3
- **Reached by:** Click 'Screen'
- **Screenshot:** [artifacts/N004_cf8c2d76.png](artifacts/N004_cf8c2d76.png)
- **DOM:** [artifacts/N004_cf8c2d76.html](artifacts/N004_cf8c2d76.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left)
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, middle-left)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, middle-left)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (left sidebar, middle-left)
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, middle-left)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Screen' | in_page_state | N018 Screen | Samsung VXT CMS — A | mutating |
| Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' | in_page_state | N019 Screen | Samsung VXT CMS — C | mutating |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N019 Screen | Samsung VXT CMS — C | — |
| Click 'Screen' | in_page_state | N020 Screen | Samsung VXT CMS — S | — |
| Click 'div' | no_change | (self) | inert |
| Click 'Content' | navigation | N021 Content | Samsung VXT CMS | — |
| Click 'div' | navigation | N021 Content | Samsung VXT CMS | — |
| Click 'Content' | navigation | N021 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N022 Playlist | Samsung VXT CMS | — |
| Click 'div' | navigation | N022 Playlist | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N022 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N023 Schedule | Samsung VXT CMS | — |
| Click 'div' | navigation | N023 Schedule | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N023 Schedule | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N024 Channel | Samsung VXT CMS | — |
| Click 'div' | navigation | N024 Channel | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N024 Channel | Samsung VXT CMS | — |
| Click 'div' | navigation | N024 Channel | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N025 Screen | Samsung VXT CMS — d | — |
| Click 'AppsN' | navigation | N026 Samsung VXT CMS | — |
| Click 'div' | navigation | N026 Samsung VXT CMS | — |
| Click 'AppsN' | navigation | N026 Samsung VXT CMS | — |
| Click 'Screen' | navigation | (self) | — |
| Click 'Content' | navigation | N021 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N022 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N023 Schedule | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N024 Channel | Samsung VXT CMS | — |
| Click 'AppsN' | navigation | N026 Samsung VXT CMS | — |

## N005 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 70 · **Interactive extracted:** 70 · **DOM nodes:** 673 · **Visits:** 2
- **Reached by:** Click 'Content'

**Action elements**

```
checkbox: (unnamed) [[data-testid="content_card_checkbox_0"]] (main area, top-left)
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_card_more_0"]] (main area, top-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]] (header, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-left)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]] (header, top-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

## N006 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 0 · **Actionable:** 70 · **Interactive extracted:** 70 · **DOM nodes:** 654 · **Visits:** 2
- **Reached by:** Click 'Playlist'

**Action elements**

```
checkbox: (unnamed) [[data-testid="playlistCard_checkbox_0"]] (main area, top-left)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="playlist_card_more_0"]] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]] (header, top-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

## N007 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 0 · **Actionable:** 64 · **Interactive extracted:** 64 · **DOM nodes:** 619 · **Visits:** 2
- **Reached by:** Click 'Schedule'

**Action elements**

```
checkbox: (unnamed) [[data-testid="schedule_card_checkbox_0"]] (main area, top-left)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="FcmsCardMoreButton"]] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 schedule [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 schedule [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

## N008 — HOME | Samsung VXT CMS — New

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 439 · **Visits:** 1
- **Reached by:** Click 'New'
- **Screenshot:** [artifacts/N008_37849a15.png](artifacts/N008_37849a15.png)
- **DOM:** [artifacts/N008_37849a15.html](artifacts/N008_37849a15.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Add Screen [[data-testid="dashboard_screen_addbtn_addscreen"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Screen Wall [[data-testid="dashboard_screen_addbtn_newscreenwall"]] (main area, top-centre)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Plan Notice [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Not exercised by the crawler**

- inferred_clickable: Add Screen -- queued for depth 1
- inferred_clickable: New Screen Wall -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1

## N009 — HOME | Samsung VXT CMS — New

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 438 · **Visits:** 1
- **Reached by:** Click 'New'
- **Screenshot:** [artifacts/N009_fff58205.png](artifacts/N009_fff58205.png)
- **DOM:** [artifacts/N009_fff58205.html](artifacts/N009_fff58205.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Add Content [[data-testid="dashboard_content_addbtn_addcontent"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Create Content [[data-testid="dashboard_content_addbtn_createcontent"]] (main area, top-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Plan Notice [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Not exercised by the crawler**

- inferred_clickable: Create Content -- queued for depth 1
- inferred_clickable: Add Content -- queued for depth 1

## N010 — HOME | Samsung VXT CMS — New

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 441 · **Visits:** 1
- **Reached by:** Click 'New'
- **Screenshot:** [artifacts/N010_38471b41.png](artifacts/N010_38471b41.png)
- **DOM:** [artifacts/N010_38471b41.html](artifacts/N010_38471b41.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: (unnamed) [#root > div.add-btn-popover:nth-of-type(4) > ul.select-ul.openNew-list > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: General [[data-testid="dashboard_playlist_addbtn_general"]] (main area, top-right)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Plan Notice [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Sync Play [[data-testid="dashboard_playlist_addbtn_syncplay"]] (main area, top-right)
inferred_clickable: Takeover Sync Play [[data-testid="dashboard_playlist_addbtn_takeoversyncplay"]] (main area, top-right)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Not exercised by the crawler**

- inferred_clickable: General -- queued for depth 1
- inferred_clickable: Sync Play -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: Takeover Sync Play -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1

## N011 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 0 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 537 · **Visits:** 6
- **Reached by:** Click 'PROAllocation 3Used 0Available 3'
- **Screenshot:** [artifacts/N011_b7d3a3a7.png](artifacts/N011_b7d3a3a7.png)
- **DOM:** [artifacts/N011_b7d3a3a7.html](artifacts/N011_b7d3a3a7.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled) (main area, bottom-centre)
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: More [#ModalFooter_btnMore] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left)
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: (unnamed) [#ProCard_statusColor] (main area, bottom-centre)
inferred_clickable: 0 [role=listitem[name="0"]] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left)
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation] (main area, bottom-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]] (main area, bottom-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left)
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left)
inferred_clickable: Finish Trial [[data-testid="icon_close"]] (main area, bottom-right)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left)
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed] (main area, bottom-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left)
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace] (main area, bottom-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input] (main area, bottom-centre)
text_input: Allocable [#input_text2] (disabled) (main area, bottom-centre)
text_input: Allocated [#input_text1] (disabled) (main area, bottom-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | navigation | N037 HOME | Samsung VXT CMS | — |
| Click 'General' | navigation | N038 Settings | Samsung VXT CMS | — |
| Click 'button' | in_page_state | N039 Settings | Samsung VXT CMS — | — |
| Click 'Tech Inquiry' | navigation | N047 Settings | Samsung VXT CMS | — |
| Click 'General' | navigation | N038 Settings | Samsung VXT CMS | — |
| Click 'button' | navigation | N039 Settings | Samsung VXT CMS — | — |

## N012 — HOME | Samsung VXT CMS — Plan Notice

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 466 · **Visits:** 1
- **Reached by:** Click 'Plan Notice'
- **Screenshot:** [artifacts/N012_a1676fd0.png](artifacts/N012_a1676fd0.png)
- **DOM:** [artifacts/N012_a1676fd0.html](artifacts/N012_a1676fd0.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (main area, middle-left)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: (unnamed) [#root > div.popper-container:nth-of-type(4) > ul > li:nth-of-type(2)] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, middle-left)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- generic_button: Upgrade Now -- queued for depth 1

## N013 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 532 · **Visits:** 2
- **Reached by:** Click 'VXT Labs'
- **Screenshot:** [artifacts/N013_f04fa4aa.png](artifacts/N013_f04fa4aa.png)
- **DOM:** [artifacts/N013_f04fa4aa.html](artifacts/N013_f04fa4aa.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-centre)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-centre)
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: Back [[data-testid="icon_back"]] (header, top-left)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, bottom-left)
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)] (main area, bottom-left)
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, bottom-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | navigation | N040 Samsung VXT CMS | mutating |
| Click 'NEW' | in_page_state | N041 Samsung VXT CMS — SmartPlug | — |
| Click 'img' | in_page_state | N041 Samsung VXT CMS — SmartPlug | — |
| Click 'BETA' | in_page_state | N041 Samsung VXT CMS — SmartPlug | — |
| Click 'SmartPlug' | in_page_state | N041 Samsung VXT CMS — SmartPlug | — |
| Click 'img' | no_change | (self) | inert |
| Click 'img' | in_page_state | N042 Samsung VXT CMS — img | — |
| Click 'img' | in_page_state | (self) | state-cap |
| Click 'img' | in_page_state | (self) | state-cap |
| Click 'img' | in_page_state | (self) | state-cap |
| Click 'ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly' | in_page_state | (self) | state-cap |
| Click 'ShadowGen' | in_page_state | (self) | state-cap |
| Click 'AI Image Upscaler' | no_change | (self) | inert |
| Click 'AI Writing Assistant' | in_page_state | (self) | state-cap |
| Click 'Image Generator' | in_page_state | (self) | state-cap |
| Click 'AI CorpPost' | in_page_state | (self) | state-cap |
| Click '' | navigation | N011 Settings | Samsung VXT CMS | — |

## N014 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 164 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N014_9b254a0e.png](artifacts/N014_9b254a0e.png)
- **DOM:** [artifacts/N014_9b254a0e.html](artifacts/N014_9b254a0e.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N015 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 167 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy'
- **Screenshot:** [artifacts/N015_37cf2bb8.png](artifacts/N015_37cf2bb8.png)
- **DOM:** [artifacts/N015_37cf2bb8.html](artifacts/N015_37cf2bb8.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Version 1.3 [#select] (main area, top-right)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Version 1.3' | no_change | (self) | inert |

## N016 — Cookie Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/cookie
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N016_868a41ac.png](artifacts/N016_868a41ac.png)
- **DOM:** [artifacts/N016_868a41ac.html](artifacts/N016_868a41ac.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N017 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N017_e4b14cd7.png](artifacts/N017_e4b14cd7.png)
- **DOM:** [artifacts/N017_e4b14cd7.html](artifacts/N017_e4b14cd7.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N018 — Screen | Samsung VXT CMS — Add Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 484 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen'
- **Screenshot:** [artifacts/N018_105670e6.png](artifacts/N018_105670e6.png)
- **DOM:** [artifacts/N018_105670e6.html](artifacts/N018_105670e6.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Close [#footer_rightPart_okBtn] (main area, bottom-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (left sidebar, middle-left)
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Samsung Screen [[data-testid="screen_addscreen_smg_screen"]] (main area, middle-centre)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Virtual Screen [[data-testid="screen_addscreen_virtual_screen"]] (main area, middle-centre)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
```

**Not exercised by the crawler**

- inferred_clickable: Samsung Screen -- queued for depth 2
- inferred_clickable: Virtual Screen -- queued for depth 2
- generic_button: Close -- queued for depth 2

## N019 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 469 · **Visits:** 2
- **Reached by:** Click 'Screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N019_67784b26.png](artifacts/N019_67784b26.png)
- **DOM:** [artifacts/N019_67784b26.html](artifacts/N019_67784b26.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [#place_list > li.ga-button-action-class.selected > span.check_off:nth-of-type(2)] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Default Workspace [role=listitem[name="Default Workspace"]] (left sidebar, top-left)
inferred_clickable: Default Workspace [#place_list > li.ga-button-action-class.selected > span.place_name_class:nth-of-type(1)] (left sidebar, top-left)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (left sidebar, middle-left)
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
```

**Not exercised by the crawler**

- inferred_clickable: CHITNU TEAMDefault Workspace -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: Default Workspace -- queued for depth 2
- inferred_clickable: Default Workspace -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2

## N020 — Screen | Samsung VXT CMS — Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 452 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Screen'
- **Screenshot:** [artifacts/N020_f2afbc9f.png](artifacts/N020_f2afbc9f.png)
- **DOM:** [artifacts/N020_f2afbc9f.html](artifacts/N020_f2afbc9f.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (left sidebar, middle-left)
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
```

## N021 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 591 · **Visits:** 4
- **Reached by:** Click 'content'
- **Screenshot:** [artifacts/N021_025f8bfc.png](artifacts/N021_025f8bfc.png)
- **DOM:** [artifacts/N021_025f8bfc.html](artifacts/N021_025f8bfc.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0] (main area, middle-centre)
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0] (main area, middle-centre)
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N033 Content | Samsung VXT CMS —  | — |

## N022 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 67 · **Interactive extracted:** 67 · **DOM nodes:** 607 · **Visits:** 4
- **Reached by:** Click 'Screen' → Click 'Playlist'
- **Screenshot:** [artifacts/N022_d32f987b.png](artifacts/N022_d32f987b.png)
- **DOM:** [artifacts/N022_d32f987b.html](artifacts/N022_d32f987b.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: GeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 playlist' | in_page_state | N035 Playlist | Samsung VXT CMS — | — |

## N023 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 62 · **Interactive extracted:** 62 · **DOM nodes:** 627 · **Visits:** 4
- **Reached by:** Click 'schedule'
- **Screenshot:** [artifacts/N023_d9f1d723.png](artifacts/N023_d9f1d723.png)
- **DOM:** [artifacts/N023_d9f1d723.html](artifacts/N023_d9f1d723.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 schedule [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 schedule [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: New ScheduleGeneralGeneral2026-08-20 23:51souresh Anand [#image_listwrap > ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3)] (main area, middle-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 schedule' | in_page_state | N036 Schedule | Samsung VXT CMS — | — |

## N024 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 1 · **Actionable:** 63 · **Interactive extracted:** 63 · **DOM nodes:** 630 · **Visits:** 5
- **Reached by:** Click 'Screen' → Click 'Channel'
- **Screenshot:** [artifacts/N024_40e2b12e.png](artifacts/N024_40e2b12e.png)
- **DOM:** [artifacts/N024_40e2b12e.html](artifacts/N024_40e2b12e.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="channel_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 channel [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 channel [#channelList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#channelCardNum > span.font16 > span.list_num:nth-of-type(1)] (main area, bottom-left)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CH 1CH 2New Channel2 channelsGeneralGeneral [[data-testid="channelCard_0"]] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: channels [#channelCardNum > span.font16 > span:nth-of-type(2)] (main area, bottom-left)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [#channelCardInfo] (main area, bottom-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]] (main area, top-right)
inferred_clickable: New Channel [#channelCardTitle] (main area, middle-centre)
inferred_clickable: New Channel2 channelsGeneralGeneral [#channelCard_0 > div.image_info.list_view:nth-of-type(3)] (main area, bottom-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Channelsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Channels [role=textbox[name="Search Channels"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Channelsand' | in_page_state | N043 Channel | Samsung VXT CMS —  | — |
| Click 'Search Channelsand' | navigation | N062 Channel | Samsung VXT CMS | — |

## N025 — Screen | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 43 · **Interactive extracted:** 43 · **DOM nodes:** 518 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'div'
- **Screenshot:** [artifacts/N025_95554e6d.png](artifacts/N025_95554e6d.png)
- **DOM:** [artifacts/N025_95554e6d.html](artifacts/N025_95554e6d.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_list"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="navbar_li_playlist"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [#navbar_leftControl] (left sidebar, middle-left)
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand] (left sidebar, top-left)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (left sidebar, middle-left)
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (left sidebar, top-left) [app frame]
```

**Not exercised by the crawler**

- inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2

## N026 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 1 · **Actionable:** 167 · **Interactive extracted:** 167 · **DOM nodes:** 1159 · **Visits:** 4
- **Reached by:** Click 'Screen' → Click 'AppsN'
- **Screenshot:** [artifacts/N026_2a28014d.png](artifacts/N026_2a28014d.png)
- **DOM:** [artifacts/N026_2a28014d.html](artifacts/N026_2a28014d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_search"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-centre)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(1)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(2)] (main area, middle-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > img:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > img] (main area, middle-right)
inferred_clickable: (unnamed) [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > img._app-logo_1wr29_1] (main area, top-right)
inferred_clickable: (unnamed) [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > img] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_right"]] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_thumbnail_arrow_left"]] (main area, middle-left)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-right)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-right)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-right)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(4) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(5) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(5) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-right)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(6) > div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(8) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(8) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(9) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(10) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div._app-box-container_1x05b_1:nth-of-type(11) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (left sidebar, top-left)
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)] (main area, top-right)
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Automation [div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: Automation [div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, top-right)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, top-right)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-centre)
inferred_clickable: CalendarCalendar [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-right)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Data SyncData Sync [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: DropboxDropbox [div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-right)
inferred_clickable: DropboxDropboxDropbox lets you create immersive slideshows instantly from your photos and videos. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(6) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-right)
inferred_clickable: EWQ SuperQueueEWQ SuperQueue [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)] (main area, top-right)
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)] (main area, top-right)
inferred_clickable: Gen AI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)] (main area, top-right)
inferred_clickable: Google DriveGoogle Drive [div > div > div._app-info-card_1v7dv_1:nth-of-type(4) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: LDSK EnterpriseLDSK Enterprise [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Link My POSLink My POS [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Microsoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div.fcms_simple_bar:nth-of-type(2)] (main area, top-right)
inferred_clickable: Microsoft ExcelMicrosoft Excel [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Microsoft ExcelMicrosoft Excel [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Microsoft ExcelMicrosoft ExcelMicrosoft Excel enables you easily share your spreadsheet data from any cell range you choose. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: Microsoft OneDriveMicrosoft OneDrive [div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: Microsoft OneDriveMicrosoft OneDriveMicrosoft One Drive enables you to instantly play your image and video into dynamic slideshows. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(7) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: Microsoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div.fcms_simple_bar:nth-of-type(2)] (main area, top-right)
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Microsoft Power BIMicrosoft Power BIMicrosoft Power BI enables you to instantly visualize your report and dashboard on screen [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: Microsoft PowerPoint enables you to instantly play dynamic slideshow. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div.fcms_simple_bar:nth-of-type(2)] (main area, top-right)
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: Microsoft PowerPointMicrosoft PowerPointMicrosoft PowerPoint enables you to instantly play dynamic slideshow. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(2) > div > div > div._app-info-card_1v7dv_1:nth-of-type(8) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: Microsoft SharePoint enables you to effortlessly share and collaborate on news posts with your team. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div.fcms_simple_bar:nth-of-type(2)] (main area, top-right)
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div > div > div._app-info-card_1v7dv_1:nth-of-type(5) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Ngine AutomotiveNgine Automotive [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Ngine Real EstateNgine Real Estate [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Productivity [div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span] (main area, top-right)
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)] (main area, top-right)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: ShadowGenShadowGenBETASamsung VXT Canvas enables you to create the shadow effects effortlessly [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-centre)
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, top-right)
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-right)
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0] (main area, bottom-centre)
text_input: Search Apps [role=textbox[name="Search Apps"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | blocked_mutation | (self) | mutating |
| Click 'img' | no_change | (self) | inert |

## N027 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 67 · **Interactive extracted:** 67 · **DOM nodes:** 577 · **Visits:** 1
- **Reached by:** Click 'Content'
- **Screenshot:** [artifacts/N027_198f357b.png](artifacts/N027_198f357b.png)
- **DOM:** [artifacts/N027_198f357b.html](artifacts/N027_198f357b.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0] (main area, middle-centre)
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0] (main area, middle-centre)
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Contentsand' | in_page_state | N028 Content | Samsung VXT CMS —  | — |
| Click 'Search Contentsand' | navigation | N028 Content | Samsung VXT CMS —  | — |

## N028 — Content | Samsung VXT CMS — Search Contentsand

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 133 · **Interactive extracted:** 133 · **DOM nodes:** 724 · **Visits:** 2
- **Reached by:** Click 'Content' → Click 'Search Contentsand'
- **Screenshot:** [artifacts/N028_8cbd7aae.png](artifacts/N028_8cbd7aae.png)
- **DOM:** [artifacts/N028_8cbd7aae.html](artifacts/N028_8cbd7aae.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Canvas [[data-testid="search_systemtag_3"]] (main area, top-centre)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-left)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvas [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-centre)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, bottom-centre)
inferred_clickable: E-Paper [[data-testid="search_systemtag_144"]] (main area, top-centre)
inferred_clickable: E-PaperE-Paper [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)] (main area, top-centre)
inferred_clickable: Embargo: Activated [[data-testid="search_systemtag_172"]] (main area, top-centre)
inferred_clickable: Embargo: ActivatedEmbargo: Activated [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: Embargo: Released [[data-testid="search_systemtag_173"]] (main area, top-centre)
inferred_clickable: Embargo: ReleasedEmbargo: Released [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)] (main area, top-centre)
inferred_clickable: Image [[data-testid="search_systemtag_2"]] (main area, top-centre)
inferred_clickable: ImageImage [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Landscape [[data-testid="search_systemtag_169"]] (main area, middle-centre)
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: Lifespan: Ended [[data-testid="search_systemtag_176"]] (main area, middle-centre)
inferred_clickable: Lifespan: EndedLifespan: Ended [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(10)] (main area, middle-centre)
inferred_clickable: Lifespan: Ready [[data-testid="search_systemtag_174"]] (main area, top-centre)
inferred_clickable: Lifespan: ReadyLifespan: Ready [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)] (main area, top-centre)
inferred_clickable: Lifespan: Started [[data-testid="search_systemtag_175"]] (main area, middle-centre)
inferred_clickable: Lifespan: StartedLifespan: Started [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(9)] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Not Published [[data-testid="search_systemtag_12"]] (main area, top-centre)
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Not Shared [[data-testid="search_systemtag_10"]] (main area, top-centre)
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre)
inferred_clickable: Office [[data-testid="search_systemtag_7"]] (main area, top-centre)
inferred_clickable: OfficeOffice [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Portrait [[data-testid="search_systemtag_170"]] (main area, middle-centre)
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: Published [[data-testid="search_systemtag_11"]] (main area, top-centre)
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: Shared [[data-testid="search_systemtag_8"]] (main area, top-centre)
inferred_clickable: Shared By Others [[data-testid="search_systemtag_9"]] (main area, top-centre)
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre)
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Ticker [[data-testid="search_systemtag_227"]] (main area, top-centre)
inferred_clickable: TickerTicker [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)] (main area, top-centre)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, bottom-centre)
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: Video [[data-testid="search_systemtag_1"]] (main area, top-centre)
inferred_clickable: VideoVideo [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: Web(HTML) [[data-testid="search_systemtag_5"]] (main area, top-centre)
inferred_clickable: Web(HTML)Web(HTML) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre)
inferred_clickable: Web(URL) [[data-testid="search_systemtag_6"]] (main area, top-centre)
inferred_clickable: Web(URL)Web(URL) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre)
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre)
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, bottom-centre)
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre)
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, bottom-centre)
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre)
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, bottom-centre)
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre)
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, bottom-centre)
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre)
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, bottom-centre)
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, bottom-centre)
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'CanvasCanvas' | in_page_state | N044 Content | Samsung VXT CMS —  | mutating |

**Not exercised by the crawler**

- inferred_clickable: CanvasCanvasCanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvasCanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvas -- queued for depth 2
- inferred_clickable: Canvas -- queued for depth 2
- inferred_clickable: ImageImage -- queued for depth 2
- inferred_clickable: Image -- queued for depth 2
- inferred_clickable: VideoVideo -- queued for depth 2
- inferred_clickable: Video -- queued for depth 2
- inferred_clickable: Web(HTML)Web(HTML) -- queued for depth 2
- inferred_clickable: Web(HTML) -- queued for depth 2
- inferred_clickable: Web(URL)Web(URL) -- queued for depth 2
- inferred_clickable: Web(URL) -- queued for depth 2
- inferred_clickable: OfficeOffice -- queued for depth 2
- inferred_clickable: Office -- queued for depth 2
- inferred_clickable: E-PaperE-Paper -- queued for depth 2
- inferred_clickable: E-Paper -- queued for depth 2
- inferred_clickable: TickerTicker -- queued for depth 2
- inferred_clickable: Ticker -- queued for depth 2
- inferred_clickable: PublishedPublished -- queued for depth 2
- inferred_clickable: Published -- queued for depth 2
- inferred_clickable: Not PublishedNot Published -- queued for depth 2
- inferred_clickable: Not Published -- queued for depth 2
- inferred_clickable: SharedShared -- queued for depth 2
- inferred_clickable: Shared -- queued for depth 2
- inferred_clickable: Shared By OthersShared By Others -- queued for depth 2
- inferred_clickable: Shared By Others -- queued for depth 2
- inferred_clickable: Not SharedNot Shared -- queued for depth 2
- inferred_clickable: Not Shared -- queued for depth 2
- inferred_clickable: Embargo: ActivatedEmbargo: Activated -- queued for depth 2
- inferred_clickable: Embargo: Activated -- queued for depth 2
- inferred_clickable: Embargo: ReleasedEmbargo: Released -- queued for depth 2
- inferred_clickable: Embargo: Released -- queued for depth 2
- inferred_clickable: Lifespan: ReadyLifespan: Ready -- queued for depth 2
- inferred_clickable: Lifespan: Ready -- queued for depth 2
- inferred_clickable: Lifespan: StartedLifespan: Started -- queued for depth 2
- inferred_clickable: Lifespan: Started -- queued for depth 2
- inferred_clickable: Lifespan: EndedLifespan: Ended -- queued for depth 2
- inferred_clickable: Lifespan: Ended -- queued for depth 2
- inferred_clickable: LandscapeLandscape -- queued for depth 2
- inferred_clickable: Landscape -- queued for depth 2
- inferred_clickable: PortraitPortrait -- queued for depth 2
- inferred_clickable: Portrait -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2

## N029 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 66 · **Interactive extracted:** 66 · **DOM nodes:** 528 · **Visits:** 1
- **Reached by:** Click 'Playlist'
- **Screenshot:** [artifacts/N029_5ccefd7b.png](artifacts/N029_5ccefd7b.png)
- **DOM:** [artifacts/N029_5ccefd7b.html](artifacts/N029_5ccefd7b.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: GeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Playlistsand' | in_page_state | N030 Playlist | Samsung VXT CMS — | — |

## N030 — Playlist | Samsung VXT CMS — Search Playlistsand

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 115 · **Interactive extracted:** 115 · **DOM nodes:** 677 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand'
- **Screenshot:** [artifacts/N030_f0ea4c9a.png](artifacts/N030_f0ea4c9a.png)
- **DOM:** [artifacts/N030_f0ea4c9a.html](artifacts/N030_f0ea4c9a.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-centre)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-centre)
inferred_clickable: General [[data-testid="search_systemtag_30"]] (main area, top-centre)
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneral [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Landscape [[data-testid="search_systemtag_177"]] (main area, middle-centre)
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No Content [[data-testid="search_systemtag_179"]] (main area, top-centre)
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Not Published [[data-testid="search_systemtag_37"]] (main area, top-centre)
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Not Shared [[data-testid="search_systemtag_35"]] (main area, top-centre)
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Portrait [[data-testid="search_systemtag_178"]] (main area, middle-centre)
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: Published [[data-testid="search_systemtag_36"]] (main area, top-centre)
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: Shared [[data-testid="search_systemtag_33"]] (main area, top-centre)
inferred_clickable: Shared By Others [[data-testid="search_systemtag_34"]] (main area, top-centre)
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre)
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Sync Play [[data-testid="search_systemtag_31"]] (main area, top-centre)
inferred_clickable: Sync PlaySync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Takeover Sync Play [[data-testid="search_systemtag_32"]] (main area, top-centre)
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre)
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre)
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre)
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre)
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre)
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre)
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre)
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre)
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre)
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre)
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre)
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre)
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre)
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 2
- inferred_clickable: GeneralGeneral -- queued for depth 2
- inferred_clickable: GeneralGeneral -- queued for depth 2
- inferred_clickable: General -- queued for depth 2
- inferred_clickable: Sync PlaySync Play -- queued for depth 2
- inferred_clickable: Sync Play -- queued for depth 2
- inferred_clickable: Takeover Sync PlayTakeover Sync Play -- queued for depth 2
- inferred_clickable: Takeover Sync Play -- queued for depth 2
- inferred_clickable: PublishedPublished -- queued for depth 2
- inferred_clickable: Published -- queued for depth 2
- inferred_clickable: Not PublishedNot Published -- queued for depth 2
- inferred_clickable: Not Published -- queued for depth 2
- inferred_clickable: SharedShared -- queued for depth 2
- inferred_clickable: Shared -- queued for depth 2
- inferred_clickable: Shared By OthersShared By Others -- queued for depth 2
- inferred_clickable: Shared By Others -- queued for depth 2
- inferred_clickable: Not SharedNot Shared -- queued for depth 2
- inferred_clickable: Not Shared -- queued for depth 2
- inferred_clickable: No ContentNo Content -- queued for depth 2
- inferred_clickable: No Content -- queued for depth 2
- inferred_clickable: LandscapeLandscape -- queued for depth 2
- inferred_clickable: Landscape -- queued for depth 2
- inferred_clickable: PortraitPortrait -- queued for depth 2
- inferred_clickable: Portrait -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2

## N031 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 61 · **Interactive extracted:** 61 · **DOM nodes:** 522 · **Visits:** 1
- **Reached by:** Click 'Schedule'
- **Screenshot:** [artifacts/N031_c1703931.png](artifacts/N031_c1703931.png)
- **DOM:** [artifacts/N031_c1703931.html](artifacts/N031_c1703931.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 schedule [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 schedule [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: New ScheduleGeneralGeneral2026-08-20 23:51souresh Anand [#image_listwrap > ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3)] (main area, middle-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Schedulesand' | in_page_state | N032 Schedule | Samsung VXT CMS — | mutating |
| Click 'Search Schedulesand' | navigation | N045 Schedule | Samsung VXT CMS | — |

## N032 — Schedule | Samsung VXT CMS — Search Schedulesand

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 107 · **Interactive extracted:** 107 · **DOM nodes:** 634 · **Visits:** 1
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand'
- **Screenshot:** [artifacts/N032_3d9bc565.png](artifacts/N032_3d9bc565.png)
- **DOM:** [artifacts/N032_3d9bc565.html](artifacts/N032_3d9bc565.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 schedule [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 schedule [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-centre) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, bottom-centre) [app frame]
inferred_clickable: General [[data-testid="search_systemtag_52"]] (main area, top-centre)
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneral [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Landscape [[data-testid="search_systemtag_180"]] (main area, middle-centre)
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: No Content [[data-testid="search_systemtag_182"]] (main area, top-centre)
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Not Published [[data-testid="search_systemtag_58"]] (main area, top-centre)
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre) [app frame]
inferred_clickable: Not Shared [[data-testid="search_systemtag_56"]] (main area, top-centre)
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Portrait [[data-testid="search_systemtag_181"]] (main area, middle-centre)
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
inferred_clickable: Published [[data-testid="search_systemtag_57"]] (main area, top-centre)
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: Shared [[data-testid="search_systemtag_54"]] (main area, top-centre)
inferred_clickable: Shared By Others [[data-testid="search_systemtag_55"]] (main area, top-centre)
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre) [app frame]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre) [app frame]
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Sync Play [[data-testid="search_systemtag_53"]] (main area, top-centre)
inferred_clickable: Sync PlaySync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 2
- inferred_clickable: GeneralGeneral -- queued for depth 2
- inferred_clickable: GeneralGeneral -- queued for depth 2
- inferred_clickable: General -- queued for depth 2
- inferred_clickable: Sync PlaySync Play -- queued for depth 2
- inferred_clickable: Sync Play -- queued for depth 2
- inferred_clickable: PublishedPublished -- queued for depth 2
- inferred_clickable: Published -- queued for depth 2
- inferred_clickable: Not PublishedNot Published -- queued for depth 2
- inferred_clickable: Not Published -- queued for depth 2
- inferred_clickable: SharedShared -- queued for depth 2
- inferred_clickable: Shared -- queued for depth 2
- inferred_clickable: Shared By OthersShared By Others -- queued for depth 2
- inferred_clickable: Shared By Others -- queued for depth 2
- inferred_clickable: Not SharedNot Shared -- queued for depth 2
- inferred_clickable: Not Shared -- queued for depth 2
- inferred_clickable: No ContentNo Content -- queued for depth 2
- inferred_clickable: No Content -- queued for depth 2
- inferred_clickable: LandscapeLandscape -- queued for depth 2
- inferred_clickable: Landscape -- queued for depth 2
- inferred_clickable: PortraitPortrait -- queued for depth 2
- inferred_clickable: Portrait -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2
- inferred_clickable: TodayToday -- queued for depth 2
- inferred_clickable: Today -- queued for depth 2
- inferred_clickable: YesterdayYesterday -- queued for depth 2
- inferred_clickable: Yesterday -- queued for depth 2
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 2
- inferred_clickable: Within 3 Days -- queued for depth 2
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 2
- inferred_clickable: Within a Week -- queued for depth 2
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 2
- inferred_clickable: Within a Month -- queued for depth 2
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 2
- inferred_clickable: Within 3 Months -- queued for depth 2
- inferred_clickable: Custom -- queued for depth 2

## N033 — Content | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 574 · **Visits:** 1
- **Reached by:** Click 'content' → Click 'div'
- **Screenshot:** [artifacts/N033_9f71b948.png](artifacts/N033_9f71b948.png)
- **DOM:** [artifacts/N033_9f71b948.html](artifacts/N033_9f71b948.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"] >> nth=0] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-left)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: CanvasCanvasCanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvasCanvasCanvas -- queued for depth 2
- inferred_clickable: CanvasCanvas -- queued for depth 2

## N034 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 560 · **Visits:** 1
- **Reached by:** Click 'playlist'
- **Screenshot:** [artifacts/N034_99e1d6ef.png](artifacts/N034_99e1d6ef.png)
- **DOM:** [artifacts/N034_99e1d6ef.html](artifacts/N034_99e1d6ef.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 playlist' | in_page_state | N035 Playlist | Samsung VXT CMS — | mutating |

## N035 — Playlist | Samsung VXT CMS — 1 playlist

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 72 · **Interactive extracted:** 72 · **DOM nodes:** 558 · **Visits:** 2
- **Reached by:** Click 'playlist' → Click '1 playlist'
- **Screenshot:** [artifacts/N035_81a34b4b.png](artifacts/N035_81a34b4b.png)
- **DOM:** [artifacts/N035_81a34b4b.html](artifacts/N035_81a34b4b.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="playlistCard_checkbox_0"]] (main area, top-left)
destructive: Delete [[data-testid="playlist_toolbar_delete"]] (main area, top-right)
generic_button: Add Tags [[data-testid="playlist_toolbar_addtags"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0] (main area, top-right)
generic_button: Set to Screens [[data-testid="playlist_toolbar_set2screen"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 1 of 1 selected [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 of 1 selected [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 1 of 1 selected [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(4)] (main area, top-centre)
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2)] (main area, middle-right)
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)] (main area, middle-right)
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: 1 of 1 selected -- queued for depth 3
- inferred_clickable: 1 of 1 selected -- queued for depth 3
- inferred_clickable: 1 of 1 selected -- queued for depth 3
- generic_button: Set to Screens -- queued for depth 3
- generic_button: Add Tags -- queued for depth 3
- destructive: Delete -- queued for depth 3
- checkbox: (unnamed) -- queued for depth 3
- inferred_clickable: New Playlist -- queued for depth 3
- inferred_clickable: 2 contents -- queued for depth 3
- inferred_clickable: 2 -- queued for depth 3
- inferred_clickable: contents -- queued for depth 3
- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 3
- inferred_clickable: GeneralGeneral -- queued for depth 3
- inferred_clickable: 02:00.0 -- queued for depth 3
- inferred_clickable: 47.21 KB -- queued for depth 3
- inferred_clickable: 2026-08-20 09:18 -- queued for depth 3
- inferred_clickable: souresh Anand -- queued for depth 3

## N036 — Schedule | Samsung VXT CMS — 1 schedule

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 66 · **Interactive extracted:** 66 · **DOM nodes:** 518 · **Visits:** 1
- **Reached by:** Click 'schedule' → Click '1 schedule'
- **Screenshot:** [artifacts/N036_f9a0d677.png](artifacts/N036_f9a0d677.png)
- **DOM:** [artifacts/N036_f9a0d677.html](artifacts/N036_f9a0d677.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="schedule_card_checkbox_0"]] (main area, top-left)
destructive: Delete [role=button[name="Delete"]] (main area, top-right)
generic_button: Add Tags [role=button[name="Add Tags"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
generic_button: Set to Screens [role=button[name="Set to Screens"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 of 1 selected [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 of 1 selected [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 1 of 1 selected [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(4)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: 1 of 1 selected -- queued for depth 2
- inferred_clickable: 1 of 1 selected -- queued for depth 2
- inferred_clickable: 1 of 1 selected -- queued for depth 2
- generic_button: Set to Screens -- queued for depth 2
- generic_button: Add Tags -- queued for depth 2
- destructive: Delete -- queued for depth 2
- checkbox: (unnamed) -- queued for depth 2
- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 2
- inferred_clickable: GeneralGeneral -- queued for depth 2
- inferred_clickable: 2026-08-20 23:51 -- queued for depth 2
- inferred_clickable: souresh Anand -- queued for depth 2

## N037 — HOME | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 1 · **Actionable:** 45 · **Interactive extracted:** 45 · **DOM nodes:** 371 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'div'

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-right)
generic_button: refresh [#refreshScreenBtn] (main area, middle-right)
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]] (main area, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, middle-left)
inferred_clickable: Apps [role=listitem[name="Apps"]] (main area, middle-right)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-centre) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed1.50MB [role=listitem[name="StorageUsed1.50MB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
```

## N038 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 509 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'General'
- **Screenshot:** [artifacts/N038_eef435c9.png](artifacts/N038_eef435c9.png)
- **DOM:** [artifacts/N038_eef435c9.html](artifacts/N038_eef435c9.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (main area, middle-centre)
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]] (main area, top-right)
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]] (main area, bottom-centre)
inferred_clickable: 20:41 [[data-testid="select-Time Format"]] (main area, bottom-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left)
inferred_clickable: English [[data-testid="select-Language"]] (main area, middle-centre)
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left)
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]] (main area, bottom-centre)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left)
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]] (main area, bottom-centre)
inferred_clickable: Mon [[data-testid="select-First Day of Week"]] (main area, bottom-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left)
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div] (main area, middle-centre)
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]] (main area, middle-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Register Phone Number' | in_page_state | N061 Settings | Samsung VXT CMS — | mutating |
| Click 'div' | no_change | (self) | inert |
| Click 'Register Phone Number' | in_page_state | N061 Settings | Samsung VXT CMS — | mutating |
| Click 'English' | blocked_mutation | (self) | mutating |
| Click '2022-04-19' | blocked_mutation | (self) | mutating |
| Click 'Mon' | blocked_mutation | (self) | mutating |
| Click '20:41' | blocked_mutation | (self) | mutating |
| Click 'Individual contributor' | blocked_mutation | (self) | mutating |
| Click 'Exhibition' | blocked_mutation | (self) | mutating |
| Click 'Register Phone Number' | navigation | N061 Settings | Samsung VXT CMS — | — |

## N039 — Settings | Samsung VXT CMS — button

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 647 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'button'
- **Screenshot:** [artifacts/N039_a3ac712a.png](artifacts/N039_a3ac712a.png)
- **DOM:** [artifacts/N039_a3ac712a.html](artifacts/N039_a3ac712a.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled) (main area, bottom-centre)
generic_button: (unnamed) [#ModalFooter_btnMore] (main area, top-right)
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left)
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: (unnamed) [#ProCard_statusColor] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, bottom-right)
inferred_clickable: 0 [role=listitem[name="0"]] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left)
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation] (main area, bottom-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]] (main area, bottom-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left)
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left)
inferred_clickable: Lock Plan [[data-testid="button_Lock Plan"]] (main area, top-right)
inferred_clickable: Merge Plan [[data-testid="button_Merge Plan"]] (main area, top-right)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left)
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed] (main area, bottom-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left)
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace] (main area, bottom-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input] (main area, bottom-centre)
text_input: Allocable [#input_text2] (disabled) (main area, bottom-centre)
text_input: Allocated [#input_text1] (disabled) (main area, bottom-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Lock Plan' | in_page_state | N011 Settings | Samsung VXT CMS | mutating |

**Not exercised by the crawler**

- inferred_clickable: Lock Plan -- queued for depth 2
- inferred_clickable: Merge Plan -- queued for depth 2

## N040 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 1 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'div'

_No actionable elements extracted._

## N041 — Samsung VXT CMS — SmartPlug

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 448 · **Visits:** 4
- **Reached by:** Click 'VXT Labs' → Click 'NEW'
- **Screenshot:** [artifacts/N041_e0e79420.png](artifacts/N041_e0e79420.png)
- **DOM:** [artifacts/N041_e0e79420.html](artifacts/N041_e0e79420.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Close [[data-testid="vxtlabs_feature_detail_close"]] (main area, bottom-right)
inferred_clickable: (unnamed) [#signage_modal > div.cEWgRo:nth-of-type(1) > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (header, top-left)
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-centre)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, bottom-right)
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-centre)
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, bottom-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, bottom-right)
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, bottom-left)
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)] (main area, bottom-left)
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, bottom-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- generic_button: Close -- queued for depth 2

## N042 — Samsung VXT CMS — img

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 1109 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'img'
- **Screenshot:** [artifacts/N042_37b82b07.png](artifacts/N042_37b82b07.png)
- **DOM:** [artifacts/N042_37b82b07.html](artifacts/N042_37b82b07.html)

**Action elements**

```
checkbox: By installing this app, you agree to the Terms and Conditions and Permissions. [#CheckBoxInput] (left sidebar, top-left)
disclosure: Africa [role=button[name="Africa"]] (main area, bottom-centre)
disclosure: Asia [role=button[name="Asia"]] (main area, bottom-centre)
disclosure: Europe [role=button[name="Europe"]] (main area, bottom-centre)
disclosure: North America [role=button[name="North America"]] (main area, bottom-centre)
disclosure: Oceania [role=button[name="Oceania"]] (main area, bottom-centre)
disclosure: South America [role=button[name="South America"]] (main area, bottom-centre)
generic_button: Buy Now [role=button[name="Buy Now"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Install [role=button[name="Install"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (header, top-left)
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, top-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, middle-left)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, middle-centre)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (left sidebar, bottom-left)
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > img._app-logo_1wr29_1] (main area, bottom-centre)
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1] (left sidebar, bottom-left)
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-centre)
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, top-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, middle-centre)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, middle-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, middle-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, middle-right)
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0] (main area, middle-right)
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0] (main area, bottom-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CalendarCalendar [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: Data SyncData Sync [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)] (main area, bottom-centre)
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div > div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)] (main area, bottom-left)
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root] (main area, bottom-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, top-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, middle-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, middle-centre)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, middle-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, middle-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (main area, middle-right)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0] (left sidebar, bottom-left)
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, bottom-left)
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)] (main area, bottom-left)
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0] (main area, top-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 2
- generic_button: Buy Now -- queued for depth 2
- generic_button: Install -- queued for depth 2
- checkbox: By installing this app, you agree to the Terms and Conditions and Permissions. -- queued for depth 2
- inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: Data SyncData Sync -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: AI Writing AssistantAI Writing AssistantBETA -- queued for depth 2
- inferred_clickable: BETA -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: CalendarCalendar -- queued for depth 2
- disclosure: Asia -- queued for depth 2
- disclosure: Africa -- queued for depth 2
- disclosure: Europe -- queued for depth 2
- disclosure: Oceania -- queued for depth 2
- disclosure: North America -- queued for depth 2
- disclosure: South America -- queued for depth 2

## N043 — Channel | Samsung VXT CMS — Search Channelsand

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 2 · **Actionable:** 109 · **Interactive extracted:** 109 · **DOM nodes:** 645 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Channel' → Click 'Search Channelsand'
- **Screenshot:** [artifacts/N043_419e6dcb.png](artifacts/N043_419e6dcb.png)
- **DOM:** [artifacts/N043_419e6dcb.html](artifacts/N043_419e6dcb.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="channel_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 channel [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 channel [#channelList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#channelCardNum > span.font16 > span.list_num:nth-of-type(1)] (main area, bottom-left)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CH 1CH 2New Channel2 channelsGeneralGeneralGeneralGeneral [[data-testid="channelCard_0"]] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: channels [#channelCardNum > span.font16 > span:nth-of-type(2)] (main area, bottom-left)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-centre) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, bottom-centre) [app frame]
inferred_clickable: General [[data-testid="search_systemtag_142"]] (main area, top-centre)
inferred_clickable: GeneralGeneral [#channelCardInfo > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, bottom-left)
inferred_clickable: GeneralGeneral [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre) [app frame]
inferred_clickable: GeneralGeneralGeneralGeneral [#channelCardInfo] (main area, bottom-centre)
inferred_clickable: Landscape [[data-testid="search_systemtag_183"]] (main area, middle-centre)
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]] (main area, top-right)
inferred_clickable: New Channel [#channelCardTitle] (main area, middle-centre)
inferred_clickable: No Content [[data-testid="search_systemtag_185"]] (main area, top-centre)
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Not Published [[data-testid="search_systemtag_77"]] (main area, top-centre)
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre) [app frame]
inferred_clickable: Not Shared [[data-testid="search_systemtag_75"]] (main area, top-centre)
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Portrait [[data-testid="search_systemtag_184"]] (main area, middle-centre)
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
inferred_clickable: Published [[data-testid="search_systemtag_76"]] (main area, top-centre)
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-centre) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Channelsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: Shared [[data-testid="search_systemtag_73"]] (main area, top-centre)
inferred_clickable: Shared By Others [[data-testid="search_systemtag_74"]] (main area, top-centre)
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre) [app frame]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Sync Play [[data-testid="search_systemtag_143"]] (main area, top-centre)
inferred_clickable: Sync PlaySync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre) [app frame]
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-centre) [app frame]
text_input: Search Channels [role=textbox[name="Search Channels"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: CH 1CH 2New Channel2 channelsGeneralGeneralGeneralGeneral -- queued for depth 3
- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 3
- inferred_clickable: GeneralGeneral -- queued for depth 3
- inferred_clickable: GeneralGeneral -- queued for depth 3
- inferred_clickable: General -- queued for depth 3
- inferred_clickable: Sync PlaySync Play -- queued for depth 3
- inferred_clickable: Sync Play -- queued for depth 3
- inferred_clickable: PublishedPublished -- queued for depth 3
- inferred_clickable: Published -- queued for depth 3
- inferred_clickable: Not PublishedNot Published -- queued for depth 3
- inferred_clickable: Not Published -- queued for depth 3
- inferred_clickable: SharedShared -- queued for depth 3
- inferred_clickable: Shared -- queued for depth 3
- inferred_clickable: Shared By OthersShared By Others -- queued for depth 3
- inferred_clickable: Shared By Others -- queued for depth 3
- inferred_clickable: Not SharedNot Shared -- queued for depth 3
- inferred_clickable: Not Shared -- queued for depth 3
- inferred_clickable: No ContentNo Content -- queued for depth 3
- inferred_clickable: No Content -- queued for depth 3
- inferred_clickable: LandscapeLandscape -- queued for depth 3
- inferred_clickable: Landscape -- queued for depth 3
- inferred_clickable: PortraitPortrait -- queued for depth 3
- inferred_clickable: Portrait -- queued for depth 3
- inferred_clickable: TodayToday -- queued for depth 3
- inferred_clickable: Today -- queued for depth 3
- inferred_clickable: YesterdayYesterday -- queued for depth 3
- inferred_clickable: Yesterday -- queued for depth 3
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 3
- inferred_clickable: Within 3 Days -- queued for depth 3
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 3
- inferred_clickable: Within a Week -- queued for depth 3
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 3
- inferred_clickable: Within a Month -- queued for depth 3
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 3
- inferred_clickable: Within 3 Months -- queued for depth 3
- inferred_clickable: Custom -- queued for depth 3
- inferred_clickable: TodayToday -- queued for depth 3
- inferred_clickable: Today -- queued for depth 3
- inferred_clickable: YesterdayYesterday -- queued for depth 3
- inferred_clickable: Yesterday -- queued for depth 3
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 3
- inferred_clickable: Within 3 Days -- queued for depth 3
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 3
- inferred_clickable: Within a Week -- queued for depth 3
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 3
- inferred_clickable: Within a Month -- queued for depth 3
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 3
- inferred_clickable: Within 3 Months -- queued for depth 3
- inferred_clickable: Custom -- queued for depth 3

## N044 — Content | Samsung VXT CMS — Search Contentsand — CanvasCanvas

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 2 · **Actionable:** 73 · **Interactive extracted:** 73 · **DOM nodes:** 605 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'CanvasCanvas'
- **Screenshot:** [artifacts/N044_64a0d561.png](artifacts/N044_64a0d561.png)
- **DOM:** [artifacts/N044_64a0d561.html](artifacts/N044_64a0d561.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Create Content [#content_toolbar_pc_topbtn_Create] (main area, top-centre)
generic_button: more [[data-testid="content_page_toolbar_btnmore"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox] (header, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_circle_delete"]] (header, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0] (main area, middle-centre)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)] (main area, top-left)
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Canvas [[data-testid="Canvas"] >> nth=0] (header, top-centre)
inferred_clickable: CanvasCanvas [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox] (header, top-centre)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-left)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]] (left sidebar, middle-left)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input] (header, top-centre)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: CanvasCanvasand -- queued for depth 3
- text_input: (unnamed) -- queued for depth 3
- inferred_clickable: CanvasCanvas -- queued for depth 3
- inferred_clickable: Canvas -- queued for depth 3
- inferred_clickable: (unnamed) -- queued for depth 3
- inferred_clickable: (unnamed) -- queued for depth 3
- text_input: (unnamed) -- queued for depth 3
- inferred_clickable: (unnamed) -- queued for depth 3

## N045 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 61 · **Interactive extracted:** 61 · **DOM nodes:** 526 · **Visits:** 1
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand'
- **Screenshot:** [artifacts/N045_5535763d.png](artifacts/N045_5535763d.png)
- **DOM:** [artifacts/N045_5535763d.html](artifacts/N045_5535763d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 schedule [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 schedule [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 schedule' | in_page_state | N046 Schedule | Samsung VXT CMS — | mutating |

## N046 — Schedule | Samsung VXT CMS — 1 schedule

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 65 · **Interactive extracted:** 65 · **DOM nodes:** 523 · **Visits:** 1
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand' → Click '1 schedule'
- **Screenshot:** [artifacts/N046_27d7a487.png](artifacts/N046_27d7a487.png)
- **DOM:** [artifacts/N046_27d7a487.html](artifacts/N046_27d7a487.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="schedule_card_checkbox_0"]] (main area, top-left)
destructive: Delete [role=button[name="Delete"]] (main area, top-right)
generic_button: Add Tags [role=button[name="Add Tags"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="schedule_fcmsmore_btn"] >> nth=0] (main area, top-right)
generic_button: Set to Screens [role=button[name="Set to Screens"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="schedule_date_or_name_sort"] >> nth=0] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 of 1 selected [[data-testid="schedule_fcmsCheckbox"]] (main area, top-left)
inferred_clickable: 1 of 1 selected [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 1 of 1 selected [div.contents_box > div.topbtn_con:nth-of-type(1) > div.topbtn_wrap > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(4)] (main area, top-centre)
inferred_clickable: 2026-08-20 23:51 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span:nth-of-type(1)] (main area, middle-right)
inferred_clickable: 20Aug [#scheduleCard_leftCon] (main area, middle-left)
inferred_clickable: 20Aug [#scheduleCard_rightCon] (main area, middle-centre)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Schedulesand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: 1 of 1 selected -- queued for depth 3
- inferred_clickable: 1 of 1 selected -- queued for depth 3
- inferred_clickable: 1 of 1 selected -- queued for depth 3
- generic_button: Set to Screens -- queued for depth 3
- generic_button: Add Tags -- queued for depth 3
- destructive: Delete -- queued for depth 3
- checkbox: (unnamed) -- queued for depth 3
- inferred_clickable: GeneralGeneralGeneralGeneral -- queued for depth 3
- inferred_clickable: GeneralGeneral -- queued for depth 3
- inferred_clickable: 2026-08-20 23:51 -- queued for depth 3
- inferred_clickable: souresh Anand -- queued for depth 3

## N047 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 283 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry'
- **Screenshot:** [artifacts/N047_8d6adb87.png](artifacts/N047_8d6adb87.png)
- **DOM:** [artifacts/N047_8d6adb87.html](artifacts/N047_8d6adb87.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Inquiry [role=button[name="New Inquiry"]] (main area, bottom-right)
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Tech Inquiry Permissions' | in_page_state | N048 Settings | Samsung VXT CMS — | — |
| Click 'New Inquiry' | navigation | N049 Settings | Samsung VXT CMS | — |
| Click 'Organization' | navigation | N050 Settings | Samsung VXT CMS | mutating |
| Click 'Workspace' | navigation | N051 Settings | Samsung VXT CMS | mutating |
| Click 'User' | navigation | N052 Settings | Samsung VXT CMS | mutating |
| Click 'Plan' | navigation | N053 Settings | Samsung VXT CMS | mutating |
| Click 'Tag' | navigation | N054 Settings | Samsung VXT CMS | mutating |
| Click 'Event' | navigation | N055 Settings | Samsung VXT CMS | mutating |
| Click 'div' | navigation | N055 Settings | Samsung VXT CMS | mutating |
| Click 'Screen Preset' | navigation | N056 Settings | Samsung VXT CMS | mutating |
| Click 'Emergency Alert' | navigation | N057 Settings | Samsung VXT CMS | mutating |
| Click 'Activity Log' | navigation | N058 Settings | Samsung VXT CMS | mutating |
| Click 'Edit Home' | navigation | N059 Settings | Samsung VXT CMS | mutating |
| Click 'div' | navigation | N060 Settings | Samsung VXT CMS | mutating |
| Click 'Tech Inquiry Permissions' | navigation | N048 Settings | Samsung VXT CMS — | — |
| Click 'New Inquiry' | navigation | N049 Settings | Samsung VXT CMS | — |
| Click 'Organization' | navigation | N050 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N051 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N052 Settings | Samsung VXT CMS | — |
| Click 'Plan' | navigation | N053 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N072 Settings | Samsung VXT CMS | — |
| Click 'Event' | navigation | N055 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N056 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N057 Settings | Samsung VXT CMS | — |
| Click 'Activity Log' | navigation | N079 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N080 Settings | Samsung VXT CMS | — |

## N048 — Settings | Samsung VXT CMS — Tech Inquiry Permissions

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 343 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tech Inquiry Permissions'
- **Screenshot:** [artifacts/N048_d8ab2c91.png](artifacts/N048_d8ab2c91.png)
- **DOM:** [artifacts/N048_d8ab2c91.html](artifacts/N048_d8ab2c91.html)

**Action elements**

```
generic_button: Cancel [#footer_rightPart_cancelBtn] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Inquiry [role=button[name="New Inquiry"]] (main area, bottom-right)
generic_button: Save [#footer_rightPart_okBtn] (disabled) (main area, bottom-right)
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [#modal_pop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, middle-right) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: All Users [[data-testid="select_default"] >> nth=0] (main area, middle-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Owner and Admin [[data-testid="select_default"] >> nth=0] (main area, middle-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N047 Settings | Samsung VXT CMS | mutating |

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 3
- inferred_clickable: (unnamed) -- queued for depth 3
- inferred_clickable: All Users -- queued for depth 3
- inferred_clickable: Owner and Admin -- queued for depth 3
- generic_button: Cancel -- queued for depth 3
- generic_button: Save -- queued for depth 3

## N049 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** page · **Depth:** 2 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 443 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'New Inquiry'
- **Screenshot:** [artifacts/N049_891bd27f.png](artifacts/N049_891bd27f.png)
- **DOM:** [artifacts/N049_891bd27f.html](artifacts/N049_891bd27f.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]] (main area, bottom-centre)
generic_button: Open [role=button[name="Open"]] (main area, bottom-right)
generic_button: Request [role=button[name="Request"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (main area, middle-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span] (main area, middle-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Select [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class] (main area, bottom-centre)
text_input: (unnamed) [#select >> nth=0] (main area, bottom-centre)
text_input: Enter a subject. [role=textbox[name="Enter a subject."]] (main area, middle-centre)
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]] (main area, bottom-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Register Phone Number' | in_page_state | N064 Settings | Samsung VXT CMS — | — |
| Click 'Select' | no_change | (self) | inert |
| Click 'Open' | file_chooser | (self) | mutating, upload |
| Click 'Drop the files here to attach.' | no_change | (self) | inert |
| Click 'Register Phone Number' | navigation | N064 Settings | Samsung VXT CMS — | — |

## N050 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 455 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Organization'
- **Screenshot:** [artifacts/N050_7e6abd8d.png](artifacts/N050_7e6abd8d.png)
- **DOM:** [artifacts/N050_7e6abd8d.html](artifacts/N050_7e6abd8d.html)

**Action elements**

```
generic_button: Add [#add_phone_number] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Entertainment [[data-testid="select-Industry"]] (main area, middle-centre)
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Information [[data-testid="settings_organization_information"]] (main area, top-centre)
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]] (main area, top-centre)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Store Owner [[data-testid="select-CMS User"]] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]] (main area, top-right)
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: ~10 [[data-testid="select-Number of Employees"]] (main area, bottom-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_ORGANIZATION_NAME"]] (main area, middle-centre)
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_NAME"]] (main area, bottom-centre)
text_input: (unnamed) [[data-testid="org_input_VX_SID_CMS_CCAUG_PRIMARY_CONTACT_EMAIL"]] (main area, bottom-centre)
text_input: Register Phone Number [role=textbox[name="Register Phone Number"]] (main area, bottom-centre)
text_input: Select [[data-testid="select-Country/Region"]] (main area, bottom-centre)
form (inferred): submit=Add [#add_phone_number] fields=(contactName, contactEmail)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Information' | blocked_mutation | (self) | mutating |
| Click 'Customization' | in_page_state | N065 Settings | Samsung VXT CMS — | mutating |
| Click 'Preset' | in_page_state | N066 Settings | Samsung VXT CMS — | mutating |
| Click 'Tag' | in_page_state | N067 Settings | Samsung VXT CMS — | — |
| Click 'Scheduling' | in_page_state | N068 Settings | Samsung VXT CMS — | — |
| Click 'Information' | blocked_mutation | (self) | mutating |
| Click 'Customization' | in_page_state | N065 Settings | Samsung VXT CMS — | mutating |
| Click 'Preset' | in_page_state | (self) | state-cap |
| Click 'Tag' | in_page_state | (self) | mutating, state-cap |
| Click 'Scheduling' | in_page_state | (self) | mutating, state-cap |
| Click 'Entertainment' | no_change | (self) | inert |
| Click 'Store Owner' | no_change | (self) | inert |
| Click '~10' | no_change | (self) | inert |
| Click 'Add' | in_page_state | (self) | state-cap |

## N051 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 2 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 397 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Workspace'
- **Screenshot:** [artifacts/N051_6c5e41bb.png](artifacts/N051_6c5e41bb.png)
- **DOM:** [artifacts/N051_6c5e41bb.html](artifacts/N051_6c5e41bb.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Allocation [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Available [#FcmsTable_sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: No workspaces. [[data-testid="No workspaces."]] (main area, middle-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Allocation' | no_change | (self) | inert |

## N052 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 36 · **Interactive extracted:** 36 · **DOM nodes:** 419 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'User'
- **Screenshot:** [artifacts/N052_b81fd3f4.png](artifacts/N052_b81fd3f4.png)
- **DOM:** [artifacts/N052_b81fd3f4.html](artifacts/N052_b81fd3f4.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]] (main area, top-right)
generic_button: more [#topOption_btn_more_options] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [div:nth-of-type(2) > div.account.account-contents-wrap > div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.rightAfterBtn.MuiBox-root:nth-of-type(2) > div.topbtn_option.ga-button-action-class] (main area, top-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]] (main area, top-centre)
inferred_clickable: No users. [[data-testid="No users."]] (main area, middle-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]] (main area, top-centre)
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]] (main area, top-right)
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Member' | no_change | (self) | inert |
| Click 'Owner' | in_page_state | N069 Settings | Samsung VXT CMS — | — |
| Click 'Pending' | in_page_state | N070 Settings | Samsung VXT CMS — | mutating |
| Click 'Owner' | navigation | N069 Settings | Samsung VXT CMS — | — |
| Click 'Pending' | navigation | N070 Settings | Samsung VXT CMS — | — |

## N053 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 2 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 475 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Plan'
- **Screenshot:** [artifacts/N053_e149b4d5.png](artifacts/N053_e149b4d5.png)
- **DOM:** [artifacts/N053_e149b4d5.html](artifacts/N053_e149b4d5.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [#liItemContents0 > div >> nth=0] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"] >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [div.tab_content.primary > div.account-box.user-details > div.SCROLL_BAR_CLASS:nth-of-type(2) > ul.account-list-box > li.account-list-tr:nth-of-type(2) > div.link_spring.top_spring:nth-of-type(1)] (main area, middle-centre)
inferred_clickable: (unnamed) [#liItemContents0 > div >> nth=0] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"] >> nth=0] (main area, middle-centre)
inferred_clickable: 0 [#liItemContents2 >> nth=0] (main area, middle-centre)
inferred_clickable: 2026-09-19 [#SubscriptionTable_nextPaymentDate >> nth=0] (main area, middle-right)
inferred_clickable: 2026-10-01 [#SubscriptionTable_nextPaymentDate >> nth=0] (main area, middle-right)
inferred_clickable: 3 [#liItemContents1 >> nth=0] (main area, middle-centre)
inferred_clickable: 3 [#liItemContents3 >> nth=0] (main area, middle-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]] (main area, top-centre)
inferred_clickable: Available [#sortColumn >> nth=0] (main area, middle-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Workspace [#liItemContents4 >> nth=0] (main area, middle-right)
inferred_clickable: Default Workspace [#liItemContents4 >> nth=0] (main area, middle-right)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1) >> nth=0] (main area, middle-right)
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1) >> nth=0] (main area, middle-right)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Next Payment [#sortColumn >> nth=0] (main area, middle-right)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Plan [#sortColumn >> nth=0] (main area, middle-centre)
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]] (main area, top-centre)
inferred_clickable: Pro [#liItemContents0 >> nth=0] (main area, middle-centre)
inferred_clickable: S Series Trial [#liItemContents0 > dl.dl-d > dt > span >> nth=0] (main area, middle-centre)
inferred_clickable: S Series TrialVX-TRIAL [#liItemContents0 >> nth=0] (main area, middle-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Total [#sortColumn >> nth=0] (main area, middle-centre)
inferred_clickable: Used [#sortColumn >> nth=0] (main area, middle-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#sortColumn >> nth=0] (main area, middle-right)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Primary Plan' | blocked_mutation | (self) | mutating |
| Click 'Additional Plan' | in_page_state | N071 Settings | Samsung VXT CMS — | mutating |
| Click 'Additional Plan' | navigation | N071 Settings | Samsung VXT CMS — | — |

## N054 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 2 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 404 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: No tag. [[data-testid="No tag."]] (main area, middle-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, top-right) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]] (header, top-centre)
```

## N055 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 2 · **Actionable:** 25 · **Interactive extracted:** 25 · **DOM nodes:** 402 · **Visits:** 3
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Event'
- **Screenshot:** [artifacts/N055_73b565cd.png](artifacts/N055_73b565cd.png)
- **DOM:** [artifacts/N055_73b565cd.html](artifacts/N055_73b565cd.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Event [role=button[name="New Event"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'New Event' | navigation | N074 Settings | Samsung VXT CMS | mutating |
| Click 'New Event' | navigation | N074 Settings | Samsung VXT CMS | — |

## N056 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 2 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 408 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Screen Preset'
- **Screenshot:** [artifacts/N056_281d7601.png](artifacts/N056_281d7601.png)
- **DOM:** [artifacts/N056_281d7601.html](artifacts/N056_281d7601.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Profile [role=button[name="New Profile"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]] (main area, top-centre)
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]] (main area, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Screen Profile' | no_change | (self) | inert |
| Click 'Certificate' | in_page_state | N075 Settings | Samsung VXT CMS — | — |
| Click 'Screen Software' | in_page_state | N076 Settings | Samsung VXT CMS — | — |
| Click 'New Profile' | in_page_state | N077 Settings | Samsung VXT CMS — | mutating |

## N057 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert
- **Type:** page · **Depth:** 2 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 408 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Emergency Alert'
- **Screenshot:** [artifacts/N057_90a409b3.png](artifacts/N057_90a409b3.png)
- **DOM:** [artifacts/N057_90a409b3.html](artifacts/N057_90a409b3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Emergency Alert [role=button[name="New Emergency Alert"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Emergency Alert' | navigation | N078 Settings | Samsung VXT CMS | mutating |

## N058 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 2 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 425 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Activity Log'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Action [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Detail [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Path [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Target [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: When [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Where [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

## N059 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 328 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Inquiry [role=button[name="New Inquiry"]] (main area, bottom-right)
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

## N060 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 2 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 462 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'div'

**Action elements**

```
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add] (main area, middle-right)
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]] (main area, bottom-right)
generic_button: Cancel [role=button[name="Cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Done [role=button[name="Done"]] (main area, bottom-right)
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]] (main area, top-centre)
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon] (main area, top-right)
inferred_clickable: Info Card [role=listitem[name="Info Card"]] (main area, top-right)
inferred_clickable: Title [role=listitem[name="Title"]] (main area, top-right)
radio: Logo [#title-settings-logo] (main area, top-right)
radio: Organization Name [#title-settings-organization-name] (main area, top-right)
```

## N061 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 581 · **Visits:** 3
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'General' → Click 'Register Phone Number'
- **Screenshot:** [artifacts/N061_523f6918.png](artifacts/N061_523f6918.png)
- **DOM:** [artifacts/N061_523f6918.html](artifacts/N061_523f6918.html)

**Action elements**

```
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled) (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (main area, middle-centre)
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]] (main area, top-right)
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]] (main area, bottom-centre)
inferred_clickable: 20:41 [[data-testid="select-Time Format"]] (main area, bottom-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: English [[data-testid="select-Language"]] (main area, middle-centre)
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]] (main area, bottom-centre)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]] (main area, bottom-centre)
inferred_clickable: Mon [[data-testid="select-First Day of Week"]] (main area, bottom-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div] (main area, middle-centre)
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]] (main area, middle-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: Phone Number [#phone_input] (main area, middle-centre)
text_input: Select [[data-testid="select-Country Code"]] (main area, middle-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N038 Settings | Samsung VXT CMS | mutating |

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 3
- inferred_clickable: (unnamed) -- queued for depth 3
- text_input: Select -- queued for depth 3
- text_input: Phone Number -- queued for depth 3
- generic_button: Send Code -- queued for depth 3
- generic_button: Cancel -- queued for depth 3

## N062 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 3 · **Actionable:** 62 · **Interactive extracted:** 62 · **DOM nodes:** 536 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Channel' → Click 'Search Channelsand'
- **Screenshot:** [artifacts/N062_2398e774.png](artifacts/N062_2398e774.png)
- **DOM:** [artifacts/N062_2398e774.html](artifacts/N062_2398e774.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="channel_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 channel [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 channel [#channelList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 2 [#channelCardNum > span.font16 > span.list_num:nth-of-type(1)] (main area, bottom-left)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CH 1CH 2New Channel2 channelsGeneralGeneralGeneralGeneral [[data-testid="channelCard_0"]] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: channels [#channelCardNum > span.font16 > span:nth-of-type(2)] (main area, bottom-left)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [#channelCardInfo > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, bottom-left)
inferred_clickable: GeneralGeneralGeneralGeneral [#channelCardInfo] (main area, bottom-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]] (main area, top-right)
inferred_clickable: New Channel [#channelCardTitle] (main area, middle-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Channelsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Channels [role=textbox[name="Search Channels"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 channel' | in_page_state | N063 Channel | Samsung VXT CMS —  | mutating |
| Click '1 channel' | navigation | N063 Channel | Samsung VXT CMS —  | — |

## N063 — Channel | Samsung VXT CMS — 1 channel

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 3 · **Actionable:** 66 · **Interactive extracted:** 66 · **DOM nodes:** 533 · **Visits:** 2
- **Reached by:** Click 'Screen' → Click 'Channel' → Click 'Search Channelsand' → Click '1 channel'
- **Screenshot:** [artifacts/N063_1794e1d6.png](artifacts/N063_1794e1d6.png)
- **DOM:** [artifacts/N063_1794e1d6.html](artifacts/N063_1794e1d6.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="channelCard_checkbox_0"]] (main area, top-left)
destructive: Delete [#channel_deleteBtn] (main area, top-right)
generic_button: Add Tags [#channel_addTagsBtn] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"] >> nth=0] (main area, top-right)
generic_button: Set to Screens [#channel_set2ScreensBtn] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#header_logoImg] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (left sidebar, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [#navbar_leftControl2] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="channel_sort"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (left sidebar, top-left) [app frame]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (left sidebar, top-left) [app frame]
inferred_clickable: 1 of 1 selected [[data-testid="FcmsCheckBoxWrapper"]] (main area, top-left)
inferred_clickable: 1 of 1 selected [#channelList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)] (main area, top-left)
inferred_clickable: 1 of 1 selected [#channelList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(4)] (main area, top-centre)
inferred_clickable: 2 [#channelCardNum > span.font16 > span.list_num:nth-of-type(1)] (main area, bottom-left)
inferred_clickable: and [[data-testid="and_or_toggle"]] (header, top-centre) [app frame]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: CH 1CH 2New Channel2 channelsGeneralGeneralGeneralGeneral [[data-testid="channelCard_0"]] (main area, middle-centre)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: channels [#channelCardNum > span.font16 > span:nth-of-type(2)] (main area, bottom-left)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (left sidebar, top-left) [app frame]
inferred_clickable: Content [[data-testid="navbar_li_content"]] (left sidebar, top-left) [app frame]
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: GeneralGeneral [#channelCardInfo > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, bottom-left)
inferred_clickable: GeneralGeneralGeneralGeneral [#channelCardInfo] (main area, bottom-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: New Channel [#channelCardTitle] (main area, middle-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (left sidebar, top-left) [app frame]
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (left sidebar, top-left) [app frame]
inferred_clickable: Search Channelsand [[data-testid="search_input_wrapper"]] (header, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Channels [role=textbox[name="Search Channels"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 of 1 selected' | in_page_state | N062 Channel | Samsung VXT CMS | mutating |

**Not exercised by the crawler**

- inferred_clickable: 1 of 1 selected -- queued for depth 4
- inferred_clickable: 1 of 1 selected -- queued for depth 4
- inferred_clickable: 1 of 1 selected -- queued for depth 4
- generic_button: Set to Screens -- queued for depth 4
- generic_button: Add Tags -- queued for depth 4
- destructive: Delete -- queued for depth 4
- checkbox: (unnamed) -- queued for depth 4

## N064 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 475 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'New Inquiry' → Click 'Register Phone Number'
- **Screenshot:** [artifacts/N064_da109b4b.png](artifacts/N064_da109b4b.png)
- **DOM:** [artifacts/N064_da109b4b.html](artifacts/N064_da109b4b.html)

**Action elements**

```
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]] (main area, bottom-centre)
generic_button: Open [role=button[name="Open"]] (main area, bottom-right)
generic_button: Request [role=button[name="Request"]] (main area, top-right)
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled) (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (main area, middle-centre)
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span] (main area, middle-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Select [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class] (main area, bottom-left)
text_input: (unnamed) [#select >> nth=0] (main area, bottom-centre)
text_input: Enter a subject. [role=textbox[name="Enter a subject."]] (main area, middle-centre)
text_input: Phone Number [#phone_input] (main area, middle-centre)
text_input: Select [[data-testid="select-Country Code"]] (main area, middle-centre)
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]] (main area, bottom-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N049 Settings | Samsung VXT CMS | — |

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- text_input: Select -- queued for depth 4
- text_input: Phone Number -- queued for depth 4
- generic_button: Send Code -- queued for depth 4
- generic_button: Cancel -- queued for depth 4

## N065 — Settings | Samsung VXT CMS — Customization

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 3 · **Actionable:** 49 · **Interactive extracted:** 49 · **DOM nodes:** 898 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Organization' → Click 'Customization'
- **Screenshot:** [artifacts/N065_cb57d581.png](artifacts/N065_cb57d581.png)
- **DOM:** [artifacts/N065_cb57d581.html](artifacts/N065_cb57d581.html)

**Action elements**

```
disclosure: Admin Privilege Control [role=button[name="Admin Privilege Control"]] (main area, bottom-centre)
disclosure: App Splash Logo [role=button[name="App Splash Logo"]] (main area, middle-centre)
disclosure: Content Embargo & Lifespan [role=button[name="Content Embargo & Lifespan"]] (main area, bottom-centre)
disclosure: Default Content [role=button[name="Default Content"]] (main area, bottom-centre)
disclosure: Screen Custom Fields [role=button[name="Screen Custom Fields"]] (main area, bottom-centre)
generic_button: Apply [role=button[name="Apply"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0] (main area, bottom-right)
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > div.flex_col.gap20px:nth-of-type(3) > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)] (main area, bottom-centre)
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track] (main area, bottom-right)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0] (main area, bottom-right)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0] (main area, bottom-right)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span] (main area, middle-left)
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Information [[data-testid="settings_organization_information"]] (main area, top-centre)
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]] (main area, top-centre)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]] (main area, top-right)
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- inferred_clickable: Information -- queued for depth 4
- inferred_clickable: Customization -- queued for depth 4
- generic_button: Apply -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- disclosure: App Splash Logo -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- disclosure: Default Content -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- disclosure: Screen Custom Fields -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- disclosure: Content Embargo & Lifespan -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- disclosure: Admin Privilege Control -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4

## N066 — Settings | Samsung VXT CMS — Preset

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 3 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 456 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Organization' → Click 'Preset'
- **Screenshot:** [artifacts/N066_2df846e5.png](artifacts/N066_2df846e5.png)
- **DOM:** [artifacts/N066_2df846e5.html](artifacts/N066_2df846e5.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [div.pt40.pb20:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track >> nth=0] (main area, middle-right)
inferred_clickable: (unnamed) [#SIGNAGE > li:nth-of-type(1) > div.dim:nth-of-type(2) > div:nth-of-type(1) > div.addcardcomp] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0] (main area, bottom-centre)
inferred_clickable: (unnamed) [div.pt40.pb20:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track >> nth=0] (main area, bottom-right)
inferred_clickable: (unnamed) [#SIGNAGE > li.mb40:nth-of-type(2) > div.dim:nth-of-type(2) > div:nth-of-type(1) > div.addcardcomp] (main area, bottom-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Android [role=listitem[name="Android"]] (main area, middle-centre)
inferred_clickable: Android [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, middle-centre)
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]] (main area, middle-right)
inferred_clickable: BrightSign [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(6) > span] (main area, middle-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span] (main area, middle-left)
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: E-Paper [role=listitem[name="E-Paper"]] (main area, middle-centre)
inferred_clickable: E-Paper [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Flip [role=listitem[name="Flip"]] (main area, middle-right)
inferred_clickable: Flip [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(7) > span] (main area, middle-right)
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Indoor LED Signage [role=listitem[name="Indoor LED Signage"]] (main area, middle-centre)
inferred_clickable: Indoor LED Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, middle-centre)
inferred_clickable: Information [[data-testid="settings_organization_information"]] (main area, top-centre)
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: Legacy [role=listitem[name="Legacy"]] (main area, middle-right)
inferred_clickable: Legacy [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(8) > span] (main area, middle-right)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]] (main area, top-centre)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Signage [role=listitem[name="Signage"]] (main area, middle-left)
inferred_clickable: Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]] (main area, top-right)
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Windows [role=listitem[name="Windows"]] (main area, middle-right)
inferred_clickable: Windows [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, middle-right)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- inferred_clickable: Information -- queued for depth 4
- inferred_clickable: Preset -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- inferred_clickable: Signage -- queued for depth 4
- inferred_clickable: Signage -- queued for depth 4
- inferred_clickable: Indoor LED Signage -- queued for depth 4
- inferred_clickable: Indoor LED Signage -- queued for depth 4
- inferred_clickable: E-Paper -- queued for depth 4
- inferred_clickable: E-Paper -- queued for depth 4
- inferred_clickable: Android -- queued for depth 4
- inferred_clickable: Android -- queued for depth 4
- inferred_clickable: Windows -- queued for depth 4
- inferred_clickable: Windows -- queued for depth 4
- inferred_clickable: BrightSign -- queued for depth 4
- inferred_clickable: BrightSign -- queued for depth 4
- inferred_clickable: Flip -- queued for depth 4
- inferred_clickable: Flip -- queued for depth 4
- inferred_clickable: Legacy -- queued for depth 4
- inferred_clickable: Legacy -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4

## N067 — Settings | Samsung VXT CMS — Tag

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 3 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 469 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Organization' → Click 'Tag'
- **Screenshot:** [artifacts/N067_9216d372.png](artifacts/N067_9216d372.png)
- **DOM:** [artifacts/N067_9216d372.html](artifacts/N067_9216d372.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (main area, middle-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Global CategoryAvailable for [role=button[name="Global CategoryAvailable for"]] (main area, middle-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_question"]] (main area, top-centre)
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"]] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"]] (main area, middle-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Global Category [[data-testid="setting_tag_details_rename"]] (main area, middle-centre)
inferred_clickable: Information [[data-testid="settings_organization_information"]] (main area, top-centre)
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]] (main area, top-centre)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: scrollable content [role=region[name="scrollable content"]] (main area, bottom-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]] (main area, top-right)
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- inferred_clickable: Information -- queued for depth 4
- inferred_clickable: Tag -- queued for depth 4
- inferred_clickable: scrollable content -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- generic_button: Add Category -- queued for depth 4
- generic_button: (unnamed) -- queued for depth 4
- generic_button: Global CategoryAvailable for -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Global Category -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4

## N068 — Settings | Samsung VXT CMS — Scheduling

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 3 · **Actionable:** 46 · **Interactive extracted:** 46 · **DOM nodes:** 608 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Organization' → Click 'Scheduling'
- **Screenshot:** [artifacts/N068_33eebb65.png](artifacts/N068_33eebb65.png)
- **DOM:** [artifacts/N068_33eebb65.html](artifacts/N068_33eebb65.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(3) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track] (main area, middle-right)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0] (main area, bottom-centre)
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(5) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span] (main area, middle-left)
inferred_clickable: Do not show again. [div.simplebar-offset > div.simplebar-content-wrapper > div.simplebar-content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Information [[data-testid="settings_organization_information"]] (main area, top-centre)
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_organization_preset"]] (main area, top-centre)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Sunday [[data-testid="select_default"]] (main area, bottom-right)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag [[data-testid="settings_organization_tag"]] (main area, top-right)
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Screen [role=link[name="Screen"]] (main area, bottom-centre) -> https://www.samsungvx.com/screen
nav_link: Settings > Preset [role=link[name="Settings > Preset"]] (main area, bottom-right) -> https://www.samsungvx.com/settings/screenPreset
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [#input_box > input.text_field2] (disabled) (main area, middle-right)
text_input: (unnamed) [#select >> nth=0] (main area, middle-right)
text_input: (unnamed) [#select >> nth=0] (main area, bottom-right)
```

**Not exercised by the crawler**

- inferred_clickable: Information -- queued for depth 4
- inferred_clickable: Scheduling -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- inferred_clickable: Do not show again. -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- text_input: (unnamed) -- queued for depth 4
- text_input: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Sunday -- queued for depth 4
- text_input: (unnamed) -- queued for depth 4
- nav_link: Screen -- queued for depth 4
- nav_link: Settings > Preset -- queued for depth 4

## N069 — Settings | Samsung VXT CMS — Owner

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 3 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 366 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'User' → Click 'Owner'
- **Screenshot:** [artifacts/N069_40a2aa55.png](artifacts/N069_40a2aa55.png)
- **DOM:** [artifacts/N069_40a2aa55.html](artifacts/N069_40a2aa55.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_more"]] (main area, middle-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]] (main area, top-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]] (main area, top-centre)
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Role' | in_page_state | N085 Settings | Samsung VXT CMS — | — |

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 4

## N070 — Settings | Samsung VXT CMS — Pending

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 3 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 350 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'User' → Click 'Pending'
- **Screenshot:** [artifacts/N070_9c1b4a06.png](artifacts/N070_9c1b4a06.png)
- **DOM:** [artifacts/N070_9c1b4a06.html](artifacts/N070_9c1b4a06.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Date Sent [#FcmsTable_sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]] (main area, top-centre)
inferred_clickable: No users. [[data-testid="No users."]] (main area, middle-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]] (main area, top-centre)
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]] (main area, top-right)
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, top-centre) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Invite User' | in_page_state | (self) | state-cap |
| Click 'Role' | no_change | (self) | inert |
| Click 'No users.' | no_change | (self) | inert |

**Not exercised by the crawler**

- inferred_clickable: Date Sent -- queued for depth 4

## N071 — Settings | Samsung VXT CMS — Additional Plan

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 3 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 306 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Plan' → Click 'Additional Plan'
- **Screenshot:** [artifacts/N071_c3a08a9a.png](artifacts/N071_c3a08a9a.png)
- **DOM:** [artifacts/N071_c3a08a9a.html](artifacts/N071_c3a08a9a.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]] (main area, top-centre)
inferred_clickable: Available [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Next Payment [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: No Plans [[data-testid="No Plans"]] (main area, middle-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Plan [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]] (main area, top-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Total [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Used [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#sortColumn >> nth=0] (main area, top-right)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Register Activation Code' | blocked_mutation | (self) | mutating |
| Click 'Next Payment' | no_change | (self) | inert |
| Click 'No Plans' | no_change | (self) | inert |

**Not exercised by the crawler**

- inferred_clickable: No Plans -- queued for depth 4

## N072 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 3 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 333 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag'
- **Screenshot:** [artifacts/N072_e468c7e3.png](artifacts/N072_e468c7e3.png)
- **DOM:** [artifacts/N072_e468c7e3.html](artifacts/N072_e468c7e3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default TagsetRegion, Location, Subject, Others [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents1] (main area, middle-right)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, top-right) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Tagset' | no_change | (self) | inert |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N073 Settings | Samsung VXT CMS | — |
| Click 'Default Workspace' | navigation | N073 Settings | Samsung VXT CMS | — |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N073 Settings | Samsung VXT CMS | — |

## N073 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 733 · **Visits:** 3
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others'
- **Screenshot:** [artifacts/N073_a67c73ca.png](artifacts/N073_a67c73ca.png)
- **DOM:** [artifacts/N073_a67c73ca.html](artifacts/N073_a67c73ca.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input] (main area, top-left)
generic_button: (unnamed) [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled) (main area, middle-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]] (main area, bottom-centre)
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]] (main area, bottom-centre)
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]] (main area, bottom-centre)
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (header, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span] (header, top-centre)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, middle-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Default Tagset' | in_page_state | N086 Settings | Samsung VXT CMS — | — |
| Click 'span' | in_page_state | N086 Settings | Samsung VXT CMS — | — |
| Click 'checkbox' | in_page_state | N087 Settings | Samsung VXT CMS — | error |
| Click 'Add Workspace' | in_page_state | N088 Settings | Samsung VXT CMS — | — |
| Click 'Workspace' | no_change | (self) | inert |
| Click 'Default Workspace' | no_change | (self) | inert |
| Click 'Add Category' | in_page_state | N089 Settings | Samsung VXT CMS — | mutating |
| Click 'Change Color' | in_page_state | (self) | state-cap |
| Click 'Region' | in_page_state | (self) | state-cap, mutating |
| Click 'div' | in_page_state | (self) | state-cap |

## N074 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 3 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 472 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Event' → Click 'New Event'
- **Screenshot:** [artifacts/N074_c775cc72.png](artifacts/N074_c775cc72.png)
- **DOM:** [artifacts/N074_c775cc72.html](artifacts/N074_c775cc72.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (main area, top-right) [app frame]
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Save [[data-testid="setting_event_new_add_save"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_question"]] (main area, top-centre)
inferred_clickable: 1.5 [[data-testid="select_default"] >> nth=0] (main area, bottom-right)
inferred_clickable: 115200 [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: 4 [[data-testid="select_default"] >> nth=0] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: ASCII [[data-testid="select_default"] >> nth=0] (main area, bottom-right)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Workspace [#FcmsTable_liItemA0] (main area, bottom-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: None [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: None [[data-testid="select_default"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, bottom-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd] (main area, middle-centre)
radio: Network [#event_type_network] (main area, middle-right)
radio: Serial Port [#event_type_serial] (main area, middle-left)
radio: Weather [#event_type_weather] (main area, middle-centre)
text_input: Enter key. [role=textbox[name="Enter key."]] (main area, bottom-right)
text_input: Enter port number. [role=textbox[name="Enter port number."]] (disabled) (main area, bottom-centre)
text_input: New Event [[data-testid="FCMSInput"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Save' | in_page_state | (self) | state-cap |
| Click 'Connect external devices through serial port communication t' | in_page_state | (self) | state-cap |
| Click 'Serial Port' | in_page_state | (self) | state-cap |
| Click 'Weather' | in_page_state | (self) | state-cap |
| Click 'Crowd Count' | in_page_state | (self) | state-cap |
| Click 'Network' | in_page_state | (self) | state-cap |
| Click '115200' | in_page_state | (self) | state-cap |
| Click 'Add' | in_page_state | (self) | state-cap |
| Click 'Default Workspace' | navigation | N090 Settings | Samsung VXT CMS | — |

## N075 — Settings | Samsung VXT CMS — Certificate

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 3 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Screen Preset' → Click 'Certificate'
- **Screenshot:** [artifacts/N075_07662a8e.png](artifacts/N075_07662a8e.png)
- **DOM:** [artifacts/N075_07662a8e.html](artifacts/N075_07662a8e.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Certificate [role=button[name="New Certificate"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]] (main area, top-centre)
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]] (main area, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- generic_button: New Certificate -- queued for depth 4

## N076 — Settings | Samsung VXT CMS — Screen Software

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 3 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Screen Preset' → Click 'Screen Software'
- **Screenshot:** [artifacts/N076_cda0e47d.png](artifacts/N076_cda0e47d.png)
- **DOM:** [artifacts/N076_cda0e47d.html](artifacts/N076_cda0e47d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Screen Software [role=button[name="New Screen Software"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]] (main area, top-centre)
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]] (main area, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- generic_button: New Screen Software -- queued for depth 4

## N077 — Settings | Samsung VXT CMS — New Profile

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 381 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Screen Preset' → Click 'New Profile'
- **Screenshot:** [artifacts/N077_f5954a75.png](artifacts/N077_f5954a75.png)
- **DOM:** [artifacts/N077_f5954a75.html](artifacts/N077_f5954a75.html)

**Action elements**

```
external_link: Supported Models → [role=link[name="Supported Models →"]] (left sidebar, bottom-left) -> https://vxt.samsung.com/pricing
generic_button: Cancel [#footer_rightPart_cancelBtn] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: New Profile [role=button[name="New Profile"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, middle-left)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, middle-right)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, bottom-centre)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, bottom-right)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0] (main area, bottom-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]] (main area, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]] (main area, top-centre)
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]] (main area, top-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- external_link: Supported Models → -- queued for depth 4
- generic_button: Cancel -- queued for depth 4

## N078 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 421 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Emergency Alert' → Click 'New Emergency Alert'

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]] (main area, bottom-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, bottom-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (main area, bottom-centre) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: New Emergency Alert [[data-testid="FCMSInput"]] (header, top-centre)
```

## N079 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 3 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 633 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Activity Log'
- **Screenshot:** [artifacts/N079_41a46fe6.png](artifacts/N079_41a46fe6.png)
- **DOM:** [artifacts/N079_41a46fe6.html](artifacts/N079_41a46fe6.html)

**Action elements**

```
generic_button: Apply [[data-testid="setting_activity_log_apply"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Export [[data-testid="activity_btnExport"]] (disabled) (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_activityLog_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Action [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Detail [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Path [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Target [#sortColumn >> nth=0] (main area, top-right)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: When [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Where [#sortColumn >> nth=0] (main area, top-centre)
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Logs [[data-testid="Activity Log_settingHeader_input"]] (header, top-centre)
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(1) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class] (main area, top-centre)
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(2) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class] (main area, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Apply' | no_change | (self) | inert |
| Click 'When' | no_change | (self) | inert |

## N080 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 3 · **Actionable:** 46 · **Interactive extracted:** 46 · **DOM nodes:** 432 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home'
- **Screenshot:** [artifacts/N080_4c54d46e.png](artifacts/N080_4c54d46e.png)
- **DOM:** [artifacts/N080_4c54d46e.html](artifacts/N080_4c54d46e.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (left sidebar, middle-left) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add] (main area, middle-right)
generic_button: Apps [role=button[name="Apps"]] (main area, middle-centre)
generic_button: Cancel [role=button[name="Cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-left)
generic_button: Done [role=button[name="Done"]] (main area, bottom-right)
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-centre)
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]] (left sidebar, middle-left)
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]] (main area, middle-left)
generic_button: refresh [#refreshScreenBtn] (main area, middle-centre)
generic_button: Reset All [[data-testid="reset-dashboard-button"]] (main area, bottom-right)
generic_button: StorageUsed1.50MB [role=button[name="StorageUsed1.50MB"]] (main area, middle-centre)
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: * Supported formats File format: *.png Image height: 58 px F [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre) [app frame]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (left sidebar, middle-left)
inferred_clickable: Content [#dashboard_contentCard] (main area, top-left)
inferred_clickable: content [#contentCard_defaultImg] (main area, top-left)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-left) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: Info Card [role=listitem[name="Info Card"]] (main area, top-right)
inferred_clickable: Mobile View [[data-testid="icon_ic_mobile"]] (main area, top-centre)
inferred_clickable: PC View [[data-testid="icon_ic_web"]] (main area, top-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, top-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, top-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (left sidebar, middle-left)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, top-centre)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, top-centre)
inferred_clickable: Screen [#dashboard_screenCard] (left sidebar, top-left)
inferred_clickable: screen [#screenCard_defaultImg] (left sidebar, top-left)
inferred_clickable: Title [role=listitem[name="Title"]] (main area, top-right)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo] (main area, top-right)
radio: Organization Name [#title-settings-organization-name] (main area, top-right)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'PC View' | no_change | (self) | inert |
| Click 'Mobile View' | in_page_state | N081 Settings | Samsung VXT CMS — | — |
| Click 'Organization Name' | blocked_mutation | (self) | mutating |
| Click '* Supported formats File format: *.png Image height: 58 px F' | no_change | (self) | inert |
| Click 'Logo' | file_chooser | (self) | mutating, upload |
| Click 'button' | file_chooser | (self) | upload |
| Click 'Apps' | blocked_mutation | (self) | mutating |
| Click 'Normal-' | in_page_state | N082 Settings | Samsung VXT CMS — | mutating |
| Click 'Warning-' | in_page_state | N082 Settings | Samsung VXT CMS — | — |
| Click 'Deactivated-' | in_page_state | N082 Settings | Samsung VXT CMS — | — |
| Click 'Reset All' | in_page_state | N083 Settings | Samsung VXT CMS — | — |
| Click 'Cancel' | navigation | N084 Samsung VXT CMS | mutating |
| Click 'Cancel' | navigation | N079 Settings | Samsung VXT CMS | — |

## N081 — Settings | Samsung VXT CMS — Mobile View

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 3 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 505 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home' → Click 'Mobile View'
- **Screenshot:** [artifacts/N081_43c2cd34.png](artifacts/N081_43c2cd34.png)
- **DOM:** [artifacts/N081_43c2cd34.html](artifacts/N081_43c2cd34.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (main area, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add] (main area, middle-right)
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]] (main area, bottom-right)
generic_button: Apps [role=button[name="Apps"]] (main area, bottom-centre)
generic_button: Cancel [role=button[name="Cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, bottom-centre)
generic_button: Done [role=button[name="Done"]] (main area, bottom-right)
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, bottom-centre)
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, bottom-left)
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]] (main area, bottom-centre)
generic_button: refresh [#refreshScreenBtn] (main area, bottom-centre)
generic_button: StorageUsed1.50MBVideo0.00KBImage0.00KBCanvas1.50MBOffice0.00KBWeb(HTML)0.00KBOthers0.00KB [role=button[name="StorageUsed1.50MBVideo0.00KBImage0.00KBCanvas1.50MBOffice0.00KBWeb(HTML)0.00KBOthers0.00KB"]] (main area, bottom-centre)
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, bottom-left)
inferred_clickable: (unnamed) [#moHeader_menu] (header, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-right)
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)] (left sidebar, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (main area, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-mobile_1ukjs_2:nth-of-type(2) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.storage-mobile:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, bottom-centre)
inferred_clickable: * Supported formats File format: *.png Image height: 58 px F [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (header, top-centre) [app frame]
inferred_clickable: 0 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span] (main area, bottom-centre)
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span] (main area, middle-centre)
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span] (main area, bottom-centre)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-left)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (main area, bottom-left)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, bottom-left)
inferred_clickable: Content [#dashboard_contentCard] (main area, middle-centre)
inferred_clickable: content [#contentCard_defaultImg] (main area, middle-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#moHeader_place > div > div.select_bottom_wrap > div:nth-of-type(1)] (header, top-left)
inferred_clickable: Info Card [role=listitem[name="Info Card"]] (main area, top-right)
inferred_clickable: logo [#moHeader_logoImg\ ga-button-action-class] (header, top-centre)
inferred_clickable: Mobile View [[data-testid="icon_ic_mobile"]] (main area, top-centre)
inferred_clickable: PC View [[data-testid="icon_ic_web"]] (main area, top-left)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-right)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-right)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (main area, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span] (main area, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, bottom-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-centre)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-centre)
inferred_clickable: Title [role=listitem[name="Title"]] (main area, top-right)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, bottom-left)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (main area, bottom-left) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (main area, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (main area, bottom-centre) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (main area, bottom-left) [app frame] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo] (main area, top-right)
radio: Organization Name [#title-settings-organization-name] (main area, top-right)
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: logo -- queued for depth 4
- inferred_clickable: Default Workspace .st0{opacity:0.8;} -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: Allocation 3 -- queued for depth 4
- inferred_clickable: 3 -- queued for depth 4
- inferred_clickable: Used 0 -- queued for depth 4
- inferred_clickable: 0 -- queued for depth 4
- inferred_clickable: Available 3 -- queued for depth 4
- inferred_clickable: 3 -- queued for depth 4
- generic_button: StorageUsed1.50MBVideo0.00KBImage0.00KBCanvas1.50MBOffice0.00KBWeb(HTML)0.00KBOthers0.00KB -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4

## N082 — Settings | Samsung VXT CMS — Deactivated-

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 128 · **Interactive extracted:** 128 · **DOM nodes:** 604 · **Visits:** 3
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home' → Click 'Normal-'
- **Screenshot:** [artifacts/N082_93c00641.png](artifacts/N082_93c00641.png)
- **DOM:** [artifacts/N082_93c00641.html](artifacts/N082_93c00641.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (left sidebar, middle-left) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add] (main area, middle-right)
generic_button: Apps [role=button[name="Apps"]] (main area, middle-centre)
generic_button: Cancel [role=button[name="Cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-left)
generic_button: Done [role=button[name="Done"]] (main area, bottom-right)
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-centre)
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]] (left sidebar, middle-left)
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]] (main area, middle-left)
generic_button: refresh [#refreshScreenBtn] (main area, middle-centre)
generic_button: Reset All [[data-testid="reset-dashboard-button"]] (main area, bottom-right)
generic_button: StorageUsed1.50MB [role=button[name="StorageUsed1.50MB"]] (main area, middle-centre)
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: (unnamed) [div.advanced_option.active > div:nth-of-type(2) > div._f_ti_1qe1m_65:nth-of-type(1) > div.screen-status-title > div > div.center-wrapper.hover-icon] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0] (main area, top-left)
inferred_clickable: * Supported formats File format: *.png Image height: 58 px F [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre) [app frame]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (left sidebar, middle-left)
inferred_clickable: Android [[data-testid="search_systemtag_104"]] (main area, top-centre)
inferred_clickable: AndroidAndroid [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)] (main area, top-centre)
inferred_clickable: BrightSign [[data-testid="search_systemtag_188"]] (main area, top-right)
inferred_clickable: BrightSignBrightSign [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)] (main area, top-right)
inferred_clickable: Business TV [[data-testid="search_systemtag_95"]] (main area, top-centre)
inferred_clickable: Business TVBusiness TV [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: Connected [[data-testid="search_systemtag_106"]] (main area, top-left)
inferred_clickable: ConnectedConnected [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-left)
inferred_clickable: Content [#dashboard_contentCard] (main area, top-left)
inferred_clickable: content [#contentCard_defaultImg] (main area, top-left)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, top-right) [app frame]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)] (main area, middle-right) [app frame]
inferred_clickable: Deactivated [[data-testid="search_systemtag_115"]] (main area, top-centre)
inferred_clickable: DeactivatedDeactivated [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(12)] (main area, top-centre)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-left) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: Disconnected [[data-testid="search_systemtag_107"]] (main area, top-centre)
inferred_clickable: DisconnectedDisconnected [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-left)
inferred_clickable: DP: No Signal [[data-testid="search_systemtag_189"]] (main area, top-centre)
inferred_clickable: DP: No SignalDP: No Signal [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(9)] (main area, top-centre)
inferred_clickable: E-Paper [[data-testid="search_systemtag_96"]] (main area, top-centre)
inferred_clickable: E-PaperE-Paper [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre)
inferred_clickable: Flip [[data-testid="search_systemtag_99"]] (main area, top-centre)
inferred_clickable: FlipFlip [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre)
inferred_clickable: HDMI: No Signal [[data-testid="search_systemtag_113"]] (main area, top-left)
inferred_clickable: HDMI: No SignalHDMI: No Signal [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)] (main area, top-left)
inferred_clickable: Indoor LED Signage [[data-testid="search_systemtag_93"]] (main area, top-centre)
inferred_clickable: Indoor LED SignageIndoor LED Signage [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-centre)
inferred_clickable: Info Card [role=listitem[name="Info Card"]] (main area, top-right)
inferred_clickable: Landscape [[data-testid="search_systemtag_186"]] (main area, top-left)
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-left) [app frame]
inferred_clickable: Legacy [[data-testid="search_systemtag_194"]] (main area, top-right)
inferred_clickable: LegacyLegacy [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(9)] (main area, top-right)
inferred_clickable: Now Playing [[data-testid="search_systemtag_109"]] (main area, top-centre)
inferred_clickable: Now PlayingNow Playing [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre)
inferred_clickable: Player Inactive [[data-testid="search_systemtag_111"]] (main area, top-centre)
inferred_clickable: Player InactivePlayer Inactive [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: Playing Default Content [[data-testid="search_systemtag_112"]] (main area, top-right)
inferred_clickable: Playing Default ContentPlaying Default Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)] (main area, top-right)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, top-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, top-centre)
inferred_clickable: Portrait [[data-testid="search_systemtag_187"]] (main area, top-left)
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-left) [app frame]
inferred_clickable: Power Off [[data-testid="search_systemtag_110"]] (main area, top-centre)
inferred_clickable: Power OffPower Off [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (left sidebar, middle-left)
inferred_clickable: RM Inactive [[data-testid="search_systemtag_114"]] (main area, top-centre)
inferred_clickable: RM InactiveRM Inactive [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(11)] (main area, top-centre)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, top-centre)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, top-centre)
inferred_clickable: Screen [#dashboard_screenCard] (left sidebar, top-left)
inferred_clickable: screen [#screenCard_defaultImg] (left sidebar, top-left)
inferred_clickable: Screen Wall [[data-testid="search_systemtag_101"]] (main area, top-centre)
inferred_clickable: Screen WallScreen Wall [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(11)] (main area, top-centre)
inferred_clickable: Signage [[data-testid="search_systemtag_92"]] (main area, top-left)
inferred_clickable: SignageSignage [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-left)
inferred_clickable: Sleep [[data-testid="search_systemtag_108"]] (main area, top-centre)
inferred_clickable: SleepSleep [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre)
inferred_clickable: Title [role=listitem[name="Title"]] (main area, top-right)
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, top-left) [app frame]
inferred_clickable: Today [[data-testid="Today"] >> nth=0] (main area, middle-left) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, top-left) [app frame]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)] (main area, middle-left) [app frame]
inferred_clickable: Unknown [[data-testid="search_systemtag_105"]] (main area, top-centre)
inferred_clickable: UnknownUnknown [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(12)] (main area, top-centre)
inferred_clickable: Virtual Screen [[data-testid="search_systemtag_102"]] (main area, top-left)
inferred_clickable: Virtual ScreenVirtual Screen [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(10)] (main area, top-left)
inferred_clickable: Wait for Pairing [[data-testid="search_systemtag_117"]] (main area, top-right)
inferred_clickable: Wait for PairingWait for Pairing [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(13)] (main area, top-right)
inferred_clickable: Wait for VXT Player Update [[data-testid="search_systemtag_145"]] (main area, top-centre)
inferred_clickable: Wait for VXT Player UpdateWait for VXT Player Update [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(10)] (main area, top-centre)
inferred_clickable: Windows [[data-testid="search_systemtag_103"]] (main area, top-centre)
inferred_clickable: WindowsWindows [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, top-centre) [app frame]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre) [app frame]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, top-centre) [app frame]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)] (main area, middle-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0] (main area, middle-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, top-centre) [app frame]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)] (main area, middle-centre) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, top-left) [app frame]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0] (main area, middle-left) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, top-left) [app frame]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)] (main area, middle-left) [app frame]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo] (main area, top-right)
radio: Organization Name [#title-settings-organization-name] (main area, top-right)
```

**Not exercised by the crawler**

- inferred_clickable: SignageSignage -- queued for depth 4
- inferred_clickable: Signage -- queued for depth 4
- inferred_clickable: Indoor LED SignageIndoor LED Signage -- queued for depth 4
- inferred_clickable: Indoor LED Signage -- queued for depth 4
- inferred_clickable: Business TVBusiness TV -- queued for depth 4
- inferred_clickable: Business TV -- queued for depth 4
- inferred_clickable: E-PaperE-Paper -- queued for depth 4
- inferred_clickable: E-Paper -- queued for depth 4
- inferred_clickable: FlipFlip -- queued for depth 4
- inferred_clickable: Flip -- queued for depth 4
- inferred_clickable: WindowsWindows -- queued for depth 4
- inferred_clickable: Windows -- queued for depth 4
- inferred_clickable: AndroidAndroid -- queued for depth 4
- inferred_clickable: Android -- queued for depth 4
- inferred_clickable: BrightSignBrightSign -- queued for depth 4
- inferred_clickable: BrightSign -- queued for depth 4
- inferred_clickable: LegacyLegacy -- queued for depth 4
- inferred_clickable: Legacy -- queued for depth 4
- inferred_clickable: Virtual ScreenVirtual Screen -- queued for depth 4
- inferred_clickable: Virtual Screen -- queued for depth 4
- inferred_clickable: Screen WallScreen Wall -- queued for depth 4
- inferred_clickable: Screen Wall -- queued for depth 4
- inferred_clickable: UnknownUnknown -- queued for depth 4
- inferred_clickable: Unknown -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: (unnamed) -- queued for depth 4
- inferred_clickable: ConnectedConnected -- queued for depth 4
- inferred_clickable: Connected -- queued for depth 4
- inferred_clickable: DisconnectedDisconnected -- queued for depth 4
- inferred_clickable: Disconnected -- queued for depth 4
- inferred_clickable: SleepSleep -- queued for depth 4
- inferred_clickable: Sleep -- queued for depth 4
- inferred_clickable: Now PlayingNow Playing -- queued for depth 4
- inferred_clickable: Now Playing -- queued for depth 4
- inferred_clickable: Power OffPower Off -- queued for depth 4
- inferred_clickable: Power Off -- queued for depth 4
- inferred_clickable: Player InactivePlayer Inactive -- queued for depth 4
- inferred_clickable: Player Inactive -- queued for depth 4
- inferred_clickable: Playing Default ContentPlaying Default Content -- queued for depth 4
- inferred_clickable: Playing Default Content -- queued for depth 4
- inferred_clickable: HDMI: No SignalHDMI: No Signal -- queued for depth 4
- inferred_clickable: HDMI: No Signal -- queued for depth 4
- inferred_clickable: DP: No SignalDP: No Signal -- queued for depth 4
- inferred_clickable: DP: No Signal -- queued for depth 4
- inferred_clickable: Wait for VXT Player UpdateWait for VXT Player Update -- queued for depth 4
- inferred_clickable: Wait for VXT Player Update -- queued for depth 4
- inferred_clickable: RM InactiveRM Inactive -- queued for depth 4
- inferred_clickable: RM Inactive -- queued for depth 4
- inferred_clickable: DeactivatedDeactivated -- queued for depth 4
- inferred_clickable: Deactivated -- queued for depth 4
- inferred_clickable: Wait for PairingWait for Pairing -- queued for depth 4
- inferred_clickable: Wait for Pairing -- queued for depth 4
- inferred_clickable: LandscapeLandscape -- queued for depth 4
- inferred_clickable: Landscape -- queued for depth 4
- inferred_clickable: PortraitPortrait -- queued for depth 4
- inferred_clickable: Portrait -- queued for depth 4
- inferred_clickable: TodayToday -- queued for depth 4
- inferred_clickable: Today -- queued for depth 4
- inferred_clickable: YesterdayYesterday -- queued for depth 4
- inferred_clickable: Yesterday -- queued for depth 4
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 4
- inferred_clickable: Within 3 Days -- queued for depth 4
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 4
- inferred_clickable: Within a Week -- queued for depth 4
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 4
- inferred_clickable: Within a Month -- queued for depth 4
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 4
- inferred_clickable: Within 3 Months -- queued for depth 4
- inferred_clickable: Custom -- queued for depth 4
- inferred_clickable: TodayToday -- queued for depth 4
- inferred_clickable: Today -- queued for depth 4
- inferred_clickable: YesterdayYesterday -- queued for depth 4
- inferred_clickable: Yesterday -- queued for depth 4
- inferred_clickable: Within 3 DaysWithin 3 Days -- queued for depth 4
- inferred_clickable: Within 3 Days -- queued for depth 4
- inferred_clickable: Within a WeekWithin a Week -- queued for depth 4
- inferred_clickable: Within a Week -- queued for depth 4
- inferred_clickable: Within a MonthWithin a Month -- queued for depth 4
- inferred_clickable: Within a Month -- queued for depth 4
- inferred_clickable: Within 3 MonthsWithin 3 Months -- queued for depth 4
- inferred_clickable: Within 3 Months -- queued for depth 4
- inferred_clickable: Custom -- queued for depth 4

## N083 — Settings | Samsung VXT CMS — Reset All

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 439 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home' → Click 'Reset All'
- **Screenshot:** [artifacts/N083_7ff07dcc.png](artifacts/N083_7ff07dcc.png)
- **DOM:** [artifacts/N083_7ff07dcc.html](artifacts/N083_7ff07dcc.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (left sidebar, middle-left) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add] (main area, middle-right)
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]] (main area, bottom-right)
generic_button: Apps [role=button[name="Apps"]] (main area, middle-centre)
generic_button: Cancel [role=button[name="Cancel"]] (main area, bottom-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]] (main area, middle-left)
generic_button: Done [role=button[name="Done"]] (main area, bottom-right)
generic_button: editHome [[data-testid="dashboard_editbtn"]] (main area, middle-centre)
generic_button: No [role=button[name="No"]] (main area, middle-centre)
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]] (left sidebar, middle-left)
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]] (main area, middle-left)
generic_button: refresh [#refreshScreenBtn] (main area, middle-centre)
generic_button: StorageUsed1.50MB [role=button[name="StorageUsed1.50MB"]] (main area, middle-centre)
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-left)
generic_button: Yes [role=button[name="Yes"]] (main area, middle-centre)
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]] (left sidebar, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]] (main area, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (left sidebar, middle-left)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-centre)
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon] (main area, top-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre) [app frame]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]] (left sidebar, middle-left)
inferred_clickable: Content [#dashboard_contentCard] (main area, top-left)
inferred_clickable: content [#contentCard_defaultImg] (main area, top-left)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (main area, top-left) [app frame]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div] (main area, top-centre) [app frame]
inferred_clickable: Info Card [role=listitem[name="Info Card"]] (main area, top-right)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, top-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, top-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (left sidebar, middle-left)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, top-centre)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, top-centre)
inferred_clickable: Screen [#dashboard_screenCard] (left sidebar, top-left)
inferred_clickable: screen [#screenCard_defaultImg] (left sidebar, top-left)
inferred_clickable: Title [role=listitem[name="Title"]] (main area, top-right)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (left sidebar, middle-left) [app frame] -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo] (main area, top-right)
radio: Organization Name [#title-settings-organization-name] (main area, top-right)
```

**Not exercised by the crawler**

- generic_button: No -- queued for depth 4
- generic_button: Yes -- queued for depth 4

## N084 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 3 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Edit Home' → Click 'Cancel'

_No actionable elements extracted._

## N085 — Settings | Samsung VXT CMS — Owner — Role

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 57 · **Interactive extracted:** 57 · **DOM nodes:** 426 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'User' → Click 'Owner' → Click 'Role'
- **Screenshot:** [artifacts/N085_e85632c2.png](artifacts/N085_e85632c2.png)
- **DOM:** [artifacts/N085_e85632c2.html](artifacts/N085_e85632c2.html)

**Action elements**

```
destructive: Prime Owner possesses all owner privileges plus additional rights to invite up to 3 owners and delete the organization. [#RolesTable_Guide_undefined >> nth=0] (main area, middle-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]] (header, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_prime_owner"]] (main area, middle-centre)
inferred_clickable: A-Manager [ul.account-list-box > li.account-list-tr:nth-of-type(4) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.a_manager] (main area, bottom-centre)
inferred_clickable: A-ManagerAll-Manager manages screens and content for their workspaces. [role=listitem[name="A-ManagerAll-Manager manages screens and content for their workspaces."]] (main area, bottom-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Admin [role=listitem[name="Admin"]] (main area, middle-centre)
inferred_clickable: Admin can manage their own workspaces, including plan management. [#RolesTable_Guide_undefined >> nth=0] (main area, middle-centre)
inferred_clickable: AdminAdmin can manage their own workspaces, including plan management. [role=listitem[name="AdminAdmin can manage their own workspaces, including plan management."]] (main area, middle-centre)
inferred_clickable: All-Manager manages screens and content for their workspaces. [#RolesTable_Guide_undefined >> nth=0] (main area, bottom-centre)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: C-Manager [ul.account-list-box > li.account-list-tr:nth-of-type(6) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.c_manager] (main area, bottom-centre)
inferred_clickable: C-ManagerContent-Manager can create or manage content, but content publishing and screen management are limited. [role=listitem[name="C-ManagerContent-Manager can create or manage content, but content publishing and screen management are limited."]] (main area, bottom-centre)
inferred_clickable: Content-Manager can create or manage content, but content publishing and screen management are limited. [#RolesTable_Guide_undefined >> nth=0] (main area, bottom-centre)
inferred_clickable: Description [role=listitem[name="Description"]] (main area, top-left)
inferred_clickable: Description [div.tab_content.role > div._tab_comp_w4n70_1.contents_2dep:nth-of-type(1) > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span] (main area, top-left)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Installer [ul.account-list-box > li.account-list-tr:nth-of-type(8) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.installer] (main area, bottom-centre)
inferred_clickable: Installer can add the screens and edit basic screen information. [#RolesTable_Guide_undefined >> nth=0] (main area, bottom-centre)
inferred_clickable: InstallerInstaller can add the screens and edit basic screen information. [role=listitem[name="InstallerInstaller can add the screens and edit basic screen information."]] (main area, bottom-centre)
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]] (main area, top-centre)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]] (main area, top-centre)
inferred_clickable: Owner [role=listitem[name="Owner"]] (main area, middle-centre)
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]] (main area, top-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Prime Owner [ul.account-list-box > li.account-list-tr:nth-of-type(1) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.prime_owner] (main area, middle-centre)
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]] (main area, top-right)
inferred_clickable: S-Manager [ul.account-list-box > li.account-list-tr:nth-of-type(5) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.s_manager] (main area, bottom-centre)
inferred_clickable: S-ManagerScreen-Manager can add or manage screens, but content management is limited. [role=listitem[name="S-ManagerScreen-Manager can add or manage screens, but content management is limited."]] (main area, bottom-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Screen-Manager can add or manage screens, but content management is limited. [#RolesTable_Guide_undefined >> nth=0] (main area, bottom-centre)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Tag-Bound Role [role=listitem[name="Tag-Bound Role"]] (main area, top-centre)
inferred_clickable: Tag-Bound Role [div._tab_comp_w4n70_1.contents_2dep:nth-of-type(1) > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span > div.flex_center.gap6px] (main area, top-centre)
inferred_clickable: Tag-Bound Role [ul.account-list-box > li.account-list-tr:nth-of-type(9) > div.account-list-con > ul.account-list-contents > li:nth-of-type(1) > div.rolebadge.tag_bound] (main area, bottom-centre)
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Viewer [role=listitem[name="Viewer"]] (main area, bottom-centre)
inferred_clickable: Viewer can view content, screens and users in the workspaces they have access to. [#RolesTable_Guide_undefined >> nth=0] (main area, bottom-centre)
inferred_clickable: ViewerViewer can view content, screens and users in the workspaces they have access to. [role=listitem[name="ViewerViewer can view content, screens and users in the workspaces they have access to."]] (main area, bottom-centre)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]] (header, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: Description -- queued for depth 5
- inferred_clickable: Description -- queued for depth 5
- inferred_clickable: Tag-Bound Role -- queued for depth 5
- inferred_clickable: Tag-Bound Role -- queued for depth 5
- inferred_clickable: Prime Owner -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5
- destructive: Prime Owner possesses all owner privileges plus additional rights to invite up to 3 owners and delete the organization. -- queued for depth 5
- inferred_clickable: Owner -- queued for depth 5
- inferred_clickable: AdminAdmin can manage their own workspaces, including plan management. -- queued for depth 5
- inferred_clickable: Admin -- queued for depth 5
- inferred_clickable: Admin can manage their own workspaces, including plan management. -- queued for depth 5
- inferred_clickable: A-ManagerAll-Manager manages screens and content for their workspaces. -- queued for depth 5
- inferred_clickable: A-Manager -- queued for depth 5
- inferred_clickable: All-Manager manages screens and content for their workspaces. -- queued for depth 5
- inferred_clickable: S-ManagerScreen-Manager can add or manage screens, but content management is limited. -- queued for depth 5
- inferred_clickable: S-Manager -- queued for depth 5
- inferred_clickable: Screen-Manager can add or manage screens, but content management is limited. -- queued for depth 5
- inferred_clickable: C-ManagerContent-Manager can create or manage content, but content publishing and screen management are limited. -- queued for depth 5
- inferred_clickable: C-Manager -- queued for depth 5
- inferred_clickable: Content-Manager can create or manage content, but content publishing and screen management are limited. -- queued for depth 5
- inferred_clickable: ViewerViewer can view content, screens and users in the workspaces they have access to. -- queued for depth 5
- inferred_clickable: Viewer -- queued for depth 5
- inferred_clickable: Viewer can view content, screens and users in the workspaces they have access to. -- queued for depth 5
- inferred_clickable: InstallerInstaller can add the screens and edit basic screen information. -- queued for depth 5
- inferred_clickable: Installer -- queued for depth 5
- inferred_clickable: Installer can add the screens and edit basic screen information. -- queued for depth 5
- inferred_clickable: Tag-Bound Role -- queued for depth 5

## N086 — Settings | Samsung VXT CMS — span

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 4 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 719 · **Visits:** 2
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Default Tagset'
- **Screenshot:** [artifacts/N086_8f1e69d7.png](artifacts/N086_8f1e69d7.png)
- **DOM:** [artifacts/N086_8f1e69d7.html](artifacts/N086_8f1e69d7.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input] (main area, top-left)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled) (main area, middle-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]] (main area, bottom-centre)
generic_button: More [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]] (main area, bottom-centre)
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]] (main area, bottom-centre)
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Add Tag [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Change Color [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, middle-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: Default Tagset [[data-testid="FCMSInput"]] (header, top-centre)
```

**Not exercised by the crawler**

- text_input: Default Tagset -- queued for depth 5

## N087 — Settings | Samsung VXT CMS — checkbox

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 4 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 714 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'checkbox'
- **Screenshot:** [artifacts/N087_546c84e5.png](artifacts/N087_546c84e5.png)
- **DOM:** [artifacts/N087_546c84e5.html](artifacts/N087_546c84e5.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input] (main area, top-left)
destructive: Remove Workspace [[data-testid="setting_tag_details_add_workspace"]] (main area, top-right)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled) (main area, middle-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]] (main area, bottom-centre)
generic_button: More [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]] (main area, bottom-centre)
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]] (main area, bottom-centre)
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Change Color [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span] (header, top-centre)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (header, top-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, middle-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

**Not exercised by the crawler**

- destructive: Remove Workspace -- queued for depth 5

## N088 — Settings | Samsung VXT CMS — Add Workspace

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 766 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Add Workspace'
- **Screenshot:** [artifacts/N088_e442ded7.png](artifacts/N088_e442ded7.png)
- **DOM:** [artifacts/N088_e442ded7.html](artifacts/N088_e442ded7.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input] (main area, top-left)
generic_button: (unnamed) [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled) (main area, middle-right)
generic_button: Add [[data-testid="setting_tag_details_apply"]] (main area, bottom-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]] (main area, top-right)
generic_button: Cancel [[data-testid="setting_tag_details_close"]] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]] (main area, bottom-centre)
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]] (main area, bottom-centre)
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]] (main area, bottom-centre)
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (header, top-centre)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_close"] >> nth=0] (main area, top-right)
inferred_clickable: (unnamed) [#SelectOrgDialog_search] (main area, top-right)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span] (header, top-centre)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, middle-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="setting_tag_details_search_workspace"]] (main area, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5
- search: Search Workspaces -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5
- generic_button: Cancel -- queued for depth 5
- generic_button: Add -- queued for depth 5

## N089 — Settings | Samsung VXT CMS — Add Category

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 804 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Add Category'
- **Screenshot:** [artifacts/N089_1eaee483.png](artifacts/N089_1eaee483.png)
- **DOM:** [artifacts/N089_1eaee483.html](artifacts/N089_1eaee483.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input] (main area, top-left)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled) (main area, middle-right)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]] (main area, middle-right)
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]] (main area, top-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]] (main area, bottom-centre)
generic_button: More [#ModalFooter_btnMore] (main area, top-right) [app frame]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]] (main area, bottom-centre)
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]] (main area, bottom-centre)
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]] (main area, bottom-centre)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [div.account-box-top.chip-turquoise:nth-of-type(1) > div.card-chip-name:nth-of-type(1) > div.mr8:nth-of-type(1) > div.tag-color-editbox-target > div > div] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [div.tag-box:nth-of-type(5) > div.account-box.yes-hover:nth-of-type(2) > div.account-box-top.chip-turquoise:nth-of-type(1) > div.flex_center:nth-of-type(2) > ul.toggle_btn.clearfix > li:nth-of-type(1)] (main area, bottom-right)
inferred_clickable: (unnamed) [div.tag-box:nth-of-type(5) > div.account-box.yes-hover:nth-of-type(2) > div.account-box-top.chip-turquoise:nth-of-type(1) > div.flex_center:nth-of-type(2) > ul.toggle_btn.clearfix > li:nth-of-type(2)] (main area, bottom-right)
inferred_clickable: (unnamed) [#tagsetDetail_divTagIcon] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0] (main area, bottom-left)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0] (main area, bottom-left)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span] (header, top-centre)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (main area, middle-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (header, top-centre)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0] (main area, bottom-centre)
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
inferred_clickable: Workspace [#FcmsTable_sortColumn] (main area, middle-centre)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div.account-box.yes-hover:nth-of-type(2) > div.account-box-top.chip-turquoise:nth-of-type(1) > div.card-chip-name:nth-of-type(1) > div.flex_center:nth-of-type(2) > div.name_edit_box.tagname_edit_box > input.ga-button-action-class] (main area, bottom-centre)
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 5
- text_input: (unnamed) -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5
- inferred_clickable: (unnamed) -- queued for depth 5

## N090 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 4 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 441 · **Visits:** 1
- **Reached by:** Click 'PROAllocation 3Used 0Available 3' → Click 'Tech Inquiry' → Click 'Event' → Click 'New Event' → Click 'Default Workspace'

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] (main area, middle-centre) -> https://vxt.samsung.com/pricing
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (header, top-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (left sidebar, middle-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (main area, top-right) [app frame]
inferred_clickable: (unnamed) [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)] (main area, middle-left)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (main area, middle-centre) [app frame]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamationundefined"]] (main area, middle-centre)
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > ul.general-tab-list > li:nth-of-type(3) > div.general-tab-chart.center-wrapper:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class] (main area, middle-right)
inferred_clickable: 0 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span] (main area, middle-centre)
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span] (main area, middle-centre)
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span] (main area, middle-centre)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (main area, middle-centre) [app frame]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_planundefined"]] (main area, middle-centre)
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (main area, middle-centre) [app frame]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (header, top-right) [app frame]
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]] (main area, top-centre)
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span] (main area, top-centre)
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span] (header, top-centre)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (left sidebar, bottom-left) [app frame]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Event [[data-testid="setting_event"]] (left sidebar, middle-left) [app frame]
inferred_clickable: General [[data-testid="setting_general"]] (left sidebar, top-left) [app frame]
inferred_clickable: General [[data-testid="settings_workspace_general"]] (main area, top-centre)
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span] (main area, top-centre)
inferred_clickable: More [[data-testid="Workspace_top_option"]] (main area, top-right)
inferred_clickable: Notification [#notificationIconId] (header, top-right) [app frame]
inferred_clickable: Organization [[data-testid="setting_organization"]] (left sidebar, top-left) [app frame]
inferred_clickable: Plan [[data-testid="setting_plan"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]] (main area, top-right)
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span] (main area, top-right)
inferred_clickable: PRO [[data-testid="dashboard_planviewundefined"]] (main area, middle-centre)
inferred_clickable: PRO [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (main area, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [role=listitem[name="PROAllocation 3Used 0Available 3"]] (main area, middle-centre)
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (header, top-centre)
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]] (main area, top-right)
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span] (main area, top-right)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (left sidebar, middle-left) [app frame]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Tag [[data-testid="setting_tag"]] (left sidebar, middle-left) [app frame]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-centre) [app frame]
inferred_clickable: User [[data-testid="setting_user"]] (left sidebar, middle-left) [app frame]
inferred_clickable: User [[data-testid="settings_workspace_user"]] (main area, top-centre)
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span] (main area, top-centre)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: Workspace [[data-testid="setting_place"]] (left sidebar, top-left) [app frame]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (left sidebar, bottom-left) [app frame] -> https://www.samsungvx.com/settings/techInquiry
```

