# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T19:36:34+00:00  
**States:** 32 · **Transitions:** 65 · **Actionable elements:** 1663 of 1663 extracted

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
| Click 'Screen' | navigation | N004 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N005 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N006 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N007 Schedule | Samsung VXT CMS | mutating |
| Click 'New' | in_page_state | N008 HOME | Samsung VXT CMS — New | — |
| Click 'New' | in_page_state | N009 HOME | Samsung VXT CMS — New | — |
| Click 'New' | in_page_state | N010 HOME | Samsung VXT CMS — New | — |
| Click 'New' | blocked_mutation | (self) | mutating |
| Click 'screen' | navigation | N004 Screen | Samsung VXT CMS | mutating |
| Click 'logo' | blocked_mutation | (self) | mutating |
| Click 'img' | blocked_mutation | (self) | mutating |
| Click 'Buy Now' | blocked_mutation | (self) | mutating |
| Click 'VXT Labs' | navigation | N011 Samsung VXT CMS | — |
| Click 'Notification' | in_page_state | N012 HOME | Samsung VXT CMS — Not | mutating |
| Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' | in_page_state | (self) | mutating, state-cap |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | (self) | mutating, state-cap |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | (self) | state-cap |
| Click 'Terms and Conditions' | navigation | N013 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N015 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N016 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N017 Samsung VXT CMS | — |
| Click 'Screen' | navigation | N004 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N020 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N022 Playlist | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N024 Schedule | Samsung VXT CMS | — |
| Click 'VXT Labs' | navigation | N011 Samsung VXT CMS | — |

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
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N019 Screen | Samsung VXT CMS — C | mutating |
| Click 'Screen' | no_change | (self) | inert |
| Click 'Add Screen' | navigation | N018 Screen | Samsung VXT CMS — A | — |

## N005 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 70 · **Interactive extracted:** 70 · **DOM nodes:** 673 · **Visits:** 1
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
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (header, top-centre)
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]] (header, top-right)
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
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
text_input: Search Contents [role=textbox[name="Search Contents"]] (header, top-centre)
```

## N006 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 0 · **Actionable:** 70 · **Interactive extracted:** 70 · **DOM nodes:** 654 · **Visits:** 1
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
- **Type:** page · **Depth:** 0 · **Actionable:** 64 · **Interactive extracted:** 64 · **DOM nodes:** 619 · **Visits:** 1
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

## N011 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 520 · **Visits:** 2
- **Reached by:** Click 'VXT Labs'
- **Screenshot:** [artifacts/N011_f04fa4aa.png](artifacts/N011_f04fa4aa.png)
- **DOM:** [artifacts/N011_f04fa4aa.html](artifacts/N011_f04fa4aa.html)

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
| Click 'div' | navigation | N026 Samsung VXT CMS | — |
| Click 'NEW' | in_page_state | N027 Samsung VXT CMS — SmartPlug | — |
| Click 'img' | in_page_state | N027 Samsung VXT CMS — SmartPlug | — |
| Click 'BETA' | in_page_state | N027 Samsung VXT CMS — SmartPlug | — |
| Click 'SmartPlug' | in_page_state | N027 Samsung VXT CMS — SmartPlug | — |
| Click 'img' | no_change | (self) | inert |
| Click 'img' | no_change | (self) | inert |
| Click '' | navigation | N004 Screen | Samsung VXT CMS | — |
| Click 'NEW' | navigation | N027 Samsung VXT CMS — SmartPlug | — |

## N012 — HOME | Samsung VXT CMS — Notification

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 59 · **Interactive extracted:** 59 · **DOM nodes:** 1181 · **Visits:** 1
- **Reached by:** Click 'Notification'
- **Screenshot:** [artifacts/N012_0f1ad938.png](artifacts/N012_0f1ad938.png)
- **DOM:** [artifacts/N012_0f1ad938.html](artifacts/N012_0f1ad938.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [#notiFilterStateId > button.btn_icon] (main area, middle-right)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Close [#footer_rightPart_okBtn] (main area, bottom-right)
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
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right)
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > div.earlywarning-badge] (main area, top-left)
inferred_clickable: (unnamed) [[data-testid="SearchInputIcon"]] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_notification_all"]] (main area, middle-right) [app frame]
inferred_clickable: (unnamed) [[data-testid="icon_export"]] (main area, middle-right)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (main area, top-centre)
inferred_clickable: All [#pc_filterRMStateId > div.select.select_btn] (main area, middle-right)
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
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]] (main area, top-left)
inferred_clickable: Early Warning [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > span.ellipsis] (main area, top-left)
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]] (main area, middle-left)
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]] (main area, top-centre)
inferred_clickable: Playlist [#dashboard_playlistCard] (main area, middle-centre)
inferred_clickable: playlist [#playlistCard_defaultImg] (main area, middle-centre)
inferred_clickable: PRO [[data-testid="dashboard_planview0"]] (left sidebar, middle-left)
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span] (left sidebar, middle-left)
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard] (main area, middle-left)
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]] (main area, middle-centre)
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]] (left sidebar, top-left)
inferred_clickable: Schedule [#dashboard_scheduleCard] (main area, middle-right)
inferred_clickable: schedule [#scheduleCard_defaultImg] (main area, middle-right)
inferred_clickable: Screen [#dashboard_screenCard] (main area, middle-left)
inferred_clickable: screen [#screenCard_defaultImg] (main area, middle-left)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]] (main area, middle-centre)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (main area, middle-left)
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]] (main area, middle-centre)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (footer, bottom-centre) [app frame] -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (footer, bottom-left) [app frame] -> https://www.samsungvx.com/terms
text_input: Search Functions or Screens [role=textbox[name="Search Functions or Screens"]] (main area, top-centre)
```

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: RM State -- queued for depth 1
- inferred_clickable: Early Warning -- queued for depth 1
- inferred_clickable: Early Warning -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: Notice -- queued for depth 1
- text_input: Search Functions or Screens -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- inferred_clickable: All -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- generic_button: (unnamed) -- queued for depth 1
- inferred_clickable: (unnamed) -- queued for depth 1
- generic_button: Close -- queued for depth 1

## N013 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 164 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N013_9b254a0e.png](artifacts/N013_9b254a0e.png)
- **DOM:** [artifacts/N013_9b254a0e.html](artifacts/N013_9b254a0e.html)

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
| Click 'chatbot' | in_page_state | N014 Terms and Conditions | Samsu | mutating |
| Click 'chatbot' | navigation | N014 Terms and Conditions | Samsu | — |

## N014 — Terms and Conditions | Samsung VXT CMS — chatbot

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 193 · **Visits:** 2
- **Reached by:** Click 'Terms and Conditions' → Click 'chatbot'
- **Screenshot:** [artifacts/N014_5954f80d.png](artifacts/N014_5954f80d.png)
- **DOM:** [artifacts/N014_5954f80d.html](artifacts/N014_5954f80d.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (footer, bottom-centre) [app frame] -> https://vxt.samsung.com/contact-us
generic_button: Minimize [#closeChatBtn] (main area, top-right)
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
| Click 'Minimize' | in_page_state | N013 Terms and Conditions | Samsu | — |

**Not exercised by the crawler**

- generic_button: Minimize -- queued for depth 2

## N015 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 169 · **Visits:** 1
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
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 164 · **Visits:** 1
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
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 490 · **Visits:** 2
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

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Samsung Screen' | in_page_state | N028 Screen | Samsung VXT CMS — A | mutating |

**Not exercised by the crawler**

- inferred_clickable: Samsung Screen -- queued for depth 2
- inferred_clickable: Virtual Screen -- queued for depth 2
- generic_button: Close -- queued for depth 2

## N019 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 475 · **Visits:** 2
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
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (header, top-right) [app frame]
inferred_clickable: (unnamed) [#notificationIconId] (header, top-right) [app frame]
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

**Not exercised by the crawler**

- inferred_clickable: CHITNU TEAMDefault Workspace -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: Default Workspace -- queued for depth 2
- inferred_clickable: Default Workspace -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2

## N020 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 566 · **Visits:** 1
- **Reached by:** Click 'Content'
- **Screenshot:** [artifacts/N020_9f71b948.png](artifacts/N020_9f71b948.png)
- **DOM:** [artifacts/N020_9f71b948.html](artifacts/N020_9f71b948.html)

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

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Contentsand' | in_page_state | N021 Content | Samsung VXT CMS —  | mutating |
| Click 'Search Contentsand' | navigation | (self) | — |

## N021 — Content | Samsung VXT CMS — Search Contentsand

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 134 · **Interactive extracted:** 134 · **DOM nodes:** 731 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand'
- **Screenshot:** [artifacts/N021_9dc79b2b.png](artifacts/N021_9dc79b2b.png)
- **DOM:** [artifacts/N021_9dc79b2b.html](artifacts/N021_9dc79b2b.html)

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
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
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

**Not exercised by the crawler**

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

## N022 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 67 · **Interactive extracted:** 67 · **DOM nodes:** 529 · **Visits:** 1
- **Reached by:** Click 'Playlist'
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
| Click 'Search Playlistsand' | in_page_state | N023 Playlist | Samsung VXT CMS — | — |
| Click 'Search Playlistsand' | navigation | N029 Playlist | Samsung VXT CMS | — |

## N023 — Playlist | Samsung VXT CMS — Search Playlistsand

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 116 · **Interactive extracted:** 116 · **DOM nodes:** 678 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand'
- **Screenshot:** [artifacts/N023_77fab44c.png](artifacts/N023_77fab44c.png)
- **DOM:** [artifacts/N023_77fab44c.html](artifacts/N023_77fab44c.html)

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
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]] (main area, top-right)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)] (main area, top-right)
inferred_clickable: No Content [[data-testid="search_systemtag_179"]] (main area, top-centre)
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
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

## N024 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 62 · **Interactive extracted:** 62 · **DOM nodes:** 523 · **Visits:** 1
- **Reached by:** Click 'Schedule'
- **Screenshot:** [artifacts/N024_d9f1d723.png](artifacts/N024_d9f1d723.png)
- **DOM:** [artifacts/N024_d9f1d723.html](artifacts/N024_d9f1d723.html)

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
| Click 'Search Schedulesand' | in_page_state | N025 Schedule | Samsung VXT CMS — | mutating |
| Click 'Search Schedulesand' | navigation | N031 Schedule | Samsung VXT CMS | — |

## N025 — Schedule | Samsung VXT CMS — Search Schedulesand

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 1 · **Actionable:** 108 · **Interactive extracted:** 108 · **DOM nodes:** 635 · **Visits:** 1
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand'
- **Screenshot:** [artifacts/N025_3760e9ce.png](artifacts/N025_3760e9ce.png)
- **DOM:** [artifacts/N025_3760e9ce.html](artifacts/N025_3760e9ce.html)

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
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
inferred_clickable: No Content [[data-testid="search_systemtag_182"]] (main area, top-centre)
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)] (main area, top-centre)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (left sidebar, middle-left) [app frame]
inferred_clickable: No tags1 [role=listitem[name="No tags1"]] (left sidebar, middle-left)
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

## N026 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'div'

_No actionable elements extracted._

## N027 — Samsung VXT CMS — SmartPlug

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 448 · **Visits:** 5
- **Reached by:** Click 'VXT Labs' → Click 'NEW'
- **Screenshot:** [artifacts/N027_e0e79420.png](artifacts/N027_e0e79420.png)
- **DOM:** [artifacts/N027_e0e79420.html](artifacts/N027_e0e79420.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Close [[data-testid="vxtlabs_feature_detail_close"]] (main area, bottom-right)
inferred_clickable: (unnamed) [#signage_modal > div.cEWgRo:nth-of-type(1) > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (main area, top-right)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (main area, top-right)
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

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N011 Samsung VXT CMS | — |

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 2
- inferred_clickable: (unnamed) -- queued for depth 2
- generic_button: Close -- queued for depth 2

## N028 — Screen | Samsung VXT CMS — Add Screen — Samsung Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 2 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 521 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen' → Click 'Samsung Screen'
- **Screenshot:** [artifacts/N028_4c674996.png](artifacts/N028_4c674996.png)
- **DOM:** [artifacts/N028_4c674996.html](artifacts/N028_4c674996.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen] (main area, bottom-centre)
generic_button: chatbot [#startChatBtn] (main area, bottom-right) [app frame]
generic_button: Pair My Screen [[data-testid="screen_addscreen_smg_screen_pair"]] (main area, bottom-right)
generic_button: Previous [role=button[name="Previous"]] (main area, bottom-left)
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
inferred_clickable: (unnamed) [#modalpop_wrap > div.screen_pop_wrap:nth-of-type(1) > div.pop_cont.ftescreen_wrap > div.swiper.swiper-initialized > div.swiper-button-next:nth-of-type(3)] (main area, middle-right)
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

**Not exercised by the crawler**

- inferred_clickable: (unnamed) -- queued for depth 3
- generic_button: Previous -- queued for depth 3
- generic_button: Pair My Screen -- queued for depth 3

## N029 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 2 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 567 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand'
- **Screenshot:** [artifacts/N029_99e1d6ef.png](artifacts/N029_99e1d6ef.png)
- **DOM:** [artifacts/N029_99e1d6ef.html](artifacts/N029_99e1d6ef.html)

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
| Click '1 playlist' | in_page_state | N030 Playlist | Samsung VXT CMS — | mutating |
| Click '1 playlist' | navigation | N030 Playlist | Samsung VXT CMS — | — |

## N030 — Playlist | Samsung VXT CMS — 1 playlist

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 2 · **Actionable:** 72 · **Interactive extracted:** 72 · **DOM nodes:** 564 · **Visits:** 2
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand' → Click '1 playlist'
- **Screenshot:** [artifacts/N030_81a34b4b.png](artifacts/N030_81a34b4b.png)
- **DOM:** [artifacts/N030_81a34b4b.html](artifacts/N030_81a34b4b.html)

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
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (main area, middle-centre)
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
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Playlists [role=textbox[name="Search Playlists"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 of 1 selected' | in_page_state | N029 Playlist | Samsung VXT CMS | mutating |

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

## N031 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 62 · **Interactive extracted:** 62 · **DOM nodes:** 527 · **Visits:** 1
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand'
- **Screenshot:** [artifacts/N031_f4286c8a.png](artifacts/N031_f4286c8a.png)
- **DOM:** [artifacts/N031_f4286c8a.html](artifacts/N031_f4286c8a.html)

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
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox] (main area, middle-centre)
inferred_clickable: GeneralGeneralGeneralGeneral [ul.image_listbox.list_view > li.image_listitem.list_view > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1] (main area, middle-centre)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (left sidebar, top-left) [app frame]
inferred_clickable: logo [#header_logo] (header, top-left) [app frame]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (left sidebar, middle-left) [app frame]
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]] (main area, top-right)
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
| Click '1 schedule' | in_page_state | N032 Schedule | Samsung VXT CMS — | mutating |
| Click '1 schedule' | navigation | N032 Schedule | Samsung VXT CMS — | — |

## N032 — Schedule | Samsung VXT CMS — 1 schedule

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 66 · **Interactive extracted:** 66 · **DOM nodes:** 524 · **Visits:** 2
- **Reached by:** Click 'Schedule' → Click 'Search Schedulesand' → Click '1 schedule'
- **Screenshot:** [artifacts/N032_f9a0d677.png](artifacts/N032_f9a0d677.png)
- **DOM:** [artifacts/N032_f9a0d677.html](artifacts/N032_f9a0d677.html)

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
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)] (main area, middle-right)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (header, top-right) [app frame]
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (left sidebar, top-left) [app frame]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (left sidebar, top-left) [app frame]
text_input: Search Schedules [role=textbox[name="Search Schedules"]] (header, top-centre)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '1 of 1 selected' | in_page_state | N031 Schedule | Samsung VXT CMS | mutating |

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

