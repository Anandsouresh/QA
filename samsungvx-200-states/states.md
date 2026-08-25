# Discovered states

**Target:** https://www.samsungvx.com/  
**Generated:** 2026-08-20T04:04:26+00:00  
**States:** 99 · **Transitions:** 291 · **Actionable elements:** 5187 of 5187 extracted

## N001 — HOME | Samsung VXT CMS *(entry)*

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 49 · **Interactive extracted:** 49 · **DOM nodes:** 425 · **Visits:** 1
- **Reached by:** entry point
- **Screenshot:** [artifacts/N001_6087e0b6.png](artifacts/N001_6087e0b6.png)
- **DOM:** [artifacts/N001_6087e0b6.html](artifacts/N001_6087e0b6.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
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
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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
| Click 'Content' | navigation | N008 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N009 Playlist | Samsung VXT CMS | — |
| Click 'logo' | blocked_mutation | (self) | mutating |
| Click 'img' | blocked_mutation | (self) | mutating |
| Click 'Notification' | in_page_state | N010 HOME | Samsung VXT CMS — Not | mutating |
| Click 'Default Workspace .st0{opacity:0.8;}' | in_page_state | N006 HOME | Samsung VXT CMS — Def | — |
| Click 'chatbot' | in_page_state | (self) | mutating, state-cap |
| Click 'Terms and Conditions' | navigation | N013 Terms and Conditions | Samsu | — |
| Click 'Privacy Policy' | navigation | N014 Privacy Policy | Samsung VXT | — |
| Click 'Cookie Policy' | navigation | N015 Cookie Policy | Samsung VXT  | — |
| Click 'EU Data Act' | navigation | N016 Samsung VXT CMS | — |
| Click 'VXT Labs' | navigation | N003 Samsung VXT CMS | — |
| Click 'Screen' | navigation | N007 Screen | Samsung VXT CMS | — |
| Click 'Content' | navigation | N029 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N035 Playlist | Samsung VXT CMS | — |

## N002 — vxt.samsung.com

- **URL:** https://vxt.samsung.com/contact-us
- **Type:** boundary · **Depth:** 0 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** n/a · **Visits:** 7
- **Reached by:** Click 'Contact Us'

_No actionable elements extracted._

## N003 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** page · **Depth:** 0 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 516 · **Visits:** 2
- **Reached by:** Click 'VXT Labs'
- **Screenshot:** [artifacts/N003_f04fa4aa.png](artifacts/N003_f04fa4aa.png)
- **DOM:** [artifacts/N003_f04fa4aa.html](artifacts/N003_f04fa4aa.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: AI CorpPost [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Image Upscaler [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: AI Writing Assistant [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: Back [[data-testid="icon_back"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)]
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Back' | navigation | N017 Samsung VXT CMS | — |
| Click 'NEW' | in_page_state | N018 Samsung VXT CMS — NEW | — |
| Click 'img' | in_page_state | N018 Samsung VXT CMS — NEW | — |
| Click 'BETA' | in_page_state | N018 Samsung VXT CMS — NEW | — |
| Click 'SmartPlug' | in_page_state | N018 Samsung VXT CMS — NEW | — |
| Click 'img' | no_change | (self) | inert |
| Click 'img' | in_page_state | N019 Samsung VXT CMS — img | — |
| Click 'Back' | navigation | N016 Samsung VXT CMS | — |

## N004 — HOME | Samsung VXT CMS — souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 437 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com'
- **Screenshot:** [artifacts/N004_d208b259.png](artifacts/N004_d208b259.png)
- **DOM:** [artifacts/N004_d208b259.html](artifacts/N004_d208b259.html)

**Action elements**

```
destructive: Sign Out [[data-testid="dashboard_signout"]]
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
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
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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
| Click 'Manual' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Settings' | navigation | N005 Settings | Samsung VXT CMS — | — |
| Click 'Settings' | navigation | N020 Settings | Samsung VXT CMS | — |

## N005 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 38 · **Interactive extracted:** 38 · **DOM nodes:** 657 · **Visits:** 2
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
- **Type:** page · **Depth:** 0 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 564 · **Visits:** 1
- **Reached by:** Click 'Default Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N006_bbbfa40e.png](artifacts/N006_bbbfa40e.png)
- **DOM:** [artifacts/N006_bbbfa40e.html](artifacts/N006_bbbfa40e.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_up"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
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
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
inferred_clickable: Schedule [#dashboard_scheduleCard]
inferred_clickable: Schedule [[data-testid="dashboard_schedule"]]
inferred_clickable: schedule [#scheduleCard_defaultImg]
inferred_clickable: Screen [#dashboard_screenCard]
inferred_clickable: Screen [[data-testid="dashboard_screen"]]
inferred_clickable: screen [#screenCard_defaultImg]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
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
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N001 HOME | Samsung VXT CMS | — |

## N007 — Screen | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 0 · **Actionable:** 52 · **Interactive extracted:** 52 · **DOM nodes:** 551 · **Visits:** 3
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
inferred_clickable: Deactivated [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(1) > div.ga-button-action-class] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]]
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)]
inferred_clickable: No tags0 [role=listitem[name="No tags0"]]
inferred_clickable: Normal [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(2) > div.ga-button-action-class] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Screen' | in_page_state | N025 Screen | Samsung VXT CMS — A | — |
| Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}' | in_page_state | N028 Screen | Samsung VXT CMS — C | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N028 Screen | Samsung VXT CMS — C | — |
| Click 'Screen' | no_change | (self) | inert |
| Click 'Content' | navigation | N029 Content | Samsung VXT CMS | — |

## N008 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 0 · **Actionable:** 71 · **Interactive extracted:** 71 · **DOM nodes:** 690 · **Visits:** 2
- **Reached by:** Click 'Content'

**Action elements**

```
checkbox: (unnamed) [[data-testid="content_card_checkbox_0"]]
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
inferred_clickable: (unnamed) [[data-testid="content_card_more_0"]]
inferred_clickable: (unnamed) [[data-testid="content_card_more_0_icon"]]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0]
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0]
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)]
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N009 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 0 · **Actionable:** 70 · **Interactive extracted:** 70 · **DOM nodes:** 671 · **Visits:** 1
- **Reached by:** Click 'Playlist'

**Action elements**

```
checkbox: (unnamed) [[data-testid="playlistCard_checkbox_0"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="playlist_card_more_0"]]
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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

## N010 — HOME | Samsung VXT CMS — Notification

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 63 · **Interactive extracted:** 63 · **DOM nodes:** 1167 · **Visits:** 1
- **Reached by:** Click 'Notification'
- **Screenshot:** [artifacts/N010_4f72a7a6.png](artifacts/N010_4f72a7a6.png)
- **DOM:** [artifacts/N010_4f72a7a6.html](artifacts/N010_4f72a7a6.html)

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
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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
| Click 'button' | in_page_state | N011 HOME | Samsung VXT CMS — Not | mutating |
| Click 'Close' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N001 HOME | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N012 HOME | Samsung VXT CMS — Not | — |
| Click 'div' | no_change | (self) | inert |
| Click 'div' | in_page_state | N011 HOME | Samsung VXT CMS — Not | — |

## N011 — HOME | Samsung VXT CMS — Notification — button

- **URL:** https://www.samsungvx.com/
- **Type:** dropdown · **Depth:** 0 · **Actionable:** 65 · **Interactive extracted:** 65 · **DOM nodes:** 1260 · **Visits:** 1
- **Reached by:** Click 'Notification' → Click 'button'
- **Screenshot:** [artifacts/N011_c8fbd316.png](artifacts/N011_c8fbd316.png)
- **DOM:** [artifacts/N011_c8fbd316.html](artifacts/N011_c8fbd316.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [#notiFilterStateId > button.btn_icon]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Later [[data-testid="plan_dialog_later"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: Upgrade Now [[data-testid="plan_dialog_upgrade_now"]]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
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
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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

## N012 — HOME | Samsung VXT CMS — Notification — div

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 0 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 503 · **Visits:** 1
- **Reached by:** Click 'Notification' → Click 'div'
- **Screenshot:** [artifacts/N012_9ce26e96.png](artifacts/N012_9ce26e96.png)
- **DOM:** [artifacts/N012_9ce26e96.html](artifacts/N012_9ce26e96.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Close [#footer_rightPart_okBtn]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: Upgrade Now [#early_btnUpgradePlan]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)]
inferred_clickable: (unnamed) [[data-testid="icon_close"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.scrl_tab.scrlTab:nth-of-type(2) > ul.tabs.strong-class > li.ga-button-action-class.selected:nth-of-type(2) > div.earlywarning-badge]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
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
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notice [[data-testid="noti_dialog_tab_NOTI"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: Quick GlanceNormal-Warning-Deactivated- [role=listitem[name="Quick GlanceNormal-Warning-Deactivated-"]]
inferred_clickable: RM State [[data-testid="noti_dialog_tab_RM"]]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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

## N013 — Terms and Conditions | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/terms
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Terms and Conditions'
- **Screenshot:** [artifacts/N013_9b254a0e.png](artifacts/N013_9b254a0e.png)
- **DOM:** [artifacts/N013_9b254a0e.html](artifacts/N013_9b254a0e.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N014 — Privacy Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/privacy
- **Type:** page · **Depth:** 1 · **Actionable:** 13 · **Interactive extracted:** 13 · **DOM nodes:** 169 · **Visits:** 1
- **Reached by:** Click 'Privacy Policy'
- **Screenshot:** [artifacts/N014_37cf2bb8.png](artifacts/N014_37cf2bb8.png)
- **DOM:** [artifacts/N014_37cf2bb8.html](artifacts/N014_37cf2bb8.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Version 1.3 [#select]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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

## N015 — Cookie Policy | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/cookie
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'Cookie Policy'
- **Screenshot:** [artifacts/N015_868a41ac.png](artifacts/N015_868a41ac.png)
- **DOM:** [artifacts/N015_868a41ac.html](artifacts/N015_868a41ac.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Contact Us' | new_tab | N002 vxt.samsung.com | boundary |

## N016 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/euda
- **Type:** page · **Depth:** 1 · **Actionable:** 12 · **Interactive extracted:** 12 · **DOM nodes:** 166 · **Visits:** 1
- **Reached by:** Click 'EU Data Act'
- **Screenshot:** [artifacts/N016_e4b14cd7.png](artifacts/N016_e4b14cd7.png)
- **DOM:** [artifacts/N016_e4b14cd7.html](artifacts/N016_e4b14cd7.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
- **Type:** page · **Depth:** 1 · **Actionable:** 0 · **Interactive extracted:** 0 · **DOM nodes:** 22 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'Back'

_No actionable elements extracted._

## N018 — Samsung VXT CMS — NEW

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 33 · **Interactive extracted:** 33 · **DOM nodes:** 448 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'NEW'
- **Screenshot:** [artifacts/N018_e0e79420.png](artifacts/N018_e0e79420.png)
- **DOM:** [artifacts/N018_e0e79420.html](artifacts/N018_e0e79420.html)

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

## N019 — Samsung VXT CMS — img

- **URL:** https://www.samsungvx.com/vxtlabs
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 1104 · **Visits:** 1
- **Reached by:** Click 'VXT Labs' → Click 'img'
- **Screenshot:** [artifacts/N019_37b82b07.png](artifacts/N019_37b82b07.png)
- **DOM:** [artifacts/N019_37b82b07.html](artifacts/N019_37b82b07.html)

**Action elements**

```
checkbox: By installing this app, you agree to the Terms and Conditions and Permissions. [#CheckBoxInput]
disclosure: Africa [role=button[name="Africa"]]
disclosure: Asia [role=button[name="Asia"]]
disclosure: Europe [role=button[name="Europe"]]
disclosure: North America [role=button[name="North America"]]
disclosure: Oceania [role=button[name="Oceania"]]
disclosure: South America [role=button[name="South America"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Install [role=button[name="Install"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(2) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(3) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(5) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardMedia-root:nth-of-type(3)]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
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
inferred_clickable: Close [[data-testid="icon_close"]] (app frame)
inferred_clickable: Image Generator [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(4) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root]
inferred_clickable: Microsoft Power BIMicrosoft Power BI [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft Power BIMicrosoft Power BIMicrosoft Power BI enables you to instantly visualize your report and dashboard on screen [div > div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPoint [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Microsoft PowerPointMicrosoft PowerPointMicrosoft PowerPoint enables you to instantly play dynamic slideshow. [div > div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: ShadowGen [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: ShadowGenSamsung VXT Canvas enables you to create the shadow effects effortlessly [div.MuiBox-root:nth-of-type(3) > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4)]
inferred_clickable: SmartPlug [div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active > div.MuiPaper-root.MuiPaper-outlined > div.MuiCardContent-root:nth-of-type(4) > div.MuiStack-root >> nth=0]
inferred_clickable: SmartThings ProSmartThings Pro [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Africa' | no_change | (self) | inert |

## N020 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 537 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings'
- **Screenshot:** [artifacts/N020_eef435c9.png](artifacts/N020_eef435c9.png)
- **DOM:** [artifacts/N020_eef435c9.html](artifacts/N020_eef435c9.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]]
inferred_clickable: Plan [[data-testid="setting_plan"]]
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]]
inferred_clickable: User [[data-testid="setting_user"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | navigation | N001 HOME | Samsung VXT CMS | — |
| Click 'General' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'Organization' | navigation | N021 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N022 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N023 Settings | Samsung VXT CMS | — |
| Click 'Register Phone Number' | in_page_state | N005 Settings | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Click 'Register Phone Number' | in_page_state | N005 Settings | Samsung VXT CMS — | — |
| Click 'Plan' | navigation | N024 Settings | Samsung VXT CMS | — |
| Click 'Tech Inquiry' | navigation | N043 Settings | Samsung VXT CMS | — |
| Click 'Organization' | navigation | N051 Settings | Samsung VXT CMS | — |
| Click 'Workspace' | navigation | N022 Settings | Samsung VXT CMS | — |
| Click 'User' | navigation | N023 Settings | Samsung VXT CMS | — |
| Click 'Plan' | navigation | N024 Settings | Samsung VXT CMS | — |

## N021 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 1 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 614 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]]
inferred_clickable: Plan [[data-testid="setting_plan"]]
inferred_clickable: Register Phone Number [#onboarding_area > div:nth-of-type(1) > ul > li:nth-of-type(3) > div]
inferred_clickable: Register Phone Number [[data-testid="Settings_General_Register_Phone_Number"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]]
inferred_clickable: User [[data-testid="setting_user"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] -> https://www.samsungvx.com/settings/techInquiry
```

## N022 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place
- **Type:** page · **Depth:** 1 · **Actionable:** 37 · **Interactive extracted:** 37 · **DOM nodes:** 588 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace'
- **Screenshot:** [artifacts/N022_d456a6ab.png](artifacts/N022_d456a6ab.png)
- **DOM:** [artifacts/N022_d456a6ab.html](artifacts/N022_d456a6ab.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Workspace [[data-testid="settings_workspace_new_add"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_place_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Storage [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Workspaces [[data-testid="Workspace_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'New Workspace' | blocked_mutation | (self) | mutating |
| Click 'Allocation' | no_change | (self) | inert |
| Click 'Default Workspace' | navigation | N056 Settings | Samsung VXT CMS | — |
| Click '3' | navigation | N056 Settings | Samsung VXT CMS | — |
| Click '0' | navigation | N056 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N057 Settings | Samsung VXT CMS | — |
| Click 'div' | navigation | N057 Settings | Samsung VXT CMS | — |
| Click 'Default Workspace' | navigation | N056 Settings | Samsung VXT CMS | — |
| Click 'Edit Home' | navigation | N057 Settings | Samsung VXT CMS | — |

## N023 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 1 · **Actionable:** 36 · **Interactive extracted:** 36 · **DOM nodes:** 571 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User'
- **Screenshot:** [artifacts/N023_b81fd3f4.png](artifacts/N023_b81fd3f4.png)
- **DOM:** [artifacts/N023_b81fd3f4.html](artifacts/N023_b81fd3f4.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
generic_button: more [#topOption_btn_more_options]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
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
inferred_clickable: Member [[data-testid="setting_user_liItem_member"]]
inferred_clickable: More [div:nth-of-type(2) > div.account.account-contents-wrap > div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.rightAfterBtn.MuiBox-root:nth-of-type(2) > div.topbtn_option.ga-button-action-class]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'Member' | no_change | (self) | inert |
| Click 'Owner' | in_page_state | N058 Settings | Samsung VXT CMS — | — |
| Click 'Pending' | in_page_state | N059 Settings | Samsung VXT CMS — | — |

## N024 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 1 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 587 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Plan'
- **Screenshot:** [artifacts/N024_b8f7b730.png](artifacts/N024_b8f7b730.png)
- **DOM:** [artifacts/N024_b8f7b730.html](artifacts/N024_b8f7b730.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]]
inferred_clickable: 0 [#liItemContents2]
inferred_clickable: 2026-10-01 [#SubscriptionTable_nextPaymentDate]
inferred_clickable: 3 [#liItemContents1]
inferred_clickable: 3 [#liItemContents3]
inferred_clickable: Active [#liItemContents0 > div]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Additional Plan [[data-testid="setting_plan_additional"]]
inferred_clickable: Available [#sortColumn >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Default Workspace [#liItemContents4]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: Expiration [#liItemContents5 > div.t-bs-gray:nth-of-type(1)]
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Next Payment [#sortColumn >> nth=0]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Plan [#sortColumn >> nth=0]
inferred_clickable: Primary Plan [[data-testid="setting_plan_primary"]]
inferred_clickable: S Series Trial [#liItemContents0 > dl.dl-d > dt > span]
inferred_clickable: S Series TrialVX-TRIAL [#liItemContents0]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Total [#sortColumn >> nth=0]
inferred_clickable: Used [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Primary Plan' | no_change | (self) | inert |
| Click 'Additional Plan' | in_page_state | N060 Settings | Samsung VXT CMS — | — |

## N025 — Screen | Samsung VXT CMS — Add Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 490 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen'
- **Screenshot:** [artifacts/N025_105670e6.png](artifacts/N025_105670e6.png)
- **DOM:** [artifacts/N025_105670e6.html](artifacts/N025_105670e6.html)

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
| Click 'Samsung Screen' | in_page_state | N026 Screen | Samsung VXT CMS — A | — |
| Click 'Virtual Screen' | in_page_state | N027 Screen | Samsung VXT CMS — A | — |

## N026 — Screen | Samsung VXT CMS — Add Screen — Samsung Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 521 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen' → Click 'Samsung Screen'
- **Screenshot:** [artifacts/N026_4c674996.png](artifacts/N026_4c674996.png)
- **DOM:** [artifacts/N026_4c674996.html](artifacts/N026_4c674996.html)

**Action elements**

```
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Pair My Screen [[data-testid="screen_addscreen_smg_screen_pair"]]
generic_button: Previous [role=button[name="Previous"]]
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
inferred_clickable: (unnamed) [#modalpop_wrap > div.screen_pop_wrap:nth-of-type(1) > div.pop_cont.ftescreen_wrap > div.swiper.swiper-initialized > div.swiper-button-next:nth-of-type(3)]
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
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

## N027 — Screen | Samsung VXT CMS — Add Screen — Virtual Screen

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 492 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'Add Screen' → Click 'Virtual Screen'
- **Screenshot:** [artifacts/N027_48316e79.png](artifacts/N027_48316e79.png)
- **DOM:** [artifacts/N027_48316e79.html](artifacts/N027_48316e79.html)

**Action elements**

```
external_link: https://player.samsungvx.com [role=link[name="https://player.samsungvx.com"]] -> https://player.samsungvx.com
generic_button: Add Screen [#screen_page_pc_btn_add_screen]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Pair My Screen [[data-testid="screen_addscreen_smg_screen_pair"]]
generic_button: Previous [role=button[name="Previous"]]
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
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

## N028 — Screen | Samsung VXT CMS — CHITNU TEAMDefault Workspace .st0{opacity:0.8;}

- **URL:** https://www.samsungvx.com/screen
- **Type:** page · **Depth:** 1 · **Actionable:** 55 · **Interactive extracted:** 55 · **DOM nodes:** 481 · **Visits:** 1
- **Reached by:** Click 'Screen' → Click 'CHITNU TEAMDefault Workspace .st0{opacity:0.8;}'
- **Screenshot:** [artifacts/N028_67784b26.png](artifacts/N028_67784b26.png)
- **DOM:** [artifacts/N028_67784b26.html](artifacts/N028_67784b26.html)

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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Warning [#pc_tagexplorer_id > div.tagexplorerScroll:nth-of-type(2) > ul:nth-of-type(1) > li:nth-of-type(3) > div.ga-button-action-class] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | in_page_state | N007 Screen | Samsung VXT CMS | — |
| Click 'CHITNU TEAMDefault Workspace' | in_page_state | N007 Screen | Samsung VXT CMS | — |
| Click 'Default Workspace' | in_page_state | N007 Screen | Samsung VXT CMS | — |

## N029 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 623 · **Visits:** 2
- **Reached by:** Click 'Content'
- **Screenshot:** [artifacts/N029_9f71b948.png](artifacts/N029_9f71b948.png)
- **DOM:** [artifacts/N029_9f71b948.html](artifacts/N029_9f71b948.html)

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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
inferred_clickable: and [[data-testid="and_or_toggle"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]]
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Contentsand' | in_page_state | N030 Content | Samsung VXT CMS —  | mutating |
| Click 'and' | in_page_state | (self) | state-cap |

## N030 — Content | Samsung VXT CMS — Search Contentsand

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 134 · **Interactive extracted:** 134 · **DOM nodes:** 725 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand'
- **Screenshot:** [artifacts/N030_9dc79b2b.png](artifacts/N030_9dc79b2b.png)
- **DOM:** [artifacts/N030_9dc79b2b.html](artifacts/N030_9dc79b2b.html)

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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
| Click 'Canvas' | in_page_state | N031 Content | Samsung VXT CMS —  | mutating |
| Click 'CanvasCanvas' | in_page_state | N031 Content | Samsung VXT CMS —  | mutating |
| Click 'Custom' | in_page_state | N032 Content | Samsung VXT CMS —  | — |
| Click 'Custom' | in_page_state | N032 Content | Samsung VXT CMS —  | — |
| Click 'E-Paper' | in_page_state | N033 Content | Samsung VXT CMS —  | — |
| Click 'E-PaperE-Paper' | in_page_state | N033 Content | Samsung VXT CMS —  | — |
| Click 'Embargo: Activated' | in_page_state | N034 Content | Samsung VXT CMS —  | — |
| Click 'Embargo: ActivatedEmbargo: Activated' | in_page_state | N034 Content | Samsung VXT CMS —  | — |

## N031 — Content | Samsung VXT CMS — Search Contentsand — Canvas

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 74 · **Interactive extracted:** 74 · **DOM nodes:** 606 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'Canvas'
- **Screenshot:** [artifacts/N031_92196eec.png](artifacts/N031_92196eec.png)
- **DOM:** [artifacts/N031_92196eec.html](artifacts/N031_92196eec.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
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

## N032 — Content | Samsung VXT CMS — Search Contentsand — Custom

- **URL:** https://www.samsungvx.com/content
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 137 · **Interactive extracted:** 137 · **DOM nodes:** 725 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'Custom'
- **Screenshot:** [artifacts/N032_e2132d09.png](artifacts/N032_e2132d09.png)
- **DOM:** [artifacts/N032_e2132d09.html](artifacts/N032_e2132d09.html)

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
generic_button: OK [role=button[name="OK"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
text_input: (unnamed) [#cusTimeContainer > div.input_bundle_wrap.filter_wrapper > div.dateInputContainer.date:nth-of-type(1) > input.ipt_textbox.ga-button-action-class >> nth=0]
text_input: (unnamed) [#cusTimeContainer > div.input_bundle_wrap.filter_wrapper > div.dateInputContainer.date:nth-of-type(3) > input.ipt_textbox.ga-button-action-class >> nth=0]
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N033 — Content | Samsung VXT CMS — Search Contentsand — E-Paper

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 63 · **Interactive extracted:** 63 · **DOM nodes:** 553 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'E-Paper'
- **Screenshot:** [artifacts/N033_1fff6706.png](artifacts/N033_1fff6706.png)
- **DOM:** [artifacts/N033_1fff6706.html](artifacts/N033_1fff6706.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
inferred_clickable: E-Paper [[data-testid="E-Paper"]]
inferred_clickable: E-PaperE-Paper [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: E-PaperE-Paperand [[data-testid="search_input_wrapper"]]
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

## N034 — Content | Samsung VXT CMS — Search Contentsand — Embargo: Activated

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 63 · **Interactive extracted:** 63 · **DOM nodes:** 553 · **Visits:** 1
- **Reached by:** Click 'Content' → Click 'Search Contentsand' → Click 'Embargo: Activated'
- **Screenshot:** [artifacts/N034_9f7adeaf.png](artifacts/N034_9f7adeaf.png)
- **DOM:** [artifacts/N034_9f7adeaf.html](artifacts/N034_9f7adeaf.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
inferred_clickable: Embargo: Activated [[data-testid="Embargo: Activated"]]
inferred_clickable: Embargo: ActivatedEmbargo: Activated [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: Embargo: ActivatedEmbargo: Activatedand [[data-testid="search_input_wrapper"]]
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

## N035 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 560 · **Visits:** 1
- **Reached by:** Click 'Playlist'
- **Screenshot:** [artifacts/N035_99e1d6ef.png](artifacts/N035_99e1d6ef.png)
- **DOM:** [artifacts/N035_99e1d6ef.html](artifacts/N035_99e1d6ef.html)

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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search Playlistsand' | in_page_state | N036 Playlist | Samsung VXT CMS — | — |
| Click 'Add to Favorites' | no_change | (self) | inert |
| Click '1 playlist' | in_page_state | N040 Playlist | Samsung VXT CMS — | mutating |
| Click '1 playlist' | in_page_state | N040 Playlist | Samsung VXT CMS — | — |
| Click 'New Playlist' | in_page_state | (self) | state-cap |
| Click 'div' | in_page_state | (self) | state-cap |
| Click 'more' | in_page_state | (self) | state-cap |
| Click 'New Playlist' | navigation | N041 Playlist | Samsung VXT CMS | — |
| Click 'img' | navigation | N041 Playlist | Samsung VXT CMS | — |
| Click 'div' | navigation | N042 Content | Samsung VXT CMS | — |
| Click 'New Playlist' | navigation | N041 Playlist | Samsung VXT CMS | — |

## N036 — Playlist | Samsung VXT CMS — Search Playlistsand

- **URL:** https://www.samsungvx.com/playlist
- **Type:** dropdown · **Depth:** 1 · **Actionable:** 116 · **Interactive extracted:** 116 · **DOM nodes:** 672 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand'
- **Screenshot:** [artifacts/N036_77fab44c.png](artifacts/N036_77fab44c.png)
- **DOM:** [artifacts/N036_77fab44c.html](artifacts/N036_77fab44c.html)

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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
| Click 'General' | in_page_state | N037 Playlist | Samsung VXT CMS — | — |
| Click 'GeneralGeneral' | in_page_state | N037 Playlist | Samsung VXT CMS — | — |
| Click 'Landscape' | in_page_state | N038 Playlist | Samsung VXT CMS — | — |
| Click 'LandscapeLandscape' | in_page_state | N038 Playlist | Samsung VXT CMS — | mutating |
| Click 'No Content' | in_page_state | N039 Playlist | Samsung VXT CMS — | — |
| Click 'No ContentNo Content' | in_page_state | N039 Playlist | Samsung VXT CMS — | mutating |

## N037 — Playlist | Samsung VXT CMS — Search Playlistsand — General

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 74 · **Interactive extracted:** 74 · **DOM nodes:** 580 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand' → Click 'General'
- **Screenshot:** [artifacts/N037_75aa2462.png](artifacts/N037_75aa2462.png)
- **DOM:** [artifacts/N037_75aa2462.html](artifacts/N037_75aa2462.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
inferred_clickable: General [[data-testid="General"] >> nth=0]
inferred_clickable: GeneralGeneral [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneraland [[data-testid="search_input_wrapper"]]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
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
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input]
```

## N038 — Playlist | Samsung VXT CMS — Search Playlistsand — Landscape

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 76 · **Interactive extracted:** 76 · **DOM nodes:** 580 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand' → Click 'Landscape'
- **Screenshot:** [artifacts/N038_174f2adc.png](artifacts/N038_174f2adc.png)
- **DOM:** [artifacts/N038_174f2adc.html](artifacts/N038_174f2adc.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="playlistCard_checkbox_0"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: (unnamed) [[data-testid="playlist_card_more_0"]]
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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Landscape [[data-testid="Landscape"]]
inferred_clickable: LandscapeLandscape [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: LandscapeLandscapeand [[data-testid="search_input_wrapper"]]
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
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input]
```

## N039 — Playlist | Samsung VXT CMS — Search Playlistsand — No Content

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 60 · **Interactive extracted:** 60 · **DOM nodes:** 534 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'Search Playlistsand' → Click 'No Content'
- **Screenshot:** [artifacts/N039_fd3e786c.png](artifacts/N039_fd3e786c.png)
- **DOM:** [artifacts/N039_fd3e786c.html](artifacts/N039_fd3e786c.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: Delete [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox > div.chip-ibox]
inferred_clickable: Delete [[data-testid="icon_circle_delete"]]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: No Content [[data-testid="No Content"]]
inferred_clickable: No ContentNo Content [#input_search > div.tag-input-wrapper:nth-of-type(1) > span.chip.chip-chkbox]
inferred_clickable: No ContentNo Contentand [[data-testid="search_input_wrapper"]]
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
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(1) > input]
text_input: (unnamed) [#input_search > div.tag-input-wrapper:nth-of-type(1) > div:nth-of-type(2) > input]
```

## N040 — Playlist | Samsung VXT CMS — 1 playlist

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 1 · **Actionable:** 72 · **Interactive extracted:** 72 · **DOM nodes:** 558 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click '1 playlist'
- **Screenshot:** [artifacts/N040_81a34b4b.png](artifacts/N040_81a34b4b.png)
- **DOM:** [artifacts/N040_81a34b4b.html](artifacts/N040_81a34b4b.html)

**Action elements**

```
checkbox: (unnamed) [[data-testid="playlistCard_checkbox_0"]]
destructive: Delete [[data-testid="playlist_toolbar_delete"]]
generic_button: Add Tags [[data-testid="playlist_toolbar_addtags"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
generic_button: Set to Screens [[data-testid="playlist_toolbar_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
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
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)]
inferred_clickable: 1 of 1 selected [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 1 of 1 selected [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)]
inferred_clickable: 1 of 1 selected [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(4)]
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)]
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2)]
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)]
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)]
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
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
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(2) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(2) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add Tags' | in_page_state | (self) | mutating, state-cap |
| Click 'Set to Screens' | in_page_state | (self) | mutating, state-cap |
| Click '1 of 1 selected' | in_page_state | N035 Playlist | Samsung VXT CMS | — |
| Click '1 of 1 selected' | in_page_state | N035 Playlist | Samsung VXT CMS | — |
| Click '1 of 1 selected' | in_page_state | N035 Playlist | Samsung VXT CMS | — |

## N041 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** page · **Depth:** 1 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 546 · **Visits:** 3
- **Reached by:** Click 'Playlist' → Click 'New Playlist'
- **Screenshot:** [artifacts/N041_2f42f31a.png](artifacts/N041_2f42f31a.png)
- **DOM:** [artifacts/N041_2f42f31a.html](artifacts/N041_2f42f31a.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'logo' | navigation | N061 HOME | Samsung VXT CMS | — |
| Click 'span' | in_page_state | N062 Playlist | Samsung VXT CMS — | — |
| Click 'button' | no_change | (self) | inert |
| Click 'more' | in_page_state | N063 Playlist | Samsung VXT CMS — | — |
| Click 'Set to Screens' | in_page_state | N065 Playlist | Samsung VXT CMS — | — |
| Click 'Save' | no_change | (self) | inert |
| Click 'Add Content' | in_page_state | (self) | state-cap |
| Click '01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas' | no_change | (self) | inert |
| Click 'Content' | navigation | N042 Content | Samsung VXT CMS | — |
| Click 'Playlist' | navigation | N035 Playlist | Samsung VXT CMS | — |
| Click 'div' | no_change | (self) | inert |
| Click 'Schedule' | navigation | N067 Schedule | Samsung VXT CMS | — |
| Click 'div' | navigation | N067 Schedule | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N067 Schedule | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N068 Channel | Samsung VXT CMS | — |
| Click 'logo' | navigation | N001 HOME | Samsung VXT CMS | — |
| Click 'Schedule' | navigation | N067 Schedule | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N068 Channel | Samsung VXT CMS | — |

## N042 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 1 · **Actionable:** 68 · **Interactive extracted:** 68 · **DOM nodes:** 631 · **Visits:** 2
- **Reached by:** Click 'Playlist' → Click 'div'

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
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N043 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** page · **Depth:** 2 · **Actionable:** 24 · **Interactive extracted:** 24 · **DOM nodes:** 283 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry'
- **Screenshot:** [artifacts/N043_8d6adb87.png](artifacts/N043_8d6adb87.png)
- **DOM:** [artifacts/N043_8d6adb87.html](artifacts/N043_8d6adb87.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: New Inquiry [role=button[name="New Inquiry"]]
generic_button: Tech Inquiry Permissions [role=button[name="Tech Inquiry Permissions"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Tech Inquiry Permissions' | in_page_state | N044 Settings | Samsung VXT CMS — | — |
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N046 Settings | Samsung VXT CMS | mutating |
| Click 'Event' | navigation | N047 Settings | Samsung VXT CMS | mutating |
| Click 'div' | navigation | N047 Settings | Samsung VXT CMS | mutating |
| Click 'Screen Preset' | navigation | N048 Settings | Samsung VXT CMS | mutating |
| Click 'Emergency Alert' | navigation | N049 Settings | Samsung VXT CMS | mutating |
| Click 'Activity Log' | navigation | N050 Settings | Samsung VXT CMS | mutating |
| Click 'New Inquiry' | navigation | N045 Settings | Samsung VXT CMS | — |
| Click 'Tag' | navigation | N070 Settings | Samsung VXT CMS | — |
| Click 'Event' | navigation | N047 Settings | Samsung VXT CMS | — |
| Click 'Screen Preset' | navigation | N048 Settings | Samsung VXT CMS | — |
| Click 'Emergency Alert' | navigation | N049 Settings | Samsung VXT CMS | — |
| Click 'Activity Log' | navigation | N072 Settings | Samsung VXT CMS | — |

## N044 — Settings | Samsung VXT CMS — Tech Inquiry Permissions

- **URL:** https://www.samsungvx.com/settings/techInquiry
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 340 · **Visits:** 1
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
- **Type:** page · **Depth:** 2 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 443 · **Visits:** 2
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
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (app frame)
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
| Click 'Register Phone Number' | in_page_state | N069 Settings | Samsung VXT CMS — | — |
| Click 'Select' | no_change | (self) | inert |
| Click 'Open' | file_chooser | (self) | mutating, upload |
| Click 'Drop the files here to attach.' | no_change | (self) | inert |

## N046 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 2 · **Actionable:** 27 · **Interactive extracted:** 27 · **DOM nodes:** 355 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Tag'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Tagsets [[data-testid="Tag_settingHeader_input"]]
```

## N047 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/event
- **Type:** page · **Depth:** 2 · **Actionable:** 25 · **Interactive extracted:** 25 · **DOM nodes:** 347 · **Visits:** 3
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Event'
- **Screenshot:** [artifacts/N047_33952104.png](artifacts/N047_33952104.png)
- **DOM:** [artifacts/N047_33952104.html](artifacts/N047_33952104.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_event_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Events [[data-testid="Event_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |

## N048 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/screenPreset
- **Type:** page · **Depth:** 2 · **Actionable:** 26 · **Interactive extracted:** 26 · **DOM nodes:** 356 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Screen Preset'
- **Screenshot:** [artifacts/N048_647bf2f7.png](artifacts/N048_647bf2f7.png)
- **DOM:** [artifacts/N048_647bf2f7.html](artifacts/N048_647bf2f7.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Screen Profile [[data-testid="setting_screen_present_screen_profile"]]
inferred_clickable: Screen Software [[data-testid="setting_screen_present_screen_software"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Screen Profile' | no_change | (self) | inert |
| Click 'Certificate' | no_change | (self) | inert |
| Click 'Screen Software' | no_change | (self) | inert |

## N049 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/emergencyAlert
- **Type:** page · **Depth:** 2 · **Actionable:** 23 · **Interactive extracted:** 23 · **DOM nodes:** 363 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Emergency Alert'
- **Screenshot:** [artifacts/N049_cc555a5b.png](artifacts/N049_cc555a5b.png)
- **DOM:** [artifacts/N049_cc555a5b.html](artifacts/N049_cc555a5b.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N050 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 2 · **Actionable:** 29 · **Interactive extracted:** 29 · **DOM nodes:** 385 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Activity Log'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Path [#sortColumn >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Target [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#sortColumn >> nth=0]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: When [#sortColumn >> nth=0]
inferred_clickable: Where [#sortColumn >> nth=0]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N051 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 419 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization'
- **Screenshot:** [artifacts/N051_7e6abd8d.png](artifacts/N051_7e6abd8d.png)
- **DOM:** [artifacts/N051_7e6abd8d.html](artifacts/N051_7e6abd8d.html)

**Action elements**

```
generic_button: Add [#add_phone_number]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
| Click 'Customization' | in_page_state | N052 Settings | Samsung VXT CMS — | — |
| Click 'Preset' | in_page_state | N053 Settings | Samsung VXT CMS — | — |
| Click 'Tag' | in_page_state | N054 Settings | Samsung VXT CMS — | — |
| Click 'Scheduling' | in_page_state | N055 Settings | Samsung VXT CMS — | — |
| Click 'Information' | no_change | (self) | inert |
| Click 'Customization' | in_page_state | N052 Settings | Samsung VXT CMS — | — |
| Click 'Preset' | in_page_state | N053 Settings | Samsung VXT CMS — | — |
| Click 'Tag' | in_page_state | N054 Settings | Samsung VXT CMS — | — |

## N052 — Settings | Samsung VXT CMS — Customization

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 53 · **Interactive extracted:** 53 · **DOM nodes:** 896 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Customization'
- **Screenshot:** [artifacts/N052_2afece2d.png](artifacts/N052_2afece2d.png)
- **DOM:** [artifacts/N052_2afece2d.html](artifacts/N052_2afece2d.html)

**Action elements**

```
disclosure: Admin Privilege ControlUpgrade Now [role=button[name="Admin Privilege ControlUpgrade Now"]]
disclosure: App Splash Logo [role=button[name="App Splash Logo"]]
disclosure: Content Embargo & LifespanUpgrade Now [role=button[name="Content Embargo & LifespanUpgrade Now"]]
disclosure: Default Content [role=button[name="Default Content"]]
disclosure: Screen Custom FieldsUpgrade Now [role=button[name="Screen Custom FieldsUpgrade Now"]]
generic_button: Apply [role=button[name="Apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Close [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Smart Download optimizes bandwidth by enabling local content [div._tab_content_y859n_1350.tab_content > div.flex_col.gap20px:nth-of-type(3) > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'App Splash Logo' | no_change | (self) | inert |
| Click 'Default Content' | no_change | (self) | inert |
| Click 'Upgrade Now' | no_change | (self) | inert |

## N053 — Settings | Samsung VXT CMS — Preset

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 56 · **Interactive extracted:** 56 · **DOM nodes:** 422 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Preset'
- **Screenshot:** [artifacts/N053_16229520.png](artifacts/N053_16229520.png)
- **DOM:** [artifacts/N053_16229520.html](artifacts/N053_16229520.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
generic_button: Upgrade Now [#WorkspaceScreen_Upgrade >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Android [role=listitem[name="Android"]]
inferred_clickable: Android [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]]
inferred_clickable: BrightSign [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(6) > span]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Close [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(3) > span]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Set up Screen Profile once to automatically apply it when ad [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Set up Screen Profile once to automatically apply it when ad [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Signage [role=listitem[name="Signage"]]
inferred_clickable: Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Windows [role=listitem[name="Windows"]]
inferred_clickable: Windows [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Upgrade Now' | blocked_mutation | (self) | mutating |
| Click 'BrightSign' | blocked_mutation | (self) | mutating |

## N054 — Settings | Samsung VXT CMS — Tag

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 462 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Tag'
- **Screenshot:** [artifacts/N054_9216d372.png](artifacts/N054_9216d372.png)
- **DOM:** [artifacts/N054_9216d372.html](artifacts/N054_9216d372.html)

**Action elements**

```
generic_button: (unnamed) [#ModalFooter_btnMore]
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Global CategoryAvailable for [role=button[name="Global CategoryAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
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
inferred_clickable: Need consistent tags across all workspaces? Global tags let [[data-testid="icon_question"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | blocked_mutation | (self) | mutating |
| Click 'Information' | in_page_state | N051 Settings | Samsung VXT CMS | — |

## N055 — Settings | Samsung VXT CMS — Scheduling

- **URL:** https://www.samsungvx.com/settings/organization
- **Type:** page · **Depth:** 2 · **Actionable:** 46 · **Interactive extracted:** 46 · **DOM nodes:** 579 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Organization' → Click 'Scheduling'
- **Screenshot:** [artifacts/N055_33eebb65.png](artifacts/N055_33eebb65.png)
- **DOM:** [artifacts/N055_33eebb65.html](artifacts/N055_33eebb65.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(3) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_question"] >> nth=0]
inferred_clickable: (unnamed) [div.p24.pt40:nth-of-type(5) > div:nth-of-type(2) > div > div.toggle_switch > label > span.toggle_track]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Close [[data-testid="icon_close"]] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_organization_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Scheduled Publishing allows the Owner to schedule content pu [[data-testid="icon_question"] >> nth=0]
inferred_clickable: Scheduling [[data-testid="settings_organization_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Sunday [[data-testid="select_default"]]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tag [[data-testid="settings_organization_tag"]]
inferred_clickable: Tag [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
| Click 'div' | no_change | (self) | inert |
| Click 'span' | blocked_mutation | (self) | mutating |
| Click 'Do not show again.' | no_change | (self) | inert |

## N056 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 2 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 442 · **Visits:** 4
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace'
- **Screenshot:** [artifacts/N056_139be4f3.png](artifacts/N056_139be4f3.png)
- **DOM:** [artifacts/N056_139be4f3.html](artifacts/N056_139be4f3.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
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
inferred_clickable: More [[data-testid="Workspace_top_option"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: S Series Trial [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: S Series Trial [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [role=listitem[name="S Series TrialAllocation 3Used 0Available 3"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Learn more' | new_tab | N002 vxt.samsung.com | boundary |
| Click 'Default Workspace' | in_page_state | N073 Settings | Samsung VXT CMS — | — |
| Click 'Rename' | in_page_state | N073 Settings | Samsung VXT CMS — | — |
| Click 'General' | no_change | (self) | inert |
| Click 'User' | in_page_state | N074 Settings | Samsung VXT CMS — | — |
| Click 'Customization' | in_page_state | N076 Settings | Samsung VXT CMS — | — |
| Click 'Preset' | in_page_state | N077 Settings | Samsung VXT CMS — | — |
| Click 'Scheduling' | in_page_state | (self) | state-cap |

## N057 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 2 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 496 · **Visits:** 3
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Edit Home'
- **Screenshot:** [artifacts/N057_986fa79c.png](artifacts/N057_986fa79c.png)
- **DOM:** [artifacts/N057_986fa79c.html](artifacts/N057_986fa79c.html)

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: (unnamed) [div > div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.center-wrapper.image-picker:nth-of-type(2) > button.image-picker-add]
generic_button: Apps [role=button[name="Apps"]]
generic_button: Cancel [role=button[name="Cancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Deactivated- [[data-testid="dashboard_quickglance_deactivated"]]
generic_button: Done [role=button[name="Done"]]
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: Normal- [[data-testid="dashboard_quickglance_normal"]]
generic_button: Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite [role=button[name="Quick GlanceCreated with Sketch.Normal-Warning-Deactivated- To pick up a draggable item, press the space bar. While dragging, use the arrow keys to move the ite"]]
generic_button: refresh [#refreshScreenBtn]
generic_button: Reset All [[data-testid="reset-dashboard-button"]]
generic_button: StorageUsed0.00KB [role=button[name="StorageUsed0.00KB"]]
generic_button: Warning- [[data-testid="dashboard_quickglance_warning"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: * Supported formats File format: *.png Image height: 58 px F [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Allocation 3Used 0Available 3 [[data-testid="dashboard_curr_plan0"]]
inferred_clickable: Content [#dashboard_contentCard]
inferred_clickable: Content [[data-testid="dashboard_content"]]
inferred_clickable: content [#contentCard_defaultImg]
inferred_clickable: Default Workspace .st0{opacity:0.8;} [[data-testid="dashboard_workspace_change"]] (app frame)
inferred_clickable: Default Workspace .st0{opacity:0.8;} [#select-wrap > div]
inferred_clickable: Info Card [role=listitem[name="Info Card"]]
inferred_clickable: Mobile View [[data-testid="icon_ic_mobile"]]
inferred_clickable: PC View [[data-testid="icon_ic_web"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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
| Click 'PC View' | no_change | (self) | inert |
| Click 'Mobile View' | in_page_state | N078 Settings | Samsung VXT CMS — | — |
| Click 'Organization Name' | no_change | (self) | inert |

## N058 — Settings | Samsung VXT CMS — Owner

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 30 · **Interactive extracted:** 30 · **DOM nodes:** 366 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User' → Click 'Owner'
- **Screenshot:** [artifacts/N058_40a2aa55.png](artifacts/N058_40a2aa55.png)
- **DOM:** [artifacts/N058_40a2aa55.html](artifacts/N058_40a2aa55.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Owner [[data-testid="setting_user_liItem_owner"]]
inferred_clickable: Pending [[data-testid="setting_user_liItem_pending"]]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Role [[data-testid="setting_user_liItem_role"]]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |

## N059 — Settings | Samsung VXT CMS — Pending

- **URL:** https://www.samsungvx.com/settings/user
- **Type:** page · **Depth:** 2 · **Actionable:** 34 · **Interactive extracted:** 34 · **DOM nodes:** 343 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'User' → Click 'Pending'
- **Screenshot:** [artifacts/N059_9c1b4a06.png](artifacts/N059_9c1b4a06.png)
- **DOM:** [artifacts/N059_9c1b4a06.html](artifacts/N059_9c1b4a06.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Invite User [[data-testid="setting_user_btn_invite_user"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_user_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn >> nth=0] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [[data-testid="User_settingHeader_input"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Date Sent' | no_change | (self) | inert |

## N060 — Settings | Samsung VXT CMS — Additional Plan

- **URL:** https://www.samsungvx.com/settings/subscription
- **Type:** page · **Depth:** 2 · **Actionable:** 32 · **Interactive extracted:** 32 · **DOM nodes:** 306 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Plan' → Click 'Additional Plan'
- **Screenshot:** [artifacts/N060_c3a08a9a.png](artifacts/N060_c3a08a9a.png)
- **DOM:** [artifacts/N060_c3a08a9a.html](artifacts/N060_c3a08a9a.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Register Activation Code [[data-testid="setting_plan_register_activation_code"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#sortColumn >> nth=0]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'No Plans' | no_change | (self) | inert |

## N061 — HOME | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/
- **Type:** page · **Depth:** 2 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 376 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'logo'

**Action elements**

```
external_link: Contact Us [[data-testid="dashboard_contactus"]] (app frame) -> https://vxt.samsung.com/contact-us
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: editHome [[data-testid="dashboard_editbtn"]]
generic_button: refresh [#refreshScreenBtn]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_keyboard_arrow"]]
inferred_clickable: (unnamed) [li._info-card-area-pc_1ukjs_1:nth-of-type(6) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.center-wrapper.storage-pc:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
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
inferred_clickable: New [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: New [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: Normal- [[data-testid="dashboard_quickglance_normal"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Warning- [[data-testid="dashboard_quickglance_warning"]]
nav_link: Cookie Policy [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/cookie
nav_link: EU Data Act [[data-testid="dashboard_cookies"] >> nth=0] (app frame) -> https://www.samsungvx.com/euda
nav_link: Privacy Policy [[data-testid="dashboard_privacy"]] (app frame) -> https://www.samsungvx.com/privacy
nav_link: Terms and Conditions [[data-testid="dashboard_terms"]] (app frame) -> https://www.samsungvx.com/terms
```

## N062 — Playlist | Samsung VXT CMS — span

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** page · **Depth:** 2 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 625 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'span'
- **Screenshot:** [artifacts/N062_79f36f40.png](artifacts/N062_79f36f40.png)
- **DOM:** [artifacts/N062_79f36f40.html](artifacts/N062_79f36f40.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
text_input: New Playlist [[data-testid="playlist_detail_name_input"]]
```

## N063 — Playlist | Samsung VXT CMS — more

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 50 · **Interactive extracted:** 50 · **DOM nodes:** 516 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'more'
- **Screenshot:** [artifacts/N063_a32eec3a.png](artifacts/N063_a32eec3a.png)
- **DOM:** [artifacts/N063_a32eec3a.html](artifacts/N063_a32eec3a.html)

**Action elements**

```
destructive: Delete [[data-testid="playlist_new_general_more_delete"]]
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Content Journey Map [[data-testid="playlist_new_general_more_cjmap"]]
inferred_clickable: Duplicate [[data-testid="playlist_new_general_more_duplicate"]]
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Content Journey Map' | in_page_state | N064 Playlist | Samsung VXT CMS — | mutating |
| Click 'Duplicate' | in_page_state | N041 Playlist | Samsung VXT CMS | mutating |

## N064 — Playlist | Samsung VXT CMS — more — Content Journey Map

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** page · **Depth:** 2 · **Actionable:** 54 · **Interactive extracted:** 54 · **DOM nodes:** 570 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'more' → Click 'Content Journey Map'
- **Screenshot:** [artifacts/N064_67dea394.png](artifacts/N064_67dea394.png)
- **DOM:** [artifacts/N064_67dea394.html](artifacts/N064_67dea394.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div.right_icon_class:nth-of-type(1) > div]
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: 02:00.002:00.0 [#start_journeymap > div.journey-map-parents.hide-line:nth-of-type(2) > div.ga-button-action-class:nth-of-type(1)]
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

## N065 — Playlist | Samsung VXT CMS — Set to Screens

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** dropdown · **Depth:** 2 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 636 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Set to Screens'
- **Screenshot:** [artifacts/N065_37f9b83d.png](artifacts/N065_37f9b83d.png)
- **DOM:** [artifacts/N065_37f9b83d.html](artifacts/N065_37f9b83d.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Cancel [[data-testid="set_to_screens_btncancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Publish [[data-testid="schedule_footer_rightpart_okbtn"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="selectScreen_sort"]]
inferred_clickable: (unnamed) [[data-testid="select-wrap"]]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Screensand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
text_input: Search Screens [role=textbox[name="Search Screens"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N041 Playlist | Samsung VXT CMS | — |
| Click 'div' | in_page_state | N066 Playlist | Samsung VXT CMS — | — |
| Click 'div' | in_page_state | (self) | state-cap |
| Click 'span' | no_change | (self) | inert |

## N066 — Playlist | Samsung VXT CMS — Set to Screens — div

- **URL:** https://www.samsungvx.com/playlist/113561F7-FA56-49A8-A0B4-90050FD6C284
- **Type:** page · **Depth:** 2 · **Actionable:** 66 · **Interactive extracted:** 66 · **DOM nodes:** 731 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Set to Screens' → Click 'div'
- **Screenshot:** [artifacts/N066_0dba3f23.png](artifacts/N066_0dba3f23.png)
- **DOM:** [artifacts/N066_0dba3f23.html](artifacts/N066_0dba3f23.html)

**Action elements**

```
generic_button: (unnamed) [[data-testid="playlist_new_general_preview"]]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_0]
generic_button: 01:00.0Untitled Canvas00:01:00.0CanvasCanvasCanvasCanvas [#playlistDetail_contentList_1]
generic_button: Add Content [[data-testid="playlist_newplaylist_general_addcontent"]]
generic_button: Cancel [[data-testid="set_to_screens_btncancel"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_detail_toolbar_more"]]
generic_button: Publish [[data-testid="schedule_footer_rightpart_okbtn"]]
generic_button: Save [[data-testid="playlist_new_general_save"]]
generic_button: Set to Screens [[data-testid="playlist_new_general_set2screen"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]]
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_tooltip"]]
inferred_clickable: (unnamed) [#playlistDetail_weight > div:nth-of-type(2) > div.toggle_switch > label > span.toggle_track.ga-button-action-class]
inferred_clickable: (unnamed) [#playlistDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_date_down"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_date_up"]]
inferred_clickable: (unnamed) [[data-testid="icon_name_down"]]
inferred_clickable: (unnamed) [[data-testid="icon_name_up"]]
inferred_clickable: (unnamed) [[data-testid="select-wrap"]]
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [div:nth-of-type(1) > div.left.flex > div.detail_area.move:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(2) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Date [[data-testid="selectScreen_sortoption_li_updated_time_desc"]]
inferred_clickable: Date [[data-testid="selectScreen_sortoption_li_updated_time_asc"]]
inferred_clickable: DateDateNameName [[data-testid="selectScreen_sort"]]
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Name [[data-testid="selectScreen_sortoption_li_content_name_desc"]]
inferred_clickable: Name [[data-testid="selectScreen_sortoption_li_content_name_asc"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Screensand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
text_input: Search Screens [role=textbox[name="Search Screens"]]
```

## N067 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 2 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 497 · **Visits:** 4
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule'
- **Screenshot:** [artifacts/N067_2847a137.png](artifacts/N067_2847a137.png)
- **DOM:** [artifacts/N067_2847a137.html](artifacts/N067_2847a137.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
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
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Schedule' | in_page_state | N079 Schedule | Samsung VXT CMS — | — |
| Click 'div' | navigation | N068 Channel | Samsung VXT CMS | — |
| Click 'Channel' | navigation | N068 Channel | Samsung VXT CMS | — |
| Click 'div' | navigation | N068 Channel | Samsung VXT CMS | — |
| Click '' | navigation | N089 Channel | Samsung VXT CMS —  | — |

## N068 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 2 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 504 · **Visits:** 5
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel'
- **Screenshot:** [artifacts/N068_aa7ea0c5.png](artifacts/N068_aa7ea0c5.png)
- **DOM:** [artifacts/N068_aa7ea0c5.html](artifacts/N068_aa7ea0c5.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
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
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'New Channel' | in_page_state | N082 Channel | Samsung VXT CMS —  | — |
| Click 'div' | in_page_state | N084 Channel | Samsung VXT CMS —  | — |
| Click 'AppsN' | navigation | N088 Samsung VXT CMS | — |
| Click 'div' | navigation | N088 Samsung VXT CMS | — |
| Click 'AppsN' | navigation | N088 Samsung VXT CMS | — |
| Click 'AppsN' | navigation | N088 Samsung VXT CMS | — |

## N069 — Settings | Samsung VXT CMS — Register Phone Number

- **URL:** https://www.samsungvx.com/settings/techInquiryNew
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 475 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'New Inquiry' → Click 'Register Phone Number'
- **Screenshot:** [artifacts/N069_da109b4b.png](artifacts/N069_da109b4b.png)
- **DOM:** [artifacts/N069_da109b4b.html](artifacts/N069_da109b4b.html)

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
inferred_clickable: (unnamed) [[data-testid="icon_phone"]] (app frame)
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

## N070 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag
- **Type:** page · **Depth:** 3 · **Actionable:** 28 · **Interactive extracted:** 28 · **DOM nodes:** 333 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Tag'
- **Screenshot:** [artifacts/N070_e468c7e3.png](artifacts/N070_e468c7e3.png)
- **DOM:** [artifacts/N070_e468c7e3.html](artifacts/N070_e468c7e3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_tag_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Tagset [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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
| Click 'Default TagsetRegion, Location, Subject, Others' | navigation | N071 Settings | Samsung VXT CMS | — |
| Click 'Default Workspace' | navigation | N071 Settings | Samsung VXT CMS | — |

## N071 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/tag/78935
- **Type:** page · **Depth:** 3 · **Actionable:** 48 · **Interactive extracted:** 48 · **DOM nodes:** 740 · **Visits:** 2
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Tag' → Click 'Default TagsetRegion, Location, Subject, Others'

**Action elements**

```
checkbox: (unnamed) [div.account.account-contents-wrap > div.contents_box.tagset_workspace > div:nth-of-type(3) > div > div > input]
generic_button: (unnamed) [#tagsetDetail_btnDeleteTagMode] (disabled)
generic_button: Add Category [[data-testid="tagsetDetail_btnChangeAddCategoryMode"]]
generic_button: Add Workspace [[data-testid="setting_tag_details_add_workspace"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: LocationAvailable for [role=button[name="LocationAvailable for"]]
generic_button: More [#ModalFooter_btnMore]
generic_button: OthersAvailable for [role=button[name="OthersAvailable for"]]
generic_button: RegionAvailable for [role=button[name="RegionAvailable for"]]
generic_button: SubjectAvailable for [role=button[name="SubjectAvailable for"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="setting_tag_details_add_tag"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Change Color [[data-testid="icon_common_category"] >> nth=0]
inferred_clickable: Default Tagset [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Default Workspace [#FcmsTable_liItemContents0]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: Location [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Others [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Region [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(2) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [[data-testid="setting_tag_details_rename"] >> nth=0]
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
inferred_clickable: Workspace [#FcmsTable_sortColumn]
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N072 — Settings | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/settings/activityLog
- **Type:** page · **Depth:** 3 · **Actionable:** 35 · **Interactive extracted:** 35 · **DOM nodes:** 565 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Tech Inquiry' → Click 'Activity Log'
- **Screenshot:** [artifacts/N072_41a46fe6.png](artifacts/N072_41a46fe6.png)
- **DOM:** [artifacts/N072_41a46fe6.html](artifacts/N072_41a46fe6.html)

**Action elements**

```
generic_button: Apply [[data-testid="setting_activity_log_apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Export [[data-testid="activity_btnExport"]] (disabled)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="setting_activityLog_search_icon"]]
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Path [#sortColumn >> nth=0]
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Target [#sortColumn >> nth=0]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [#sortColumn >> nth=0]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
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

## N073 — Settings | Samsung VXT CMS — Default Workspace

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 49 · **Interactive extracted:** 49 · **DOM nodes:** 422 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'Default Workspace'
- **Screenshot:** [artifacts/N073_dbda2dfd.png](artifacts/N073_dbda2dfd.png)
- **DOM:** [artifacts/N073_dbda2dfd.html](artifacts/N073_dbda2dfd.html)

**Action elements**

```
external_link: Learn more [role=link[name="Learn more"]] -> https://vxt.samsung.com/pricing
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
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
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: More [[data-testid="Workspace_top_option"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: S Series Trial [[data-testid="dashboard_planviewundefined"]]
inferred_clickable: S Series Trial [ul > li.home-card.ga-button-action-class > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [role=listitem[name="S Series TrialAllocation 3Used 0Available 3"]]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: Used 0 [role=listitem[name="Used 0"]]
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
text_input: Default Workspace [[data-testid="FCMSInput"]]
```

## N074 — Settings | Samsung VXT CMS — User

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 378 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'User'
- **Screenshot:** [artifacts/N074_51971322.png](artifacts/N074_51971322.png)
- **DOM:** [artifacts/N074_51971322.html](artifacts/N074_51971322.html)

**Action elements**

```
generic_button: Add User [[data-testid="settings_workspace_user_adduser"] >> nth=0]
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: More [[data-testid="Workspace_top_option"]]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(2) > span]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Add User' | in_page_state | N075 Settings | Samsung VXT CMS — | — |
| Click 'General' | in_page_state | N056 Settings | Samsung VXT CMS | — |
| Click 'No users.' | no_change | (self) | inert |
| Click 'Role' | no_change | (self) | inert |
| Click 'User' | no_change | (self) | inert |

## N075 — Settings | Samsung VXT CMS — User — Add User

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 415 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'User' → Click 'Add User'
- **Screenshot:** [artifacts/N075_b5a15298.png](artifacts/N075_b5a15298.png)
- **DOM:** [artifacts/N075_b5a15298.html](artifacts/N075_b5a15298.html)

**Action elements**

```
generic_button: Add [[data-testid="settings_workspace_user_adduser_ok"]]
generic_button: Add User [[data-testid="settings_workspace_user_adduser"] >> nth=0]
generic_button: Cancel [[data-testid="settings_workspace_user_adduser_cancel"]]
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
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [#SelectUserDialog_search]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: No users. [[data-testid="No users."]]
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: Role [#FcmsTable_sortColumn >> nth=0]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(2) > span]
inferred_clickable: User [#FcmsTable_sortColumn >> nth=0] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
search: Search Users [#SelectUserDialog_input]
```

## N076 — Settings | Samsung VXT CMS — Customization

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 827 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'Customization'
- **Screenshot:** [artifacts/N076_683a0434.png](artifacts/N076_683a0434.png)
- **DOM:** [artifacts/N076_683a0434.html](artifacts/N076_683a0434.html)

**Action elements**

```
disclosure: App Splash Logo [role=button[name="App Splash Logo"]]
disclosure: Content Embargo & LifespanUpgrade Now [role=button[name="Content Embargo & LifespanUpgrade Now"]]
disclosure: Default Content [role=button[name="Default Content"]]
disclosure: Screen Custom FieldsUpgrade Now [role=button[name="Screen Custom FieldsUpgrade Now"]]
generic_button: Apply [role=button[name="Apply"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
generic_button: Upgrade Now [role=button[name="Upgrade Now"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [div._tab_container_w4n70_13 > div.flex_col.gap40px > div.MuiStack-root:nth-of-type(3) > div.MuiBox-root > div:nth-of-type(1) > div.center-wrapper.hover-icon:nth-of-type(3)]
inferred_clickable: (unnamed) [div.MuiBox-root > div.MuiStack-root:nth-of-type(2) > div.center-wrapper.MuiBox-root > div.toggle_switch > label > span.toggle_track]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_expand"] >> nth=0]
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(3) > span]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: More [[data-testid="Workspace_top_option"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

## N077 — Settings | Samsung VXT CMS — Preset

- **URL:** https://www.samsungvx.com/settings/place/8AD89E5C-90FE-4F44-8A8C-F78707191F89
- **Type:** page · **Depth:** 3 · **Actionable:** 56 · **Interactive extracted:** 56 · **DOM nodes:** 407 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Default Workspace' → Click 'Preset'
- **Screenshot:** [artifacts/N077_328d0390.png](artifacts/N077_328d0390.png)
- **DOM:** [artifacts/N077_328d0390.html](artifacts/N077_328d0390.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Upgrade Now [[data-testid="settings_workspace_preset_profile_upgrade_now"]]
generic_button: Upgrade Now [[data-testid="settings_workspace_preset_certificate_upgrade_now"]]
generic_button: Upgrade Now [[data-testid="settings_workspace_preset_firmware_upgrade_now"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_back"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_new_window"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"] >> nth=0] (app frame)
inferred_clickable: Activity Log [[data-testid="setting_activityLog"]] (app frame)
inferred_clickable: Android [role=listitem[name="Android"]]
inferred_clickable: Android [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(4) > span]
inferred_clickable: BrightSign [role=listitem[name="BrightSign"]]
inferred_clickable: BrightSign [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(6) > span]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Customization [[data-testid="settings_workspace_customization"]]
inferred_clickable: Customization [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Default Workspace [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > h2.title_h2_class.ellipsis > span]
inferred_clickable: E-Paper [role=listitem[name="E-Paper"]]
inferred_clickable: E-Paper [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(3) > span]
inferred_clickable: Edit Home [[data-testid="setting_editHome"]] (app frame)
inferred_clickable: Emergency Alert [[data-testid="setting_alert"]] (app frame)
inferred_clickable: Event [[data-testid="setting_event"]] (app frame)
inferred_clickable: Flip [role=listitem[name="Flip"]]
inferred_clickable: Flip [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(7) > span]
inferred_clickable: General [[data-testid="setting_general"]] (app frame)
inferred_clickable: General [[data-testid="settings_workspace_general"]]
inferred_clickable: General [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(1) > span]
inferred_clickable: Indoor LED Signage [role=listitem[name="Indoor LED Signage"]]
inferred_clickable: Indoor LED Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: Legacy [role=listitem[name="Legacy"]]
inferred_clickable: Legacy [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(8) > span]
inferred_clickable: More [[data-testid="Workspace_top_option"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Organization [[data-testid="setting_organization"]] (app frame)
inferred_clickable: Plan [[data-testid="setting_plan"]] (app frame)
inferred_clickable: Preset [[data-testid="settings_workspace_preset"]]
inferred_clickable: Preset [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(4) > span]
inferred_clickable: Rename [header > div._head_area_1ijv6_59:nth-of-type(3) > div._on_1ijv6_195 > div:nth-of-type(3) > div._name_edit_wrap_1ijv6_326 > span._name_edit_open_1ijv6_333]
inferred_clickable: Scheduling [[data-testid="settings_workspace_scheduling"]]
inferred_clickable: Scheduling [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Screen Preset [[data-testid="setting_screenPreset"]] (app frame)
inferred_clickable: Signage [role=listitem[name="Signage"]]
inferred_clickable: Signage [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class.selected:nth-of-type(1) > span]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Tag [[data-testid="setting_tag"]] (app frame)
inferred_clickable: User [[data-testid="setting_user"]] (app frame)
inferred_clickable: User [[data-testid="settings_workspace_user"]]
inferred_clickable: User [div.account-tr.tab-tr:nth-of-type(1) > div._tab_comp_w4n70_1.noshortSwiper > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: Windows [role=listitem[name="Windows"]]
inferred_clickable: Windows [#PresetTab > div.scrl_tab.scrlTab:nth-of-type(1) > ul.tabs > li.ga-button-action-class:nth-of-type(5) > span]
inferred_clickable: Workspace [[data-testid="setting_place"]] (app frame)
nav_link: Tech Inquiry [role=link[name="Tech Inquiry"]] (app frame) -> https://www.samsungvx.com/settings/techInquiry
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Upgrade Now' | no_change | (self) | inert |
| Click 'Upgrade Now' | in_page_state | (self) | state-cap |

## N078 — Settings | Samsung VXT CMS — Mobile View

- **URL:** https://www.samsungvx.com/settings/editHome
- **Type:** page · **Depth:** 3 · **Actionable:** 58 · **Interactive extracted:** 58 · **DOM nodes:** 505 · **Visits:** 1
- **Reached by:** Click 'souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com' → Click 'Settings' → Click 'Workspace' → Click 'Edit Home' → Click 'Mobile View'
- **Screenshot:** [artifacts/N078_f65ab7b0.png](artifacts/N078_f65ab7b0.png)
- **DOM:** [artifacts/N078_f65ab7b0.html](artifacts/N078_f65ab7b0.html)

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
inferred_clickable: (unnamed) [#moHeader_menu]
inferred_clickable: (unnamed) [[data-testid="dashboard_screen_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_content_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_playlist_newbtn"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_schedule_newbtn"]]
inferred_clickable: (unnamed) [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > div._dot_comp_18hso_1.bg-green:nth-of-type(1)]
inferred_clickable: (unnamed) [[data-testid="icon_badge_trial"]] (app frame)
inferred_clickable: (unnamed) [li._info-card-area-mobile_1ukjs_2:nth-of-type(2) > ul > li.home-card.ga-button-action-class:nth-of-type(2) > div.storage-mobile:nth-of-type(2) > div.doughnut-chart > div.ga-button-action-class]
inferred_clickable: * Supported formats File format: *.png Image height: 58 px F [div.selected:nth-of-type(1) > div.settings-tab > div:nth-of-type(2) > div.settings-tab-option-header:nth-of-type(1) > div:nth-of-type(2) > div.center-wrapper.hover-icon]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
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
inferred_clickable: Mobile View [[data-testid="icon_ic_mobile"]]
inferred_clickable: PC View [[data-testid="icon_ic_web"]]
inferred_clickable: Playlist [#dashboard_playlistCard]
inferred_clickable: Playlist [[data-testid="dashboard_playlist"]]
inferred_clickable: playlist [#playlistCard_defaultImg]
inferred_clickable: S Series Trial [[data-testid="dashboard_planview0"]]
inferred_clickable: S Series Trial [#planCard_item0 > div > div.home-card-header:nth-of-type(1) > div.ga-button-action-class > span]
inferred_clickable: S Series TrialAllocation 3Used 0Available 3 [#dashboard_planCard]
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
| Click 'div' | no_change | (self) | inert |

## N079 — Schedule | Samsung VXT CMS — New Schedule

- **URL:** https://www.samsungvx.com/schedule
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 410 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule'
- **Screenshot:** [artifacts/N079_f84de247.png](artifacts/N079_f84de247.png)
- **DOM:** [artifacts/N079_f84de247.html](artifacts/N079_f84de247.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [#select-wrap > ul.select-ul.on > li.ga-button-action-class:nth-of-type(2) > span]
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
inferred_clickable: General [[data-testid="schedule_genral_btn"]]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Sync Play [[data-testid="schedule_syncplay_btn"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'span' | navigation | N080 Schedule | Samsung VXT CMS | — |
| Click 'General' | navigation | N081 Schedule | Samsung VXT CMS | — |
| Click 'Sync Play' | navigation | N080 Schedule | Samsung VXT CMS | — |
| Click '' | navigation | N090 Schedule | Samsung VXT CMS | — |

## N080 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 3 · **Actionable:** 45 · **Interactive extracted:** 45 · **DOM nodes:** 667 · **Visits:** 2
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click 'span'

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Sync Play [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

## N081 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 3 · **Actionable:** 45 · **Interactive extracted:** 45 · **DOM nodes:** 667 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click 'General'

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)]
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

## N082 — Channel | Samsung VXT CMS — New Channel

- **URL:** https://www.samsungvx.com/channel
- **Type:** dropdown · **Depth:** 3 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 423 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'New Channel'
- **Screenshot:** [artifacts/N082_72d1ac5d.png](artifacts/N082_72d1ac5d.png)
- **DOM:** [artifacts/N082_72d1ac5d.html](artifacts/N082_72d1ac5d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: (unnamed) [#select-wrap > ul.select-ul.on > li.ga-button-action-class:nth-of-type(2) > span] (app frame)
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
inferred_clickable: General [[data-testid="channel_fcms_general_btn"]]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: Sync Play [role=listitem[name="Sync Play"]]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'General' | navigation | N083 Channel | Samsung VXT CMS | — |
| Click 'General' | navigation | N096 Channel | Samsung VXT CMS | — |

## N083 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel/create
- **Type:** page · **Depth:** 3 · **Actionable:** 42 · **Interactive extracted:** 42 · **DOM nodes:** 400 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'New Channel' → Click 'General'

**Action elements**

```
generic_button: Add Channel [#channelDetail_addContentBtn]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"]]
generic_button: Save [#channelDetail_general_saveBtn]
generic_button: Set to Screens [#channelDetail_general_set2ScreensBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [#channelDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AppsN [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: AppsN [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: N [#navbar_li_apps > div:nth-of-type(2) > div._menu-suffix-icon_1gcwv_1] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Settings [role=listitem[name="Settings"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

## N084 — Channel | Samsung VXT CMS — div

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 3 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 391 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'div'
- **Screenshot:** [artifacts/N084_569d8c59.png](artifacts/N084_569d8c59.png)
- **DOM:** [artifacts/N084_569d8c59.html](artifacts/N084_569d8c59.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [#navbar_leftControl]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: Menu [[data-testid="icon_list"]]
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [[data-testid="icon_screen"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'listitem' | navigation | N085 Content | Samsung VXT CMS | — |
| Click 'listitem' | navigation | N086 Playlist | Samsung VXT CMS | — |
| Click 'listitem' | navigation | N087 Schedule | Samsung VXT CMS | — |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | navigation | N088 Samsung VXT CMS | — |
| Click '.st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;}' | in_page_state | N089 Channel | Samsung VXT CMS —  | — |
| Click 'Menu' | in_page_state | N089 Channel | Samsung VXT CMS —  | — |
| Click 'Menu' | in_page_state | N089 Channel | Samsung VXT CMS —  | — |
| Click '' | navigation | N098 Schedule | Samsung VXT CMS | — |
| Click '' | navigation | N088 Samsung VXT CMS | — |

## N085 — Content | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/content
- **Type:** page · **Depth:** 3 · **Actionable:** 59 · **Interactive extracted:** 59 · **DOM nodes:** 583 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'div' → Click 'listitem'

**Action elements**

```
generic_button: Add Content [#content_toolbar_pc_topbtn_Add]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Create Content [#content_toolbar_pc_topbtn_Create]
generic_button: more [[data-testid="content_page_toolbar_btnmore"]]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="content_sort"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="select-wrap"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: (unnamed) [#content_card_boxWrap >> nth=0]
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [#navbar_leftControl]
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: 2 contents [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.f_bold:nth-of-type(1)]
inferred_clickable: 2 contents [#content_toolbar_pc_topbtnWrap > div:nth-of-type(1) > div.ga-button-action-class.checkbox_wrapper > label > span.gray3:nth-of-type(2)]
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvas [#content_card_div_test_2 > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: CanvasCanvasCanvasCanvas [#content_card_div_test_2 >> nth=0]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: Menu [[data-testid="icon_list"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags2 [role=listitem[name="No tags2"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: or [[data-testid="and_or_toggle"]]
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Search Contentsor [[data-testid="search_input_wrapper"]]
inferred_clickable: Search using objects, scenes and text recognized by AI in yo [[data-testid="icon_ai_search"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Contents [role=textbox[name="Search Contents"]]
```

## N086 — Playlist | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/playlist
- **Type:** page · **Depth:** 3 · **Actionable:** 59 · **Interactive extracted:** 59 · **DOM nodes:** 550 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'div' → Click 'listitem'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="playlist_toolbar_more"] >> nth=0]
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="playlist_sort"] >> nth=0]
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [#navbar_leftControl] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: 02:00.0 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(1)]
inferred_clickable: 1 playlist [[data-testid="FcmsCheckBoxWrapper"]]
inferred_clickable: 1 playlist [#playlistList_toolbar > div.ga-button-action-class.checkbox_wrapper:nth-of-type(1) > label > span.gray3:nth-of-type(2)]
inferred_clickable: 2 [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span.list_num:nth-of-type(1)]
inferred_clickable: 2 contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2)]
inferred_clickable: 2026-08-20 09:18 [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(3)]
inferred_clickable: 47.21 KB [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(2)]
inferred_clickable: Add to Favorites [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: contents [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.flex_center:nth-of-type(2) > span.font16 > span:nth-of-type(2)]
inferred_clickable: GeneralGeneral [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1 > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: GeneralGeneralGeneralGeneral [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1]
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: Menu [[data-testid="icon_list"]] (app frame)
inferred_clickable: New Playlist [[data-testid="playlist_newplaylist"]]
inferred_clickable: New Playlist [#playlistCard_0 > div.image_info.list_view:nth-of-type(3) > div.con_name02.list_view:nth-of-type(1)]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags1 [role=listitem[name="No tags1"]]
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Search Playlistsand [[data-testid="search_input_wrapper"]]
inferred_clickable: souresh Anand [div.image_info.list_view:nth-of-type(3) > div.chip_wrap.list_view:nth-of-type(3) > ul > li.content_info > div.info_table:nth-of-type(2) > span.division:nth-of-type(4)]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Playlists [role=textbox[name="Search Playlists"]]
```

## N087 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 3 · **Actionable:** 39 · **Interactive extracted:** 39 · **DOM nodes:** 401 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'div' → Click 'listitem'

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;} [#navbar_leftControl] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: Menu [#place_wrap] (app frame)
inferred_clickable: Menu [[data-testid="icon_list"]] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Others [#treeCategory_Others_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Others0Loading... [role=listitem[name="Others0Loading..."]] (app frame)
inferred_clickable: Refresh [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: Region [#treeCategory_Region_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Region0Loading... [role=listitem[name="Region0Loading..."]] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [[data-testid="icon_screen"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Subject [#treeCategory_Subject_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Subject0Loading... [role=listitem[name="Subject0Loading..."]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

## N088 — Samsung VXT CMS

- **URL:** https://www.samsungvx.com/apps
- **Type:** page · **Depth:** 3 · **Actionable:** 167 · **Interactive extracted:** 167 · **DOM nodes:** 1140 · **Visits:** 5
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'AppsN'
- **Screenshot:** [artifacts/N088_2a28014d.png](artifacts/N088_2a28014d.png)
- **DOM:** [artifacts/N088_2a28014d.html](artifacts/N088_2a28014d.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
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
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: CalendarCalendar [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
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
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Productivity [div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search [[data-testid="icon_search"]]
inferred_clickable: ShadowGenShadowGenBETASamsung VXT Canvas enables you to create the shadow effects effortlessly [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Search' | blocked_mutation | (self) | mutating |
| Click 'img' | no_change | (self) | inert |
| Click 'AI StudioAI StudioGen AI' | in_page_state | N099 Samsung VXT CMS — AI StudioA | — |
| Click 'img' | in_page_state | N099 Samsung VXT CMS — AI StudioA | — |

## N089 — Channel | Samsung VXT CMS — div — .st0{fill:#FAFAFA;} .st1{fill:#F3F3F3;} .st2{opacity:0.6;enable-background:new ;} .st3{fill:#BDBDBD;}

- **URL:** https://www.samsungvx.com/channel
- **Type:** page · **Depth:** 3 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 420 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click ''
- **Screenshot:** [artifacts/N089_3d69edf3.png](artifacts/N089_3d69edf3.png)
- **DOM:** [artifacts/N089_3d69edf3.html](artifacts/N089_3d69edf3.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Channel [[data-testid="channel_fcms_new_channel_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

## N090 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 4 · **Actionable:** 44 · **Interactive extracted:** 44 · **DOM nodes:** 633 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click ''
- **Screenshot:** [artifacts/N090_ae679aac.png](artifacts/N090_ae679aac.png)
- **DOM:** [artifacts/N090_ae679aac.html](artifacts/N090_ae679aac.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'General' | no_change | (self) | inert |
| Click 'Add Content' | in_page_state | N091 Schedule | Samsung VXT CMS — | mutating |
| Click 'Set to Screens' | no_change | (self) | inert |
| Click 'Save' | no_change | (self) | inert |
| Click 'more' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'August 2026Week 34' | in_page_state | N093 Schedule | Samsung VXT CMS — | — |
| Click 'div' | no_change | (self) | inert |
| Click 'span' | in_page_state | N094 Schedule | Samsung VXT CMS — | — |
| Click 'div' | in_page_state | N094 Schedule | Samsung VXT CMS — | — |
| Click 'Apps' | native_dialog | (self) | confirmation_required |
| Click 'Apps' | native_dialog | (self) | confirmation_required |

## N091 — Schedule | Samsung VXT CMS — Add Content

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 51 · **Interactive extracted:** 51 · **DOM nodes:** 782 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click '' → Click 'Add Content'
- **Screenshot:** [artifacts/N091_9ace10c4.png](artifacts/N091_9ace10c4.png)
- **DOM:** [artifacts/N091_9ace10c4.html](artifacts/N091_9ace10c4.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
generic_button: Cancel [[data-testid="schedule_content_popup_cancel_btn"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="schedule_fcmsmore_button"]]
generic_button: OK [[data-testid="schedule_content_popup_ok_btn"]]
generic_button: Save [[data-testid="schedule_save_btn"]]
generic_button: Set to Screens [[data-testid="schedule_set2screen_btn"]]
generic_button: Today [[data-testid="schedule_today_btn"]]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_content_popup_add_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Once [[data-testid="select-Repeat"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
text_input: (unnamed) [#schedule_content_popup_start_date > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0] (app frame)
text_input: (unnamed) [#select >> nth=0] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Cancel' | in_page_state | N090 Schedule | Samsung VXT CMS | mutating |
| Click 'div' | in_page_state | N092 Schedule | Samsung VXT CMS — | mutating |
| Click 'Once' | no_change | (self) | inert |

## N092 — Schedule | Samsung VXT CMS — Add Content — div

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 72 · **Interactive extracted:** 72 · **DOM nodes:** 940 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click '' → Click 'Add Content' → Click 'div'
- **Screenshot:** [artifacts/N092_6dcab59d.png](artifacts/N092_6dcab59d.png)
- **DOM:** [artifacts/N092_6dcab59d.html](artifacts/N092_6dcab59d.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#schedule_prev_week_btn]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_content_popup_add_btn"]]
inferred_clickable: (unnamed) [#modalpop_wrap > div.pop_ti._pop_ti_1e26u_2185:nth-of-type(1) > div.flex_center.gap24px:nth-of-type(2) > div:nth-of-type(2)] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="add_to_favorites"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="schedule_sort_search_results"]]
inferred_clickable: (unnamed) [[data-testid="select-wrap"]] (app frame)
inferred_clickable: (unnamed) [div.flex_center_between.ml10:nth-of-type(2) > div.flex_center:nth-of-type(2) > div.flex_center.showToggle > div.toggle_switch > label.toggle_label > span.toggle_track] (app frame)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: (unnamed) [#screenImage >> nth=0] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: and [[data-testid="and_or_toggle"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 34 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CanvasCanvas [li.image_listitem:nth-of-type(1) > div.image_info:nth-of-type(2) > div.hd-flex:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: CanvasCanvas [li.image_listitem:nth-of-type(2) > div.image_info:nth-of-type(2) > div.hd-flex:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1) > div._tags-inline-container_1r1vx_9:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: CanvasCanvasCanvasCanvas [ul.screenpage_ul > ul.image_listbox.list_view2 > li.image_listitem:nth-of-type(1) > div.image_info:nth-of-type(2) > div.hd-flex:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1)]
inferred_clickable: CanvasCanvasCanvasCanvas [ul.screenpage_ul > ul.image_listbox.list_view2 > li.image_listitem:nth-of-type(2) > div.image_info:nth-of-type(2) > div.hd-flex:nth-of-type(2) > div._tag-list-container_1r1vx_1._tags-inline-grower_1c00t_1:nth-of-type(1)]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Content [[data-testid="schedule_selectcontentdialog_content"]]
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Once [[data-testid="select-Repeat"]]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Playlist [[data-testid="schedule_selectcontentdialog_playlist"]]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Search Contentsand [[data-testid="search_input_wrapper"]] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Untitled Canvas [#image_listwrap > ul.screenpage_ul > ul.image_listbox.list_view2 > li.image_listitem:nth-of-type(1) > div.image_info:nth-of-type(2) > div._con_name01_5qb2z_1:nth-of-type(1)]
inferred_clickable: Untitled Canvas [#image_listwrap > ul.screenpage_ul > ul.image_listbox.list_view2 > li.image_listitem:nth-of-type(2) > div.image_info:nth-of-type(2) > div._con_name01_5qb2z_1:nth-of-type(1)]
text_input: (unnamed) [#schedule_content_popup_start_date > div.dateInputContainer.date > input.ipt_textbox.ga-button-action-class]
text_input: (unnamed) [#select >> nth=0] (app frame)
text_input: (unnamed) [#select >> nth=0] (app frame)
text_input: Search Contents [role=textbox[name="Search Contents"]] (app frame)
```

## N093 — Schedule | Samsung VXT CMS — August 2026Week 34

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 4 · **Actionable:** 116 · **Interactive extracted:** 116 · **DOM nodes:** 738 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click '' → Click 'August 2026Week 34'
- **Screenshot:** [artifacts/N093_5032e201.png](artifacts/N093_5032e201.png)
- **DOM:** [artifacts/N093_5032e201.html](artifacts/N093_5032e201.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [[data-testid="icon_dropdown_left"]]
inferred_clickable: (unnamed) [[data-testid="icon_dropdown_right"]]
inferred_clickable: (unnamed) [#day_0 >> nth=0]
inferred_clickable: (unnamed) [#day_1 >> nth=0]
inferred_clickable: (unnamed) [#day_2 >> nth=0]
inferred_clickable: (unnamed) [#day_3 >> nth=0]
inferred_clickable: (unnamed) [#day_4 >> nth=0]
inferred_clickable: (unnamed) [#day_5 >> nth=0]
inferred_clickable: (unnamed) [#day_2 >> nth=0]
inferred_clickable: (unnamed) [#day_3 >> nth=0]
inferred_clickable: (unnamed) [#day_4 >> nth=0]
inferred_clickable: (unnamed) [#day_5 >> nth=0]
inferred_clickable: (unnamed) [#day_6 >> nth=0]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: 1 [#day_6 >> nth=0]
inferred_clickable: 10 [#day_1 >> nth=0]
inferred_clickable: 10 [#day_1 > span >> nth=0]
inferred_clickable: 11 [#day_2 >> nth=0]
inferred_clickable: 11 [#day_2 > span >> nth=0]
inferred_clickable: 12 [#day_3 >> nth=0]
inferred_clickable: 12 [#day_3 > span >> nth=0]
inferred_clickable: 13 [#day_4 >> nth=0]
inferred_clickable: 13 [#day_4 > span >> nth=0]
inferred_clickable: 14 [#day_5 >> nth=0]
inferred_clickable: 14 [#day_5 > span >> nth=0]
inferred_clickable: 15 [#day_6 >> nth=0]
inferred_clickable: 15 [#day_6 > span >> nth=0]
inferred_clickable: 16 [#day_0 >> nth=0]
inferred_clickable: 16 [#day_0 > span >> nth=0]
inferred_clickable: 17 [#day_1 >> nth=0]
inferred_clickable: 17 [#day_1 > span >> nth=0]
inferred_clickable: 18 [#day_2 >> nth=0]
inferred_clickable: 18 [#day_2 > span >> nth=0]
inferred_clickable: 19 [#day_3 >> nth=0]
inferred_clickable: 19 [#day_3 > span >> nth=0]
inferred_clickable: 2 [#day_0 >> nth=0]
inferred_clickable: 2 [#day_0 > span >> nth=0]
inferred_clickable: 20 [#day_4 >> nth=0]
inferred_clickable: 21 [#day_5 >> nth=0]
inferred_clickable: 21 [#day_5 > span >> nth=0]
inferred_clickable: 22 [#day_6 >> nth=0]
inferred_clickable: 22 [#day_6 > span >> nth=0]
inferred_clickable: 23 [#day_0 >> nth=0]
inferred_clickable: 23 [#day_0 > span >> nth=0]
inferred_clickable: 24 [#day_1 >> nth=0]
inferred_clickable: 24 [#day_1 > span >> nth=0]
inferred_clickable: 25 [#day_2 >> nth=0]
inferred_clickable: 25 [#day_2 > span >> nth=0]
inferred_clickable: 26 [#day_3 >> nth=0]
inferred_clickable: 26 [#day_3 > span >> nth=0]
inferred_clickable: 27 [#day_4 >> nth=0]
inferred_clickable: 27 [#day_4 > span >> nth=0]
inferred_clickable: 28 [#day_5 >> nth=0]
inferred_clickable: 28 [#day_5 > span >> nth=0]
inferred_clickable: 29 [#day_6 >> nth=0]
inferred_clickable: 29 [#day_6 > span >> nth=0]
inferred_clickable: 3 [#day_1 >> nth=0]
inferred_clickable: 3 [#day_1 > span >> nth=0]
inferred_clickable: 30 [#day_0 >> nth=0]
inferred_clickable: 30 [#day_0 > span >> nth=0]
inferred_clickable: 31 [#day_1 >> nth=0]
inferred_clickable: 31 [#day_1 > span >> nth=0]
inferred_clickable: 4 [#day_2 >> nth=0]
inferred_clickable: 4 [#day_2 > span >> nth=0]
inferred_clickable: 5 [#day_3 >> nth=0]
inferred_clickable: 5 [#day_3 > span >> nth=0]
inferred_clickable: 6 [#day_4 >> nth=0]
inferred_clickable: 6 [#day_4 > span >> nth=0]
inferred_clickable: 7 [#day_5 >> nth=0]
inferred_clickable: 8 [#day_6 >> nth=0]
inferred_clickable: 8 [#day_6 > span >> nth=0]
inferred_clickable: 9 [#day_0 >> nth=0]
inferred_clickable: 9 [#day_0 > span >> nth=0]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 33 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'div' | no_change | (self) | inert |
| Click 'div' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |
| Click 'listitem' | no_change | (self) | inert |

## N094 — Schedule | Samsung VXT CMS — span

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** page · **Depth:** 4 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 696 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click '' → Click 'span'
- **Screenshot:** [artifacts/N094_8cc75e6b.png](artifacts/N094_8cc75e6b.png)
- **DOM:** [artifacts/N094_8cc75e6b.html](artifacts/N094_8cc75e6b.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon.width_100_percent:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon.width_100_percent:nth-of-type(1) > div.tag_help_class.is_first > span > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="FcmsEditTags_add_edited_tag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 35 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Enter text. [[data-testid="FcmsEditTags_edit_new_tag"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'August 2026Week 35' | in_page_state | N095 Schedule | Samsung VXT CMS — | — |

## N095 — Schedule | Samsung VXT CMS — span — August 2026Week 35

- **URL:** https://www.samsungvx.com/schedule/create
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 119 · **Interactive extracted:** 119 · **DOM nodes:** 746 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Schedule' → Click 'New Schedule' → Click '' → Click 'span' → Click 'August 2026Week 35'
- **Screenshot:** [artifacts/N095_95dca541.png](artifacts/N095_95dca541.png)
- **DOM:** [artifacts/N095_95dca541.html](artifacts/N095_95dca541.html)

**Action elements**

```
generic_button: Add Content [[data-testid="schedule_add_content_btn"]]
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
inferred_clickable: (unnamed) [[data-testid="icon_dropdown_left"]]
inferred_clickable: (unnamed) [[data-testid="icon_dropdown_right"]]
inferred_clickable: (unnamed) [#day_0 >> nth=0]
inferred_clickable: (unnamed) [#day_1 >> nth=0]
inferred_clickable: (unnamed) [#day_2 >> nth=0]
inferred_clickable: (unnamed) [#day_3 >> nth=0]
inferred_clickable: (unnamed) [#day_4 >> nth=0]
inferred_clickable: (unnamed) [#day_5 >> nth=0]
inferred_clickable: (unnamed) [#day_2 >> nth=0]
inferred_clickable: (unnamed) [#day_3 >> nth=0]
inferred_clickable: (unnamed) [#day_4 >> nth=0]
inferred_clickable: (unnamed) [#day_5 >> nth=0]
inferred_clickable: (unnamed) [#day_6 >> nth=0]
inferred_clickable: (unnamed) [#schedule_next_week_btn]
inferred_clickable: (unnamed) [div.date_select:nth-of-type(1) > div.tag_area:nth-of-type(2) > div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon.width_100_percent:nth-of-type(1) > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="schedule_icon_addTag"]]
inferred_clickable: (unnamed) [div.visible_tag_wrapper:nth-of-type(2) > div.edit_tags_container > div.add_tag_icon.width_100_percent:nth-of-type(1) > div.tag_help_class.is_first > span > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="FcmsEditTags_add_edited_tag"]]
inferred_clickable: (unnamed) [[data-testid="schedule_month_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_week_view_btn"]]
inferred_clickable: (unnamed) [[data-testid="schedule_list_view_btn"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: 1 [#day_6 >> nth=0]
inferred_clickable: 10 [#day_1 >> nth=0]
inferred_clickable: 10 [#day_1 > span >> nth=0]
inferred_clickable: 11 [#day_2 >> nth=0]
inferred_clickable: 11 [#day_2 > span >> nth=0]
inferred_clickable: 12 [#day_3 >> nth=0]
inferred_clickable: 12 [#day_3 > span >> nth=0]
inferred_clickable: 13 [#day_4 >> nth=0]
inferred_clickable: 13 [#day_4 > span >> nth=0]
inferred_clickable: 14 [#day_5 >> nth=0]
inferred_clickable: 14 [#day_5 > span >> nth=0]
inferred_clickable: 15 [#day_6 >> nth=0]
inferred_clickable: 15 [#day_6 > span >> nth=0]
inferred_clickable: 16 [#day_0 >> nth=0]
inferred_clickable: 16 [#day_0 > span >> nth=0]
inferred_clickable: 17 [#day_1 >> nth=0]
inferred_clickable: 17 [#day_1 > span >> nth=0]
inferred_clickable: 18 [#day_2 >> nth=0]
inferred_clickable: 18 [#day_2 > span >> nth=0]
inferred_clickable: 19 [#day_3 >> nth=0]
inferred_clickable: 19 [#day_3 > span >> nth=0]
inferred_clickable: 2 [#day_0 >> nth=0]
inferred_clickable: 2 [#day_0 > span >> nth=0]
inferred_clickable: 20 [#day_4 >> nth=0]
inferred_clickable: 21 [#day_5 >> nth=0]
inferred_clickable: 21 [#day_5 > span >> nth=0]
inferred_clickable: 22 [#day_6 >> nth=0]
inferred_clickable: 22 [#day_6 > span >> nth=0]
inferred_clickable: 23 [#day_0 >> nth=0]
inferred_clickable: 23 [#day_0 > span >> nth=0]
inferred_clickable: 24 [#day_1 >> nth=0]
inferred_clickable: 24 [#day_1 > span >> nth=0]
inferred_clickable: 25 [#day_2 >> nth=0]
inferred_clickable: 25 [#day_2 > span >> nth=0]
inferred_clickable: 26 [#day_3 >> nth=0]
inferred_clickable: 26 [#day_3 > span >> nth=0]
inferred_clickable: 27 [#day_4 >> nth=0]
inferred_clickable: 27 [#day_4 > span >> nth=0]
inferred_clickable: 28 [#day_5 >> nth=0]
inferred_clickable: 28 [#day_5 > span >> nth=0]
inferred_clickable: 29 [#day_6 >> nth=0]
inferred_clickable: 29 [#day_6 > span >> nth=0]
inferred_clickable: 3 [#day_1 >> nth=0]
inferred_clickable: 3 [#day_1 > span >> nth=0]
inferred_clickable: 30 [#day_0 >> nth=0]
inferred_clickable: 30 [#day_0 > span >> nth=0]
inferred_clickable: 31 [#day_1 >> nth=0]
inferred_clickable: 31 [#day_1 > span >> nth=0]
inferred_clickable: 4 [#day_2 >> nth=0]
inferred_clickable: 4 [#day_2 > span >> nth=0]
inferred_clickable: 5 [#day_3 >> nth=0]
inferred_clickable: 5 [#day_3 > span >> nth=0]
inferred_clickable: 6 [#day_4 >> nth=0]
inferred_clickable: 6 [#day_4 > span >> nth=0]
inferred_clickable: 7 [#day_5 >> nth=0]
inferred_clickable: 8 [#day_6 >> nth=0]
inferred_clickable: 8 [#day_6 > span >> nth=0]
inferred_clickable: 9 [#day_0 >> nth=0]
inferred_clickable: 9 [#day_0 > span >> nth=0]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: August 2026Week 35 [#schedule_date_sort]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [#contents_wrap > div.contents_box > div.topbtn_wrap.schedule:nth-of-type(1) > div.schedule-type.flex_center:nth-of-type(1) > span.ellipsis.tag_help_class:nth-of-type(2)]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Rename [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
text_input: Enter text. [[data-testid="FcmsEditTags_edit_new_tag"]]
```

## N096 — Channel | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/channel/create
- **Type:** page · **Depth:** 4 · **Actionable:** 41 · **Interactive extracted:** 41 · **DOM nodes:** 371 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'New Channel' → Click 'General'
- **Screenshot:** [artifacts/N096_58180904.png](artifacts/N096_58180904.png)
- **DOM:** [artifacts/N096_58180904.html](artifacts/N096_58180904.html)

**Action elements**

```
generic_button: Add Channel [#channelDetail_addContentBtn]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"]]
generic_button: Save [#channelDetail_general_saveBtn]
generic_button: Set to Screens [#channelDetail_general_set2ScreensBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [#channelDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Settings [role=listitem[name="Settings"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'more' | no_change | (self) | inert |
| Click 'Set to Screens' | no_change | (self) | inert |
| Click 'Save' | no_change | (self) | inert |
| Click 'Add Channel' | no_change | (self) | inert |
| Click 'span' | no_change | (self) | inert |
| Click 'GeneralGeneral' | no_change | (self) | inert |
| Click 'General' | no_change | (self) | inert |
| Click 'span' | in_page_state | N097 Channel | Samsung VXT CMS —  | — |

## N097 — Channel | Samsung VXT CMS — span

- **URL:** https://www.samsungvx.com/channel/create
- **Type:** page · **Depth:** 4 · **Actionable:** 44 · **Interactive extracted:** 44 · **DOM nodes:** 464 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'New Channel' → Click 'General' → Click 'span'
- **Screenshot:** [artifacts/N097_d1c56f88.png](artifacts/N097_d1c56f88.png)
- **DOM:** [artifacts/N097_d1c56f88.html](artifacts/N097_d1c56f88.html)

**Action elements**

```
generic_button: Add Channel [#channelDetail_addContentBtn]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: more [[data-testid="channel_fcmsmoreButton_btn_more"]]
generic_button: Save [#channelDetail_general_saveBtn]
generic_button: Set to Screens [#channelDetail_general_set2ScreensBtn]
inferred_clickable: (unnamed) [[data-testid="icon_back"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="name_edit_icon"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#info_inner > div.topbtn_con:nth-of-type(1) > ul.tab_wrap.col2 > li.ga-button-action-class:nth-of-type(2) > span]
inferred_clickable: (unnamed) [#channelDetail_tagList > div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon.width_100_percent > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="icon_circleplus"]]
inferred_clickable: (unnamed) [div.tag_info_wrap.hd-border-bottom > div.edit_tags_container > div.add_tag_icon.width_100_percent > div.tag_help_class.is_first > span > span.icon_add.ga-button-action-class]
inferred_clickable: (unnamed) [[data-testid="FcmsEditTags_add_edited_tag"]]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: General [[data-testid="General"]]
inferred_clickable: GeneralGeneral [div.tab_container > div.tab_content:nth-of-type(1) > div.info_table:nth-of-type(1) > ul.info_section > li.info_txt.flex_center:nth-of-type(2) > span.chip.chip-chkbox]
inferred_clickable: Info [role=listitem[name="Info"]]
inferred_clickable: logo [#container > header > div._head_logo_1ijv6_14:nth-of-type(1)] (app frame)
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: Settings [role=listitem[name="Settings"]]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
text_input: Enter text. [[data-testid="FcmsEditTags_edit_new_tag"]]
```

## N098 — Schedule | Samsung VXT CMS

- **URL:** https://www.samsungvx.com/schedule
- **Type:** page · **Depth:** 4 · **Actionable:** 47 · **Interactive extracted:** 47 · **DOM nodes:** 404 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'div' → Click ''
- **Screenshot:** [artifacts/N098_8cbb4ac1.png](artifacts/N098_8cbb4ac1.png)
- **DOM:** [artifacts/N098_8cbb4ac1.html](artifacts/N098_8cbb4ac1.html)

**Action elements**

```
generic_button: chatbot [#startChatBtn] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_refresh"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_arrow_right"] >> nth=0] (app frame)
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_screen"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_contents"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_playlist"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_schedule"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_channel"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_badge_p"]] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_ic_apps"]] (app frame)
inferred_clickable: (unnamed) [#navbar_leftControl2] (app frame)
inferred_clickable: .st0{opacity:0.8;} [#tagAllExpand] (app frame)
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"] >> nth=0] (app frame)
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Location [#treeCategory_Location_1 > span.ellipsis.tag_help_class:nth-of-type(1)] (app frame)
inferred_clickable: Location0Loading... [role=listitem[name="Location0Loading..."]] (app frame)
inferred_clickable: logo [#header_logo] (app frame)
inferred_clickable: New Schedule [[data-testid="schedule_new_schedule_btn"]]
inferred_clickable: No tags [#treeCategory_Notags_1 > span.ga-button-action-class:nth-of-type(1)] (app frame)
inferred_clickable: No tags0 [role=listitem[name="No tags0"]] (app frame)
inferred_clickable: Notification [#notificationIconId] (app frame)
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
inferred_clickable: VXT Labs [[data-testid="dashboard_vxt_lab"]] (app frame)
```

## N099 — Samsung VXT CMS — AI StudioAI StudioGen AI

- **URL:** https://www.samsungvx.com/apps
- **Type:** dropdown · **Depth:** 4 · **Actionable:** 186 · **Interactive extracted:** 186 · **DOM nodes:** 1798 · **Visits:** 1
- **Reached by:** Click 'Playlist' → Click 'New Playlist' → Click 'Channel' → Click 'AppsN' → Click 'AI StudioAI StudioGen AI'
- **Screenshot:** [artifacts/N099_df563c55.png](artifacts/N099_df563c55.png)
- **DOM:** [artifacts/N099_df563c55.html](artifacts/N099_df563c55.html)

**Action elements**

```
disclosure: Africa [role=button[name="Africa"]]
disclosure: Asia [role=button[name="Asia"]]
disclosure: Europe [role=button[name="Europe"]]
disclosure: North America [role=button[name="North America"]]
disclosure: Oceania [role=button[name="Oceania"]]
disclosure: South America [role=button[name="South America"]]
generic_button: Buy Now [role=button[name="Buy Now"]]
generic_button: chatbot [#startChatBtn] (app frame)
generic_button: Install [role=button[name="Install"]]
inferred_clickable: (unnamed) [#header_logoImg] (app frame)
inferred_clickable: (unnamed) [[data-testid="icon_search"]]
inferred_clickable: (unnamed) [[data-testid="dashboard_vxt_lab"]] (app frame)
inferred_clickable: (unnamed) [#notificationIconId] (app frame)
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
inferred_clickable: (unnamed) [[data-testid="icon_close"]] (app frame)
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: (unnamed) [div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > img._app-logo_1wr29_1]
inferred_clickable: .st0{opacity:0.8;} [[data-testid="icon_arrow_down"]] (app frame)
inferred_clickable: AI CorpPostAI CorpPostBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(10) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: AI StudioAI Studio [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: AI StudioAI StudioGen AI [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-next:nth-of-type(2) > div > div._app-info_fjwgk_1:nth-of-type(1)]
inferred_clickable: AI Writing AssistantAI Writing AssistantBETA [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(9) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Apps [[data-testid="navbar_li_apps"]] (app frame)
inferred_clickable: Apps [#navbar_li_apps > div:nth-of-type(2)] (app frame)
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: Automation [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2)]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: BETA [[data-testid="icon_bataBadge27"] >> nth=0]
inferred_clickable: Buy Now [[data-testid="dashboard_buyplan"]] (app frame)
inferred_clickable: CalendarCalendar [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: CalendarCalendar [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: CalendarCalendar [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Channel [[data-testid="navbar_li_channel"]] (app frame)
inferred_clickable: Channel [#navbar_li_channel > div:nth-of-type(2)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace [#place_wrap > div.ellipsis._p_name_wrap_p0i4l_31:nth-of-type(1)] (app frame)
inferred_clickable: CHITNU TEAMDefault Workspace .st0{opacity:0.8;} [#place_wrap] (app frame)
inferred_clickable: Content [[data-testid="navbar_li_content"]] (app frame)
inferred_clickable: Content [#navbar_li_content > div:nth-of-type(2)] (app frame)
inferred_clickable: Data SyncData Sync [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData Sync [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Data SyncData Sync [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(3) > div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: Data SyncData SyncRegister your data sources and create the dynamic content easy and fast. [div > div > div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2)]
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
inferred_clickable: Microsoft SharePointMicrosoft SharePoint [div:nth-of-type(2) > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
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
inferred_clickable: NEW [[data-testid="icon_posLabel"] >> nth=0]
inferred_clickable: Ngine AutomotiveNgine Automotive [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Ngine Real EstateNgine Real Estate [div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Playlist [[data-testid="navbar_li_playlist"]] (app frame)
inferred_clickable: Playlist [#navbar_li_playlist > div:nth-of-type(2)] (app frame)
inferred_clickable: Productivity [div.swiper-slide.swiper-slide-active:nth-of-type(1) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(3) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(4) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(5) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Productivity [div.swiper-slide:nth-of-type(6) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-sub_fjwgk_44:nth-of-type(2) > span]
inferred_clickable: Register your data sources and create the dynamic content easy and fast. [div > div.swiper.swiper-initialized > div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(7) > div > div.fcms_simple_bar:nth-of-type(2)]
inferred_clickable: Schedule [[data-testid="navbar_li_schedule"]] (app frame)
inferred_clickable: Schedule [#navbar_li_schedule > div:nth-of-type(2)] (app frame)
inferred_clickable: Screen [[data-testid="navbar_li_screen"]] (app frame)
inferred_clickable: Screen [#navbar_li_screen > div:nth-of-type(2)] (app frame)
inferred_clickable: ShadowGenShadowGenBETASamsung VXT Canvas enables you to create the shadow effects effortlessly [div._apps-page_1cguz_1.fcms_simple_bar > div._app-box-container_1x05b_1:nth-of-type(7) > div > div > div._app-info-card_1v7dv_1 > div._app-info_fjwgk_1:nth-of-type(2)]
inferred_clickable: SmartThings ProSmartThings Pro [div.swiper-wrapper:nth-of-type(1) > div.swiper-slide:nth-of-type(8) > div > div._app-info_fjwgk_1:nth-of-type(1) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1)]
inferred_clickable: SmartThings ProSmartThings Pro [div > div > div._app-info-card_1v7dv_1:nth-of-type(3) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: SmartThingsSmartThings [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: souresh Anandsouresanand@gmail.comSettingsManualSign Outsouresh Anandsouresanand@gmail.com [[data-testid="dashboard_profile"]] (app frame)
inferred_clickable: Stingray MusicStingray Music [div > div > div._app-info-card_1v7dv_1:nth-of-type(1) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Stingray StreamsStingray Streams [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1 > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
inferred_clickable: Vistar MediaVistar Media [div > div > div._app-info-card_1v7dv_1:nth-of-type(2) > div._app-info_fjwgk_1:nth-of-type(2) > div._app-meta_fjwgk_9 > div._app-name_fjwgk_27:nth-of-type(1) >> nth=0]
text_input: Search Apps [role=textbox[name="Search Apps"]]
```

**Transitions**

| Action | Outcome | Goes to | Notes |
|---|---|---|---|
| Click 'Asia' | no_change | (self) | inert |

