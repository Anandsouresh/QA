# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T18:28:35+00:00  
**States:** 82 · **Transitions:** 226 · **Actionable elements:** 3674 of 3674 extracted

## N001 — HOME | Samsung VXT CMS *(entry)*

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 430 · **Visits:** 1
- **Reached by:** entry point
- **Screenshot:** [artifacts/N001_4792e46f.png](artifacts/N001_4792e46f.png)
- **DOM:** [artifacts/N001_4792e46f.html](artifacts/N001_4792e46f.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]]
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
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
| Click 'VXT Labs' | navigation | N003 Samsung VXT CMS | — |
| Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' | in_page_state | N004 HOME | Samsung VXT CMS — sou | — |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | N006 HOME | Samsung VXT CMS — Def | — |
| Click '.st0{opacity:0.8;}' | in_page_state | N006 HOME | Samsung VXT CMS — Def | — |
| Click 'Screen' | navigation | N007 Screen | Samsung VXT CMS | — |
| Click 'Screen' | navigation | N007 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N008 Content | Samsung VXT CMS | — |
| Click 'Content' | navigation | N008 Content | Samsung VXT CMS | mutating |
| Click 'Playlist' | navigation | N009 Playlist | Samsung VXT CMS | mutating |
| Click 'logo' | blocked_mutation | (self) | mutating |
| Click 'img' | blocked_mutation | (self) | mutating |
| Click 'Notification' | in_page_state | N010 HOME | Samsung VXT CMS — Not | mutating |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | N006 HOME | Samsung VXT CMS — Def | mutating |
| Click 'chatbot' | in_page_state | N012 HOME | Samsung VXT CMS — cha | mutating |
| Click 'Terms and Conditions' | navigation | N014 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N015 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N016 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N017 Samsung VXT CMS | — |
| Click 'VXT Labs' | navigation | N003 Samsung VXT CMS | — |
| Click 'Screen' | navigation | N007 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N008 Content | Samsung VXT CMS | — |
| Click 'Content' | navigation | N032 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N009 Playlist | Samsung VXT CMS | — |

## N002 — vxt.samsung.com

- **URL:** https://vxt.samsung.com/contact-us
- **Type:** boundary · **Depth:** 0 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** n/a · **Visits:** 7
- **Reached by:** Click 'Contact Us'

_No actionable elements extracted._

## N003 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 517 · **Visits:** 2
- **Reached by:** Click 'VXT Labs'
- **Screenshot:** [artifacts/N003_f04fa4aa.png](artifacts/N003_f04fa4aa.png)
- **DOM:** [artifacts/N003_f04fa4aa.html](artifacts/N003_f04fa4aa.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]]
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)]
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | navigation | N018 Samsung VXT CMS | mutating |
| Click 'NEW' | in_page_state | N019 Samsung VXT CMS — NEW | — |
| Click 'img' | in_page_state | N019 Samsung VXT CMS — NEW | — |
| Click 'BETA' | in_page_state | N019 Samsung VXT CMS — NEW | — |
| Click 'SmartPlug' | in_page_state | N019 Samsung VXT CMS — NEW | — |
| Click 'img' | no_change | (self) | inert |
| Click 'img' | no_change | (self) | inert |
| Click '' | navigation | N017 Samsung VXT CMS | — |

## N004 — HOME | Samsung VXT CMS — souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 53 · **Interactive extracted:** 53 · **DOM nodes:** 442 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com'
- **Screenshot:** [artifacts/N004_2c34b1ca.png](artifacts/N004_2c34b1ca.png)
- **DOM:** [artifacts/N004_2c34b1ca.html](artifacts/N004_2c34b1ca.html)

**Action elements**

```
destructive: Sign Out [[data-testid="dashboard_signout"]]
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]]
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Manual [[data-testid="dashboard_manual"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Settings [[data-testid="dashboard_setting"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]]
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Manual' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Settings' | navigation | N005 Settings | Samsung VXT CMS — | — |
| Click 'Settings' | navigation | N020 Settings | Samsung VXT CMS | — |

## N005 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 545 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings'
- **Screenshot:** [artifacts/N005_523f6918.png](artifacts/N005_523f6918.png)
- **DOM:** [artifacts/N005_523f6918.html](artifacts/N005_523f6918.html)

**Action elements**

```
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]]
inferred_clickable: 20:41 [[data-testid="select-Time Format"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]]
inferred_clickable: English [[data-testid="select-Language"]]
inferred_clickable: Event [[data-testid="setting_event"]]
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]]
inferred_clickable: General [[data-testid="setting_general"]]
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]]
inferred_clickable: Mon [[data-testid="select-First Day of Week"]]
inferred_clickable: Organization [[data-testid="setting_organization"]]
inferred_clickable: Plan [[data-testid="setting_plan"]]
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]]
inferred_clickable: User [[data-testid="setting_user"]]
inferred_clickable: Workspace [[data-testid="setting_place"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
text_input: Phone Number [#phone_input]
text_input: Select [[data-testid="select-Country Code"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N020 Settings | Samsung VXT CMS | — |

## N006 — HOME | Samsung VXT CMS — Default Workspace .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 569 · **Visits:** 1
- **Reached by:** Click 'Default Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N006_0331e0df.png](artifacts/N006_0331e0df.png)
- **DOM:** [artifacts/N006_0331e0df.html](artifacts/N006_0331e0df.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace [#select-wrap > div]
inferred_clickable: Default Workspace [[data-testid="dashboardPlaces_liPlaces_Item0"]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
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
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N007 — Screen | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 0 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 525 · **Visits:** 3
- **Reached by:** Click 'Screen'
- **Screenshot:** [artifacts/N007_cf8c2d76.png](artifacts/N007_cf8c2d76.png)
- **DOM:** [artifacts/N007_cf8c2d76.html](artifacts/N007_cf8c2d76.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [#navbar_leftControl2]
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]]
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll.SCROLL_BAR_CLASS:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Screen' | in_page_state | N026 Screen | Samsung VXT CMS — A | — |
| Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' | in_page_state | N027 Screen | Samsung VXT CMS — C | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N027 Screen | Samsung VXT CMS — C | — |
| Click 'Screen' | blocked_mutation | (self) | mutating |

## N008 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 668 · **Visits:** 3
- **Reached by:** Click 'Content'
- **Screenshot:** [artifacts/N008_025f8bfc.png](artifacts/N008_025f8bfc.png)
- **DOM:** [artifacts/N008_025f8bfc.html](artifacts/N008_025f8bfc.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_contents"]]
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]]
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]]
inferred_clickable: (unnamed) [[data-testid="icon_channel"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]]
inferred_clickable: (unnamed) [#navbar_leftControl2]
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)]
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]]
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0]
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Contentsand' | in_page_state | N028 Content | Samsung VXT CMS —  | — |
| Click 'and' | in_page_state | N030 Content | Samsung VXT CMS —  | — |

## N009 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 0 · **Actionable:** 67 · **Interactive extracted:** 67 · **DOM nodes:** 649 · **Visits:** 2
- **Reached by:** Click 'Playlist'
- **Screenshot:** [artifacts/N009_d32f987b.png](artifacts/N009_d32f987b.png)
- **DOM:** [artifacts/N009_d32f987b.html](artifacts/N009_d32f987b.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)]
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)]
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)]
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)]
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)]
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)]
inferred_clickable: GeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Playlistsand' | in_page_state | N033 Playlist | Samsung VXT CMS — | mutating |
| Click 'div' | in_page_state | N033 Playlist | Samsung VXT CMS — | — |

## N010 — HOME | Samsung VXT CMS — Notification

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 64 · **Interactive extracted:** 64 · **DOM nodes:** 1178 · **Visits:** 1
- **Reached by:** Click 'Notification'
- **Screenshot:** [artifacts/N010_0f1ad938.png](artifacts/N010_0f1ad938.png)
- **DOM:** [artifacts/N010_0f1ad938.html](artifacts/N010_0f1ad938.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [#notiFilterStateId > button.btn_icon]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: (unnamed) [[data-testid="SearchInputIcon"]]
inferred_clickable: (unnamed) [[data-testid="icon_notification_all"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_export"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: All [#pc_filterRMStateId > div.select.select_btn]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]]
inferred_clickable: Early Warning [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class:nth-of-type(2) > span.ellipsis]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
text_input: Search Functions or Screens [role=textbox[name="Search Functions or Screens"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'button' | blocked_mutation | (self) | mutating |
| Click 'Close' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N011 HOME | Samsung VXT CMS — Not | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |

## N011 — HOME | Samsung VXT CMS — Notification — div

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 82 · **Interactive extracted:** 82 · **DOM nodes:** 628 · **Visits:** 1
- **Reached by:** Click 'Notification' → Click 'div'
- **Screenshot:** [artifacts/N011_b5f0c8cb.png](artifacts/N011_b5f0c8cb.png)
- **DOM:** [artifacts/N011_b5f0c8cb.html](artifacts/N011_b5f0c8cb.html)

**Action elements**

```
checkbox: Abnormal Fan Operation [#reportItemCheck_label1]
checkbox: Content Playback Issue [#reportItemCheck_label10]
checkbox: E-Paper Battery Low [#reportItemCheck_label8]
checkbox: Emergency Alert Occurrence [#reportItemCheck_label9]
checkbox: Network Issue [#reportItemCheck_label3]
checkbox: No Signal on Input Source [#reportItemCheck_label7]
checkbox: Screen Disconnection [#reportItemCheck_label5]
checkbox: Screen Power Off [#reportItemCheck_label4]
checkbox: Screen Temperature Issue [#reportItemCheck_label0]
checkbox: Screen/Panel Issue [#reportItemCheck_label2]
checkbox: VXT Player Inactive [#reportItemCheck_label6]
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: Add User [#recipientAddButton]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_cancelBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: Save [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class.selected:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: (unnamed) [#input_box > div.date.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: 0 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: Early Warning [[data-testid="noti_dialog_tab_EW"]]
inferred_clickable: Early Warning [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class.selected:nth-of-type(2) > span.ellipsis]
inferred_clickable: Email Report [role=listitem[name="Email Report"]]
inferred_clickable: Email Report [#earlyWarningTabId > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Mobile App [role=listitem[name="Mobile App"]]
inferred_clickable: Mobile App [#earlyWarningTabId > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
text_input: (unnamed) [#select]
```

## N012 — HOME | Samsung VXT CMS — chatbot

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 465 · **Visits:** 1
- **Reached by:** Click 'chatbot'
- **Screenshot:** [artifacts/N012_85edd937.png](artifacts/N012_85edd937.png)
- **DOM:** [artifacts/N012_85edd937.html](artifacts/N012_85edd937.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Minimize [#closeChatBtn]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamation0"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: 0 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Minimize' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | navigation | N013 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N013 Settings | Samsung VXT CMS | mutating |
| Click '3' | navigation | N013 Settings | Samsung VXT CMS | mutating |
| Click '3' | navigation | N013 Settings | Samsung VXT CMS | mutating |
| Click '' | navigation | N035 Settings | Samsung VXT CMS | — |

## N013 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 0 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 563 · **Visits:** 4
- **Reached by:** Click 'chatbot' → Click 'div'

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Minimize [#closeChatBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [#ProCard_statusColor]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]]
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]]
inferred_clickable: Event [[data-testid="setting_event"]]
inferred_clickable: General [[data-testid="setting_general"]]
inferred_clickable: Organization [[data-testid="setting_organization"]]
inferred_clickable: Plan [[data-testid="setting_plan"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]]
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [[data-testid="setting_user"]]
inferred_clickable: Workspace [[data-testid="setting_place"]]
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

## N014 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 172 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N014_9b254a0e.png](artifacts/N014_9b254a0e.png)
- **DOM:** [artifacts/N014_9b254a0e.html](artifacts/N014_9b254a0e.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
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
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
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
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 164 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N016_868a41ac.png](artifacts/N016_868a41ac.png)
- **DOM:** [artifacts/N016_868a41ac.html](artifacts/N016_868a41ac.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
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
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 164 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N017_e4b14cd7.png](artifacts/N017_e4b14cd7.png)
- **DOM:** [artifacts/N017_e4b14cd7.html](artifacts/N017_e4b14cd7.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N018 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'div'

_No actionable elements extracted._

## N019 — Samsung VXT CMS — NEW

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 448 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'NEW'
- **Screenshot:** [artifacts/N019_e0e79420.png](artifacts/N019_e0e79420.png)
- **DOM:** [artifacts/N019_e0e79420.html](artifacts/N019_e0e79420.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [[data-testid="vxtlabs_feature_detail_close"]]
inferred_clickable: (unnamed) [#signage_modal > div.cEWgRo:nth-of-type(1) > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadgeWh47"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)]
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Close' | in_page_state | N003 Samsung VXT CMS | — |
| Click 'div' | in_page_state | N003 Samsung VXT CMS | — |

## N020 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 376 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings'
- **Screenshot:** [artifacts/N020_eef435c9.png](artifacts/N020_eef435c9.png)
- **DOM:** [artifacts/N020_eef435c9.html](artifacts/N020_eef435c9.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]]
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [[data-testid="icon_option_icon"]]
inferred_clickable: 2022-04-19 [[data-testid="select-Date Format"]]
inferred_clickable: 20:41 [[data-testid="select-Time Format"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]]
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]]
inferred_clickable: English [[data-testid="select-Language"]]
inferred_clickable: Event [[data-testid="setting_event"]]
inferred_clickable: Exhibition [[data-testid="select-How did you hear about us?"]]
inferred_clickable: General [[data-testid="setting_general"]]
inferred_clickable: Individual contributor [[data-testid="select-What is your role?"]]
inferred_clickable: Mon [[data-testid="select-First Day of Week"]]
inferred_clickable: Organization [[data-testid="setting_organization"]]
inferred_clickable: Plan [[data-testid="setting_plan"]]
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]]
inferred_clickable: User [[data-testid="setting_user"]]
inferred_clickable: Workspace [[data-testid="setting_place"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | navigation | N021 HOME | Samsung VXT CMS | — |
| Click 'General' | no_change | (self) | inert |
| Click 'Organization' | navigation | N022 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N023 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N024 Settings | Samsung VXT CMS | — |
| Click 'Register Phone Number' | in_page_state | N005 Settings | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Click 'Register Phone Number' | in_page_state | N005 Settings | Samsung VXT CMS — | — |
| Click 'Plan' | navigation | N025 Settings | Samsung VXT CMS | — |
| Click 'Tech Inquiry' | navigation | N043 Settings | Samsung VXT CMS | — |
| Click '' | navigation | N001 HOME | Samsung VXT CMS | — |
| Click 'Organization' | navigation | N022 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N052 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N024 Settings | Samsung VXT CMS | — |
| Click 'Plan' | navigation | N025 Settings | Samsung VXT CMS | — |

## N021 — HOME | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 1 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 484 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'div'

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_keyboard_arrow"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocate Licenses [[data-testid="dashboard_planview0"]]
inferred_clickable: Allocate LicensesAllocation -Used -Available - [#dashboard_planCard]
inferred_clickable: Allocation - [role=listitem[name="Allocation -"]]
inferred_clickable: Allocation -Used -Available - [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Apps [role=listitem[name="Apps"]]
inferred_clickable: Apps [#contents_wrap > ul.home-cards > li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(3) > div.home-card-header]
inferred_clickable: Available - [role=listitem[name="Available -"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: StorageUsed0.00KB [role=listitem[name="StorageUsed0.00KB"]]
inferred_clickable: Used - [role=listitem[name="Used -"]]
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

## N022 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 1 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 621 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization'
- **Screenshot:** [artifacts/N022_7e6abd8d.png](artifacts/N022_7e6abd8d.png)
- **DOM:** [artifacts/N022_7e6abd8d.html](artifacts/N022_7e6abd8d.html)

**Action elements**

```
generic_button: Add [#add_phone_number]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Entertainment [[data-testid="select-Industry"]]
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Store Owner [[data-testid="select-CMS User"]]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: ~10 [[data-testid="select-Number of Employees"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
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
| Click 'Information' | no_change | (self) | inert |
| Click 'Customization' | in_page_state | N047 Settings | Samsung VXT CMS — | — |
| Click 'Preset' | in_page_state | N049 Settings | Samsung VXT CMS — | mutating |
| Click 'Tag' | in_page_state | N050 Settings | Samsung VXT CMS — | — |
| Click 'Scheduling' | in_page_state | N051 Settings | Samsung VXT CMS — | — |
| Click 'Information' | no_change | (self) | inert |
| Click 'Customization' | in_page_state | N047 Settings | Samsung VXT CMS — | — |
| Click 'Preset' | in_page_state | N049 Settings | Samsung VXT CMS — | — |
| Click 'Tag' | in_page_state | N050 Settings | Samsung VXT CMS — | mutating |
| Click 'Scheduling' | in_page_state | N051 Settings | Samsung VXT CMS — | — |

## N023 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 1 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 559 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Available [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: No workspaces. [[data-testid="No workspaces."]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]]
```

## N024 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 1 · **Actionable:** 36 · **Interactive extracted:** 36 · **DOM nodes:** 572 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User'
- **Screenshot:** [artifacts/N024_b81fd3f4.png](artifacts/N024_b81fd3f4.png)
- **DOM:** [artifacts/N024_b81fd3f4.html](artifacts/N024_b81fd3f4.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [div:nth-of-type(2) > div.account.account-contents-wrap > div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.rightAfterBtn.MuiBox-root:nth-of-type(2) > div.topbtn_option.ga-button-action-class]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Recent Login [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Member' | blocked_mutation | (self) | mutating |
| Click 'Owner' | in_page_state | N054 Settings | Samsung VXT CMS — | mutating |
| Click 'Pending' | in_page_state | N055 Settings | Samsung VXT CMS — | — |

## N025 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 1 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 622 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Plan'
- **Screenshot:** [artifacts/N025_e149b4d5.png](artifacts/N025_e149b4d5.png)
- **DOM:** [artifacts/N025_e149b4d5.html](artifacts/N025_e149b4d5.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#liItemContents0 > div >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"] >> nth=0]
inferred_clickable: (unnamed) [div.tab_content.primary > div.account-box.user-details > div.SCROLL_BAR_CLASS:nth-of-type(2) > ul.account-list-box > li.account-list-tr:nth-of-type(2) > div.link_spring.top_spring:nth-of-type(1)]
inferred_clickable: (unnamed) [#liItemContents0 > div >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"] >> nth=0]
inferred_clickable: 0 [#liItemContents2 >> nth=0]
inferred_clickable: 2026-09-19 [#SubscriptionTable_nextPaymentDate >> nth=0]
inferred_clickable: 2026-10-01 [#SubscriptionTable_nextPaymentDate >> nth=0]
inferred_clickable: 3 [#liItemContents1 >> nth=0]
inferred_clickable: 3 [#liItemContents3 >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#liItemContents4 >> nth=0]
inferred_clickable: Default Workspace [#liItemContents4 >> nth=0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1) >> nth=0]
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1) >> nth=0]
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: Pro [#liItemContents0 >> nth=0]
inferred_clickable: S Series Trial [#liItemContents0 > dl.dl-d > dt > span >> nth=0]
inferred_clickable: S Series TrialVX-TRIAL [#liItemContents0 >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Primary Plan' | no_change | (self) | inert |
| Click 'Additional Plan' | in_page_state | N056 Settings | Samsung VXT CMS — | — |

## N026 — Screen | Samsung VXT CMS — Add Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 490 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen'
- **Screenshot:** [artifacts/N026_105670e6.png](artifacts/N026_105670e6.png)
- **DOM:** [artifacts/N026_105670e6.html](artifacts/N026_105670e6.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]]
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Samsung Screen [[data-testid="screen_addscreen_smg_screen"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Virtual Screen [[data-testid="screen_addscreen_virtual_screen"]]
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Samsung Screen' | no_change | (self) | inert |

## N027 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 481 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N027_67784b26.png](artifacts/N027_67784b26.png)
- **DOM:** [artifacts/N027_67784b26.html](artifacts/N027_67784b26.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [#place_list > li.ga-button-action-class.selected > span.check_off:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagFavoritesExpand]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (app frame)
inferred_clickable: Default Workspace [role=listitem[name="Default Workspace"]]
inferred_clickable: Default Workspace [#place_list > li.ga-button-action-class.selected > span.place_name_class:nth-of-type(1)]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]]
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N007 Screen | Samsung VXT CMS | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N007 Screen | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N007 Screen | Samsung VXT CMS | — |

## N028 — Content | Samsung VXT CMS — Search Contentsand

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 134 · **Interactive extracted:** 134 · **DOM nodes:** 725 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand'
- **Screenshot:** [artifacts/N028_9dc79b2b.png](artifacts/N028_9dc79b2b.png)
- **DOM:** [artifacts/N028_9dc79b2b.html](artifacts/N028_9dc79b2b.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Canvas [[data-testid="search_systemtag_3"]]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: E-Paper [[data-testid="search_systemtag_144"]]
inferred_clickable: E-PaperE-Paper [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)]
inferred_clickable: Embargo: Activated [[data-testid="search_systemtag_172"]]
inferred_clickable: Embargo: ActivatedEmbargo: Activated [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Embargo: Released [[data-testid="search_systemtag_173"]]
inferred_clickable: Embargo: ReleasedEmbargo: Released [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)]
inferred_clickable: Image [[data-testid="search_systemtag_2"]]
inferred_clickable: ImageImage [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Landscape [[data-testid="search_systemtag_169"]]
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Lifespan: Ended [[data-testid="search_systemtag_176"]]
inferred_clickable: Lifespan: EndedLifespan: Ended [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(10)]
inferred_clickable: Lifespan: Ready [[data-testid="search_systemtag_174"]]
inferred_clickable: Lifespan: ReadyLifespan: Ready [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)]
inferred_clickable: Lifespan: Started [[data-testid="search_systemtag_175"]]
inferred_clickable: Lifespan: StartedLifespan: Started [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(9)]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: Not Published [[data-testid="search_systemtag_12"]]
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Not Shared [[data-testid="search_systemtag_10"]]
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Office [[data-testid="search_systemtag_7"]]
inferred_clickable: OfficeOffice [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Portrait [[data-testid="search_systemtag_170"]]
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Published [[data-testid="search_systemtag_11"]]
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: Shared [[data-testid="search_systemtag_8"]]
inferred_clickable: Shared By Others [[data-testid="search_systemtag_9"]]
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Ticker [[data-testid="search_systemtag_227"]]
inferred_clickable: TickerTicker [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Video [[data-testid="search_systemtag_1"]]
inferred_clickable: VideoVideo [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Web(HTML) [[data-testid="search_systemtag_5"]]
inferred_clickable: Web(HTML)Web(HTML) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Web(URL) [[data-testid="search_systemtag_6"]]
inferred_clickable: Web(URL)Web(URL) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Canvas' | in_page_state | N029 Content | Samsung VXT CMS —  | — |

## N029 — Content | Samsung VXT CMS — Search Contentsand — Canvas

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 74 · **Interactive extracted:** 74 · **DOM nodes:** 606 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'Canvas'
- **Screenshot:** [artifacts/N029_92196eec.png](artifacts/N029_92196eec.png)
- **DOM:** [artifacts/N029_92196eec.html](artifacts/N029_92196eec.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: (unnamed) [[data-testid="icon_circle_delete"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Canvas [[data-testid="Canvas"] >> nth=0]
inferred_clickable: CanvasCanvas [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvasand [[data-testid="search_input_wrapper"]]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input]
```

## N030 — Content | Samsung VXT CMS — and

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 134 · **Interactive extracted:** 134 · **DOM nodes:** 726 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'and'
- **Screenshot:** [artifacts/N030_afd02d1b.png](artifacts/N030_afd02d1b.png)
- **DOM:** [artifacts/N030_afd02d1b.html](artifacts/N030_afd02d1b.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Canvas [[data-testid="search_systemtag_3"]]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: E-Paper [[data-testid="search_systemtag_144"]]
inferred_clickable: E-PaperE-Paper [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)]
inferred_clickable: Embargo: Activated [[data-testid="search_systemtag_172"]]
inferred_clickable: Embargo: ActivatedEmbargo: Activated [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Embargo: Released [[data-testid="search_systemtag_173"]]
inferred_clickable: Embargo: ReleasedEmbargo: Released [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(7)]
inferred_clickable: Image [[data-testid="search_systemtag_2"]]
inferred_clickable: ImageImage [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Landscape [[data-testid="search_systemtag_169"]]
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Lifespan: Ended [[data-testid="search_systemtag_176"]]
inferred_clickable: Lifespan: EndedLifespan: Ended [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(10)]
inferred_clickable: Lifespan: Ready [[data-testid="search_systemtag_174"]]
inferred_clickable: Lifespan: ReadyLifespan: Ready [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)]
inferred_clickable: Lifespan: Started [[data-testid="search_systemtag_175"]]
inferred_clickable: Lifespan: StartedLifespan: Started [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(9)]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: Not Published [[data-testid="search_systemtag_12"]]
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Not Shared [[data-testid="search_systemtag_10"]]
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Office [[data-testid="search_systemtag_7"]]
inferred_clickable: OfficeOffice [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: or [[data-testid="and_or_toggle"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Portrait [[data-testid="search_systemtag_170"]]
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Published [[data-testid="search_systemtag_11"]]
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Contentsor [[data-testid="search_input_wrapper"]]
inferred_clickable: Shared [[data-testid="search_systemtag_8"]]
inferred_clickable: Shared By Others [[data-testid="search_systemtag_9"]]
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Ticker [[data-testid="search_systemtag_227"]]
inferred_clickable: TickerTicker [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(8)]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Video [[data-testid="search_systemtag_1"]]
inferred_clickable: VideoVideo [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Web(HTML) [[data-testid="search_systemtag_5"]]
inferred_clickable: Web(HTML)Web(HTML) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Web(URL) [[data-testid="search_systemtag_6"]]
inferred_clickable: Web(URL)Web(URL) [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'CanvasCanvas' | in_page_state | N031 Content | Samsung VXT CMS —  | — |

## N031 — Content | Samsung VXT CMS — and — CanvasCanvas

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 77 · **Interactive extracted:** 77 · **DOM nodes:** 606 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'and' → Click 'CanvasCanvas'
- **Screenshot:** [artifacts/N031_88af729b.png](artifacts/N031_88af729b.png)
- **DOM:** [artifacts/N031_88af729b.html](artifacts/N031_88af729b.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="content_card_checkbox_0"]]
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: (unnamed) [[data-testid="icon_circle_delete"]]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="content_card_more_0"]]
inferred_clickable: (unnamed) [[data-testid="content_card_more_0_icon"]]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Canvas [[data-testid="Canvas"] >> nth=0]
inferred_clickable: CanvasCanvas [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasor [[data-testid="search_input_wrapper"]]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: or [[data-testid="and_or_toggle"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input]
```

## N032 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 558 · **Visits:** 1
- **Reached by:** Click 'Content'
- **Screenshot:** [artifacts/N032_cc664968.png](artifacts/N032_cc664968.png)
- **DOM:** [artifacts/N032_cc664968.html](artifacts/N032_cc664968.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="icon_ai_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: or [[data-testid="and_or_toggle"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Contentsor [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0]
inferred_clickable: Untitled CanvasCanvasCanvas [#content_card_div_test_1 >> nth=0]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Contentsor' | in_page_state | N030 Content | Samsung VXT CMS —  | — |

## N033 — Playlist | Samsung VXT CMS — Search Playlistsand

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 116 · **Interactive extracted:** 116 · **DOM nodes:** 672 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand'
- **Screenshot:** [artifacts/N033_77fab44c.png](artifacts/N033_77fab44c.png)
- **DOM:** [artifacts/N033_77fab44c.html](artifacts/N033_77fab44c.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)]
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)]
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)]
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)]
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)]
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: General [[data-testid="search_systemtag_30"]]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneral [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Landscape [[data-testid="search_systemtag_177"]]
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No Content [[data-testid="search_systemtag_179"]]
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Not Published [[data-testid="search_systemtag_37"]]
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Not Shared [[data-testid="search_systemtag_35"]]
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Portrait [[data-testid="search_systemtag_178"]]
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Published [[data-testid="search_systemtag_36"]]
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]]
inferred_clickable: Shared [[data-testid="search_systemtag_33"]]
inferred_clickable: Shared By Others [[data-testid="search_systemtag_34"]]
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Sync Play [[data-testid="search_systemtag_31"]]
inferred_clickable: Sync PlaySync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Takeover Sync Play [[data-testid="search_systemtag_32"]]
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Custom' | in_page_state | N034 Playlist | Samsung VXT CMS — | — |
| Click 'Custom' | in_page_state | N034 Playlist | Samsung VXT CMS — | — |

## N034 — Playlist | Samsung VXT CMS — Search Playlistsand — Custom

- **URL:** https://www.samsungvx.com/playlist
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 119 · **Interactive extracted:** 119 · **DOM nodes:** 672 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand' → Click 'Custom'
- **Screenshot:** [artifacts/N034_06e774c6.png](artifacts/N034_06e774c6.png)
- **DOM:** [artifacts/N034_06e774c6.html](artifacts/N034_06e774c6.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
generic_button: OK [role=button[name="OK"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)]
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)]
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)]
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)]
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)]
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: Custom [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip_line:nth-of-type(7)]
inferred_clickable: General [[data-testid="search_systemtag_30"]]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneral [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Landscape [[data-testid="search_systemtag_177"]]
inferred_clickable: LandscapeLandscape [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No Content [[data-testid="search_systemtag_179"]]
inferred_clickable: No ContentNo Content [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Not Published [[data-testid="search_systemtag_37"]]
inferred_clickable: Not PublishedNot Published [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Not Shared [[data-testid="search_systemtag_35"]]
inferred_clickable: Not SharedNot Shared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Portrait [[data-testid="search_systemtag_178"]]
inferred_clickable: PortraitPortrait [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(3) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Published [[data-testid="search_systemtag_36"]]
inferred_clickable: PublishedPublished [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]]
inferred_clickable: Shared [[data-testid="search_systemtag_33"]]
inferred_clickable: Shared By Others [[data-testid="search_systemtag_34"]]
inferred_clickable: Shared By OthersShared By Others [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: SharedShared [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(2) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Sync Play [[data-testid="search_systemtag_31"]]
inferred_clickable: Sync PlaySync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: Takeover Sync Play [[data-testid="search_systemtag_32"]]
inferred_clickable: Takeover Sync PlayTakeover Sync Play [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(1) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: Today [[data-testid="Today"] >> nth=0]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: TodayToday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(1)]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 Days [[data-testid="Within 3 Days"] >> nth=0]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 DaysWithin 3 Days [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(3)]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 Months [[data-testid="Within 3 Months"] >> nth=0]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within 3 MonthsWithin 3 Months [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(6)]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a Month [[data-testid="Within a Month"] >> nth=0]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a MonthWithin a Month [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(5)]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a Week [[data-testid="Within a Week"] >> nth=0]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Within a WeekWithin a Week [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(4)]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: Yesterday [[data-testid="Yesterday"] >> nth=0]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(4) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
inferred_clickable: YesterdayYesterday [div.search_field.fcms_simple_bar > div.advanced_wrap:nth-of-type(2) > div.advanced_option.active > div:nth-of-type(5) > div.filter-options-wrapper:nth-of-type(2) > span.chip.chip-chkbox:nth-of-type(2)]
text_input: (unnamed) [#cusTimeContainer > div.input_bundle_wrap.filter_wrapper > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class >> nth=0]
text_input: (unnamed) [#cusTimeContainer > div.input_bundle_wrap.filter_wrapper > div.dateInputContainer.date:nth-of-type(3) > input.ipt_textbox.ga-button-action-class >> nth=0]
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

## N035 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 1 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 424 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click ''
- **Screenshot:** [artifacts/N035_b7d3a3a7.png](artifacts/N035_b7d3a3a7.png)
- **DOM:** [artifacts/N035_b7d3a3a7.html](artifacts/N035_b7d3a3a7.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [#ProCard_statusColor]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'button' | in_page_state | N036 Settings | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'Add Workspace' | no_change | (self) | inert |
| Click 'Workspace' | no_change | (self) | inert |
| Click 'Allocation' | no_change | (self) | inert |
| Click 'Used' | no_change | (self) | inert |
| Click 'Tag' | navigation | N038 Settings | Samsung VXT CMS | — |
| Click 'Event' | navigation | N039 Settings | Samsung VXT CMS | — |
| Click 'div' | navigation | N039 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N040 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N041 Settings | Samsung VXT CMS | — |
| Click 'Activity Log' | navigation | N042 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N057 Settings | Samsung VXT CMS | — |
| Click 'Event' | navigation | N039 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N040 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N041 Settings | Samsung VXT CMS | — |
| Click 'Activity Log' | navigation | N064 Settings | Samsung VXT CMS | — |

## N036 — Settings | Samsung VXT CMS — button

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 424 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'button'
- **Screenshot:** [artifacts/N036_a3ac712a.png](artifacts/N036_a3ac712a.png)
- **DOM:** [artifacts/N036_a3ac712a.html](artifacts/N036_a3ac712a.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [#ProCard_statusColor]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Lock Plan [[data-testid="button_Lock Plan"]]
inferred_clickable: Merge Plan [[data-testid="button_Merge Plan"]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Lock Plan' | in_page_state | N035 Settings | Samsung VXT CMS | mutating |
| Click 'Merge Plan' | in_page_state | N037 Settings | Samsung VXT CMS — | — |

## N037 — Settings | Samsung VXT CMS — button — Merge Plan

- **URL:** https://www.samsungvx.com/settings/subscription/A8308934-7569-41CA-A254-92A185ADD97C
- **Type:** page · **Depth:** 1 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 451 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'button' → Click 'Merge Plan'
- **Screenshot:** [artifacts/N037_2e82bcd3.png](artifacts/N037_2e82bcd3.png)
- **DOM:** [artifacts/N037_2e82bcd3.html](artifacts/N037_2e82bcd3.html)

**Action elements**

```
destructive: Confirm [#SubscriptionAllocTable_btnConfirm] (disabled)
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Workspace [[data-testid="setting_plan_details_add_workspace"]]
generic_button: Cancel [#footer_rightPart_cancelBtn]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Select [#footer_rightPart_okBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#PlanCard_cardPlan > li.card-dot:nth-of-type(2) > div:nth-of-type(1) > div.dot.green:nth-of-type(1)]
inferred_clickable: (unnamed) [#ProCard_statusColor]
inferred_clickable: (unnamed) [[data-testid="icon_close"] >> nth=0]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"] >> nth=0]
inferred_clickable: 0 [role=listitem[name="0"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation [#SubscriptionAllocTable_sortByAllocation]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default WorkspaceUsed: 0 [role=listitem[name="Default WorkspaceUsed: 0"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#SubscriptionAllocTable_sortByUsed]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#SubscriptionAllocTable_sortByWorkspace]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
number_input: (unnamed) [#UmsInput_input]
text_input: Allocable [#input_text2] (disabled)
text_input: Allocated [#input_text1] (disabled)
```

## N038 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 1 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 345 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: No tag. [[data-testid="No tag."]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]]
```

## N039 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 1 · **Actionable:** 25 · **Interactive extracted:** 25 · **DOM nodes:** 344 · **Visits:** 3
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event'
- **Screenshot:** [artifacts/N039_73b565cd.png](artifacts/N039_73b565cd.png)
- **DOM:** [artifacts/N039_73b565cd.html](artifacts/N039_73b565cd.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Event [role=button[name="New Event"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'New Event' | navigation | N059 Settings | Samsung VXT CMS | mutating |
| Click 'New Event' | navigation | N059 Settings | Samsung VXT CMS | — |

## N040 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 1 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 355 · **Visits:** 2
- **Reached by:** Click 'chatbot' → Click '' → Click 'Screen Preset'
- **Screenshot:** [artifacts/N040_281d7601.png](artifacts/N040_281d7601.png)
- **DOM:** [artifacts/N040_281d7601.html](artifacts/N040_281d7601.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Profile [role=button[name="New Profile"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Screen Profile' | blocked_mutation | (self) | mutating |
| Click 'Certificate' | in_page_state | N060 Settings | Samsung VXT CMS — | mutating |
| Click 'Screen Software' | in_page_state | N061 Settings | Samsung VXT CMS — | mutating |

## N041 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert
- **Type:** page · **Depth:** 1 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 364 · **Visits:** 2
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert'
- **Screenshot:** [artifacts/N041_90a409b3.png](artifacts/N041_90a409b3.png)
- **DOM:** [artifacts/N041_90a409b3.html](artifacts/N041_90a409b3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Emergency Alert [role=button[name="New Emergency Alert"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Emergency Alert' | navigation | N063 Settings | Samsung VXT CMS | mutating |
| Click 'New Emergency Alert' | navigation | N063 Settings | Samsung VXT CMS | — |

## N042 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 1 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 383 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Activity Log'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Action [#sortColumn >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Detail [#sortColumn >> nth=0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Path [#sortColumn >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Target [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#sortColumn >> nth=0]
inferred_clickable: When [#sortColumn >> nth=0]
inferred_clickable: Where [#sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N043 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 290 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry'
- **Screenshot:** [artifacts/N043_8d6adb87.png](artifacts/N043_8d6adb87.png)
- **DOM:** [artifacts/N043_8d6adb87.html](artifacts/N043_8d6adb87.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Inquiry [role=button[name="New Inquiry"]]
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Tech Inquiry Permissions' | in_page_state | N044 Settings | Samsung VXT CMS — | — |
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N046 Settings | Samsung VXT CMS | mutating |
| Click 'div' | navigation | N046 Settings | Samsung VXT CMS | mutating |
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N066 Settings | Samsung VXT CMS | — |

## N044 — Settings | Samsung VXT CMS — Tech Inquiry Permissions

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 349 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Tech Inquiry Permissions'
- **Screenshot:** [artifacts/N044_d8ab2c91.png](artifacts/N044_d8ab2c91.png)
- **DOM:** [artifacts/N044_d8ab2c91.html](artifacts/N044_d8ab2c91.html)

**Action elements**

```
generic_button: Cancel [#footer_rightPart_cancelBtn]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Inquiry [role=button[name="New Inquiry"]]
generic_button: Save [#footer_rightPart_okBtn] (disabled)
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#modal_pop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div]
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: All Users [[data-testid="select_default"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Owner and Admin [[data-testid="select_default"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N043 Settings | Samsung VXT CMS | mutating |
| Click 'div' | in_page_state | N043 Settings | Samsung VXT CMS | mutating |
| Click 'All Users' | no_change | (self) | inert |

## N045 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** page · **Depth:** 2 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 449 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'New Inquiry'
- **Screenshot:** [artifacts/N045_891bd27f.png](artifacts/N045_891bd27f.png)
- **DOM:** [artifacts/N045_891bd27f.html](artifacts/N045_891bd27f.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]]
generic_button: Open [role=button[name="Open"]]
generic_button: Request [role=button[name="Request"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: Enter a subject. [role=textbox[name="Enter a subject."]]
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Register Phone Number' | in_page_state | N065 Settings | Samsung VXT CMS — | — |
| Click 'Select' | no_change | (self) | inert |
| Click 'Open' | file_chooser | (self) | upload |
| Click 'Drop the files here to attach.' | no_change | (self) | inert |

## N046 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 2 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 443 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Edit Home'

**Action elements**

```
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Done [role=button[name="Done"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: Title [role=listitem[name="Title"]]
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

## N047 — Settings | Samsung VXT CMS — Customization

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 49 · **Interactive extracted:** 49 · **DOM nodes:** 898 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Customization'
- **Screenshot:** [artifacts/N047_cb57d581.png](artifacts/N047_cb57d581.png)
- **DOM:** [artifacts/N047_cb57d581.html](artifacts/N047_cb57d581.html)

**Action elements**

```
disclosure: Admin Privilege Control [role=button[name="Admin Privilege Control"]]
disclosure: App Splash Logo [role=button[name="App Splash Logo"]]
disclosure: Content Embargo & Lifespan [role=button[name="Content Embargo & Lifespan"]]
disclosure: Default Content [role=button[name="Default Content"]]
disclosure: Screen Custom Fields [role=button[name="Screen Custom Fields"]]
generic_button: Apply [role=button[name="Apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > div.flex_col.gap20px:nth-of-type(3) > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(2) > span]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Admin Privilege Control' | no_change | (self) | inert |
| Click 'App Splash Logo' | no_change | (self) | inert |
| Click 'Content Embargo & Lifespan' | no_change | (self) | inert |
| Click 'Default Content' | no_change | (self) | inert |
| Click 'Screen Custom Fields' | no_change | (self) | inert |
| Click 'div' | in_page_state | N048 Settings | Samsung VXT CMS — | — |

## N048 — Settings | Samsung VXT CMS — Customization — div

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 898 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Customization' → Click 'div'
- **Screenshot:** [artifacts/N048_b50ab24d.png](artifacts/N048_b50ab24d.png)
- **DOM:** [artifacts/N048_b50ab24d.html](artifacts/N048_b50ab24d.html)

**Action elements**

```
disclosure: Admin Privilege Control [role=button[name="Admin Privilege Control"]]
disclosure: App Splash Logo [role=button[name="App Splash Logo"]]
disclosure: Content Embargo & Lifespan [role=button[name="Content Embargo & Lifespan"]]
disclosure: Default Content [role=button[name="Default Content"]]
disclosure: Screen Custom Fields [role=button[name="Screen Custom Fields"]]
generic_button: (unnamed) [div.MuiStack-root.w100 > div.MuiStack-root:nth-of-type(1) > div.flex.flexChildrenGrow:nth-of-type(2) > div.flex_center_center.flexChildrenGrow:nth-of-type(1) > div > div.radio-screen-img.mt0]
generic_button: (unnamed) [div.MuiStack-root.w100 > div.MuiStack-root:nth-of-type(1) > div.flex.flexChildrenGrow:nth-of-type(2) > div.flex_center_center.flexChildrenGrow:nth-of-type(2) > div > div.radio-screen-img.mt0]
generic_button: Apply [role=button[name="Apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > div.flex_col.gap20px:nth-of-type(3) > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(2) > span]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N049 — Settings | Samsung VXT CMS — Preset

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 456 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Preset'
- **Screenshot:** [artifacts/N049_2df846e5.png](artifacts/N049_2df846e5.png)
- **DOM:** [artifacts/N049_2df846e5.html](artifacts/N049_2df846e5.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [div.pt40.pb20:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track >> nth=0]
inferred_clickable: (unnamed) [#SIGNAGE > li:nth-of-type(1) > div.dim:nth-of-type(2) > div:nth-of-type(1) > div.addcardcomp]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [div.pt40.pb20:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track >> nth=0]
inferred_clickable: (unnamed) [#SIGNAGE > li.mb40:nth-of-type(2) > div.dim:nth-of-type(2) > div:nth-of-type(1) > div.addcardcomp]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Android [role=listitem[name="Android"]]
inferred_clickable: Android [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]]
inferred_clickable: BrightSign [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(6) > span]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Do not show again. [div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div._tab_content_y859n_1350.tab_content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: E-Paper [role=listitem[name="E-Paper"]]
inferred_clickable: E-Paper [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: Flip [role=listitem[name="Flip"]]
inferred_clickable: Flip [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(7) > span]
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Indoor LED Signage [role=listitem[name="Indoor LED Signage"]]
inferred_clickable: Indoor LED Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Legacy [role=listitem[name="Legacy"]]
inferred_clickable: Legacy [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(8) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Signage [role=listitem[name="Signage"]]
inferred_clickable: Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Windows [role=listitem[name="Windows"]]
inferred_clickable: Windows [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'span' | blocked_mutation | (self) | mutating |

## N050 — Settings | Samsung VXT CMS — Tag

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 469 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Tag'
- **Screenshot:** [artifacts/N050_9216d372.png](artifacts/N050_9216d372.png)
- **DOM:** [artifacts/N050_9216d372.html](artifacts/N050_9216d372.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Global CategoryAvailable for [role=button[name="Global CategoryAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(1) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"]]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Global Category [[data-testid="setting_tag_details_rename"]]
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: scrollable content [role=region[name="scrollable content"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'span' | blocked_mutation | (self) | mutating |

## N051 — Settings | Samsung VXT CMS — Scheduling

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 46 · **Interactive extracted:** 46 · **DOM nodes:** 602 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Scheduling'
- **Screenshot:** [artifacts/N051_33eebb65.png](artifacts/N051_33eebb65.png)
- **DOM:** [artifacts/N051_33eebb65.html](artifacts/N051_33eebb65.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(3) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(5) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_organization_customizatoin"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Do not show again. [div.simplebar-content-wrapper > div.simplebar-content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiButtonBase-root.MuiCheckbox-root:nth-of-type(1) > span]
inferred_clickable: Do not show again. [div.simplebar-offset > div.simplebar-content-wrapper > div.simplebar-content > div.MuiBox-root:nth-of-type(2) > label.MuiFormControlLabel-root.MuiFormControlLabel-labelPlacementEnd > span.MuiTypography-root.MuiTypography-body1:nth-of-type(2)]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Information [[data-testid="settings_organization_information"]]
inferred_clickable: Information [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Sunday [[data-testid="select_default"]]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Screen [role=link[name="Screen"]] -> https://www.samsungvx.com/screen
nav_link: Settings > Preset [role=link[name="Settings > Preset"]] -> https://www.samsungvx.com/settings/screenPreset
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [#input_box > input.text_field2] (disabled)
text_input: (unnamed) [#select >> nth=0]
text_input: (unnamed) [#select >> nth=0]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | blocked_mutation | (self) | mutating |
| Click 'span' | blocked_mutation | (self) | mutating |
| Click 'Do not show again.' | no_change | (self) | inert |
| Click 'Information' | in_page_state | N022 Settings | Samsung VXT CMS | — |

## N052 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 2 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 350 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace'
- **Screenshot:** [artifacts/N052_d456a6ab.png](artifacts/N052_d456a6ab.png)
- **DOM:** [artifacts/N052_d456a6ab.html](artifacts/N052_d456a6ab.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Workspace [[data-testid="settings_workspace_new_add"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: 0 [#FcmsTable_liItemContents2]
inferred_clickable: 0 [#FcmsTable_liItemContents4]
inferred_clickable: 0.00KB [#FcmsTable_liItemContents5]
inferred_clickable: 3 [#FcmsTable_liItemContents1]
inferred_clickable: 3 [#FcmsTable_liItemContents3]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Available [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'New Workspace' | blocked_mutation | (self) | mutating |
| Click 'Allocation' | no_change | (self) | inert |
| Click 'Default Workspace' | navigation | N053 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N053 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N053 Settings | Samsung VXT CMS | — |
| Click 'Default Workspace' | navigation | N053 Settings | Samsung VXT CMS | — |

## N053 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 2 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 447 · **Visits:** 4
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace'
- **Screenshot:** [artifacts/N053_3f2ef8b8.png](artifacts/N053_3f2ef8b8.png)
- **DOM:** [artifacts/N053_3f2ef8b8.html](artifacts/N053_3f2ef8b8.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="Workspace_top_option"]]
inferred_clickable: (unnamed) [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamationundefined"]]
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > ul.general-tab-list > li:nth-of-type(3) > div.general-tab-chart.center-wrapper:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: 0 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_planundefined"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: PRO [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: PRO [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [role=listitem[name="PROAllocation 3Used 0Available 3"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Learn more' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Default Workspace' | in_page_state | N068 Settings | Samsung VXT CMS — | — |

## N054 — Settings | Samsung VXT CMS — Owner

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 366 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User' → Click 'Owner'
- **Screenshot:** [artifacts/N054_40a2aa55.png](artifacts/N054_40a2aa55.png)
- **DOM:** [artifacts/N054_40a2aa55.html](artifacts/N054_40a2aa55.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_more"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |

## N055 — Settings | Samsung VXT CMS — Pending

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 343 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User' → Click 'Pending'
- **Screenshot:** [artifacts/N055_9c1b4a06.png](artifacts/N055_9c1b4a06.png)
- **DOM:** [artifacts/N055_9c1b4a06.html](artifacts/N055_9c1b4a06.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Date Sent [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Date Sent' | no_change | (self) | inert |

## N056 — Settings | Samsung VXT CMS — Additional Plan

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 2 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 306 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Plan' → Click 'Additional Plan'
- **Screenshot:** [artifacts/N056_c3a08a9a.png](artifacts/N056_c3a08a9a.png)
- **DOM:** [artifacts/N056_c3a08a9a.html](artifacts/N056_c3a08a9a.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: No Plans [[data-testid="No Plans"]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'No Plans' | no_change | (self) | inert |

## N057 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 2 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 340 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag'
- **Screenshot:** [artifacts/N057_e468c7e3.png](artifacts/N057_e468c7e3.png)
- **DOM:** [artifacts/N057_e468c7e3.html](artifacts/N057_e468c7e3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default TagsetRegion, Location, Subject, Others [#FcmsTable_liItemContents0]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents1]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Tagset' | no_change | (self) | inert |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N058 Settings | Samsung VXT CMS | — |
| Click 'Default Workspace' | navigation | N058 Settings | Samsung VXT CMS | — |
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N058 Settings | Samsung VXT CMS | — |

## N058 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 2 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 740 · **Visits:** 3
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others'
- **Screenshot:** [artifacts/N058_a67c73ca.png](artifacts/N058_a67c73ca.png)
- **DOM:** [artifacts/N058_a67c73ca.html](artifacts/N058_a67c73ca.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Default Tagset' | in_page_state | N069 Settings | Samsung VXT CMS — | — |
| Click 'span' | in_page_state | N069 Settings | Samsung VXT CMS — | — |
| Click 'checkbox' | in_page_state | N070 Settings | Samsung VXT CMS — | mutating |
| Click 'Add Workspace' | in_page_state | N071 Settings | Samsung VXT CMS — | mutating |
| Click 'Workspace' | no_change | (self) | inert |
| Click 'div' | in_page_state | N072 Settings | Samsung VXT CMS — | mutating |
| Click 'Region' | in_page_state | N073 Settings | Samsung VXT CMS — | mutating |
| Click 'div' | in_page_state | (self) | state-cap |

## N059 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 2 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 466 · **Visits:** 2
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event' → Click 'New Event'
- **Screenshot:** [artifacts/N059_c775cc72.png](artifacts/N059_c775cc72.png)
- **DOM:** [artifacts/N059_c775cc72.html](artifacts/N059_c775cc72.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (app frame)
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_event_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: 1.5 [[data-testid="select_default"] >> nth=0]
inferred_clickable: 115200 [[data-testid="select_default"] >> nth=0]
inferred_clickable: 4 [[data-testid="select_default"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: ASCII [[data-testid="select_default"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemA0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: None [[data-testid="select_default"] >> nth=0]
inferred_clickable: None [[data-testid="select_default"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd]
radio: Network [#event_type_network]
radio: Serial Port [#event_type_serial]
radio: Weather [#event_type_weather]
text_input: Enter key. [role=textbox[name="Enter key."]]
text_input: Enter port number. [role=textbox[name="Enter port number."]] (disabled)
text_input: New Event [[data-testid="FCMSInput"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Save' | in_page_state | N074 Settings | Samsung VXT CMS — | mutating |
| Click 'Serial Port' | in_page_state | N074 Settings | Samsung VXT CMS — | mutating |
| Click 'Weather' | in_page_state | N075 Settings | Samsung VXT CMS — | mutating |
| Click 'Crowd Count' | in_page_state | N076 Settings | Samsung VXT CMS — | — |
| Click 'Network' | in_page_state | N077 Settings | Samsung VXT CMS — | — |
| Click '115200' | in_page_state | N074 Settings | Samsung VXT CMS — | — |

## N060 — Settings | Samsung VXT CMS — Certificate

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 2 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Screen Preset' → Click 'Certificate'
- **Screenshot:** [artifacts/N060_07662a8e.png](artifacts/N060_07662a8e.png)
- **DOM:** [artifacts/N060_07662a8e.html](artifacts/N060_07662a8e.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Certificate [role=button[name="New Certificate"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Certificate' | blocked_mutation | (self) | mutating |

## N061 — Settings | Samsung VXT CMS — Screen Software

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 2 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 321 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Screen Preset' → Click 'Screen Software'
- **Screenshot:** [artifacts/N061_cda0e47d.png](artifacts/N061_cda0e47d.png)
- **DOM:** [artifacts/N061_cda0e47d.html](artifacts/N061_cda0e47d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Screen Software [role=button[name="New Screen Software"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Screen Software' | in_page_state | N062 Settings | Samsung VXT CMS — | mutating |

## N062 — Settings | Samsung VXT CMS — Screen Software — New Screen Software

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 381 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Screen Preset' → Click 'Screen Software' → Click 'New Screen Software'
- **Screenshot:** [artifacts/N062_01a3d362.png](artifacts/N062_01a3d362.png)
- **DOM:** [artifacts/N062_01a3d362.html](artifacts/N062_01a3d362.html)

**Action elements**

```
external_link: Supported Models → [role=link[name="Supported Models →"]] -> https://vxt.samsung.com/pricing
generic_button: Cancel [#footer_rightPart_cancelBtn] (app frame)
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Screen Software [role=button[name="New Screen Software"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0]
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0]
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0]
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img > div > img >> nth=0]
inferred_clickable: (unnamed) [#NewProfileDialog_select > div.screen_img:nth-of-type(1) > div > img >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Certificate [[data-testid="setting_screen_present_certificate"]]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N063 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 2 · **Actionable:** 31 · **Interactive extracted:** 31 · **DOM nodes:** 415 · **Visits:** 2
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert'
- **Screenshot:** [artifacts/N063_e69ec22e.png](artifacts/N063_e69ec22e.png)
- **DOM:** [artifacts/N063_e69ec22e.html](artifacts/N063_e69ec22e.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: New Emergency Alert [[data-testid="FCMSInput"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N078 Settings | Samsung VXT CMS — | — |
| Click 'span' | no_change | (self) | inert |
| Click 'Add Workspace' | in_page_state | N082 Settings | Samsung VXT CMS — | — |

## N064 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 2 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 633 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Activity Log'
- **Screenshot:** [artifacts/N064_41a46fe6.png](artifacts/N064_41a46fe6.png)
- **DOM:** [artifacts/N064_41a46fe6.html](artifacts/N064_41a46fe6.html)

**Action elements**

```
generic_button: Apply [[data-testid="setting_activity_log_apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Export [[data-testid="activity_btnExport"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_activityLog_search_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: Action [#sortColumn >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Detail [#sortColumn >> nth=0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Path [#sortColumn >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Target [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#sortColumn >> nth=0]
inferred_clickable: When [#sortColumn >> nth=0]
inferred_clickable: Where [#sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Logs [[data-testid="Activity Log_settingHeader_input"]]
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(1) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [div.flex_center.h42:nth-of-type(1) > div.flex_center.flex_end > div.input_bundle_wrap.flex_center > div:nth-of-type(2) > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Apply' | no_change | (self) | inert |
| Click 'When' | no_change | (self) | inert |

## N065 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 475 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'New Inquiry' → Click 'Register Phone Number'
- **Screenshot:** [artifacts/N065_da109b4b.png](artifacts/N065_da109b4b.png)
- **DOM:** [artifacts/N065_da109b4b.html](artifacts/N065_da109b4b.html)

**Action elements**

```
generic_button: Cancel [[data-testid="settings_general_register_phone_cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Drop the files here to attach. [role=button[name="Drop the files here to attach."]]
generic_button: Open [role=button[name="Open"]]
generic_button: Request [role=button[name="Request"]]
generic_button: Send Code [[data-testid="settings_general_sendvericode"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_phone"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Register Phone Number [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(2) > div > span.flex_center:nth-of-type(2) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: Select [[data-testid="select_default"] >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.techInquiryContent > div:nth-of-type(3) > div.input_bundle_wrap:nth-of-type(3) > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0]
text_input: Enter a subject. [role=textbox[name="Enter a subject."]]
text_input: Phone Number [#phone_input]
text_input: Select [[data-testid="select-Country Code"]]
textarea: Enter your request in detail. Please ensure that no personal information is entered. [role=textbox[name="Enter your request in detail. Please ensure that no personal information is entered."]]
```

## N066 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 3 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 432 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Edit Home'
- **Screenshot:** [artifacts/N066_4cc011a3.png](artifacts/N066_4cc011a3.png)
- **DOM:** [artifacts/N066_4cc011a3.html](artifacts/N066_4cc011a3.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Apps [role=button[name="Apps"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
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
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Title [role=listitem[name="Title"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | in_page_state | N067 Settings | Samsung VXT CMS — | — |
| Click 'Organization Name' | no_change | (self) | inert |

## N067 — Settings | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 3 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 506 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Edit Home' → Click 'div'
- **Screenshot:** [artifacts/N067_1bf62c62.png](artifacts/N067_1bf62c62.png)
- **DOM:** [artifacts/N067_1bf62c62.html](artifacts/N067_1bf62c62.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: (unnamed) [[data-testid="reset-dashboard-button"]]
generic_button: Apps [role=button[name="Apps"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
generic_button: Done [role=button[name="Done"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]]
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: StorageUsed0.00KBVideo0.00KBImage0.00KBCanvas0.00KBOffice0.00KBWeb(HTML)0.00KBOthers0.00KB [role=button[name="StorageUsed0.00KBVideo0.00KBImage0.00KBCanvas0.00KBOffice0.00KBWeb(HTML)0.00KBOthers0.00KB"]]
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_web"]]
inferred_clickable: (unnamed) [[data-testid="icon_ic_mobile"]]
inferred_clickable: (unnamed) [#moHeader_menu]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
inferred_clickable: (unnamed) [li._info-card-area-mobile_1ukjs_2:nth-of-type(2) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.storage-mobile:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: (unnamed) [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: 0 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [#planCard_item0 > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (app frame)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (app frame)
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#moHeader_place > div > div.select_bottom_wrap > div:nth-of-type(1)]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: logo [#moHeader_logoImg\ ga-button-action-class]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: PRO [[data-testid="dashboard_planview0"]]
inferred_clickable: PRO [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: Title [role=listitem[name="Title"]]
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
radio: Logo [#title-settings-logo]
radio: Organization Name [#title-settings-organization-name]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | blocked_mutation | (self) | mutating |

## N068 — Settings | Samsung VXT CMS — Default Workspace

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 427 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'Default Workspace'
- **Screenshot:** [artifacts/N068_cd6773f3.png](artifacts/N068_cd6773f3.png)
- **DOM:** [artifacts/N068_cd6773f3.html](artifacts/N068_cd6773f3.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="Workspace_top_option"]]
inferred_clickable: (unnamed) [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > div._dot_comp_18hso_1.bg-yellow:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_plan_exclamationundefined"]]
inferred_clickable: (unnamed) [div._tab_content_y859n_1350.tab_content > ul.general-tab-list > li:nth-of-type(3) > div.general-tab-chart.center-wrapper:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: 0 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(2) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(1) > span]
inferred_clickable: 3 [li.home-card.ga-button-action-class > div > div.home-info-card.ga-button-action-class:nth-of-type(2) > ul > li:nth-of-type(3) > span]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Allocation 3 [role=listitem[name="Allocation 3"]] (app frame)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_planundefined"]]
inferred_clickable: Available 3 [role=listitem[name="Available 3"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: PRO [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: PRO [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: PROAllocation 3Used 0Available 3 [role=listitem[name="PROAllocation 3Used 0Available 3"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Default Workspace [[data-testid="FCMSInput"]]
```

## N069 — Settings | Samsung VXT CMS — Default Tagset

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 726 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Default Tagset'
- **Screenshot:** [artifacts/N069_8f1e69d7.png](artifacts/N069_8f1e69d7.png)
- **DOM:** [artifacts/N069_8f1e69d7.html](artifacts/N069_8f1e69d7.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Default Tagset [[data-testid="FCMSInput"]]
```

## N070 — Settings | Samsung VXT CMS — checkbox

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 715 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'checkbox'
- **Screenshot:** [artifacts/N070_546c84e5.png](artifacts/N070_546c84e5.png)
- **DOM:** [artifacts/N070_546c84e5.html](artifacts/N070_546c84e5.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
destructive: Remove Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N071 — Settings | Samsung VXT CMS — Add Workspace

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 773 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Add Workspace'
- **Screenshot:** [artifacts/N071_e442ded7.png](artifacts/N071_e442ded7.png)
- **DOM:** [artifacts/N071_e442ded7.html](artifacts/N071_e442ded7.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add [[data-testid="setting_tag_details_apply"]]
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: Cancel [[data-testid="setting_tag_details_close"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#SelectOrgDialog_search]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="setting_tag_details_search_workspace"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N058 Settings | Samsung VXT CMS | mutating |
| Click 'span' | blocked_mutation | (self) | mutating |

## N072 — Settings | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 786 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'div'
- **Screenshot:** [artifacts/N072_74ef6c58.png](artifacts/N072_74ef6c58.png)
- **DOM:** [artifacts/N072_74ef6c58.html](artifacts/N072_74ef6c58.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [div.account-box-top.flex_center_between:nth-of-type(1) > div.card-chip-name:nth-of-type(1) > div.mr8:nth-of-type(1) > div.tag-color-editbox-target > div:nth-of-type(1) > div >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [div.mr8:nth-of-type(1) > div.tag-color-editbox-target > div:nth-of-type(2) > div.new-colorpicker-comp > div > div.w-color-interactive.w-color-saturation:nth-of-type(1)]
inferred_clickable: (unnamed) [div.tag-color-editbox-target > div:nth-of-type(2) > div.new-colorpicker-comp > div > div:nth-of-type(2) > div:nth-of-type(1)]
inferred_clickable: (unnamed) [div.new-colorpicker-comp > div > div:nth-of-type(2) > div:nth-of-type(2) > div.w-color-alpha.w-color-alpha-horizontal > div:nth-of-type(1)]
inferred_clickable: (unnamed) [div.new-colorpicker-comp > div > div:nth-of-type(2) > div:nth-of-type(2) > div.w-color-alpha.w-color-alpha-horizontal > div.w-color-interactive:nth-of-type(2)]
inferred_clickable: (unnamed) [#tagsetDetail_divChangeCatMode]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_screen"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_icon_contents"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_move"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="tagsetDetail_divDeleteCategory"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div:nth-of-type(2) > div.new-colorpicker-comp > div > div:nth-of-type(3) > div:nth-of-type(1) > input]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | N058 Settings | Samsung VXT CMS | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | error | (self) | error |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'listitem' | in_page_state | N058 Settings | Samsung VXT CMS | mutating |
| Click 'listitem' | in_page_state | N058 Settings | Samsung VXT CMS | — |

## N073 — Settings | Samsung VXT CMS — Region

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 49 · **Interactive extracted:** 49 · **DOM nodes:** 737 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others' → Click 'Region'
- **Screenshot:** [artifacts/N073_30aa3116.png](artifacts/N073_30aa3116.png)
- **DOM:** [artifacts/N073_30aa3116.html](artifacts/N073_30aa3116.html)

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: Available for [role=button[name="Available for"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="tagsetDetail_divDeleteCategory"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: (unnamed) [div.account-box.yes-hover:nth-of-type(2) > div.account-box-top.flex_center_between:nth-of-type(1) > div.card-chip-name:nth-of-type(1) > div.flex_center:nth-of-type(2) > div.name_edit_box.tagname_edit_box > input.ga-button-action-class]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | in_page_state | (self) | mutating, state-cap |

## N074 — Settings | Samsung VXT CMS — Save

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 3 · **Actionable:** 43 · **Interactive extracted:** 43 · **DOM nodes:** 461 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event' → Click 'New Event' → Click 'Save'
- **Screenshot:** [artifacts/N074_0ad8cb15.png](artifacts/N074_0ad8cb15.png)
- **DOM:** [artifacts/N074_0ad8cb15.html](artifacts/N074_0ad8cb15.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (app frame)
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_event_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: 1.5 [[data-testid="select_default"] >> nth=0]
inferred_clickable: 115200 [[data-testid="select_default"] >> nth=0]
inferred_clickable: 4 [[data-testid="select_default"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: ASCII [[data-testid="select_default"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemA0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Event [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: None [[data-testid="select_default"] >> nth=0]
inferred_clickable: None [[data-testid="select_default"] >> nth=0]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd]
radio: Network [#event_type_network]
radio: Serial Port [#event_type_serial]
radio: Weather [#event_type_weather]
text_input: Enter key. [role=textbox[name="Enter key."]]
text_input: Enter port number. [role=textbox[name="Enter port number."]] (disabled)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Event' | in_page_state | N059 Settings | Samsung VXT CMS | — |

## N075 — Settings | Samsung VXT CMS — Weather

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 3 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 430 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event' → Click 'New Event' → Click 'Weather'
- **Screenshot:** [artifacts/N075_acd5e6a7.png](artifacts/N075_acd5e6a7.png)
- **DOM:** [artifacts/N075_acd5e6a7.html](artifacts/N075_acd5e6a7.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (app frame)
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_event_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: >= [[data-testid="select_default"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Current Temperature [[data-testid="select_default"] >> nth=0]
inferred_clickable: Default Workspace [#FcmsTable_liItemA0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Event [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd]
radio: in [#rainInch]
radio: mm, cm [#rainMmcm]
radio: Network [#event_type_network]
radio: Serial Port [#event_type_serial]
radio: Weather [#event_type_weather]
radio: °C [#TemperatureC]
radio: °F [#TemperatureF]
text_input: -140 ~ 140 [role=textbox[name="-140 ~ 140"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '>=' | no_change | (self) | inert |

## N076 — Settings | Samsung VXT CMS — Crowd Count

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 3 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 384 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event' → Click 'New Event' → Click 'Crowd Count'
- **Screenshot:** [artifacts/N076_32bdb954.png](artifacts/N076_32bdb954.png)
- **DOM:** [artifacts/N076_32bdb954.html](artifacts/N076_32bdb954.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (app frame)
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_event_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"]]
inferred_clickable: >= [[data-testid="select_default"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemA0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Event [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd]
radio: Network [#event_type_network]
radio: Serial Port [#event_type_serial]
radio: Weather [#event_type_weather]
text_input: Enter a value between 1 and 9999. [role=textbox[name="Enter a value between 1 and 9999."]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click '>=' | no_change | (self) | inert |

## N077 — Settings | Samsung VXT CMS — Network

- **URL:** https://www.samsungvx.com/settings/event/create
- **Type:** page · **Depth:** 3 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 378 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Event' → Click 'New Event' → Click 'Network'
- **Screenshot:** [artifacts/N077_8e8f56eb.png](artifacts/N077_8e8f56eb.png)
- **DOM:** [artifacts/N077_8e8f56eb.html](artifacts/N077_8e8f56eb.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (disabled) (app frame)
generic_button: Add [[data-testid="setting_event_select_add_wokspace"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_event_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemA0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Event [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
radio: Crowd Count [#event_type_crowd]
radio: Network [#event_type_network]
radio: Serial Port [#event_type_serial]
radio: Weather [#event_type_weather]
text_input: Enter key. [role=textbox[name="Enter key."]]
text_input: Enter port number. [role=textbox[name="Enter port number."]]
```

## N078 — Settings | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 43 · **Interactive extracted:** 43 · **DOM nodes:** 527 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert' → Click 'div'
- **Screenshot:** [artifacts/N078_4205e029.png](artifacts/N078_4205e029.png)
- **DOM:** [artifacts/N078_4205e029.html](artifacts/N078_4205e029.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: Cancel [[data-testid="_btncancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
generic_button: Select [[data-testid="schedule_footer_rightpart_okbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="selectContent_sort"]]
inferred_clickable: (unnamed) [[data-testid="select-wrap"]]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Emergency Alert [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N079 Settings | Samsung VXT CMS — | — |
| Click 'div' | in_page_state | N080 Settings | Samsung VXT CMS — | — |
| Click 'div' | in_page_state | N081 Settings | Samsung VXT CMS — | — |

## N079 — Settings | Samsung VXT CMS — div — Cancel

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 452 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert' → Click 'div' → Click 'Cancel'
- **Screenshot:** [artifacts/N079_cb012f96.png](artifacts/N079_cb012f96.png)
- **DOM:** [artifacts/N079_cb012f96.html](artifacts/N079_cb012f96.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Emergency Alert [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N080 — Settings | Samsung VXT CMS — div — div

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 622 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert' → Click 'div' → Click 'div'
- **Screenshot:** [artifacts/N080_d934ce3c.png](artifacts/N080_d934ce3c.png)
- **DOM:** [artifacts/N080_d934ce3c.html](artifacts/N080_d934ce3c.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: Cancel [[data-testid="_btncancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
generic_button: Select [[data-testid="schedule_footer_rightpart_okbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_date_down"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_date_up"]]
inferred_clickable: (unnamed) [[data-testid="icon_name_down"]]
inferred_clickable: (unnamed) [[data-testid="icon_name_up"]]
inferred_clickable: (unnamed) [[data-testid="select-wrap"]]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Date [[data-testid="selectContent_sortoption_li_updated_time_desc"]]
inferred_clickable: Date [[data-testid="selectContent_sortoption_li_updated_time_asc"]]
inferred_clickable: DateDateNameName [[data-testid="selectContent_sort"]]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Name [[data-testid="selectContent_sortoption_li_content_name_desc"]]
inferred_clickable: Name [[data-testid="selectContent_sortoption_li_content_name_asc"]]
inferred_clickable: New Emergency Alert [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N081 — Settings | Samsung VXT CMS — div — div

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 556 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert' → Click 'div' → Click 'div'
- **Screenshot:** [artifacts/N081_6fb29cfd.png](artifacts/N081_6fb29cfd.png)
- **DOM:** [artifacts/N081_6fb29cfd.html](artifacts/N081_6fb29cfd.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: Cancel [[data-testid="_btncancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
generic_button: Select [[data-testid="schedule_footer_rightpart_okbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="selectContent_sort"]]
inferred_clickable: (unnamed) [[data-testid="icon_list"]]
inferred_clickable: (unnamed) [[data-testid="icon_cardList"] >> nth=0]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: List View [[data-testid="content_ga_button_action_listview"]]
inferred_clickable: List ViewThumbnail View [[data-testid="select-wrap"]]
inferred_clickable: New Emergency Alert [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Thumbnail View [[data-testid="content_ga_button_action_thumbview"]]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N082 — Settings | Samsung VXT CMS — Add Workspace

- **URL:** https://www.samsungvx.com/settings/emergencyAlert/create
- **Type:** page · **Depth:** 3 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 457 · **Visits:** 1
- **Reached by:** Click 'chatbot' → Click '' → Click 'Emergency Alert' → Click 'New Emergency Alert' → Click 'Add Workspace'
- **Screenshot:** [artifacts/N082_865a5530.png](artifacts/N082_865a5530.png)
- **DOM:** [artifacts/N082_865a5530.html](artifacts/N082_865a5530.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore] (app frame)
generic_button: Add [[data-testid="setting_emergency_alert_new_add_workspace_apply"]]
generic_button: Add Workspace [[data-testid="setting_emergency_alert_new_add_workspace"]]
generic_button: Cancel [[data-testid="setting_emergency_alert_new_add_workspace_close"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Save [[data-testid="setting_emergency_alert_new_add_save"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_add_content"]]
inferred_clickable: (unnamed) [[data-testid="setting_emergency_alert_new_vol"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [#SelectOrgDialog_search]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0] (app frame)
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: New Emergency Alert [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
range: (unnamed) [div > div > div.slidecontainer > span.MuiSlider-root.MuiSlider-marked > span.MuiSlider-thumb.MuiSlider-thumbSizeMedium:nth-of-type(7) > input]
search: Search Workspaces [[data-testid="setting_emergency_alert_new_add_workspace_search_workspace"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | (self) | state-cap |

