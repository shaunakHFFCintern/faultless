# Event Handling Inventory

## 1. Registered Interactive Events

| Source Location | Target Event | Handler Name | Async? | Debounce? | Throttle? |
|:---|:---|:---|:---|:---|:---|
| `app/javascript/portal/portalHelpers.js:44` | `click` | `event` | False | False | False |
| `app/javascript/portal/portalHelpers.js:71` | `change` | `e` | False | False | False |
| `app/javascript/portal/portalHelpers.js:131` | `click` | `event` | False | False | False |
| `app/javascript/portal/portalThemeHelper.js:82` | `click` | `e` | False | False | False |
| `app/javascript/portal/portalThemeHelper.js:101` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/portal/components/SearchSuggestions.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/portal/components/PublicArticleSearch.vue:66` | `keydown` | `this` | False | False | False |
| `app/javascript/portal/components/PublicArticleSearch.vue:90` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/portal/components/SidebarThemeToggle.vue:58` | `change` | `this` | False | False | False |
| `app/javascript/portal/components/SidebarThemeToggle.vue:104` | `click` | `toggle` | False | False | False |
| `app/javascript/portal/components/SidebarThemeToggle.vue:122` | `click` | `select(opt.value)` | False | False | False |
| `app/javascript/portal/components/PublicSearchInput.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/portal/components/TableOfContents.vue:25` | `hashchange` | `this` | False | False | False |
| `app/javascript/widget/App.vue:260` | `message` | `e` | False | False | False |
| `app/javascript/widget/composables/useDarkMode.js:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useDarkMode.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAvailability.js:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAttachments.js:7` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAttachments.js:11` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAttachments.js:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAttachments.js:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/composables/useAttachments.js:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/ChatInputWrap.vue:78` | `keypress` | `this` | False | False | False |
| `app/javascript/widget/components/ChatInputWrap.vue:167` | `click` | `toggleEmojiPicker` | False | False | False |
| `app/javascript/widget/components/ChatInputWrap.vue:188` | `click` | `handleButtonClick` | False | False | False |
| `app/javascript/widget/components/Banner.vue:18` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/widget/components/TeamAvailability.vue:37` | `click` | `startConversation` | False | False | False |
| `app/javascript/widget/components/ReplyToChip.vue:41` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/widget/components/ReplyToChip.vue:53` | `click` | `navigateTo(replyTo.id)` | False | False | False |
| `app/javascript/widget/components/AgentMessageBubble.vue:129` | `submit` | `onFormSubmit` | False | False | False |
| `app/javascript/widget/components/UnreadMessageList.vue:61` | `click` | `closeFullView` | False | False | False |
| `app/javascript/widget/components/UnreadMessageList.vue:85` | `click` | `openConversationView` | False | False | False |
| `app/javascript/widget/components/ChatFooter.vue:139` | `click` | `startNewConversation` | False | False | False |
| `app/javascript/widget/components/ChatFooter.vue:147` | `click` | `sendTranscript` | False | False | False |
| `app/javascript/widget/components/UnreadMessage.vue:96` | `click` | `onClickMessage` | False | False | False |
| `app/javascript/widget/components/ChatHeader.vue:33` | `click` | `onBackButtonClick` | False | False | False |
| `app/javascript/widget/components/UserMessage.vue:120` | `click` | `toggleReply` | False | False | False |
| `app/javascript/widget/components/UserMessage.vue:173` | `click` | `retrySendMessage` | False | False | False |
| `app/javascript/widget/components/AgentMessage.vue:245` | `click` | `toggleReply` | False | False | False |
| `app/javascript/widget/components/ChatAttachment.vue:45` | `paste` | `this` | False | False | False |
| `app/javascript/widget/components/FooterReplyTo.vue:37` | `click` | `$emit('dismiss')` | False | False | False |
| `app/javascript/widget/components/HeaderActions.vue:92` | `click` | `resolveConversation` | False | False | False |
| `app/javascript/widget/components/HeaderActions.vue:99` | `click` | `popoutWindow` | False | False | False |
| `app/javascript/widget/components/HeaderActions.vue:108` | `click` | `closeWindow` | False | False | False |
| `app/javascript/widget/components/GroupedAvatars.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/ChatHeaderExpanded.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/ConversationWrap.vue:64` | `scroll` | `this` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:62` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:178` | `click` | `toggleCountryDropdown` | False | False | False |
| `app/javascript/widget/components/Form/PhoneInput.vue:231` | `click` | `onSelectCountry(country)` | False | False | False |
| `app/javascript/widget/components/PreChat/Form.vue:262` | `submit` | `onSubmit` | False | False | False |
| `app/javascript/widget/components/template/IntegrationCard.vue:63` | `click` | `joinTheCall` | False | False | False |
| `app/javascript/widget/components/template/IntegrationCard.vue:75` | `click` | `leaveTheRoom` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleBlock.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleBlock.vue:42` | `click` | `$emit('viewAll')` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleContainer.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleContainer.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleContainer.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleContainer.vue:68` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleListItem.vue:22` | `click` | `onClick` | False | False | False |
| `app/javascript/widget/components/layouts/ViewWithHeader.vue:80` | `scroll` | `this` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/components/Availability/AvailabilityText.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/widget/helpers/campaignTimer.js:11` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/widget/helpers/actionCable.js:141` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/superadmin_pages/views/dashboard/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/composables/useLocale.js:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/composables/useExpandableContent.js:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/composables/useExpandableContent.js:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/mixins/keyboardEventListenerMixins.js:31` | `keydown` | `keydownHandler` | False | False | False |
| `app/javascript/shared/components/GreetingsEditor.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/components/IframeLoader.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/components/IframeLoader.vue:44` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/shared/components/ResizableTextArea.vue:176` | `keyup` | `onKeyup` | True | False | False |
| `app/javascript/shared/components/ChatOption.vue:36` | `click` | `onClick` | False | False | False |
| `app/javascript/shared/components/StarRating.vue:55` | `click` | `selectRating(value)` | False | False | False |
| `app/javascript/shared/components/CardButton.vue:62` | `click` | `onClick` | False | False | False |
| `app/javascript/shared/components/CustomerSatisfaction.vue:148` | `click` | `selectRating(rating)` | False | False | False |
| `app/javascript/shared/components/ChatForm.vue:148` | `click` | `onSubmitClick` | False | False | False |
| `app/javascript/shared/components/ui/MultiselectDropdownItems.vue:104` | `click` | `() => onclick(option)` | False | False | False |
| `app/javascript/shared/components/ui/MultiselectDropdown.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/components/ui/MultiselectDropdown.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/components/ui/MultiselectDropdown.vue:133` | `click` | `onCloseDropdown` | False | False | False |
| `app/javascript/shared/components/ui/dropdown/AddLabel.vue:18` | `click` | `addLabel` | False | False | False |
| `app/javascript/shared/components/ui/label/LabelDropdown.vue:166` | `click` | `showCreateModal` | False | False | False |
| `app/javascript/shared/components/ui/label/LabelDropdownItem.vue:42` | `click` | `onClick` | False | False | False |
| `app/javascript/shared/components/emoji/EmojiPicker.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/components/emoji/EmojiPicker.vue:81` | `click` | `selectEmoji(emoji)` | False | False | False |
| `app/javascript/shared/components/charts/BarChart.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/shared/helpers/KeyboardHelpers.js:49` | `keydown` | `e` | False | False | False |
| `app/javascript/shared/helpers/BaseActionCableConnector.js:42` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/shared/helpers/BaseActionCableConnector.js:72` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/shared/helpers/specs/localStorage.spec.js:68` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationLabels.js:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationRequiredAttributes.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationRequiredAttributes.js:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationRequiredAttributes.js:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useConversationRequiredAttributes.js:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAgentsList.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAgentsList.js:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAgentsList.js:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAgentsList.js:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useWhatsappCallSession.js:79` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/useWhatsappCallSession.js:170` | `stop` | `resolve` | False | False | False |
| `app/javascript/dashboard/composables/useImageZoom.js:22` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/composables/useImageZoom.js:26` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/composables/useMacros.js:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useMacros.js:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useMacros.js:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:65` | `beforeunload` | `handleBeforeUnloadGlobal` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:66` | `pagehide` | `handlePageHideGlobal` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:225` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:226` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:227` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:228` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:275` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/composables/useCallSession.js:295` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/composables/useKeyboardEvents.js:82` | `keydown` | `keydownHandler` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDropdownPosition.js:120` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/composables/loadWithRetry.js:31` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/store.js:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/store.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/store.js:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCaptain.js:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useFontSize.js:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useFontSize.js:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useFontSize.js:123` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/composables/useLabelSuggestions.js:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useLabelSuggestions.js:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useLabelSuggestions.js:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useLabelSuggestions.js:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomationValues.js:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomationValues.js:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomationValues.js:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomationValues.js:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomationValues.js:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCopilotReply.js:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCopilotReply.js:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCopilotReply.js:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useCopilotReply.js:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useLiveRefresh.js:7` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/useAdmin.js:11` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAdmin.js:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useIntegrationHook.js:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useTranslations.js:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useTranslations.js:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useWhatsappEmbeddedSignup.js:70` | `message` | `messageHandler` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:112` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:119` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:126` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:133` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:137` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:141` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useInbox.js:143` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAccount.js:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAccount.js:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useDetectKeyboardLayout.js:39` | `keypress` | `handler` | False | False | False |
| `app/javascript/dashboard/composables/useUISettings.js:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useUISettings.js:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useUISettings.js:142` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useImpersonation.js:6` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/useAutomation.js:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/usePolicy.js:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/spec/useFacebookPageConnect.spec.js:17` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/spec/useWhatsappEmbeddedSignup.spec.js:22` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/composables/utils/useKbd.js:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useAppearanceHotKeys.js:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useAppearanceHotKeys.js:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useBulkActionsHotKeys.js:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useInboxHotKeys.js:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:158` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:159` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:163` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:165` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:167` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:195` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:211` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:215` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:237` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:259` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:281` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:302` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:323` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:330` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:340` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:365` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:369` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:375` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js:390` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/composables/commands/useGoToCommandHotKeys.js:192` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SidebarActionsHeader.vue:35` | `click` | `handleButtonClick(button)` | False | False | False |
| `app/javascript/dashboard/components-next/SidebarActionsHeader.vue:42` | `click` | `$emit('close')` | False | False | False |
| `app/javascript/dashboard/components-next/TeleportWithDirection.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CardLayout.vue:30` | `click` | `handleClick` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupHeader.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSortMenu.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSortMenu.vue:144` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/MobileSidebarLauncher.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/MobileSidebarLauncher.vue:57` | `click` | `toggleSidebar` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:117` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:127` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:135` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:144` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:157` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:196` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:225` | `blur` | `handleWindowBlur` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:226` | `mouseleave` | `handleWindowBlur` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:234` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue:272` | `click` | `hasChildren ? handleCollapsedClick() : undefined` | True | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue:122` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarUnreadBadge.vue:8` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarUnreadBadge.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogCard.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogCard.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogCard.vue:77` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenu.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenu.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenu.vue:121` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenu.vue:140` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:62` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:80` | `click` | `() => showAccountSwitcher && toggle()` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:106` | `click` | `onChangeAccount(account.id)` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue:145` | `click` | `emitNewAccount` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/provider.js:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/provider.js:67` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:93` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue:112` | `click` | `changeAvailabilityStatus(status.value)` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/ChannelLeaf.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupLeaf.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarNotificationBell.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarNotificationBell.vue:30` | `click` | `openNotificationPanel` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogButton.vue:11` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogButton.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogButton.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogButton.vue:32` | `click` | `toggleOpen()` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:121` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:221` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:225` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:252` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:259` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:267` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:275` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:314` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue:316` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue:142` | `click` | `toggleSubGroup(child.name)` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue:191` | `click` | `navigateAndClose(subChild.to)` | False | False | False |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue:214` | `click` | `navigateAndClose(child.to)` | False | False | False |
| `app/javascript/dashboard/components-next/Settings/SettingsAccordion.vue:22` | `click` | `toggle()` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:187` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:194` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue:213` | `click` | `handleFocus` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:89` | `click` | `changePage(1)` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:98` | `click` | `changePage(currentPage - 1)` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:117` | `click` | `changePage(currentPage + 1)` | False | False | False |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue:126` | `click` | `changePage(totalPages)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:151` | `click` | `toggleAssistantSwitcher` | False | False | False |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue:198` | `click` | `handleButtonClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesInput.vue:48` | `click` | `onClickAdd` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentFilter.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:156` | `click` | `startEdit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:163` | `click` | `emit('delete', id)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:174` | `click` | `needsOverlay ? toggleInstructionExpanded() : null` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:245` | `click` | `toggleEditing(false)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue:250` | `click` | `onClickUpdate` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue:110` | `click` | `emit('bulkDelete')` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.vue:41` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.vue:82` | `click` | `startEdit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.vue:89` | `click` | `emit('delete', id)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentFiltersBar.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentFiltersBar.vue:127` | `click` | `toggleMenu(menu.key)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:119` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue:125` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.vue:91` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantPlayground.vue:41` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantPlayground.vue:105` | `click` | `resetConversation` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantPlayground.vue:129` | `click` | `sendMessage` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/MessageList.vue:48` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:102` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:112` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:145` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:147` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:152` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue:193` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ToolsDropdown.vue:21` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ToolsDropdown.vue:48` | `click` | `onItemClick(idx)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantCard.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantCard.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantCard.vue:94` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesDialog.vue:57` | `click` | `togglePopover(!showPopover)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesDialog.vue:75` | `click` | `onClickCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesDialog.vue:77` | `click` | `onClickAdd` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue:102` | `click` | `handleBulkSync` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:153` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue:260` | `click` | `handleDocumentableClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/SuggestedRules.vue:43` | `click` | `onAddClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/SuggestedRules.vue:52` | `click` | `onClickClose` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:86` | `click` | `togglePopover(!showPopover)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:145` | `click` | `onClickCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue:150` | `click` | `onClickAdd` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/DeleteDialog.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/Paywall.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/Paywall.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/BulkDeleteDialog.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/CreateAssistantDialog.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/CreateAssistantDialog.vue:92` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/AssistantForm.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/AssistantForm.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/AssistantForm.vue:102` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/AssistantForm.vue:173` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantBasicSettingsForm.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantBasicSettingsForm.vue:91` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantBasicSettingsForm.vue:154` | `click` | `handleBasicInfoUpdate` | True | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantControlItems.vue:23` | `click` | `onClick(controlItem.routeName)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantControlItems.vue:35` | `click` | `onClick(controlItem.routeName)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantSystemSettingsForm.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantSystemSettingsForm.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantSystemSettingsForm.vue:94` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantSystemSettingsForm.vue:157` | `click` | `handleSystemMessagesUpdate` | True | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxForm.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxForm.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxForm.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxForm.vue:104` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxDialog.vue:60` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/ResponseForm.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/ResponseForm.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/ResponseForm.vue:85` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/ResponseForm.vue:120` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/LimitBanner.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/CreateResponseDialog.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/CreateResponseDialog.vue:87` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/switcher/AssistantSwitcher.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/switcher/AssistantSwitcher.vue:114` | `click` | `openCreateAssistantDialog` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/switcher/AssistantSwitcher.vue:128` | `click` | `handleAssistantChange(assistant)` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/RelatedResponses.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/RelatedResponses.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:168` | `change` | `handleFileChange` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:175` | `click` | `openFileDialog` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue:224` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/CreateDocumentDialog.vue:61` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/LimitBanner.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolCard.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolCard.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolCard.vue:93` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/ParamRow.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/ParamRow.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/ParamRow.vue:51` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:51` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:104` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:122` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:157` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:263` | `click` | `addParam` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:295` | `click` | `handleTest` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue:332` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/AuthConfig.vue:21` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CreateCustomToolDialog.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CreateCustomToolDialog.vue:82` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/CustomToolsPageEmptyState.vue:37` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/DocumentPageEmptyState.vue:52` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/ResponsePageEmptyState.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/ResponsePageEmptyState.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/ResponsePageEmptyState.vue:83` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/ResponsePageEmptyState.vue:90` | `click` | `onClearFilters` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/AssistantPageEmptyState.vue:48` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/InboxPageEmptyState.vue:34` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/Guardrails.vue:17` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/ResponseGuidelines.vue:18` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/Scenarios.vue:17` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:108` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:116` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:118` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue:159` | `click` | `emit('click')` | False | False | False |
| `app/javascript/dashboard/components-next/selectmenu/SelectMenu.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/selectmenu/SelectMenu.vue:57` | `click` | `toggleMenu` | False | False | False |
| `app/javascript/dashboard/components-next/selectmenu/SelectMenu.vue:81` | `click` | `handleSelect(option.value)` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:153` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:181` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:223` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:319` | `click` | `previousSlide` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:338` | `click` | `goToSlide(index - 1)` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:345` | `click` | `nextSlide` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:362` | `click` | `shareCurrentSlide` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue:372` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue:53` | `click` | `openModal` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue:63` | `click` | `closeBanner` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/ShareModal.vue:180` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/ShareModal.vue:204` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/ShareModal.vue:221` | `click` | `downloadImage` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/ShareModal.vue:231` | `click` | `shareImage` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/slides/BusiestDaySlide.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/slides/ConversationsSlide.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/slides/ConversationsSlide.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/slides/PersonalitySlide.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/year-in-review/slides/PersonalitySlide.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue:76` | `click` | `useCopilotResponse` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:104` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:118` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue:132` | `click` | `handleSidebarAction` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingGroup.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingGroup.vue:16` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingGroup.vue:30` | `click` | `isExpanded = !isExpanded` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/Copilot.story.vue:37` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/ToggleCopilotAssistant.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/ToggleCopilotAssistant.vue:44` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/ToggleCopilotAssistant.vue:53` | `click` | `() => emit('setAssistant', assistant)` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotEmptyState.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotEmptyState.vue:100` | `click` | `handleSuggestion(prompt)` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotLauncher.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotLauncher.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/copilot/CopilotLauncher.vue:65` | `click` | `toggleSidebar` | False | False | False |
| `app/javascript/dashboard/components-next/input/ChoiceToggle.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/input/ChoiceToggle.vue:39` | `change` | `handleSelect(option.value)` | False | False | False |
| `app/javascript/dashboard/components-next/input/DurationInput.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/input/DurationInput.vue:60` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/input/Input.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/input/Input.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/input/Input.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/input/Input.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Accordion/Accordion.vue:15` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Accordion/Accordion.vue:27` | `click` | `toggleAccordion` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:226` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue:243` | `click` | `onPickInbox(inbox)` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsLoadMore.vue:25` | `click` | `emit('loadMore')` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:88` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:101` | `click` | `toggleBlock` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue:172` | `click` | `handleConversationSidebarToggle` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue:104` | `click` | `handleFileClick` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue:112` | `click` | `handleFileClick` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue:120` | `click` | `handleRemoveFile` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue:131` | `change` | `handleFileChange` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactExportDialog.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactExportDialog.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactExportDialog.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/DeleteSegmentDialog.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:160` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:164` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:173` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:195` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue:258` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/CreateSegmentDialog.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/CreateNewContactDialog.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/CreateNewContactDialog.vue:61` | `click` | `closeDialog` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/EmptyState/ContactEmptyState.vue:58` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactDeleteSection.vue:38` | `click` | `toggleDeleteSection()` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactDeleteSection.vue:57` | `click` | `openConfirmDeleteContactDialog()` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:141` | `change` | `event => toggleSelect(event.target.checked)` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:190` | `click` | `onClickViewDetails` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:202` | `click` | `onClickExpand` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue:229` | `click` | `handleUpdateContact` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:175` | `click` | `updateContact` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue:193` | `click` | `openConfirmDeleteContactDialog` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactsList.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactsList.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactListHeaderWrapper.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactListHeaderWrapper.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactHeader.vue:74` | `click` | `emit('filter')` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactHeader.vue:94` | `click` | `emit('createSegment')` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactHeader.vue:102` | `click` | `emit('deleteSegment')` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactMoreActions.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactMoreActions.vue:67` | `click` | `showActionsDropdown = !showActionsDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactsActiveFiltersPreview.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactsActiveFiltersPreview.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactsActiveFiltersPreview.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactsActiveFiltersPreview.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactSortMenu.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactSortMenu.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactSortMenu.vue:103` | `click` | `isMenuOpen = !isMenuOpen` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactLabels/ContactLabels.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactLabels/ContactLabels.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactLabels/ContactLabels.vue:93` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMedia.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMedia.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMedia.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMedia.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactHistory.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactHistory.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactHistory.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMerge.vue:44` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMerge.vue:46` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMerge.vue:134` | `click` | `resetState` | False | True | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMerge.vue:141` | `click` | `onMergeContacts` | False | True | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactNotes.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactNotes.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactNotes.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactNotes.vue:75` | `click` | `onAdd(state.message)` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributeItem.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/components/ContactNoteItem.vue:81` | `click` | `handleDelete` | False | False | False |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/components/ContactNoteItem.vue:98` | `click` | `() => toggleExpanded()` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIcon.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIcon.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIcon.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/ColorPalette.vue:19` | `click` | `selectedColor = color.value` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:114` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:126` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:163` | `click` | `activeTab = tab.id` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:177` | `click` | `emit('remove')` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:211` | `click` | `toggleIconStyle` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:234` | `click` | `selectIcon(icon)` | False | False | False |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue:293` | `click` | `selectEmoji(emoji)` | False | False | False |
| `app/javascript/dashboard/components-next/radioCard/RadioCard.vue:78` | `change` | `handleChange` | False | False | False |
| `app/javascript/dashboard/components-next/checkbox/Checkbox.vue:34` | `change` | `handleChange` | False | False | False |
| `app/javascript/dashboard/components-next/label/AddLabel.vue:26` | `click` | `showDropdown = !showDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/label/Label.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/label/Label.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/label/Label.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/label/Label.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/label/Label.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/label/LabelItem.vue:53` | `click` | `handleRemoveLabel` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.story.vue:25` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:123` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:193` | `click` | `handleAction(item)` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue:249` | `click` | `handleAction(item)` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownPrimitives.story.vue:57` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownBody.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownBody.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownItem.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownItem.vue:53` | `click` | `triggerClick` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/HelpCenterLayout.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/HelpCenterLayout.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/HelpCenterLayout.vue:82` | `click` | `togglePortalSwitcher` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.vue:88` | `click` | `handleClick(slug)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.vue:118` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Portal/PortalEmptyState.vue:65` | `click` | `openDialog` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Article/ArticleEmptyState.vue:52` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.vue:128` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:122` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:133` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:142` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:146` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:150` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:175` | `change` | `emit('toggleSelect', id)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:181` | `click` | `handleClick(id)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue:202` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditor.vue:39` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditor.vue:45` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditor.vue:62` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditor.vue:70` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue:127` | `click` | `onClickGoBack` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue:142` | `click` | `previewArticle` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue:156` | `click` | `updateArticleStatus({ value: ARTICLE_STATUSES.PUBLISHED })` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorProperties.vue:36` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorProperties.vue:71` | `click` | `emit('close')` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:108` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:126` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:182` | `click` | `openAgentsList = !openAgentsList` | True | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:211` | `click` | `openCategoryList = !openCategoryList` | True | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue:252` | `click` | `openProperties = !openProperties` | True | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue:140` | `click` | `openConfirmDeletePortalDialog` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:111` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:116` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:118` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:122` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:254` | `click` | `removePlatform(platform.key)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:271` | `click` | `showAddMenu = !showAddMenu` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue:286` | `click` | `handleSave` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:108` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:137` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue:343` | `click` | `handleUpdatePortal` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/DNSConfigurationDialog.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/DNSConfigurationDialog.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/DNSConfigurationDialog.vue:90` | `click` | `onClose` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/DNSConfigurationDialog.vue:122` | `click` | `handleCopy` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:215` | `click` | `addCustomDomainDialogRef.dialogRef.open()` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:225` | `click` | `onClickRefreshSSLStatus` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue:236` | `click` | `addCustomDomainDialogRef.dialogRef.open()` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/AddCustomDomainDialog.vue:46` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryList.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryList.vue:50` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryList.vue:80` | `click` | `handleClick(element.slug)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue:147` | `click` | `openCategoryArticles` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:89` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:146` | `click` | `isLocaleMenuOpen = !isLocaleMenuOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:169` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:187` | `click` | `isCreateCategoryDialogOpen = !isCreateCategoryDialogOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:206` | `click` | `isEditCategoryDialogOpen = !isEditCategoryDialogOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue:221` | `click` | `emit('newArticle')` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryDialog.vue:108` | `submit` | `handleCategory` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:142` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:151` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:225` | `click` | `isEmojiPickerOpen = !isEmojiPickerOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:281` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue:292` | `click` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocaleContentDialog.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue:68` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue:74` | `click` | `openAddLocaleDialog` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleList.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleList.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleList.vue:189` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:154` | `click` | `isLocaleMenuOpen = !isLocaleMenuOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:174` | `click` | `isCategoryMenuOpen = !isCategoryMenuOpen` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue:201` | `click` | `handleNewArticle` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue:115` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:81` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:90` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:91` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:93` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:100` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:108` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:112` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:114` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:116` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:120` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:139` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:151` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:155` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:159` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:172` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:173` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:243` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:295` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:372` | `click` | `clearSelection` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:384` | `click` | `bulkUpdateStatus('published')` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:393` | `click` | `bulkUpdateStatus('draft')` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:402` | `click` | `bulkUpdateStatus('archived')` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:417` | `click` | `isCategoryMenuOpen = !isCategoryMenuOpen` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:436` | `click` | `openTranslateDialog` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:445` | `click` | `confirmBulkDelete` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue:470` | `click` | `navigateToNewArticlePage` | False | True | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:105` | `click` | `redirectToPortalHomePage` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:116` | `click` | `onClickPreviewPortal` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:129` | `click` | `openCreatePortalDialog` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue:143` | `click` | `handlePortalChange(portal)` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/CreatePortalDialog.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/CreatePortalDialog.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/CreatePortalDialog.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/CreatePortalDialog.vue:59` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/tabbar/TabBar.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/tabbar/TabBar.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/tabbar/TabBar.vue:47` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/tabbar/TabBar.vue:91` | `click` | `selectTab(index)` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageStatus.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageStatus.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageStatus.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageError.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageError.vue:54` | `click` | `emit('retry')` | False | False | False |
| `app/javascript/dashboard/components-next/message/provider.js:121` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/TranslationToggle.vue:13` | `click` | `$emit('toggle')` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue:125` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/MessageList.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:149` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:153` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:162` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:202` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:236` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:246` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:256` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:265` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:280` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:286` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:293` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:356` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:360` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:364` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:368` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:377` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:406` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:458` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:498` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/Message.vue:522` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/File.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/File.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/File.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Video.vue:23` | `click` | `showGallery = true` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:67` | `timeupdate` | `onTimeUpdate` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:181` | `click` | `playOrPause` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:204` | `click` | `changePlaybackSpeed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:212` | `click` | `toggleMute` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:219` | `click` | `downloadAudio` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue:233` | `click` | `isTranscriptExpanded = !isTranscriptExpanded` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/chips/Image.vue:28` | `click` | `showGallery = true` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/InstagramBubbles.story.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/InstagramBubbles.story.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/InstagramBubbles.story.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/InstagramBubbles.story.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:108` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:121` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:150` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:158` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:170` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue:184` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/BaseAttachment.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/BaseAttachment.vue:74` | `click` | `action.onClick` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/File.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/File.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/File.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Activity.vue:9` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue:109` | `click` | `scrollToMessage` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Video.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Video.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Video.vue:33` | `click` | `showGallery = true` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Audio.vue:9` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Unsupported.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Embed.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Image.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Image.vue:55` | `click` | `showGallery = true` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Fallback.vue:9` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Fallback.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Fallback.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Dyte.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Dyte.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Dyte.vue:64` | `click` | `leaveTheRoom` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Form.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:115` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:119` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:126` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:131` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:138` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:144` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:158` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:187` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:196` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:209` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:211` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:223` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:253` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:349` | `click` | `handleCallBack` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue:361` | `click` | `handleJoinCall` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/InstagramStory.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/InstagramStory.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/InstagramStory.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Text/Index.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Text/Index.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Text/Index.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Text/FormattedContent.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:140` | `click` | `isExpanded = true` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue:180` | `click` | `showQuotedMessage = !showQuotedMessage` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:8` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/ComposeConversation.vue:74` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/NewConversation/ComposeConversation.vue:78` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/NewConversation/ComposeConversation.vue:82` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/NewConversation/ComposeConversation.vue:204` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsAppOptions.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsAppOptions.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsAppOptions.vue:105` | `click` | `handleTemplateClick(template)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue:112` | `click` | `toggleBccInput` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/AttachmentPreviews.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/AttachmentPreviews.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/AttachmentPreviews.vue:61` | `click` | `removeAttachment(attachment.resource.id)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/AttachmentPreviews.vue:83` | `click` | `removeAttachment(attachment.resource.id)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:101` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:109` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:117` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:118` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:119` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:120` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:123` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:146` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:150` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:159` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:337` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:345` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue:435` | `submit` | `onSubmitCopilotReply` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:108` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:140` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:217` | `click` | `isEmojiPickerOpen = !isEmojiPickerOpen` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:254` | `click` | `toggleMessageSignature` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:265` | `click` | `emit('discard')` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue:274` | `click` | `emit('sendMessage')` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/InboxSelector.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/InboxSelector.vue:71` | `click` | `emit('updateInbox', null)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/InboxSelector.vue:88` | `click` | `emit('toggleDropdown', !showInboxesDropdown)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateSelector.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateSelector.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateSelector.vue:109` | `click` | `handleTemplateClick(template)` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContactSelector.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContactSelector.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContactSelector.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContactSelector.vue:133` | `click` | `emit('clearSelectedContact')` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/MessageEditor.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/MessageEditor.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateForm.vue:41` | `click` | `goBack` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateForm.vue:47` | `click` | `sendMessage` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsappTemplate.vue:45` | `click` | `goBack` | False | False | False |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsappTemplate.vue:55` | `click` | `sendMessage` | False | False | False |
| `app/javascript/dashboard/components-next/changelog-card/GroupedStackedChangelogCard.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/changelog-card/GroupedStackedChangelogCard.story.vue:66` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/changelog-card/GroupedStackedChangelogCard.story.vue:106` | `click` | `resetDemo` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:100` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:134` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue:147` | `click` | `removeTag(tag.value)` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue:83` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue:116` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:138` | `click` | `toggleEditValue(!isEditingView)` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:168` | `click` | `toggleEditValue(true)` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:176` | `click` | `emit('delete')` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue:201` | `click` | `handleInputUpdate` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/ListAttribute.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/ListAttribute.vue:61` | `click` | `toggleAttributeListDropdown(!props.isEditingView)` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/ListAttribute.vue:88` | `click` | `toggleAttributeListDropdown()` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/ListAttribute.vue:96` | `click` | `emit('delete')` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/AttributeBadge.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:93` | `click` | `toggleEditValue(!isEditingView)` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:108` | `click` | `toggleEditValue(true)` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:116` | `click` | `emit('delete')` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue:144` | `click` | `handleInputUpdate` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/CheckboxAttribute.vue:35` | `change` | `handleChange` | False | False | False |
| `app/javascript/dashboard/components-next/CustomAttributes/CheckboxAttribute.vue:43` | `click` | `emit('delete')` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue:32` | `click` | `openAlertDialog` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue:42` | `click` | `openEditDialog` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue:71` | `click` | `openConfirmDialog` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue:86` | `click` | `openConfirmDialogWithCustomFooter` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue:94` | `click` | `onConfirm()` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/dialog/Dialog.vue:160` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components-next/popover/Popover.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/popover/Popover.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/popover/Popover.vue:65` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/popover/Popover.vue:93` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/template-preview/QuickReplyTemplate.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/template-preview/TemplatePreview.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/template-preview/TemplatePreview.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/template-preview/MediaTemplate.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/template-preview/MediaTemplate.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue:173` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue:114` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue:123` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:136` | `click` | `$emit('dismiss')` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:180` | `click` | `$emit('toggleMute')` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:190` | `click` | `$emit('accept')` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:203` | `click` | `isOngoing ? $emit('end') : $emit('reject')` | False | False | False |
| `app/javascript/dashboard/components-next/call/CallCard.vue:216` | `click` | `$emit('goToConversation')` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:74` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:186` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:217` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue:223` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue:86` | `click` | `handleEdit` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue:89` | `click` | `handleDelete` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AgentCapacityPolicyCard/AgentCapacityPolicyCard.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AgentCapacityPolicyCard/AgentCapacityPolicyCard.vue:75` | `click` | `handleEdit` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AgentCapacityPolicyCard/AgentCapacityPolicyCard.vue:78` | `click` | `handleDelete` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/CardPopover.vue:56` | `click` | `handleButtonClick()` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/InboxCapacityLimits.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/InboxCapacityLimits.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/InboxCapacityLimits.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/InboxCapacityLimits.vue:172` | `click` | `handleRemoveLimit(limit.id)` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/ExclusionRules.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/ExclusionRules.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/DataTable.vue:57` | `click` | `handleNavigate(item)` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/DataTable.vue:99` | `click` | `handleDelete(item.id)` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/BaseInfo.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/BaseInfo.vue:63` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/FairDistribution.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue:98` | `click` | `togglePopover(!showPopover)` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue:128` | `click` | `handleAdd(item)` | False | False | False |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentCard/AssignmentCard.vue:20` | `click` | `handleClick` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.story.vue:23` | `click` | `incrementCount` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.story.vue:36` | `click` | `incrementCount` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.vue:42` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/button/ConfirmButton.vue:64` | `click` | `handleClick` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:197` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:209` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:210` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:212` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:223` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/button/Button.vue:232` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/table/BaseTable.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/table/BaseTable.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:115` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:128` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:142` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:152` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:156` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:190` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:224` | `click` | `handleDismiss` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:285` | `click` | `handleUploadAvatar` | False | False | False |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue:298` | `change` | `handleImageUpload` | False | False | False |
| `app/javascript/dashboard/components-next/colorpicker/ColorPicker.vue:44` | `click` | `toggleColorPicker` | False | False | False |
| `app/javascript/dashboard/components-next/switch/Switch.story.vue:45` | `change` | `onChange` | False | False | False |
| `app/javascript/dashboard/components-next/switch/Switch.vue:26` | `click` | `updateValue` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:108` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:140` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:147` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue:190` | `click` | `toggleCountryDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlight.vue:78` | `click` | `openLink(videoUrl)` | False | False | False |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlight.vue:89` | `click` | `openLink(learnMoreUrl)` | False | False | False |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlightPopover.vue:42` | `click` | `togglePopup(!isPopupVisible)` | False | False | False |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlightPopover.vue:106` | `click` | `openLink(videoUrl)` | False | False | False |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlightPopover.vue:118` | `click` | `openLink(learnMoreUrl)` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignLayout.vue:44` | `click` | `handleButtonClick` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:133` | `click` | `emit('edit')` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue:140` | `click` | `emit('delete')` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/LiveChatCampaignDetails.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/LiveChatCampaignDetails.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue:178` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignDialog.vue:47` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:165` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue:255` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignDialog.vue:47` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignDialog.vue:50` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:104` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:184` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:194` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue:310` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/EditLiveChatCampaignDialog.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/EditLiveChatCampaignDialog.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/EditLiveChatCampaignDialog.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/EditLiveChatCampaignDialog.vue:71` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.story.vue:9` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:49` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:65` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:72` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:76` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:91` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:96` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:107` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue:166` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.vue:60` | `click` | `emit('openFilter')` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.vue:99` | `click` | `emit('openFilter')` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.vue:110` | `click` | `emit('clearFilters')` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.story.vue:63` | `click` | `addFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConditionRow.story.vue:64` | `click` | `saveFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/provider.js:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/provider.js:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue:149` | `click` | `addFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue:153` | `click` | `resetFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue:162` | `click` | `updateSavedSegment` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue:166` | `click` | `validateAndSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:115` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/operators.js:125` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue:150` | `click` | `addFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue:154` | `click` | `resetFilter` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue:163` | `click` | `updateSavedCustomViews` | False | False | False |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue:167` | `click` | `validateAndSubmit` | False | False | False |
| `app/javascript/dashboard/components-next/filter/contactProvider.js:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/contactProvider.js:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue:132` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue:141` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue:173` | `click` | `toggleSelected(option)` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue:84` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue:106` | `click` | `updateSelected(option.value)` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:99` | `click` | `toggle` | True | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:122` | `click` | `toggle` | True | False | False |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue:136` | `click` | `toggleOption(option)` | True | False | False |
| `app/javascript/dashboard/components-next/breadcrumb/Breadcrumb.vue:45` | `click` | `onClick(item, index)` | False | False | False |
| `app/javascript/dashboard/components-next/icon/provider.js:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/icon/provider.js:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/icon/ChannelIcon.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/icon/ChannelIcon.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/icon/FileIcon.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/AttributeListItem.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/AttributeListItem.vue:83` | `click` | `emit('edit', attribute)` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/AttributeListItem.vue:90` | `click` | `emit('delete', attribute)` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:127` | `click` | `handleClick` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue:145` | `click` | `handleAddAttributesClick` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationResolveAttributesModal.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationResolveAttributesModal.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationResolveAttributesModal.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationResolveAttributesModal.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributeItem.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyCreateDialog.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyCreateDialog.vue:105` | `click` | `closeDialog` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesDetailsLayout.vue:45` | `click` | `emit('back')` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesDetailsLayout.vue:98` | `click` | `toggleSidebar` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanySelector.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanySelector.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:70` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue:198` | `click` | `handleUpdateCompany` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/ConfirmCompanyDeleteDialog.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributeItem.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:63` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:64` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:65` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:66` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:69` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:89` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:104` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:114` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:118` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:122` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:126` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:260` | `click` | `emit('cancelContactSelection')` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:267` | `click` | `emit('confirmContactSelection')` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue:305` | `click` | `openContact(contact.id)` | False | True | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyNotesSidebar.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyNotesSidebar.vue:74` | `click` | `openContact(note.contact.id)` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyHistorySidebar.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanyMoreActions.vue:36` | `click` | `showActionsDropdown = !showActionsDropdown` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanySortMenu.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanySortMenu.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanySortMenu.vue:93` | `click` | `isMenuOpen = !isMenuOpen` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue:42` | `click` | `onClickViewDetails` | False | False | False |
| `app/javascript/dashboard/components-next/Editor/Editor.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Editor/Editor.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Editor/Editor.vue:68` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/banner/Banner.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/banner/Banner.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/banner/Banner.vue:69` | `click` | `triggerAction` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue:167` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue:108` | `click` | `showAll = !showAll` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue:118` | `click` | `onActivate(attachment)` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:177` | `click` | `showAll = !showAll` | False | False | False |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue:187` | `click` | `onTileActivate(attachment, index)` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue:72` | `click` | `handleConversationSidebarToggle` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue:86` | `click` | `handleCopilotSidebarToggle` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue:41` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue:58` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue:80` | `click` | `$emit('click', $event)` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/UnreadBadge.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.story.vue:334` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.story.vue:348` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.story.vue:362` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.story.vue:367` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreview.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreview.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreview.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue:91` | `click` | `onCardClick` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:50` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue:67` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreviewWithMeta.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreviewWithMeta.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreviewWithMeta.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreviewWithMeta.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:29` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:41` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:83` | `Reactive Hook` | `watch` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:85` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:91` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:96` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:108` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:119` | `Reactive Hook` | `computed` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue:171` | `click` | `onShowLabels` | False | False | True |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardAvatar.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardPriorityIcon.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardPriorityIcon.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabels.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabels.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardStatusIcon.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationList.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationList.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/policy.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:66` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:128` | `click` | `refreshPage` | False | False | False |
| `app/javascript/dashboard/components/NetworkNotification.vue:137` | `click` | `closeNotification` | False | False | False |
| `app/javascript/dashboard/components/Code.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/Code.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/Code.vue:88` | `click` | `onCopy` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:139` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:143` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:157` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:161` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:165` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:169` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:174` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:178` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:190` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:197` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:222` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:229` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:249` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:262` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:269` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:320` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:359` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:367` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:376` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:852` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:854` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:855` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:858` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:859` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:862` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:863` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:867` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:874` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:878` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ChatList.vue:994` | `submit` | `handleResolveWithAttributes` | True | False | False |
| `app/javascript/dashboard/components/CustomAttribute.vue:215` | `change` | `onUpdate` | False | False | False |
| `app/javascript/dashboard/components/CustomAttribute.vue:239` | `click` | `onDelete` | False | False | False |
| `app/javascript/dashboard/components/CustomAttribute.vue:262` | `click` | `onUpdate` | False | False | False |
| `app/javascript/dashboard/components/CustomAttribute.vue:304` | `click` | `onCopy` | False | False | False |
| `app/javascript/dashboard/components/CustomAttribute.vue:314` | `click` | `onEdit` | False | False | False |
| `app/javascript/dashboard/components/CustomBrandPolicyWrapper.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:97` | `click` | `emit('addFolders')` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:111` | `click` | `emit('resetFilters')` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:123` | `click` | `emit('filtersModal')` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:138` | `click` | `emit('deleteFolders')` | False | False | False |
| `app/javascript/dashboard/components/ChatListHeader.vue:149` | `click` | `emit('filtersModal')` | False | False | False |
| `app/javascript/dashboard/components/SnackbarContainer.vue:43` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:43` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:196` | `click` | `onCardClick` | False | False | False |
| `app/javascript/dashboard/components/ConversationItem.vue:211` | `click` | `onCardClick` | False | False | False |
| `app/javascript/dashboard/components/Modal.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/Modal.vue:95` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/components/ui/Banner.vue:106` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components/ui/Banner.vue:114` | `click` | `onClickClose` | False | False | False |
| `app/javascript/dashboard/components/ui/DateRangePicker.vue:38` | `change` | `handleChange` | False | False | False |
| `app/javascript/dashboard/components/ui/DateTimePicker.vue:45` | `change` | `handleChange` | False | False | False |
| `app/javascript/dashboard/components/ui/Label.vue:107` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components/ui/Wizard.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/Wizard.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/TimeAgo.vue:101` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components/ui/ContextMenu.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/ContextMenu.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/Tabs.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/Tabs.vue:57` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/Tabs.vue:75` | `click` | `onScrollClick('left')` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/Tabs.vue:91` | `click` | `onScrollClick('right')` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/TabsItem.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/TabsItem.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/Tabs/TabsItem.vue:57` | `click` | `onTabClick` | False | False | False |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownList.vue:54` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownList.vue:59` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownList.vue:68` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownList.vue:74` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownSearch.vue:47` | `click` | `emit('remove')` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:117` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:176` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue:451` | `change` | `emitDateRange` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue:63` | `click` | `openDatePicker` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue:88` | `click` | `emit('navigateMonth', 'prev')` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue:99` | `click` | `emit('navigateMonth', 'next')` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarFooter.vue:22` | `click` | `onClickClear` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarFooter.vue:27` | `click` | `onClickApply` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarDateInput.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarDateInput.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarDateRange.vue:35` | `click` | `setDateRange(range)` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarYear.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarYear.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarYear.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarYear.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarWeek.vue:156` | `click` | `emitSelectDate(day)` | False | False | False |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarMonth.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:187` | `click` | `onCmdResolveConversation` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:197` | `click` | `onCmdOpenConversation` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:206` | `click` | `onCmdOpenConversation` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:218` | `click` | `openDropdown` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:236` | `click` | `() => openSnoozeModal()` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:248` | `click` | `() => toggleStatus(wootConstants.STATUS_TYPE.PENDING)` | True | False | False |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue:255` | `submit` | `handleResolveWithAttributes` | True | False | False |
| `app/javascript/dashboard/components/app/StatusBanner.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/copilot/CopilotContainer.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/copilot/CopilotContainer.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/copilot/CopilotContainer.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/copilot/CopilotContainer.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:189` | `click` | `verificationMethod = method` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:272` | `click` | `handleTryAnotherMethod` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:282` | `click` | `() => emit('cancel')` | False | False | False |
| `app/javascript/dashboard/components/auth/MfaVerification.vue:300` | `click` | `helpModalRef?.open()` | False | False | False |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue:47` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue:89` | `click` | `handleRevokeAll` | False | False | False |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue:120` | `click` | `handleRevoke(session)` | False | False | False |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue:136` | `click` | `() => emit('cancel')` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:131` | `click` | `table.setPageIndex(0)` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:140` | `click` | `table.previousPage()` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:149` | `click` | `table.setPageIndex(page - 1)` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:165` | `click` | `table.nextPage()` | False | False | False |
| `app/javascript/dashboard/components/table/Pagination.vue:174` | `click` | `table.setPageIndex(table.getPageCount() - 1)` | False | False | False |
| `app/javascript/dashboard/components/table/Table.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Table.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/table/Table.vue:45` | `click` | `header.column.getCanSort() && header.column.toggleSorting()` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue:115` | `click` | `onItemClick` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooter.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooter.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooter.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooter.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/AttachmentsPreview.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/AttachmentsPreview.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/AttachmentsPreview.vue:83` | `click` | `onRemoveAttachment(index)` | False | False | False |
| `app/javascript/dashboard/components/widgets/ThumbnailGroup.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ThumbnailGroup.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/AutomationFileInput.vue:57` | `change` | `onChangeFile` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:61` | `click` | `onFirstPage` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:73` | `click` | `onPrevPage` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:93` | `click` | `onNextPage` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue:105` | `click` | `onLastPage` | False | False | False |
| `app/javascript/dashboard/components/widgets/TableHeaderCell.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ShowMore.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ShowMore.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/AutomationActionInput.vue:180` | `click` | `removeAction` | False | False | False |
| `app/javascript/dashboard/components/widgets/VideoCallButton.vue:69` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChatTypeTabs.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/ChatTypeTabs.vue:52` | `change` | `onTabChange` | False | False | False |
| `app/javascript/dashboard/components/widgets/forms/PhoneInput.vue:246` | `click` | `onSelectCountry(country)` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:288` | `click` | `toggleEmojiPicker` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:322` | `click` | `toggleAudioRecorder` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:331` | `click` | `toggleAudioRecorderPlayPause` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:340` | `click` | `toggleMessageSignature` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:350` | `click` | `$emit('toggleQuotedReply')` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:359` | `click` | `$emit('selectWhatsappTemplate')` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:368` | `click` | `$emit('selectContentTemplate')` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:396` | `click` | `toggleInsertArticle` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue:407` | `click` | `onSend` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotReplyBottomPanel.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotReplyBottomPanel.vue:40` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotReplyBottomPanel.vue:48` | `click` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyTopPanel.vue:182` | `click` | `toggleCopilotMenu` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyTopPanel.vue:202` | `click` | `$emit('toggleEditorSize')` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:130` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:134` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:147` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:210` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:234` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:238` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:279` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:318` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:333` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:336` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:339` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:342` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:598` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:782` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:783` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:791` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:792` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:802` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:803` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:809` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:810` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:814` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:815` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:834` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue:917` | `change` | `onFileChange` | True | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:118` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:153` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:169` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:210` | `click` | `handleMenuItemClick(item)` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:237` | `click` | `handleSubMenuItemClick(item, subItem)` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue:255` | `click` | `handleMenuItemClick(item)` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/keyboardEmojiSelector.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/EditorModeToggle.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/EditorModeToggle.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/EditorModeToggle.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/EditorModeToggle.vue:77` | `click` | `$emit('toggleMode')` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:131` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:135` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:171` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:172` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:180` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:181` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue:221` | `click` | `handleSubmit` | True | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue:98` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue:109` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue:144` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue:178` | `click` | `onItemClick(index)` | False | False | False |
| `app/javascript/dashboard/components/widgets/WootWriter/FullEditor.vue:477` | `change` | `onFileChange` | False | False | False |
| `app/javascript/dashboard/components/widgets/mentions/MentionBox.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/mentions/MentionBox.vue:48` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/mentions/MentionBox.vue:57` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/mentions/MentionBox.vue:91` | `click` | `onListItemSelection(index)` | False | False | False |
| `app/javascript/dashboard/components/widgets/DashboardApp/Frame.vue:56` | `message` | `this` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/WootKeyShortcutModal.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/WootKeyShortcutModal.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/ConfirmationModal.vue:60` | `click` | `cancel` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/ConfirmationModal.vue:61` | `click` | `confirm` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/DeleteModal.vue:26` | `click` | `onClose` | False | False | False |
| `app/javascript/dashboard/components/widgets/modal/DeleteModal.vue:27` | `click` | `onConfirm` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/MessagesView.vue:345` | `scroll` | `this` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrdersList.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrdersList.vue:38` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/FilterItem.vue:44` | `change` | `onTabChange()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/MoreActions.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/MoreActions.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/MoreActions.vue:110` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/MessageSignatureMissingAlert.vue:22` | `click` | `openProfileSettings` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ResizableEditorWrapper.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ResizableEditorWrapper.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ResizableEditorWrapper.vue:104` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/QuotedEmailPreview.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/QuotedEmailPreview.vue:53` | `click` | `toggleExpand` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/QuotedEmailPreview.vue:61` | `click` | `emit('toggle')` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/QuotedEmailPreview.vue:72` | `click` | `toggleExpand` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBox.vue:506` | `paste` | `this` | False | True | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBox.vue:507` | `keydown` | `this` | False | True | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBox.vue:1399` | `submit` | `onSubmitCopilotReply` | True | True | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:95` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue:113` | `click` | `$emit('click', $event)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:113` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue:149` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue:152` | `click` | `copyConversationId` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyEmailHead.vue:129` | `click` | `handleAddBcc` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/OnboardingView.vue:9` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/OnboardingView.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/OnboardingView.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue:141` | `click` | `startCall` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue:99` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue:147` | `click` | `onAgentSelect(getSelectableIndex(item))` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue:111` | `change` | `onDashboardAppTabChange` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationSidebar.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ConversationSidebar.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagTools.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/TagTools.vue:40` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrderItem.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrderItem.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationCardComponents/CardLabels.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationCardComponents/CardLabels.vue:46` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationCardComponents/CardLabels.vue:90` | `click` | `onShowLabels` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/TemplatesPicker.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/TemplatesPicker.vue:90` | `click` | `refreshTemplates` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/TemplatesPicker.vue:105` | `click` | `emit('onSelect', template)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/WhatsAppTemplateReply.vue:37` | `click` | `resetTemplate` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/WhatsAppTemplateReply.vue:43` | `click` | `sendMessage` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearIssueItem.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearIssueItem.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearIssueItem.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearIssueItem.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinkIssue.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinkIssue.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinkIssue.vue:114` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssueHeader.vue:50` | `click` | `openIssue` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssueHeader.vue:54` | `click` | `unlinkIssue` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue:253` | `change` | `onChange` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssuesList.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssuesList.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssuesList.vue:75` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssuesList.vue:95` | `click` | `openCreateModal` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearSetupCTA.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearSetupCTA.vue:50` | `click` | `openLinearAccount` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateOrLinkIssue.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateOrLinkIssue.vue:65` | `change` | `onClickTabChange` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue:57` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/menuItemWithSubmenu.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/menuItemWithSubmenu.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/menuItemWithSubmenu.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:68` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:74` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:183` | `click` | `onClose` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:229` | `click` | `onZoom(0.1)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:236` | `click` | `onZoom(-0.1)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:243` | `click` | `onRotate('counter-clockwise')` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:250` | `click` | `onRotate('clockwise')` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:258` | `click` | `onClickDownload` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue:260` | `click` | `onClose` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue:75` | `click` | `toggleShowAllNRT` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/Index.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/Index.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/Index.vue:173` | `click` | `allSelected = false` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:136` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue:192` | `click` | `handleApply` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue:89` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue:151` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue:159` | `click` | `handleAssign` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkUpdateActions.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkUpdateActions.vue:87` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:122` | `click` | `handleToggleDropdown` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:185` | `click` | `handleCancel` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue:193` | `click` | `handleAssign` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesModal.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesModal.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesModal.vue:84` | `click` | `resetTemplate` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesModal.vue:90` | `click` | `sendMessage` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesPicker.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesPicker.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesPicker.vue:81` | `click` | `refreshTemplates` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesPicker.vue:99` | `click` | `emit('onSelect', template)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversation/LabelSuggestion.vue:180` | `click` | `pushOrAddLabel(label.title)` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversation/LabelSuggestion.vue:200` | `click` | `dismissSuggestions` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversation/LabelSuggestion.vue:213` | `click` | `addAllLabels` | False | False | False |
| `app/javascript/dashboard/components/widgets/conversation/conversation/LabelSuggestion.vue:226` | `click` | `dismissSuggestions` | False | False | False |
| `app/javascript/dashboard/modules/contact/ContactMergeModal.vue:29` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/modules/contact/ContactMergeModal.vue:92` | `submit` | `id => onMergeContacts(id, hide)` | False | False | False |
| `app/javascript/dashboard/modules/contact/ContactDeleteModal.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/contact/ContactDeleteModal.vue:78` | `click` | `hide` | False | False | False |
| `app/javascript/dashboard/modules/contact/ContactDeleteModal.vue:86` | `click` | `onDelete(hide)` | False | False | False |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchTabs.vue:20` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchTabs.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultSection.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultArticleItem.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultArticleItem.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultArticleItem.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultArticleItem.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:61` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:73` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:80` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:94` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:211` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue:227` | `click` | `onToggleDropdown` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/MessageContent.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/MessageContent.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/MessageContent.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:57` | `click` | `clearAllFilters` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:63` | `change` | `onFilterChange` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:78` | `change` | `onFilterChange` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:88` | `change` | `onFilterChange` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue:101` | `click` | `clearAllFilters` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:123` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:146` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:181` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:186` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:197` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:206` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:213` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:230` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:348` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:378` | `click` | `onBack` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:420` | `click` | `selectedTab = 'contacts'` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:443` | `click` | `selectedTab = 'messages'` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:466` | `click` | `selectedTab = 'conversations'` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:491` | `click` | `selectedTab = 'articles'` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchView.vue:503` | `click` | `loadMore` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/RecentSearches.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/RecentSearches.vue:87` | `click` | `onClearAll` | False | False | False |
| `app/javascript/dashboard/modules/search/components/RecentSearches.vue:100` | `click` | `onSelectSearch(search)` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationsList.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:148` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:203` | `click` | `onToggleDropdown()` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:255` | `click` | `clearCustomRange` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue:264` | `click` | `applyCustomRange` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchInboxSelector.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchInboxSelector.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchInboxSelector.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchInboxSelector.vue:113` | `click` | `onToggleDropdown` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchInput.vue:77` | `keydown` | `handler` | False | True | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:66` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/conversations/components/ReportCaptainMessageDialog.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/conversations/components/ReportCaptainMessageDialog.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/conversations/components/MessageContextMenu.vue:197` | `click` | `handleOpen` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/WidgetHead.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/WidgetFooter.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:104` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:115` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:126` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:130` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:134` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue:214` | `click` | `handleToggleWidget` | False | False | False |
| `app/javascript/dashboard/helper/Timer.js:13` | `Timer Trigger` | `setInterval` | False | False | False |
| `app/javascript/dashboard/helper/actionCable.js:161` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/helper/actionCable.js:229` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/helper/DOMHelpers.js:117` | `error` | `handleError` | False | False | False |
| `app/javascript/dashboard/helper/DOMHelpers.js:118` | `abort` | `handleError` | False | False | False |
| `app/javascript/dashboard/helper/ReconnectService.js:29` | `online` | `this` | False | False | False |
| `app/javascript/dashboard/helper/AudioAlerts/DashboardAudioNotificationHelper.js:123` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/helper/specs/DOMHelpers.spec.js:29` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/helper/specs/DOMHelpers.spec.js:77` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/Dashboard.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/Dashboard.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue:153` | `change` | `handleModelChange` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue:171` | `change` | `handleFeatureToggle` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:50` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue:100` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelSelector.vue:44` | `change` | `handleModelChange` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:81` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:94` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:128` | `change` | `toggleFeature` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue:140` | `change` | `handleModelChange` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue:175` | `click` | `openDelete(inbox)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue:683` | `change` | `onTabChange` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue:893` | `click` | `onClickShowBusinessNameInput` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue:919` | `click` | `updateInbox` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue:1230` | `click` | `updateInbox` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue:1238` | `click` | `updateInbox` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue:153` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelList.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelList.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/Settings.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/Settings.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/Settings.vue:89` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/PreChatFields.vue:30` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/PreChatFields.vue:56` | `change` | `handlePreChatFieldOptions($event, 'enabled', item)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/PreChatFields.vue:78` | `click` | `handlePreChatFieldOptions($event, 'required', item)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/VoiceConfigurationPage.vue:194` | `click` | `updateVoiceSettings` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:85` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:89` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:214` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:269` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:546` | `click` | `analyzeTemplateUtility` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:599` | `click` | `applyUtilitySuggestion` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:706` | `click` | `removeLabel(label)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue:736` | `click` | `saveSettings` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/WhatsappCallingPage.vue:196` | `click` | `updateCallingSettings` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:128` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:134` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:140` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:210` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:356` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:392` | `click` | `updateAgents` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:443` | `click` | `confirmDeletePolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:474` | `click` | `navigateToAssignmentPolicyEdit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:518` | `click` | `togglePolicyDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:543` | `click` | `navigateToCreatePolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:631` | `click` | `navigateToBilling` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:662` | `click` | `updateInbox` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:687` | `click` | `cancelDeletePolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue:693` | `click` | `deleteAssignmentPolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:206` | `click` | `syncTemplates` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:243` | `click` | `updateAllowedDomains` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:325` | `change` | `handleHmacFlag` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:372` | `click` | `handleReconfigure` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:418` | `click` | `updateWhatsAppInboxAPIKey` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue:433` | `click` | `syncTemplates` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATStarInput.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATStarInput.vue:25` | `click` | `emit('update', CSAT_DISPLAY_TYPES.STAR)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATEmojiInput.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATEmojiInput.vue:28` | `click` | `emit('update', CSAT_DISPLAY_TYPES.EMOJI)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/InputRadioGroup.vue:35` | `change` | `action({ ...item, checked: true })` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/SenderNameExamplePreview.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/ChannelName.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/ChannelName.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/BotConfiguration.vue:115` | `click` | `disconnectBot` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:143` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:147` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:153` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:155` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:187` | `click` | `handleGoToSettings` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue:285` | `click` | `handleRegisterWebhook` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/SingleSelectDropdown.vue:38` | `change` | `action(value)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Instagram.vue:74` | `click` | `requestAuthorization()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue:73` | `click` | `() => onClick(emailProvider)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/WhatsappEmbeddedSignup.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/WhatsappEmbeddedSignup.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/WhatsappEmbeddedSignup.vue:184` | `click` | `launchEmbeddedSignup` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Tiktok.vue:80` | `click` | `requestAuthorization()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Facebook.vue:154` | `click` | `startLogin()` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Voice.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Voice.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue:91` | `click` | `selectProvider(provider.key)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/EmailInboxFinish.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/EmailInboxFinish.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/OAuthChannel.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/google/Reauthorize.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue:107` | `message` | `messageHandler` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:72` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue:158` | `click` | `openAddModal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleTableBody.vue:62` | `click` | `emit('edit', customRole)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleTableBody.vue:71` | `click` | `emit('delete', customRole)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRolePaywall.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRolePaywall.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRolePaywall.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:66` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:112` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:113` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:114` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue:150` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/Index.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/Index.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/Index.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/Index.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlAttributeMap.vue:21` | `click` | `toggleExpanded` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue:183` | `change` | `toggleSaml` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlInfoSection.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlInfoSection.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlInfoSection.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlInfoSection.vue:97` | `click` | `handleCopy(item.value)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlPaywall.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlPaywall.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:133` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:166` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:187` | `click` | `toggleSort` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:231` | `click` | `openEditPopup(cannedItem)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue:240` | `click` | `openDeletePopup(cannedItem)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/canned/EditCanned.vue:76` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:125` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:173` | `click` | `openEditPopup(label)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue:182` | `click` | `openDeletePopup(label)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/labels/EditLabel.vue:70` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:172` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:263` | `click` | `openEditPopup(agent)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue:273` | `click` | `openDeletePopup(agent, index)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/AddAgent.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/AddAgent.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/AddAgent.vue:127` | `change` | `v$.selectedRoleId.$touch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:104` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:112` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:175` | `change` | `v$.selectedRoleId.$touch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue:191` | `change` | `v$.agentAvailability.$touch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:119` | `click` | `openAddModal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:177` | `click` | `openEditModal(bot)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue:187` | `click` | `openDeletePopup(bot)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:107` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:286` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue:407` | `click` | `onClickClose()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:68` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Index.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Index.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue:98` | `click` | `$emit('add')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue:137` | `click` | `$emit('delete', hook)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/SingleIntegrationHooks.vue:47` | `click` | `$emit('delete', integration.hooks[0])` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/SingleIntegrationHooks.vue:60` | `click` | `$emit('add')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Shopify.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Shopify.vue:121` | `click` | `openStoreUrlDialog` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Notion.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Notion.vue:80` | `click` | `authorize` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Integration.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Integration.vue:106` | `click` | `openDeletePopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Linear.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/NewHook.vue:140` | `submit` | `submitForm` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/IntegrationItem.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/IntegrationItem.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/IntegrationItem.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/Index.vue:132` | `click` | `openCreatePopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/DashboardAppsRow.vue:45` | `click` | `$emit('edit', app)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/DashboardAppsRow.vue:55` | `click` | `$emit('delete', app)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue:87` | `click` | `fetchChannels` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue:111` | `click` | `updateIntegration` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SlackIntegrationHelpText.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/Index.vue:138` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookRow.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookRow.vue:67` | `click` | `emit('edit', webhook)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookRow.vue:77` | `click` | `emit('delete', webhook, index)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/NewWebHook.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/NewWebHook.vue:70` | `click` | `handleCopySecret` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/NewWebHook.vue:78` | `click` | `props.onClose()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/NewWebHook.vue:93` | `submit` | `onSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/EditWebHook.vue:56` | `submit` | `onSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookForm.vue:145` | `click` | `secretVisible = !secretVisible` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookForm.vue:153` | `click` | `copySecret` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:108` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:142` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:152` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue:193` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue:113` | `click` | `$emit('delete')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroForm.vue:142` | `submit` | `submit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNode.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNode.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNode.vue:94` | `click` | `$emit('deleteNode')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNodes.vue:96` | `click` | `$emit('addNewNode')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroProperties.vue:99` | `click` | `onUpdateVisibility('global')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroProperties.vue:123` | `click` | `onUpdateVisibility('personal')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroProperties.vue:159` | `click` | `$emit('submit')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:104` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue:149` | `submit` | `saveMacro` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/components/BasePaywallModal.vue:64` | `click` | `emit('upgrade')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/Index.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/Index.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/Index.vue:103` | `click` | `handleClick(item.key)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityCreatePage.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityCreatePage.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityCreatePage.vue:73` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityCreatePage.vue:83` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:251` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:261` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue:275` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:182` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:193` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue:211` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentCreatePage.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentCreatePage.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentCreatePage.vue:94` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentCreatePage.vue:103` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityIndexPage.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityIndexPage.vue:98` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityIndexPage.vue:99` | `click` | `onClickCreatePolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentIndexPage.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentIndexPage.vue:100` | `click` | `handleBreadcrumbClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentIndexPage.vue:101` | `click` | `onClickCreatePolicy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentCapacityPolicyForm.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentCapacityPolicyForm.vue:133` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/InboxLinkDialog.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/InboxLinkDialog.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/InboxLinkDialog.vue:52` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:102` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:131` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:158` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:164` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:177` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue:209` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/Index.vue:217` | `change` | `updateProfilePicture` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/Index.vue:245` | `change` | `updateFontSize` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserLanguageSelect.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserLanguageSelect.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserLanguageSelect.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MessageSignature.vue:20` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertEvent.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertEvent.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AccessToken.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AccessToken.vue:50` | `click` | `toggleMasked` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AccessToken.vue:64` | `click` | `onClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AccessToken.vue:76` | `click` | `onReset` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:67` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:127` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:203` | `click` | `copySecret` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:229` | `click` | `cancelSetup` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:235` | `click` | `verifyCode` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:288` | `click` | `downloadBackupCodes` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:296` | `click` | `copyBackupCodes` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue:317` | `click` | `completeMfaSetup` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/NotificationPreferences.vue:289` | `change` | `onRequestPermissions` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaStatusCard.vue:41` | `click` | `startSetup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/FontSize.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue:124` | `click` | `regenerateDialogRef?.open()` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue:148` | `click` | `disableDialogRef?.open()` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue:195` | `click` | `toggleDisableMethod` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue:264` | `click` | `downloadBackupCodes` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue:272` | `click` | `copyBackupCodes` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/ActiveSessions.vue:133` | `click` | `revokeSession(session)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSettingsCard.vue:43` | `click` | `navigateToMfa` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioNotifications.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioNotifications.vue:52` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioNotifications.vue:97` | `change` | `handleAudioToneChange` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioNotifications.vue:109` | `change` | `handleAudioAlertConditions` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/NotificationCheckBox.vue:28` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertTone.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertTone.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertTone.vue:90` | `click` | `playAudio` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue:174` | `click` | `openDelete(team)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:91` | `change` | `toggleSelectAll` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue:103` | `change` | `() => handleSelectAgent(agent.id)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/teams/TeamForm.vue:123` | `click` | `isIconPickerOpen = !isIconPickerOpen` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/sla/Index.vue:164` | `click` | `openAddPopup` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/sla/Index.vue:293` | `click` | `openDeletePopup(sla)` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/sla/SlaTimeInput.vue:108` | `change` | `onThresholdUnitChange` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:174` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue:209` | `click` | `openAddPopup` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleRow.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleRow.vue:71` | `click` | `$emit('edit', automation)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleRow.vue:79` | `click` | `$emit('clone', automation)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleRow.vue:88` | `click` | `$emit('delete', automation)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:84` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:112` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:114` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:154` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:161` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:168` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:179` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:183` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:187` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:275` | `change` | `onEventChange()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:341` | `click` | `appendNewCondition` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:388` | `click` | `appendNewAction` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue:408` | `click` | `emitSaveAutomation` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/automation/EditAutomationRule.vue:44` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountId.vue:11` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:121` | `click` | `clearDeletionMark` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue:129` | `click` | `toggleDeletePopup(true)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AutoResolve.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AutoResolve.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AutoResolve.vue:45` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AutoResolve.vue:136` | `change` | `toggleAutoResolve` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AudioTranscription.vue:14` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AudioTranscription.vue:47` | `change` | `toggleAudioTranscription` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/BuildInfo.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/BuildInfo.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/BuildInfo.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/BuildInfo.vue:50` | `click` | `copyGitSha` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/conversationWorkflow/index.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/conversationWorkflow/index.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:107` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:169` | `click` | `onClickBillingPortal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:206` | `click` | `fetchLimits` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:215` | `click` | `openPurchaseCreditsModal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:240` | `click` | `onClickBillingPortal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue:256` | `click` | `onToggleChatWindow` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/BillingMeter.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/BillingMeter.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:189` | `click` | `close` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:196` | `click` | `goToConfirmStep` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:208` | `click` | `goBackToSelectStep` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue:215` | `click` | `handlePurchase` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/CreditPackageCard.vue:57` | `change` | `emit('select')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/Index.vue:115` | `click` | `downloadConversationReports` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/TeamReportsIndex.vue:23` | `click` | `onDownloadClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/SLAReports.vue:89` | `click` | `downloadReports` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/CsatResponses.vue:123` | `click` | `downloadReports` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/LabelReportsIndex.vue:23` | `click` | `onDownloadClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue:23` | `click` | `onDownloadClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/AgentReportsIndex.vue:23` | `click` | `onDownloadClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReportLink.vue:10` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/WootReports.vue:170` | `click` | `downloadReports` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/OverviewReportFilters.vue:107` | `change` | `onBusinessHoursToggle` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatMetrics.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatMetrics.vue:16` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue:100` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:89` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:100` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:102` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:135` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:139` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:149` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:159` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue:376` | `change` | `onBusinessHoursToggle` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReports.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReports.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReports.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/BotMetrics.vue:34` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:59` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue:173` | `click` | `showExpandableRows && toggleRow(row.id)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatRatingDistribution.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatExpandedRow.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatExpandedRow.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatExpandedRow.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatExpandedRow.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Filters/v3/ActiveFilterChip.vue:61` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Filters/v3/AddFilterChip.vue:65` | `click` | `toggleDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:61` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:65` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:87` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:131` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:152` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:156` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue:309` | `click` | `clearAllFilters` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportFilters.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportFilters.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportItem.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportItem.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:110` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue:250` | `click` | `clearAllFilters` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAViewDetails.vue:45` | `click` | `openSlaEvents` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapTooltip.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmap.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmap.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:106` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:115` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:239` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:248` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:284` | `click` | `toggleInboxDropdown()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue:302` | `click` | `downloadHeatmapData` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:91` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:103` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:116` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:123` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:182` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue:202` | `click` | `toggleDropdown()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/composables/useHeatmapTooltip.js:20` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/composables/useHeatmapTooltip.js:28` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/AgentTable.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/TeamTable.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue:103` | `click` | `openCreateDialog` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue:110` | `click` | `openCreateDialog` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue:55` | `click` | `handleCreate` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue:69` | `click` | `handleCreate` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:130` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:143` | `submit` | `handleSubmit` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue:165` | `click` | `handleDelete` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:75` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:97` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:105` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue:209` | `click` | `addGuardrail(item.content)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/playground/Index.vue:8` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:20` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:52` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:73` | `click` | `handleCreate` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue:76` | `click` | `handleCreate` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:80` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:88` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue:224` | `click` | `addScenario(item)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:37` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:77` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:99` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:111` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue:218` | `click` | `addGuideline(item.content)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:30` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:42` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:118` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:126` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:217` | `click` | `handleCreate` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue:264` | `click` | `handleCreate` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:31` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:37` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:44` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:53` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:145` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:153` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:223` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue:307` | `click` | `handleBulkApprove` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:39` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:42` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:43` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:169` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:173` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:214` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:296` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:302` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:334` | `click` | `handleCreateDocument` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:365` | `change` | `onFiltersChanged` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue:381` | `click` | `handleCreateDocument` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/captain/pages/CaptainPageRouteView.vue:9` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/captain/pages/AssistantsIndexPage.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue:149` | `click` | `routeToBilling()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:63` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue:172` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:49` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:203` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:213` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue:255` | `click` | `openConversation(notificationItem)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxItemHeader.vue:138` | `click` | `openSnoozeNotificationModal` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxItemHeader.vue:147` | `click` | `deleteNotification` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxDisplayMenu.vue:136` | `click` | `openSortMenu` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxDisplayMenu.vue:185` | `change` | `updateDisplayOption(option)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxListHeader.vue:97` | `click` | `openInboxDisplayMenu` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxListHeader.vue:113` | `click` | `openInboxOptionsMenu` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/PaginationButton.vue:51` | `click` | `handleUpClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/inbox/components/PaginationButton.vue:59` | `click` | `handleDownClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:38` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:100` | `click` | `emit('clearSelection')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue:131` | `click` | `emit('deleteSelected')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:36` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:38` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:61` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:62` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:63` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:66` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:67` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:68` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:69` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:74` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:75` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:80` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:87` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:92` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:93` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:98` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:99` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:102` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:103` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:107` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:115` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:124` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:132` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:140` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:431` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:437` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:449` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue:457` | `Reactive Hook` | `watch` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/UpgradePage.vue:97` | `click` | `openHelpCenterDocs` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/UpgradePage.vue:101` | `click` | `openBillingPage` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleView.vue:36` | `click` | `onBack` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleView.vue:53` | `click` | `onBack` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleView.vue:60` | `click` | `onInsert` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/Header.vue:53` | `click` | `onClose` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleSearchResultItem.vue:54` | `click` | `handlePreview` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleSearchResultItem.vue:79` | `click` | `handleCopy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleSearchResultItem.vue:86` | `click` | `handleInsert` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:34` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:50` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue:111` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsCategoriesIndexPage.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsCategoriesIndexPage.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsCategoriesIndexPage.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue:57` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsLocalesIndexPage.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsLocalesIndexPage.vue:15` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsIndexPage.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesNewPage.vue:24` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesNewPage.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsSettingsIndexPage.vue:146` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue:53` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/noAccounts/Index.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/noAccounts/Index.vue:36` | `click` | `handleLogout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue:56` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue:208` | `Reactive Hook` | `watchEffect` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue:227` | `change` | `onCommandBarChange` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/CmdBarConversationSnooze.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/commands/CmdBarConversationSnooze.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue:41` | `click` | `toggleSMSCampaignDialog()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/WhatsAppCampaignsPage.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/WhatsAppCampaignsPage.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/WhatsAppCampaignsPage.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/WhatsAppCampaignsPage.vue:43` | `click` | `toggleWhatsAppCampaignDialog()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue:27` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue:49` | `click` | `toggleLiveChatCampaignDialog()` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/notifications/components/NotificationTable.vue:66` | `click` | `onMarkAllDoneClick` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/notifications/components/NotificationTable.vue:78` | `click` | `() => onClickNotification(notificationItem)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:25` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:26` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:27` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:29` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:32` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:53` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:54` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:56` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:57` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue:62` | `Reactive Hook` | `computed` | False | True | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:29` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:31` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:35` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:39` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:42` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:48` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:52` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:82` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:187` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue:252` | `click` | `openDeleteCompanyDialog` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:67` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:71` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:157` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:173` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:184` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:214` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue:366` | `click` | `enableWebsiteEditing` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingLayout.vue:113` | `click` | `$emit('continue')` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingFormSelect.vue:23` | `change` | `$emit('update:modelValue', $event.target.value)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationAction.vue:229` | `click` | `onSelfAssign` | True | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/SharedFiles.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/SharedFiles.vue:28` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:18` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:19` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:25` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:32` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:36` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:43` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue:45` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:54` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:60` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:69` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:73` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:79` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:83` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:86` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:90` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:93` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:94` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:95` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue:105` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationParticipant.vue:178` | `click` | `onOpenDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationParticipant.vue:198` | `click` | `onSelfAssign` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationParticipant.vue:219` | `click` | `onCloseDropdown` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:33` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:40` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:44` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:78` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:115` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue:153` | `click` | `onCardClick(conversation, $event)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationView.vue:120` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationView.vue:121` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfo.vue:210` | `click` | `startEditingName` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfo.vue:323` | `click` | `toggleEditModal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/EditContact.vue:59` | `click` | `onCancel` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:21` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:22` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:23` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:87` | `Reactive Hook` | `watch` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:108` | `click` | `openCreateModal` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue:160` | `click` | `onAdd` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfoRow.vue:130` | `click` | `onCopy` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfoRow.vue:166` | `click` | `startEditing` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:46` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:47` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:51` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:58` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:62` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:70` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:76` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:92` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:96` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:123` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue:323` | `click` | `onClickToggle` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/search/SwitchLayout.vue:35` | `click` | `toggle` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/MacroItem.vue:71` | `click` | `toggleMacroPreview` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/MacroItem.vue:80` | `click` | `executeMacro(macro)` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/List.vue:30` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/MacroPreview.vue:41` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/dashboard/store/modules/conversations/actions/messageReadActions.js:11` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/v3/components/Form/CheckBox.vue:17` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/components/Form/Input.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/components/Form/Input.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/components/Form/Input.vue:101` | `click` | `togglePasswordVisibility()` | False | False | False |
| `app/javascript/v3/components/SnackBar/Container.vue:34` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/v3/views/auth/signup/Index.vue:12` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/Index.vue:13` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/PasswordRequirements.vue:14` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue:53` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue:55` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue:64` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue:68` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue:74` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/verify-email/Index.vue:26` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/v3/views/auth/verify-email/Index.vue:105` | `click` | `handleResendEmail` | False | False | False |
| `app/javascript/v3/views/login/Index.vue:150` | `Timer Trigger` | `setTimeout` | False | False | False |
| `app/javascript/v3/views/login/Saml.vue:57` | `Reactive Hook` | `computed` | False | False | False |
| `app/javascript/sdk/bubbleHelpers.js:101` | `click` | `onBubbleClick` | False | False | False |
| `app/javascript/sdk/IFrameHelper.js:119` | `wheel` | `event` | False | False | False |
| `app/javascript/entrypoints/sdk.js:27` | `turbo:before-render` | `event` | False | False | False |
| `app/javascript/entrypoints/sdk.js:40` | `turbolinks:before-render` | `event` | False | False | False |
| `app/javascript/entrypoints/sdk.js:46` | `astro:before-swap` | `event` | False | False | False |
| `app/javascript/entrypoints/portal.js:9` | `turbo:load` | `InitializationHelpers` | False | False | False |
| `app/javascript/survey/components/Rating.vue:46` | `click` | `onClick(rating)` | False | False | False |
| `app/javascript/survey/components/Feedback.vue:60` | `click` | `onClick` | False | False | False |
