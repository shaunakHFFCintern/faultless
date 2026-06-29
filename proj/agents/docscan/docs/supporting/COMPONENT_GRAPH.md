# Component Architecture Graph

## 1. Component Registry & Metrics

| Component Path | Classification | Fan-In | Fan-Out | Depth | Owner |
|:---|:---|:---|:---|:---|:---|
| `vite.lib.config.ts` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `tailwind.config.js` | Utility | 0 | 2 | 1 | Shivam Mishra |
| `app.json` | Shared Component | 0 | 0 | 0 | Vishnu Narayanan |
| `vitest.setup.js` | Utility | 0 | 1 | 3 | Sivin Varghese |
| `workbox-config.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `vite.shared.ts` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `package.json` | Shared Component | 0 | 0 | 0 | Sojan |
| `.eslintrc.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `vite.config.ts` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `vitest.config.ts` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `postcss.config.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `histoire.config.ts` | Utility | 0 | 0 | 0 | Pranav |
| `__mocks__/fileMock.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/histoire.setup.ts` | Utility | 0 | 4 | 7 | Sivin Varghese |
| `app/javascript/portal/portalHelpers.js` | Utility | 1 | 6 | 5 | Sivin Varghese |
| `app/javascript/portal/portalThemeHelper.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/portal/specs/SearchSuggestions.spec.js` | Utility | 0 | 1 | 4 | Pranav |
| `app/javascript/portal/specs/portal.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/portal/specs/portalTheme.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/portal/specs/PublicArticleSearch.spec.js` | Utility | 0 | 2 | 5 | Sojan Jose |
| `app/javascript/portal/components/SearchSuggestions.vue` | Shared Component | 2 | 2 | 3 | Sivin Varghese |
| `app/javascript/portal/components/PublicArticleSearch.vue` | Shared Component | 2 | 3 | 4 | Shivam Mishra |
| `app/javascript/portal/components/SidebarThemeToggle.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/portal/components/PublicSearchInput.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/portal/components/TableOfContents.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/portal/api/article.js` | Utility | 2 | 0 | 0 | Nithin David Thomas |
| `app/javascript/widget/App.vue` | Shared Component | 1 | 10 | 2 | Pranav Raj S |
| `app/javascript/widget/router.js` | Utility | 1 | 8 | 9 | Pranav Raj S |
| `app/javascript/widget/composables/useDarkMode.js` | Hook | 4 | 1 | 1 | Sivin Varghese |
| `app/javascript/widget/composables/useAvailability.js` | Hook | 4 | 1 | 1 | Rob Coenen |
| `app/javascript/widget/composables/useAttachments.js` | Hook | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/composables/specs/useDarkMode.spec.js` | Hook | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/widget/composables/specs/useAvailability.spec.js` | Hook | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/widget/composables/specs/useAttachments.spec.js` | Hook | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/widget/mixins/configMixin.js` | Utility | 10 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/mixins/messageMixin.js` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/widget/mixins/specs/messageMixin.spec.js` | Utility | 0 | 2 | 1 | Shivam Mishra |
| `app/javascript/widget/mixins/specs/messageFixture.js` | Utility | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/mixins/specs/configMixin.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/widget/constants/sdkEvents.js` | Utility | 3 | 0 | 0 | David Kubeš |
| `app/javascript/widget/constants/errorTypes.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/constants/widgetBusEvents.js` | Utility | 4 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/components/VideoBubble.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/components/ChatInputWrap.vue` | Shared Component | 1 | 6 | 3 | Pranav Raj S |
| `app/javascript/widget/components/Banner.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/widget/components/TeamAvailability.vue` | Shared Component | 1 | 4 | 6 | Sivin Varghese |
| `app/javascript/widget/components/ReplyToChip.vue` | Shared Component | 2 | 1 | 2 | Shivam Mishra |
| `app/javascript/widget/components/AgentTypingBubble.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/components/DragWrapper.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/widget/components/AgentMessageBubble.vue` | Shared Component | 1 | 8 | 4 | Pranav Raj S |
| `app/javascript/widget/components/UnreadMessageList.vue` | Shared Component | 2 | 6 | 5 | Sivin Varghese |
| `app/javascript/widget/components/ChatFooter.vue` | Shared Component | 1 | 8 | 5 | Pranav Raj S |
| `app/javascript/widget/components/UnreadMessage.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/widget/components/FileBubble.vue` | Shared Component | 2 | 1 | 2 | Sivin Varghese |
| `app/javascript/widget/components/ChatHeader.vue` | Shared Component | 1 | 4 | 6 | Pranav Raj S |
| `app/javascript/widget/components/UserMessage.vue` | Shared Component | 2 | 12 | 4 | Pranav Raj S |
| `app/javascript/widget/components/MessageReplyButton.vue` | Shared Component | 2 | 1 | 2 | Sivin Varghese |
| `app/javascript/widget/components/AgentMessage.vue` | Shared Component | 1 | 15 | 5 | Pranav Raj S |
| `app/javascript/widget/components/ChatAttachment.vue` | Shared Component | 1 | 6 | 2 | Pranav Raj S |
| `app/javascript/widget/components/ImageBubble.vue` | Shared Component | 2 | 0 | 0 | Nithin David Thomas |
| `app/javascript/widget/components/FooterReplyTo.vue` | Shared Component | 1 | 1 | 2 | Shivam Mishra |
| `app/javascript/widget/components/HeaderActions.vue` | Shared Component | 2 | 5 | 2 | Pranav Raj S |
| `app/javascript/widget/components/ChatSendButton.vue` | Shared Component | 1 | 2 | 2 | Pranav Raj S |
| `app/javascript/widget/components/GroupedAvatars.vue` | Shared Component | 1 | 1 | 4 | Sivin Varghese |
| `app/javascript/widget/components/ChatHeaderExpanded.vue` | Shared Component | 1 | 2 | 3 | Pranav Raj S |
| `app/javascript/widget/components/ChatMessage.vue` | Shared Component | 1 | 3 | 6 | Pranav Raj S |
| `app/javascript/widget/components/ConversationWrap.vue` | Shared Component | 1 | 6 | 7 | Pranav Raj S |
| `app/javascript/widget/components/UserMessageBubble.vue` | Shared Component | 1 | 1 | 3 | Pranav Raj S |
| `app/javascript/widget/components/Form/PhoneInput.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/widget/components/PreChat/Form.vue` | Shared Component | 1 | 7 | 3 | Sivin Varghese |
| `app/javascript/widget/components/template/EmailInput.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/widget/components/template/IntegrationCard.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/widget/components/template/Article.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/widget/components/pageComponents/Home/Article/SkeletonLoader.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleBlock.vue` | Shared Component | 1 | 2 | 1 | Khoa Nguyen |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleContainer.vue` | Shared Component | 1 | 6 | 2 | Sivin Varghese |
| `app/javascript/widget/components/pageComponents/Home/Article/ArticleListItem.vue` | Shared Component | 1 | 0 | 0 | Khoa Nguyen |
| `app/javascript/widget/components/layouts/ViewWithHeader.vue` | Layout | 1 | 6 | 7 | Pranav Raj S |
| `app/javascript/widget/components/Availability/AvailabilityContainer.vue` | Shared Component | 2 | 4 | 5 | Rob Coenen |
| `app/javascript/widget/components/Availability/AvailabilityText.vue` | Shared Component | 2 | 2 | 2 | Sivin Varghese |
| `app/javascript/widget/components/Availability/AvailabilityText.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/widget/api/events.js` | Utility | 2 | 2 | 2 | Sojan Jose |
| `app/javascript/widget/api/conversation.js` | Utility | 2 | 2 | 4 | Pranav Raj S |
| `app/javascript/widget/api/message.js` | Utility | 1 | 2 | 4 | Sojan Jose |
| `app/javascript/widget/api/conversationLabels.js` | Utility | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/widget/api/contacts.js` | Utility | 1 | 1 | 2 | Sojan Jose |
| `app/javascript/widget/api/article.js` | Utility | 2 | 2 | 4 | Nithin David Thomas |
| `app/javascript/widget/api/endPoints.js` | Utility | 6 | 2 | 3 | Pranav Raj S |
| `app/javascript/widget/api/campaign.js` | Utility | 1 | 2 | 4 | Muhsin Keloth |
| `app/javascript/widget/api/integration.js` | Utility | 1 | 2 | 2 | Pranav Raj S |
| `app/javascript/widget/api/agent.js` | Utility | 2 | 2 | 4 | David Kubeš |
| `app/javascript/widget/api/specs/endPoints.spec.js` | Utility | 0 | 1 | 4 | Muhsin Keloth |
| `app/javascript/widget/i18n/index.js` | Utility | 3 | 40 | 1 | Pranav Raj S |
| `app/javascript/widget/i18n/locale/hy.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/zh.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/tr.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/sl.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/hu.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/lt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/is.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/bn.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/nl.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ms.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/zh_CN.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ja.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/de.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ru.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/pl.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/uk.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/fi.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ta.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ur.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/sk.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ml.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/az.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/pt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/en.json` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/i18n/locale/ka.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/it.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/sr.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/hr.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/tl.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/et.json` | Shared Component | 0 | 0 | 0 | Linas Baublys |
| `app/javascript/widget/i18n/locale/sq.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/sh.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/ur_IN.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/ne.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/fr.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/am.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/el.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/bg.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/ro.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/hi.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ca.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ko.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/he.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/vi.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/fa.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/cs.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/id.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/pt_BR.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/zh_TW.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/lv.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/widget/i18n/locale/no.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/da.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/th.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/sv.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/es.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/i18n/locale/ar.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/widget/views/UnreadMessages.vue` | Page | 1 | 2 | 6 | Sivin Varghese |
| `app/javascript/widget/views/Campaigns.vue` | Page | 1 | 3 | 6 | Shivam Mishra |
| `app/javascript/widget/views/Home.vue` | Page | 1 | 3 | 7 | Pranav Raj S |
| `app/javascript/widget/views/Messages.vue` | Page | 1 | 2 | 8 | Sivin Varghese |
| `app/javascript/widget/views/ArticleViewer.vue` | Page | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/widget/views/PreChatForm.vue` | Page | 1 | 5 | 4 | Muhsin Keloth |
| `app/javascript/widget/helpers/constants.js` | Utility | 10 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/helpers/axios.js` | Utility | 16 | 1 | 1 | Sojan Jose |
| `app/javascript/widget/helpers/campaignHelper.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/helpers/IframeEventHelper.js` | Utility | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/helpers/uuid.js` | Utility | 4 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/helpers/campaignTimer.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/widget/helpers/availabilityHelpers.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/helpers/utils.js` | Utility | 17 | 1 | 1 | Pranav Raj S |
| `app/javascript/widget/helpers/WidgetAudioNotificationHelper.js` | Utility | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/widget/helpers/popoutHelper.js` | Utility | 2 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/widget/helpers/urlParamsHelper.js` | Utility | 5 | 0 | 0 | Shivam Mishra |
| `app/javascript/widget/helpers/actionCable.js` | Utility | 2 | 7 | 3 | Pranav Raj S |
| `app/javascript/widget/helpers/specs/campaignHelper.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/widget/helpers/specs/urlParamsHelper.spec.js` | Utility | 0 | 0 | 0 | Pranav |
| `app/javascript/widget/helpers/specs/availabilityHelpers.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/helpers/specs/utils.spec.js` | Utility | 0 | 1 | 2 | Pranav Raj S |
| `app/javascript/widget/helpers/specs/actionCable.spec.js` | Utility | 0 | 1 | 4 | Shivam Mishra |
| `app/javascript/widget/helpers/specs/campaignFixtures.js` | Utility | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/store/types.js` | Context / Store | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/widget/store/index.js` | Context / Store | 3 | 11 | 6 | Pranav Raj S |
| `app/javascript/widget/store/modules/events.js` | Context / Store | 1 | 1 | 3 | Pranav Raj S |
| `app/javascript/widget/store/modules/message.js` | Context / Store | 4 | 1 | 5 | Sojan Jose |
| `app/javascript/widget/store/modules/appConfig.js` | Context / Store | 4 | 0 | 0 | Sivin Varghese |
| `app/javascript/widget/store/modules/conversationLabels.js` | Context / Store | 1 | 1 | 3 | Muhsin Keloth |
| `app/javascript/widget/store/modules/conversationAttributes.js` | Context / Store | 4 | 1 | 5 | Muhsin Keloth |
| `app/javascript/widget/store/modules/contacts.js` | Context / Store | 4 | 4 | 3 | Sojan Jose |
| `app/javascript/widget/store/modules/campaign.js` | Context / Store | 4 | 3 | 5 | Muhsin Keloth |
| `app/javascript/widget/store/modules/articles.js` | Context / Store | 2 | 2 | 5 | Nithin David Thomas |
| `app/javascript/widget/store/modules/agent.js` | Context / Store | 4 | 3 | 5 | Nithin David Thomas |
| `app/javascript/widget/store/modules/specs/articles.spec.js` | Context / Store | 0 | 3 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/contact/actions.spec.js` | Context / Store | 0 | 3 | 4 | Pranav |
| `app/javascript/widget/store/modules/specs/contact/mutations.spec.js` | Context / Store | 0 | 1 | 4 | Shivam Mishra |
| `app/javascript/widget/store/modules/specs/contact/getters.spec.js` | Context / Store | 0 | 1 | 4 | Shivam Mishra |
| `app/javascript/widget/store/modules/specs/message/actions.spec.js` | Context / Store | 0 | 2 | 6 | Pranav |
| `app/javascript/widget/store/modules/specs/message/mutations.spec.js` | Context / Store | 0 | 1 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/message/getters.spec.js` | Context / Store | 0 | 1 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/agent/actions.spec.js` | Context / Store | 0 | 4 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/agent/data.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/widget/store/modules/specs/agent/mutations.spec.js` | Context / Store | 0 | 2 | 6 | Aswin Dev P.S |
| `app/javascript/widget/store/modules/specs/agent/getters.spec.js` | Context / Store | 0 | 2 | 6 | Nithin David Thomas |
| `app/javascript/widget/store/modules/specs/appConfig/actions.spec.js` | Context / Store | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/widget/store/modules/specs/appConfig/mutations.spec.js` | Context / Store | 0 | 1 | 1 | Nithin David Thomas |
| `app/javascript/widget/store/modules/specs/appConfig/getters.spec.js` | Context / Store | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/widget/store/modules/specs/campaign/actions.spec.js` | Context / Store | 0 | 5 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/campaign/data.js` | Context / Store | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/campaign/mutations.spec.js` | Context / Store | 0 | 2 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/campaign/getters.spec.js` | Context / Store | 0 | 2 | 6 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/conversationAttributes/actions.spec.js` | Context / Store | 0 | 2 | 6 | Pranav |
| `app/javascript/widget/store/modules/specs/conversationAttributes/mutations.spec.js` | Context / Store | 0 | 1 | 6 | Sojan Jose |
| `app/javascript/widget/store/modules/specs/conversationAttributes/getters.spec.js` | Context / Store | 0 | 1 | 6 | Sojan Jose |
| `app/javascript/widget/store/modules/specs/conversation/helpers.spec.js` | Context / Store | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/widget/store/modules/specs/conversation/actions.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/conversation/mutations.spec.js` | Context / Store | 0 | 1 | 3 | Muhsin Keloth |
| `app/javascript/widget/store/modules/specs/conversation/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/widget/store/modules/conversation/mutations.js` | Context / Store | 2 | 2 | 2 | Muhsin Keloth |
| `app/javascript/widget/store/modules/conversation/actions.js` | Context / Store | 2 | 3 | 2 | Muhsin Keloth |
| `app/javascript/widget/store/modules/conversation/getters.js` | Context / Store | 2 | 4 | 2 | Muhsin Keloth |
| `app/javascript/widget/store/modules/conversation/index.js` | Context / Store | 1 | 3 | 3 | Muhsin Keloth |
| `app/javascript/widget/store/modules/conversation/helpers.js` | Context / Store | 3 | 3 | 1 | Shivam Mishra |
| `app/javascript/superadmin_pages/components/playground/UserMessage.vue` | Page | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/superadmin_pages/components/playground/Header.vue` | Page | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/superadmin_pages/components/playground/TypingIndicator.vue` | Page | 1 | 1 | 1 | Sojan Jose |
| `app/javascript/superadmin_pages/components/playground/BotMessage.vue` | Page | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/superadmin_pages/views/playground/Index.vue` | Page | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/superadmin_pages/views/dashboard/Index.vue` | Page | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/shared/composables/useMessageFormatter.js` | Hook | 32 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/composables/useLocale.js` | Hook | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/composables/useFilter.js` | Hook | 2 | 5 | 1 | Shivam Mishra |
| `app/javascript/shared/composables/useExpandableContent.js` | Hook | 3 | 0 | 0 | Vinay Keerthi |
| `app/javascript/shared/composables/useNumberFormatter.js` | Hook | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/composables/useBranding.js` | Hook | 20 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/composables/specs/useMessageFormatter.spec.js` | Hook | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/shared/composables/specs/useFilter.spec.js` | Hook | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/shared/composables/specs/useNumberFormatter.spec.js` | Hook | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/composables/specs/useLocale.spec.js` | Hook | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/composables/specs/useBranding.spec.js` | Hook | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/shared/composables/specs/useExpandableContent.spec.js` | Hook | 0 | 1 | 1 | Vinay Keerthi |
| `app/javascript/shared/mixins/keyboardEventListenerMixins.js` | Utility | 2 | 1 | 2 | Shivam Mishra |
| `app/javascript/shared/mixins/inboxMixin.js` | Utility | 7 | 1 | 1 | Sojan Jose |
| `app/javascript/shared/mixins/specs/inboxMixin.spec.js` | Utility | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/mixins/specs/MockComponent.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/mixins/specs/filterFixtures.js` | Utility | 0 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/shared/constants/contentType.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/shared/constants/links.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/constants/countries.js` | Utility | 14 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/constants/sharedFrameEvents.js` | Utility | 2 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/shared/constants/campaign.js` | Utility | 4 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/constants/busEvents.js` | Utility | 22 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/constants/locales.js` | Utility | 5 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/constants/messages.js` | Utility | 30 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/components/GreetingsEditor.vue` | Shared Component | 2 | 2 | 6 | Sivin Varghese |
| `app/javascript/shared/components/Branding.vue` | Shared Component | 2 | 1 | 2 | Pranav Raj S |
| `app/javascript/shared/components/DateSeparator.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/components/ChatCard.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/shared/components/ArticleSkeletonLoader.vue` | Shared Component | 1 | 0 | 0 | Nithin David Thomas |
| `app/javascript/shared/components/IframeLoader.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/components/ChatOptions.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/shared/components/ResizableTextArea.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/ChatOption.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/StarRating.vue` | Shared Component | 2 | 0 | 0 | Khoa Nguyen |
| `app/javascript/shared/components/Button.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/CardButton.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/components/Spinner.vue` | Shared Component | 24 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/TextArea.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/components/CustomerSatisfaction.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/shared/components/EmojiOrIcon.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/components/ChatForm.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/ui/MultiselectDropdownItems.vue` | Shared Component | 2 | 5 | 3 | Sivin Varghese |
| `app/javascript/shared/components/ui/MultiselectDropdown.vue` | Shared Component | 2 | 4 | 4 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/AddLabel.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/DropdownHeader.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/DropdownSubMenu.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/DropdownMenu.vue` | Shared Component | 3 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/DropdownItem.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/ui/dropdown/DropdownDivider.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/ui/label/LabelDropdown.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/shared/components/ui/label/LabelDropdownItem.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/components/specs/DateSeparator.spec.js` | Utility | 0 | 1 | 2 | Pranav Raj S |
| `app/javascript/shared/components/specs/Spinner.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/shared/components/PhoneInput/helper.js` | Utility | 0 | 0 | 0 | Pranav |
| `app/javascript/shared/components/emoji/emojisGroup.json` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/emoji/EmojiPicker.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/emoji/pickerHelper.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/components/charts/BarChart.vue` | Shared Component | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/components/FluentIcon/Index.vue` | Shared Component | 18 | 2 | 1 | Sivin Varghese |
| `app/javascript/shared/components/FluentIcon/DashboardIcon.vue` | Shared Component | 2 | 2 | 1 | Sivin Varghese |
| `app/javascript/shared/components/FluentIcon/icons.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/shared/components/FluentIcon/Icon.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/components/FluentIcon/dashboard-icons.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/Validators.js` | Utility | 15 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/portalHelper.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/mitt.js` | Utility | 48 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/shared/helpers/emoji.js` | Utility | 3 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/shared/helpers/documentHelper.js` | Utility | 0 | 0 | 0 | Aakash Bakhle |
| `app/javascript/shared/helpers/KeyboardHelpers.js` | Utility | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/MessageFormatter.js` | Utility | 8 | 1 | 1 | Pranav Raj S |
| `app/javascript/shared/helpers/HTMLSanitizer.js` | Utility | 5 | 0 | 0 | Pranav Raj S |
| `app/javascript/shared/helpers/sessionStorage.js` | Utility | 7 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/CustomErrors.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/cache.js` | Utility | 7 | 1 | 1 | Muhsin Keloth |
| `app/javascript/shared/helpers/ReportsDataHelper.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/helpers/DateHelper.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/sanitizeData.js` | Utility | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/helpers/CustomEventHelper.js` | Utility | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/helpers/timeHelper.js` | Utility | 32 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/AudioNotificationHelper.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/clipboard.js` | Utility | 19 | 0 | 0 | Tanmay Deep Sharma |
| `app/javascript/shared/helpers/localStorage.js` | Utility | 20 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/helpers/FileHelper.js` | Utility | 11 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/colorHelper.js` | Utility | 4 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/platform.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/IntegrationHelper.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/helpers/MessageTypeHelper.js` | Utility | 4 | 0 | 0 | Sojan Jose |
| `app/javascript/shared/helpers/BaseActionCableConnector.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/shared/helpers/specs/documentHelper.spec.js` | Utility | 0 | 0 | 0 | Aakash Bakhle |
| `app/javascript/shared/helpers/specs/sanitizeData.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/shared/helpers/specs/MessageFormatter.spec.js` | Utility | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/ReportsDataHelper.spec.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/shared/helpers/specs/localStorage.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/shared/helpers/specs/timeHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/CustomEventHelper.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/shared/helpers/specs/sessionStorage.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/Emoji.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/MessageTypeHelper.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/shared/helpers/specs/cache.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/shared/helpers/specs/mitt.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/shared/helpers/specs/FileHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/ValidatorsHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/DateHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/clipboard.spec.js` | Utility | 0 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/shared/helpers/specs/KeyboardHelpers.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/CustomErrors.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/shared/helpers/specs/platform.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/portalHelper.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/shared/helpers/specs/colorHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/shared/helpers/markdownIt/link.js` | Utility | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/shared/helpers/vuex/mutationHelpers.js` | Utility | 24 | 0 | 0 | Pranav Raj S |
| `app/javascript/shared/store/globalConfig.js` | Context / Store | 4 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/App.vue` | Shared Component | 1 | 15 | 9 | Sivin Varghese |
| `app/javascript/dashboard/featureFlags.js` | Utility | 56 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/useConversationLabels.js` | Hook | 4 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useConversationRequiredAttributes.js` | Hook | 4 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/composables/useAgentsList.js` | Hook | 5 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useWhatsappCallSession.js` | Hook | 5 | 2 | 2 | Tanmay Deep Sharma |
| `app/javascript/dashboard/composables/useImageZoom.js` | Hook | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/composables/useMacros.js` | Hook | 3 | 2 | 1 | Petterson |
| `app/javascript/dashboard/composables/useReportMetrics.js` | Hook | 3 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/composables/useCallSession.js` | Hook | 2 | 7 | 5 | Muhsin Keloth |
| `app/javascript/dashboard/composables/useKeyboardNavigableList.js` | Hook | 6 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/useKeyboardEvents.js` | Hook | 22 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useDropdownPosition.js` | Hook | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/composables/useEditableAutomation.js` | Hook | 2 | 1 | 2 | Sojan Jose |
| `app/javascript/dashboard/composables/loadWithRetry.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/store.js` | Context / Store | 268 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/useCaptain.js` | Hook | 12 | 7 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/index.js` | Utility | 240 | 2 | 1 | Shivam Mishra |
| `app/javascript/dashboard/composables/useFontSize.js` | Hook | 4 | 2 | 2 | micahmills |
| `app/javascript/dashboard/composables/useLabelSuggestions.js` | Hook | 1 | 4 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/useAutomationValues.js` | Hook | 3 | 3 | 1 | Petterson |
| `app/javascript/dashboard/composables/useCopilotReply.js` | Hook | 2 | 4 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/emitter.js` | Utility | 7 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useFacebookPageConnect.js` | Hook | 2 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/composables/useLiveRefresh.js` | Hook | 4 | 0 | 0 | Pranav |
| `app/javascript/dashboard/composables/useAdmin.js` | Hook | 17 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useIntegrationHook.js` | Hook | 5 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/composables/useTranslations.js` | Hook | 3 | 2 | 2 | Pranav |
| `app/javascript/dashboard/composables/useWhatsappEmbeddedSignup.js` | Hook | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/useInbox.js` | Hook | 9 | 2 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/composables/useAccount.js` | Hook | 59 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/composables/useTransformKeys.js` | Hook | 18 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/useConfig.js` | Hook | 14 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/composables/useFileUpload.js` | Hook | 2 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/useDetectKeyboardLayout.js` | Hook | 4 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/composables/useUISettings.js` | Hook | 50 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useImpersonation.js` | Hook | 3 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/useAutomation.js` | Hook | 3 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/usePolicy.js` | Hook | 10 | 5 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/captain/constants.js` | Utility | 1 | 0 | 0 | Aakash Bakhle |
| `app/javascript/dashboard/composables/chatlist/useChatListKeyboardEvents.js` | Hook | 1 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/chatlist/useBulkActions.js` | Hook | 2 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useKeyboardNavigableList.spec.js` | Hook | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/spec/useAgentsList.spec.js` | Hook | 0 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useAutomation.spec.js` | Hook | 0 | 4 | 3 | Sojan Jose |
| `app/javascript/dashboard/composables/spec/useTranslations.spec.js` | Hook | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/composables/spec/useConversationRequiredAttributes.spec.js` | Hook | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/composables/spec/useAdmin.spec.js` | Hook | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useIntegrationHook.spec.js` | Hook | 0 | 2 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/composables/spec/useFontSize.spec.js` | Hook | 0 | 3 | 3 | micahmills |
| `app/javascript/dashboard/composables/spec/useInbox.spec.js` | Hook | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/composables/spec/useUISettings.spec.js` | Hook | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/spec/emitter.spec.js` | Utility | 0 | 2 | 2 | Vishnu Narayanan |
| `app/javascript/dashboard/composables/spec/useCaptain.spec.js` | Hook | 0 | 4 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/spec/useMacros.spec.js` | Hook | 0 | 3 | 2 | Petterson |
| `app/javascript/dashboard/composables/spec/index.spec.js` | Utility | 0 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/spec/useImageZoom.spec.js` | Hook | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useDropdownPosition.spec.js` | Hook | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useAccount.spec.js` | Hook | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useKeyboardEvents.spec.js` | Hook | 0 | 3 | 2 | Silva Dev BR |
| `app/javascript/dashboard/composables/spec/useReportMetrics.spec.js` | Hook | 0 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useFacebookPageConnect.spec.js` | Hook | 0 | 4 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/composables/spec/useWhatsappEmbeddedSignup.spec.js` | Hook | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/composables/spec/useEditableAutomation.spec.js` | Hook | 0 | 2 | 3 | Sojan Jose |
| `app/javascript/dashboard/composables/spec/useConfig.spec.js` | Hook | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useImpersonation.spec.js` | Hook | 0 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useFileUpload.spec.js` | Hook | 0 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useDetectKeyboardLayout.spec.js` | Hook | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/useConversationLabels.spec.js` | Hook | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/fixtures/reportFixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/composables/spec/fixtures/agentFixtures.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/composables/utils/useKbd.js` | Hook | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/useAppearanceHotKeys.js` | Hook | 2 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/useBulkActionsHotKeys.js` | Hook | 2 | 4 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/useInboxHotKeys.js` | Hook | 2 | 5 | 1 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/useConversationHotKeys.js` | Hook | 2 | 8 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/useGoToCommandHotKeys.js` | Hook | 2 | 4 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/spec/useInboxHotKeys.spec.js` | Hook | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/spec/useGoToCommandHotKeys.spec.js` | Hook | 0 | 5 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/spec/useBulkActionsHotKeys.spec.js` | Hook | 0 | 4 | 3 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/spec/useConversationHotKeys.spec.js` | Hook | 0 | 6 | 4 | Shivam Mishra |
| `app/javascript/dashboard/composables/commands/spec/fixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/composables/commands/spec/useAppearanceHotKeys.spec.js` | Hook | 0 | 4 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/EmptyStateLayout.vue` | Layout | 13 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/SidebarActionsHeader.vue` | Shared Component | 3 | 1 | 2 | Pranav |
| `app/javascript/dashboard/components-next/TeleportWithDirection.vue` | Shared Component | 7 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CardLayout.vue` | Layout | 20 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/SidebarActionsHeader.story.vue` | Shared Component | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupHeader.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarSortMenu.vue` | Shared Component | 2 | 5 | 5 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/MobileSidebarLauncher.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroup.vue` | Shared Component | 1 | 7 | 8 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/useSidebarKeyboardShortcuts.js` | Hook | 1 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarSubGroup.vue` | Shared Component | 2 | 6 | 7 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarUnreadBadge.vue` | Shared Component | 3 | 0 | 0 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogCard.vue` | Shared Component | 2 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenu.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarAccountSwitcher.vue` | Shared Component | 1 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/provider.js` | Utility | 6 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarProfileMenuStatus.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupSeparator.vue` | Shared Component | 1 | 1 | 6 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/ChannelLeaf.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupLeaf.vue` | Shared Component | 3 | 3 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarNotificationBell.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarGroupEmptyLeaf.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/sidebar/SidebarChangelogButton.vue` | Shared Component | 1 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/Sidebar.vue` | Shared Component | 0 | 14 | 10 | Sivin Varghese |
| `app/javascript/dashboard/components-next/sidebar/SidebarCollapsedPopover.vue` | Shared Component | 1 | 5 | 6 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/specs/ChannelLeaf.spec.js` | Utility | 0 | 1 | 2 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/specs/SidebarSubGroup.spec.js` | Utility | 0 | 3 | 8 | Sony Mathew |
| `app/javascript/dashboard/components-next/sidebar/specs/SidebarGroupLeaf.spec.js` | Utility | 0 | 1 | 5 | Sony Mathew |
| `app/javascript/dashboard/components-next/Settings/SettingsFieldSection.vue` | Shared Component | 9 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Settings/SettingsAccordion.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Settings/SettingsToggleSection.vue` | Shared Component | 8 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/taginput/TagInput.vue` | Shared Component | 7 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/taginput/helper/tagInputHelper.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/taginput/helper/spec/tagInputHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.vue` | Shared Component | 7 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/pagination/PaginationFooter.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue` | Layout | 11 | 9 | 18 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesInput.vue` | Shared Component | 3 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentFilter.vue` | Shared Component | 1 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.vue` | Shared Component | 2 | 8 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.story.vue` | Shared Component | 0 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/BulkSelectBar.vue` | Shared Component | 8 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.story.vue` | Shared Component | 0 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.vue` | Shared Component | 3 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentFiltersBar.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentSyncStatus.vue` | Shared Component | 1 | 4 | 2 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/assistant/InboxCard.vue` | Shared Component | 3 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantPlayground.vue` | Shared Component | 1 | 3 | 5 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/assistant/SuggestedRules.story.vue` | Shared Component | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/MessageList.vue` | Shared Component | 1 | 2 | 4 | Pranav |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentCard.vue` | Shared Component | 3 | 8 | 5 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantCard.story.vue` | Shared Component | 0 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/ToolsDropdown.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/ToolsDropdown.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/ScenariosCard.story.vue` | Shared Component | 0 | 1 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesDialog.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesInput.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AssistantCard.vue` | Shared Component | 2 | 5 | 5 | Pranav |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.story.vue` | Shared Component | 0 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewRulesDialog.vue` | Shared Component | 3 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/RuleCard.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/DocumentBulkActions.vue` | Shared Component | 1 | 5 | 4 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/assistant/ResponseCard.vue` | Shared Component | 5 | 7 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/SuggestedRules.vue` | Shared Component | 4 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/assistant/AddNewScenariosDialog.vue` | Shared Component | 1 | 4 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/DeleteDialog.vue` | Shared Component | 6 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/captain/pageComponents/Paywall.vue` | Shared Component | 5 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/BulkDeleteDialog.vue` | Shared Component | 3 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/CreateAssistantDialog.vue` | Shared Component | 2 | 4 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/AssistantForm.vue` | Shared Component | 1 | 4 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantBasicSettingsForm.vue` | Shared Component | 1 | 3 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantControlItems.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/assistant/settings/AssistantSystemSettingsForm.vue` | Shared Component | 1 | 4 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/settings/SettingsHeader.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/settings/SettingsHeader.vue` | Shared Component | 5 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxForm.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/inbox/ConnectInboxDialog.vue` | Shared Component | 1 | 4 | 4 | Pranav |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/ResponseForm.vue` | Shared Component | 1 | 4 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/LimitBanner.vue` | Shared Component | 2 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/captain/pageComponents/response/CreateResponseDialog.vue` | Shared Component | 2 | 4 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/switcher/AssistantSwitcher.vue` | Shared Component | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/RelatedResponses.vue` | Shared Component | 1 | 4 | 6 | Pranav |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/DocumentForm.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/CreateDocumentDialog.vue` | Shared Component | 1 | 5 | 4 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/pageComponents/document/LimitBanner.vue` | Shared Component | 1 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolCard.vue` | Shared Component | 1 | 5 | 5 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/ParamRow.vue` | Shared Component | 1 | 4 | 3 | Khoa Nguyen |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CustomToolForm.vue` | Shared Component | 1 | 8 | 4 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/AuthConfig.vue` | Shared Component | 1 | 1 | 1 | Khoa Nguyen |
| `app/javascript/dashboard/components-next/captain/pageComponents/customTool/CreateCustomToolDialog.vue` | Shared Component | 1 | 5 | 5 | Shivam Mishra |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/captainEmptyStateContent.js` | Utility | 8 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/CustomToolsPageEmptyState.vue` | Shared Component | 1 | 4 | 5 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/DocumentPageEmptyState.vue` | Shared Component | 1 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/ResponsePageEmptyState.vue` | Shared Component | 2 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/AssistantPageEmptyState.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/pageComponents/emptyStates/InboxPageEmptyState.vue` | Shared Component | 1 | 4 | 6 | Shivam Mishra |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/Settings.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/AnimatingImg.story.vue` | Shared Component | 0 | 4 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/Guardrails.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/ResponseGuidelines.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/captain/AnimatingImg/Scenarios.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/flag/Flag.vue` | Shared Component | 3 | 0 | 0 | Khoa Nguyen |
| `app/javascript/dashboard/components-next/flag/story/Flag.story.vue` | Shared Component | 0 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Inbox/InboxCard.vue` | Shared Component | 1 | 8 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/buttonGroup/ButtonGroup.vue` | Shared Component | 5 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/selectmenu/SelectMenu.vue` | Shared Component | 4 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/selectmenu/SelectMenu.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewModal.vue` | Shared Component | 1 | 12 | 2 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/YearInReviewBanner.vue` | Shared Component | 0 | 4 | 3 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/ShareModal.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/year-in-review/slides/BusiestDaySlide.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/slides/ConversationsSlide.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/slides/PersonalitySlide.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/slides/ThankYouSlide.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/year-in-review/slides/IntroSlide.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotLoader.vue` | Shared Component | 2 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotAgentMessage.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotAssistantMessage.vue` | Shared Component | 1 | 7 | 2 | Pranav |
| `app/javascript/dashboard/components-next/copilot/Copilot.vue` | Shared Component | 2 | 11 | 3 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingGroup.vue` | Shared Component | 2 | 2 | 2 | Pranav |
| `app/javascript/dashboard/components-next/copilot/Copilot.story.vue` | Shared Component | 0 | 1 | 4 | Pranav |
| `app/javascript/dashboard/components-next/copilot/ToggleCopilotAssistant.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/copilot/CopilotInput.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotEmptyState.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/copilot/CopilotLoader.story.vue` | Shared Component | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingBlock.vue` | Shared Component | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotThinkingGroup.story.vue` | Shared Component | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/components-next/copilot/CopilotLauncher.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/input/constants.js` | Utility | 5 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/input/ChoiceToggle.vue` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/input/Input.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/input/DurationInput.vue` | Shared Component | 3 | 2 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/input/Input.vue` | Shared Component | 60 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Accordion/Accordion.vue` | Shared Component | 0 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/Contacts/ContactsListLayout.vue` | Layout | 1 | 4 | 12 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/VoiceCallButton.vue` | Shared Component | 2 | 8 | 5 | Sojan Jose |
| `app/javascript/dashboard/components-next/Contacts/ContactsLoadMore.vue` | Shared Component | 1 | 1 | 2 | Pranav |
| `app/javascript/dashboard/components-next/Contacts/ContactsDetailsLayout.vue` | Layout | 1 | 4 | 10 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactImportDialog.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactMergeForm.vue` | Shared Component | 3 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactExportDialog.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/DeleteSegmentDialog.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ContactsForm.vue` | Shared Component | 4 | 8 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/CreateSegmentDialog.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/ConfirmContactDeleteDialog.vue` | Shared Component | 2 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/CreateNewContactDialog.vue` | Shared Component | 2 | 4 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/story/ContactMergeForm.story.vue` | Shared Component | 0 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/story/ContactsForm.story.vue` | Shared Component | 0 | 2 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsForm/story/fixtures.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/EmptyState/contactEmptyStateContent.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/EmptyState/ContactEmptyState.vue` | Shared Component | 2 | 5 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/EmptyState/ContactEmptyState.story.vue` | Shared Component | 0 | 1 | 9 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactDeleteSection.vue` | Shared Component | 1 | 3 | 4 | Sojan Jose |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/ContactsCard.vue` | Shared Component | 3 | 8 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/story/fixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsCard/story/ContactsCard.story.vue` | Shared Component | 0 | 2 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactDetails.vue` | Shared Component | 1 | 9 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/Pages/ContactsList.vue` | Shared Component | 1 | 3 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactListHeaderWrapper.vue` | Shared Component | 1 | 14 | 11 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/ContactHeader.vue` | Shared Component | 2 | 6 | 10 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactMoreActions.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactsActiveFiltersPreview.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/components/ContactSortMenu.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsHeader/story/ContactHeader.story.vue` | Shared Component | 0 | 1 | 11 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactLabels/ContactLabels.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMedia.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactHistory.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactMerge.vue` | Shared Component | 1 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactNotes.vue` | Shared Component | 1 | 6 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributes.vue` | Shared Component | 1 | 3 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/ContactCustomAttributeItem.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/components/ContactNoteItem.vue` | Shared Component | 2 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/components/story/ContactNoteItem.story.vue` | Shared Component | 0 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Contacts/ContactsSidebar/components/story/fixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/emoji-icon-picker/constants.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/emoji-icon-picker/icons.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIcon.vue` | Shared Component | 11 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/emoji-icon-picker/ColorPalette.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/emoji-icon-picker/EmojiIconPicker.vue` | Shared Component | 4 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/radioCard/RadioCard.vue` | Shared Component | 6 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/radioCard/RadioCard.story.vue` | Shared Component | 0 | 1 | 2 | Sojan Jose |
| `app/javascript/dashboard/components-next/checkbox/Checkbox.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/checkbox/Checkbox.vue` | Shared Component | 14 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/AddLabel.vue` | Shared Component | 2 | 1 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/Label.vue` | Shared Component | 8 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/LabelItem.vue` | Shared Component | 3 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/story/AddLabel.story.vue` | Shared Component | 0 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/story/Label.story.vue` | Shared Component | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/label/story/fixtures.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.story.vue` | Shared Component | 0 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownMenu.vue` | Shared Component | 37 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dropdown-menu/DropdownPrimitives.story.vue` | Shared Component | 0 | 7 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownBody.vue` | Shared Component | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownContainer.vue` | Shared Component | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/dropdown-menu/base/provider.js` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/dropdown-menu/base/index.js` | Utility | 0 | 5 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownSection.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownSeparator.vue` | Shared Component | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/dropdown-menu/base/DropdownItem.vue` | Shared Component | 3 | 2 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/HelpCenter/HelpCenterLayout.vue` | Layout | 5 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.story.vue` | Shared Component | 0 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/CategoryCard/CategoryCard.vue` | Shared Component | 3 | 4 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Portal/portalEmptyStateContent.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Portal/PortalEmptyState.story.vue` | Shared Component | 0 | 1 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Portal/PortalEmptyState.vue` | Shared Component | 2 | 5 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Category/CategoryEmptyState.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Category/categoryEmptyStateContent.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Article/ArticleEmptyState.vue` | Shared Component | 2 | 4 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/EmptyState/Article/ArticleEmptyState.story.vue` | Shared Component | 0 | 1 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.vue` | Shared Component | 2 | 4 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/LocaleCard/LocaleCard.story.vue` | Shared Component | 0 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.vue` | Shared Component | 4 | 11 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/ArticleCard/ArticleCard.story.vue` | Shared Component | 0 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditor.vue` | Shared Component | 2 | 6 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorHeader.vue` | Shared Component | 1 | 8 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorProperties.vue` | Shared Component | 1 | 4 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticleEditorPage/ArticleEditorControls.vue` | Shared Component | 1 | 6 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.story.vue` | Shared Component | 0 | 1 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalSettings.vue` | Shared Component | 2 | 8 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalLayoutContentSettings.vue` | Layout | 1 | 4 | 5 | Pranav |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalBaseSettings.vue` | Shared Component | 1 | 11 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/ConfirmDeletePortalDialog.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/DNSConfigurationDialog.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/PortalConfigurationSettings.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/PortalSettingsPage/AddCustomDomainDialog.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryList.vue` | Shared Component | 1 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.vue` | Shared Component | 2 | 9 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/EditCategoryDialog.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryHeaderControls.vue` | Shared Component | 2 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryDialog.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoryForm.vue` | Shared Component | 2 | 7 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/CategoryPage/CategoriesPage.story.vue` | Shared Component | 0 | 1 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocaleContentDialog.vue` | Shared Component | 1 | 4 | 3 | Pranav |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/AddLocaleDialog.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.story.vue` | Shared Component | 0 | 1 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocaleList.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/LocalePage/LocalesPage.vue` | Shared Component | 2 | 8 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleList.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticleHeaderControls.vue` | Shared Component | 1 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.story.vue` | Shared Component | 0 | 1 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/BulkTranslateDialog.vue` | Shared Component | 1 | 6 | 3 | Pranav |
| `app/javascript/dashboard/components-next/HelpCenter/Pages/ArticlePage/ArticlesPage.vue` | Shared Component | 2 | 18 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.vue` | Shared Component | 2 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/CreatePortalDialog.vue` | Shared Component | 2 | 8 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/HelpCenter/PortalSwitcher/PortalSwitcher.story.vue` | Shared Component | 0 | 1 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/tabbar/TabBar.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/tabbar/TabBar.vue` | Shared Component | 7 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/message/constants.js` | Utility | 21 | 0 | 0 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/message/MessageStatus.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/MessageError.vue` | Shared Component | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/provider.js` | Utility | 27 | 3 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/TranslationToggle.vue` | Shared Component | 2 | 0 | 0 | Khoa Nguyen |
| `app/javascript/dashboard/components-next/message/MessageMeta.vue` | Shared Component | 1 | 5 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/MessageList.vue` | Shared Component | 0 | 5 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/Message.vue` | Shared Component | 7 | 29 | 8 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/chips/File.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/message/chips/Video.vue` | Shared Component | 0 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/chips/Audio.vue` | Shared Component | 0 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/chips/AttachmentChips.vue` | Shared Component | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/chips/Image.vue` | Shared Component | 0 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/MessageBubbles.story.vue` | Shared Component | 0 | 1 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/InstagramBubbles.story.vue` | Shared Component | 0 | 1 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/TextMessages.story.vue` | Shared Component | 0 | 2 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/InstagramMessages.story.vue` | Shared Component | 0 | 2 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/EmailMessages.story.vue` | Shared Component | 0 | 4 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/stories/MediaBubbles.story.vue` | Shared Component | 0 | 1 | 9 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/instagramConversation.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/newsletterEmail.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/emailConversation.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/textWithMedia.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/textOnly.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/fixtures/simpleEmail.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/BaseAttachment.vue` | Shared Component | 4 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/message/bubbles/Contact.vue` | Shared Component | 1 | 4 | 5 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/File.vue` | Shared Component | 1 | 2 | 5 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Activity.vue` | Shared Component | 1 | 3 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Base.vue` | Shared Component | 10 | 6 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Video.vue` | Shared Component | 1 | 5 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Audio.vue` | Shared Component | 1 | 2 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Unsupported.vue` | Shared Component | 1 | 3 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/message/bubbles/Location.vue` | Shared Component | 1 | 2 | 5 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Embed.vue` | Shared Component | 1 | 2 | 4 | Mazen Khalil |
| `app/javascript/dashboard/components-next/message/bubbles/CSAT.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/message/bubbles/Image.vue` | Shared Component | 1 | 6 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Fallback.vue` | Shared Component | 1 | 3 | 4 | Sojan Jose |
| `app/javascript/dashboard/components-next/message/bubbles/Dyte.vue` | Shared Component | 1 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/message/bubbles/Form.vue` | Shared Component | 1 | 4 | 4 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/VoiceCall.vue` | Shared Component | 1 | 10 | 6 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/message/bubbles/InstagramStory.vue` | Shared Component | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Text/Index.vue` | Shared Component | 1 | 5 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Text/FormattedContent.vue` | Shared Component | 3 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Email/Index.vue` | Shared Component | 1 | 5 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/message/bubbles/Email/EmailMeta.vue` | Shared Component | 1 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/NewConversation/ComposeConversation.vue` | Shared Component | 4 | 8 | 9 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsAppOptions.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/EmailOptions.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/AttachmentPreviews.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/ComposeNewConversationForm.vue` | Shared Component | 2 | 11 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/ActionButtons.vue` | Shared Component | 1 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/InboxSelector.vue` | Shared Component | 1 | 4 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/InboxEmptyState.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateSelector.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/ContactSelector.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/MessageEditor.vue` | Shared Component | 1 | 2 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/ContentTemplateForm.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/WhatsappTemplate.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/story/ComposeNewConversationForm.story.vue` | Shared Component | 0 | 2 | 9 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/components/story/fixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/helpers/composeConversationHelper.js` | Utility | 4 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/NewConversation/helpers/specs/composeConversationHelper.spec.js` | Utility | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/changelog-card/GroupedStackedChangelogCard.vue` | Shared Component | 2 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/changelog-card/StackedChangelogCard.vue` | Shared Component | 2 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/changelog-card/GroupedStackedChangelogCard.story.vue` | Shared Component | 0 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/changelog-card/StackedChangelogCard.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/spinner/Spinner.vue` | Shared Component | 50 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components-next/spinner/Spinner.story.vue` | Shared Component | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboBox.vue` | Shared Component | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/combobox/ComboBox.vue` | Shared Component | 20 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/combobox/ComboBoxDropdown.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/combobox/ComboBox.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/combobox/TagMultiSelectComboxBox.story.vue` | Shared Component | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/OtherAttribute.vue` | Shared Component | 3 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/ListAttribute.vue` | Shared Component | 3 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/AttributeBadge.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/DateAttribute.vue` | Shared Component | 3 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/CheckboxAttribute.vue` | Shared Component | 3 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/story/CustomAttributes.story.vue` | Shared Component | 0 | 5 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/CustomAttributes/story/fixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dialog/Dialog.story.vue` | Shared Component | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/dialog/Dialog.vue` | Shared Component | 45 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/popover/Popover.vue` | Shared Component | 5 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/template-preview/CallToActionTemplate.vue` | Shared Component | 1 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/QuickReplyTemplate.vue` | Shared Component | 1 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/CardTemplate.vue` | Shared Component | 1 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/index.js` | Utility | 0 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/CSATTemplate.vue` | Shared Component | 1 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/TemplatePreviewExamples.story.vue` | Shared Component | 0 | 2 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/TemplatePreview.story.vue` | Shared Component | 0 | 2 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/TemplatePreview.vue` | Shared Component | 2 | 6 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/MediaTemplate.vue` | Shared Component | 1 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/TextTemplate.vue` | Shared Component | 0 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/WhatsAppTextTemplate.vue` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/templates/whatsapp-templates.js` | Utility | 0 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/template-preview/templates/twilio-templates.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/inline-input/InlineInput.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/inline-input/InlineInput.vue` | Shared Component | 10 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/content-templates/ContentTemplateParser.vue` | Shared Component | 2 | 3 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/textarea/TextArea.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/textarea/TextArea.vue` | Shared Component | 12 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/call/CallCard.vue` | Shared Component | 2 | 5 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/call/CallCard.story.vue` | Shared Component | 0 | 3 | 5 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/call/FloatingCallWidget.vue` | Shared Component | 1 | 9 | 6 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.story.vue` | Shared Component | 0 | 1 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentPolicyCard/AssignmentPolicyCard.vue` | Shared Component | 2 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AgentCapacityPolicyCard/AgentCapacityPolicyCard.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AgentCapacityPolicyCard/AgentCapacityPolicyCard.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/CardPopover.vue` | Shared Component | 3 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/InboxCapacityLimits.vue` | Shared Component | 2 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/ExclusionRules.vue` | Shared Component | 2 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/DataTable.vue` | Shared Component | 3 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/BaseInfo.vue` | Shared Component | 3 | 3 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/FairDistribution.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/AddDataDropdown.vue` | Shared Component | 5 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/DataTable.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/FairDistribution.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/ExclusionRules.story.vue` | Shared Component | 0 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/BaseInfo.story.vue` | Shared Component | 0 | 1 | 2 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/InboxCapacityLimits.story.vue` | Shared Component | 0 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/AddDataDropdown.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/components/story/CardPopover.story.vue` | Shared Component | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentCard/AssignmentCard.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/AssignmentPolicy/AssignmentCard/AssignmentCard.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/button/constants.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/button/Button.story.vue` | Shared Component | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/button/ConfirmButton.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/button/ConfirmButton.vue` | Shared Component | 2 | 1 | 2 | Sojan Jose |
| `app/javascript/dashboard/components-next/button/Button.vue` | Shared Component | 345 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/table/BaseTable.story.vue` | Shared Component | 0 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/table/BaseTableRow.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/table/BaseTable.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/table/index.js` | Utility | 11 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/table/BaseTableCell.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/avatar/Avatar.story.vue` | Shared Component | 0 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/avatar/Avatar.vue` | Shared Component | 35 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/colorpicker/ColorPicker.vue` | Shared Component | 2 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/switch/Switch.story.vue` | Shared Component | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/switch/Switch.vue` | Shared Component | 15 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.vue` | Shared Component | 2 | 4 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/phonenumberinput/PhoneNumberInput.story.vue` | Shared Component | 0 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlight.vue` | Shared Component | 5 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlight.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlightPopover.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/feature-spotlight/FeatureSpotlightPopover.vue` | Shared Component | 5 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/CampaignLayout.vue` | Layout | 3 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/SMSCampaignDetails.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/CampaignCard.vue` | Shared Component | 4 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/CampaignCard/LiveChatCampaignDetails.vue` | Shared Component | 1 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/EmptyState/WhatsAppCampaignEmptyState.vue` | Shared Component | 1 | 3 | 6 | Aman Kumar |
| `app/javascript/dashboard/components-next/Campaigns/EmptyState/CampaignEmptyStateContent.js` | Utility | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/EmptyState/SMSCampaignEmptyState.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/EmptyState/LiveChatCampaignEmptyState.vue` | Shared Component | 1 | 3 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/ConfirmDeleteCampaignDialog.vue` | Shared Component | 3 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/CampaignList.vue` | Shared Component | 3 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignForm.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/SMSCampaign/SMSCampaignDialog.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignForm.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/WhatsAppCampaign/WhatsAppCampaignDialog.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignDialog.vue` | Shared Component | 1 | 5 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/LiveChatCampaignForm.vue` | Shared Component | 2 | 6 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Campaigns/Pages/CampaignPage/LiveChatCampaign/EditLiveChatCampaignDialog.vue` | Shared Component | 1 | 4 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components-next/select/Select.vue` | Shared Component | 4 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.story.vue` | Shared Component | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/ConditionRow.vue` | Shared Component | 4 | 6 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/ActiveFilterPreview.vue` | Shared Component | 2 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/ConditionRow.story.vue` | Shared Component | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/provider.js` | Utility | 2 | 4 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/ContactsFilter.vue` | Shared Component | 1 | 7 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/operators.js` | Utility | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/ConversationFilter.vue` | Shared Component | 0 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/SaveCustomView.vue` | Shared Component | 0 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/contactProvider.js` | Utility | 1 | 3 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/fixtures/filterTypes.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/helper/filterHelper.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/helper/filterHelper.spec.js` | Utility | 0 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.story.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.story.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.story.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/inputs/SingleSelect.vue` | Shared Component | 4 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/filter/inputs/FilterSelect.vue` | Shared Component | 4 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/filter/inputs/MultiSelect.vue` | Shared Component | 4 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/breadcrumb/Breadcrumb.story.vue` | Shared Component | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/breadcrumb/Breadcrumb.vue` | Shared Component | 10 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/icon/Icon.vue` | Shared Component | 89 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components-next/icon/provider.js` | Utility | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/icon/FileIcon.story.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/icon/Logo.vue` | Shared Component | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components-next/icon/ChannelIcon.vue` | Shared Component | 4 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components-next/icon/FileIcon.vue` | Shared Component | 2 | 0 | 0 | Aakash Bakhle |
| `app/javascript/dashboard/components-next/icon/ChannelIcon.story.vue` | Shared Component | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components-next/icon/specs/provider.spec.js` | Utility | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/ConversationWorkflow/constants.js` | Utility | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/ConversationWorkflow/AttributeListItem.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributes.vue` | Shared Component | 1 | 8 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationResolveAttributesModal.vue` | Shared Component | 2 | 6 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/ConversationWorkflow/ConversationRequiredAttributeItem.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Companies/CompanyCreateDialog.vue` | Shared Component | 2 | 4 | 3 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompaniesDetailsLayout.vue` | Layout | 1 | 2 | 3 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompanySelector.vue` | Shared Component | 1 | 4 | 4 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompaniesListLayout.vue` | Layout | 1 | 2 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyProfileCard.vue` | Shared Component | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/ConfirmCompanyDeleteDialog.vue` | Shared Component | 1 | 1 | 3 | salmonumbrella |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributes.vue` | Shared Component | 0 | 2 | 7 | salmonumbrella |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyCustomAttributeItem.vue` | Shared Component | 1 | 6 | 6 | salmonumbrella |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyContactsSidebar.vue` | Shared Component | 1 | 4 | 4 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyNotesSidebar.vue` | Shared Component | 1 | 5 | 4 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompanyDetail/CompanyHistorySidebar.vue` | Shared Component | 1 | 3 | 6 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/CompanyHeader.vue` | Shared Component | 1 | 4 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanyMoreActions.vue` | Shared Component | 1 | 2 | 5 | Sojan Jose |
| `app/javascript/dashboard/components-next/Companies/CompaniesHeader/components/CompanySortMenu.vue` | Shared Component | 1 | 2 | 3 | salmonumbrella |
| `app/javascript/dashboard/components-next/Companies/CompaniesCard/CompaniesCard.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Editor/Editor.vue` | Shared Component | 14 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/banner/Banner.vue` | Shared Component | 7 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/whatsapp/WhatsAppTemplateParser.vue` | Shared Component | 3 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/SharedAttachments/Files.vue` | Shared Component | 2 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/SharedAttachments/Media.vue` | Shared Component | 2 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/InboxName.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/SidepanelSwitch.vue` | Shared Component | 2 | 6 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationRequiredEmpty.vue` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components-next/Conversation/Sla/SLACardLabel.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/MessagePreview.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCardExpanded.vue` | Shared Component | 1 | 11 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/UnreadBadge.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardContent.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.story.vue` | Shared Component | 0 | 1 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreview.vue` | Shared Component | 1 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/ConversationCard.vue` | Shared Component | 3 | 8 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/SLACardLabel.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardMessagePreviewWithMeta.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabelsV5.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardAvatar.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardPriorityIcon.vue` | Shared Component | 5 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardLabels.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/VoiceCallStatus.vue` | Shared Component | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components-next/Conversation/ConversationCard/CardStatusIcon.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/mixins/fileUploadMixin.js` | Utility | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/mixins/specs/fileUploadMixin.spec.js` | Utility | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/constants/globals.js` | Utility | 47 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/constants/automation.js` | Utility | 2 | 0 | 0 | Clairton Rodrigo Heinzen |
| `app/javascript/dashboard/constants/sessionStorage.js` | Utility | 5 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/constants/appEvents.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/constants/installationTypes.js` | Utility | 11 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/constants/editor.js` | Utility | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/constants/localStorage.js` | Utility | 15 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/constants/permissions.js` | Utility | 2 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/stores/companies.spec.js` | Context / Store | 0 | 2 | 3 | salmonumbrella |
| `app/javascript/dashboard/stores/companies.js` | Context / Store | 5 | 3 | 2 | Sojan Jose |
| `app/javascript/dashboard/stores/calls.js` | Context / Store | 7 | 4 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components/IntersectionObserver.vue` | Shared Component | 2 | 0 | 0 | Khoa Nguyen |
| `app/javascript/dashboard/components/ConversationList.vue` | Shared Component | 1 | 5 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components/SettingsSection.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/policy.vue` | Shared Component | 15 | 1 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/NetworkNotification.vue` | Shared Component | 1 | 3 | 2 | Pranav Raj S |
| `app/javascript/dashboard/components/Code.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ChatList.vue` | Shared Component | 1 | 25 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components/index.js` | Utility | 1 | 18 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/CustomAttribute.vue` | Shared Component | 1 | 7 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/CustomBrandPolicyWrapper.vue` | Shared Component | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components/ChatListHeader.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/SnackbarContainer.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/CustomSnoozeModal.vue` | Shared Component | 3 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components/ModalHeader.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ConversationItem.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/Modal.vue` | Shared Component | 6 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/components/Snackbar.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ChannelSelector.vue` | Shared Component | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/HelperTextPopup.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Banner.vue` | Shared Component | 5 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/PreviewCard.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DateRangePicker.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DateTimePicker.vue` | Shared Component | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components/ui/Label.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Wizard.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/TimeAgo.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/ContextMenu.vue` | Shared Component | 4 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Tabs/Tabs.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Tabs/TabsItem.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownList.vue` | Shared Component | 4 | 4 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownListItemButton.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownLoadingState.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownSearch.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownEmptyState.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/Dropdown/DropdownButton.vue` | Shared Component | 6 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/DatePicker.vue` | Shared Component | 5 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/DatePickerButton.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarFooter.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarDateInput.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarDateRange.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarYear.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarAction.vue` | Shared Component | 3 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarWeek.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarMonth.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/components/CalendarWeekLabel.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/helpers/DatePickerHelper.js` | Utility | 8 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/ui/DatePicker/helpers/specs/DatePickerHelper.spec.js` | Utility | 0 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components/buttons/ResolveAction.vue` | Shared Component | 1 | 11 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/app/versionCheckHelper.js` | Utility | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components/app/UpdateBanner.vue` | Shared Component | 1 | 5 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/app/PendingEmailVerificationBanner.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/app/StatusBanner.vue` | Shared Component | 1 | 5 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components/app/PaymentPendingBanner.vue` | Shared Component | 1 | 3 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/app/AddAccountModal.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/app/specs/versionCheckHelper.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/components/copilot/CopilotContainer.vue` | Shared Component | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/auth/MfaVerification.vue` | Shared Component | 1 | 7 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components/auth/SessionLimitOverlay.vue` | Shared Component | 1 | 2 | 2 | Vishnu Narayanan |
| `app/javascript/dashboard/components/Accordion/AccordionItem.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/table/Pagination.vue` | Shared Component | 3 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/table/BaseCell.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/table/SortButton.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components/table/Table.vue` | Shared Component | 3 | 1 | 1 | Pranav |
| `app/javascript/dashboard/components/base/Hotkey.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/BackButton.vue` | Shared Component | 6 | 1 | 17 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/TableFooterResults.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/ChannelItem.vue` | Shared Component | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/components/widgets/UserAvatarWithName.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/TableFooter.vue` | Shared Component | 2 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/SettingIntroBanner.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/AttachmentsPreview.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/ThumbnailGroup.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/AILoader.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/AutomationFileInput.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/InboxName.vue` | Shared Component | 2 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/TableFooterPagination.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/TableHeaderCell.vue` | Shared Component | 2 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components/widgets/AutomationActionTeamMessageInput.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/ShowMore.vue` | Shared Component | 2 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components/widgets/FeatureToggle.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/AutomationActionInput.vue` | Shared Component | 2 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/VideoCallButton.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/ChatTypeTabs.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/EmptyState.vue` | Shared Component | 7 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/ColorPicker.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/LoadingState.vue` | Shared Component | 6 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/forms/PhoneInput.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/forms/Input.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/constants.js` | Utility | 7 | 0 | 0 | Suhavi Sandhu |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyBottomPanel.vue` | Shared Component | 1 | 7 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotReplyBottomPanel.vue` | Shared Component | 2 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/WootWriter/ReplyTopPanel.vue` | Shared Component | 1 | 8 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/Editor.vue` | Shared Component | 9 | 15 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotMenuBar.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/keyboardEmojiSelector.vue` | Shared Component | 1 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/EditorModeToggle.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/WootWriter/CopilotEditor.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/SlashCommandMenu.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/FullEditor.vue` | Shared Component | 1 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/WootWriter/AudioRecorder.vue` | Shared Component | 1 | 2 | 2 | giquieu |
| `app/javascript/dashboard/components/widgets/WootWriter/utils/webmOpusToOgg.js` | Utility | 1 | 0 | 0 | Gabriel Jablonski |
| `app/javascript/dashboard/components/widgets/WootWriter/utils/audioConversionUtils.js` | Utility | 1 | 1 | 1 | Gabriel Jablonski |
| `app/javascript/dashboard/components/widgets/mentions/MentionBox.vue` | Shared Component | 3 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/FilterInput/FilterOperatorTypes.js` | Utility | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/components/widgets/FilterInput/FilterOperatorTypes.spec.js` | Utility | 0 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/components/widgets/DashboardApp/Frame.vue` | Shared Component | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/components/widgets/modal/constants.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/modal/WootKeyShortcutModal.vue` | Shared Component | 1 | 3 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/modal/ConfirmationModal.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/modal/DeleteModal.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/modal/ConfirmDeleteModal.vue` | Shared Component | 2 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/conversation/MessagePreview.vue` | Shared Component | 2 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/MessagesView.vue` | Shared Component | 1 | 17 | 7 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrdersList.vue` | Shared Component | 1 | 4 | 2 | Pranav |
| `app/javascript/dashboard/components/widgets/conversation/FilterItem.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/MoreActions.vue` | Shared Component | 1 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/MessageSignatureMissingAlert.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/CopilotEditorSection.vue` | Shared Component | 2 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/VariableList.vue` | Shared Component | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ResizableEditorWrapper.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/QuotedEmailPreview.vue` | Shared Component | 1 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBox.vue` | Shared Component | 1 | 33 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCard.vue` | Shared Component | 2 | 10 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/OnboardingFeatureCard.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBasicFilter.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` | Shared Component | 1 | 11 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/EmailTranscriptModal.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ReplyEmailHead.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ReplyToMessage.vue` | Shared Component | 1 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/CannedResponse.vue` | Shared Component | 1 | 1 | 4 | Pranav Raj S |
| `app/javascript/dashboard/components/widgets/conversation/OnboardingView.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationCallButton.vue` | Shared Component | 1 | 7 | 5 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components/widgets/conversation/TagAgents.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` | Shared Component | 2 | 4 | 8 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ConversationSidebar.vue` | Shared Component | 2 | 3 | 12 | Pranav |
| `app/javascript/dashboard/components/widgets/conversation/TagTools.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/VoiceCallStatus.vue` | Shared Component | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/components/widgets/conversation/ShopifyOrderItem.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ReplyBoxBanner.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/conversationCardComponents/CardLabels.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/TemplatesPicker.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/WhatsAppTemplateReply.vue` | Shared Component | 1 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/WhatsappTemplates/Modal.vue` | Shared Component | 1 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/conversation/copilot/CaptainLoader.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearIssueItem.vue` | Shared Component | 1 | 4 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinkIssue.vue` | Shared Component | 1 | 7 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssueHeader.vue` | Shared Component | 1 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateIssue.vue` | Shared Component | 1 | 7 | 5 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/IssuesList.vue` | Shared Component | 1 | 9 | 7 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/validations.js` | Utility | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/LinearSetupCTA.vue` | Shared Component | 1 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/linear/CreateOrLinkIssue.vue` | Shared Component | 1 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/linear/SearchableDropdown.vue` | Shared Component | 1 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/Index.vue` | Shared Component | 2 | 7 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/agentLoadingPlaceholder.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/menuItemWithSubmenu.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/contextMenu/menuItem.vue` | Shared Component | 3 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAEventItem.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/components/widgets/conversation/components/SLACardLabel.vue` | Shared Component | 2 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/components/GalleryView.vue` | Shared Component | 6 | 7 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/components/SLAPopoverCard.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/EmptyState/FeaturePlaceholder.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/components/widgets/conversation/EmptyState/EmptyStateMessage.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/EmptyState/EmptyState.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/Index.vue` | Shared Component | 1 | 12 | 6 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkLabelActions.vue` | Shared Component | 2 | 4 | 5 | Sojan Jose |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkTeamActions.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkUpdateActions.vue` | Shared Component | 1 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/conversationBulkActions/BulkAgentActions.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesModal.vue` | Shared Component | 1 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/ContentTemplates/ContentTemplatesPicker.vue` | Shared Component | 1 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/advancedFilterItems/index.js` | Utility | 4 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/components/widgets/conversation/advancedFilterItems/languages.js` | Utility | 11 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/components/widgets/conversation/advancedFilterItems/specs/advancedFilterItems.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/components/widgets/conversation/advancedFilterItems/specs/languages.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/components/widgets/conversation/helpers/scrollTopCalculationHelper.js` | Utility | 2 | 0 | 0 | Anubhav Jain |
| `app/javascript/dashboard/components/widgets/conversation/helpers/emailHeadHelper.js` | Utility | 2 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/components/widgets/conversation/helpers/specs/scrollTopCalculationHelper.spec.js` | Utility | 0 | 1 | 1 | Anubhav Jain |
| `app/javascript/dashboard/components/widgets/conversation/helpers/specs/emailHeadHelper.spec.js` | Utility | 0 | 1 | 1 | Jordan Brough |
| `app/javascript/dashboard/components/widgets/conversation/conversation/LabelSuggestion.vue` | Shared Component | 1 | 8 | 4 | Shivam Mishra |
| `app/javascript/dashboard/api/teams.js` | Utility | 3 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/api/automation.js` | Utility | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/onboarding.js` | Utility | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/inboxHealth.js` | Utility | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/agentCapacityPolicies.js` | Utility | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/ApiClient.js` | Utility | 111 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/api/campaigns.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/agents.js` | Utility | 2 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/api/assignableAgents.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/liveReports.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/customRole.js` | Utility | 1 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/contactNotes.js` | Utility | 1 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/inboxes.js` | Utility | 7 | 1 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/api/samlSettings.js` | Utility | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/customViews.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/labels.js` | Utility | 2 | 1 | 3 | Shivam Mishra |
| `app/javascript/dashboard/api/auth.js` | Utility | 8 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/yearInReview.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/mfa.js` | Utility | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/assignmentPolicies.js` | Utility | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/attributes.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/bulkActions.js` | Utility | 3 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/api/contacts.js` | Utility | 13 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/accountActions.js` | Utility | 2 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/api/companies.js` | Utility | 4 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/cannedResponse.js` | Utility | 1 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/CacheEnabledApiClient.js` | Utility | 3 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/api/webhooks.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/channels.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/account.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/conversations.js` | Utility | 4 | 1 | 1 | Sony Mathew |
| `app/javascript/dashboard/api/csatReports.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/endPoints.js` | Utility | 3 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/api/slaReports.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/integrations.js` | Utility | 3 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/notion_auth.js` | Utility | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/changelog.js` | Utility | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/inboxMembers.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/notificationSubscription.js` | Utility | 1 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/auditLogs.js` | Utility | 1 | 1 | 1 | Vishnu Narayanan |
| `app/javascript/dashboard/api/dashboardApps.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/userNotificationSettings.js` | Hook | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/search.js` | Utility | 2 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/api/notifications.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/reports.js` | Utility | 3 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/summaryReports.js` | Utility | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/macros.js` | Utility | 2 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/api/sla.js` | Utility | 1 | 1 | 1 | Vishnu Narayanan |
| `app/javascript/dashboard/api/agentBots.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/captain/assistant.js` | Utility | 2 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/tools.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/captain/copilotMessages.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/messageReports.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/response.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/preferences.js` | Utility | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/captain/inboxes.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/scenarios.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/captain/bulkActions.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/api/captain/tasks.js` | Utility | 3 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/captain/copilotThreads.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/captain/customTools.js` | Utility | 2 | 1 | 1 | Aakash Bakhle |
| `app/javascript/dashboard/api/captain/document.js` | Utility | 2 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/inbox/conversation.js` | Utility | 6 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/inbox/message.js` | Utility | 4 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/enterprise/account.js` | Utility | 3 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/enterprise/specs/account.spec.js` | Utility | 0 | 2 | 2 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/specs/agentBots.spec.js` | Utility | 0 | 2 | 2 | Sojan Jose |
| `app/javascript/dashboard/api/specs/slaReports.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/article.spec.js` | Utility | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/accountActions.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/userNotificationSettings.spec.js` | Hook | 0 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/automation.spec.js` | Utility | 0 | 2 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/api/specs/search.spec.js` | Utility | 0 | 2 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/api/specs/macros.spec.js` | Utility | 0 | 2 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/api/specs/agentCapacityPolicies.spec.js` | Utility | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/api/specs/tiktokClient.spec.js` | Utility | 0 | 2 | 2 | Mazen Khalil |
| `app/javascript/dashboard/api/specs/integrations.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/companies.spec.js` | Utility | 0 | 2 | 2 | salmonumbrella |
| `app/javascript/dashboard/api/specs/conversations.spec.js` | Utility | 0 | 2 | 2 | Sony Mathew |
| `app/javascript/dashboard/api/specs/assignmentPolicies.spec.js` | Utility | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/api/specs/account.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/assignableAgents.spec.js` | Utility | 0 | 1 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/webhook.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/endPoints.spec.js` | Utility | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/labels.spec.js` | Utility | 0 | 2 | 4 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/notifications.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/inboxes.spec.js` | Utility | 0 | 2 | 4 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/contacts.spec.js` | Utility | 0 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/portals.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/agents.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/csatReports.spec.js` | Utility | 0 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/teams.spec.js` | Utility | 0 | 2 | 4 | Nithin David Thomas |
| `app/javascript/dashboard/api/specs/campaign.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/reports.spec.js` | Utility | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/api/specs/bulkAction.spec.js` | Utility | 0 | 2 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/api/specs/dashboardApps.spec.js` | Utility | 0 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/api/specs/inbox/conversation.spec.js` | Utility | 0 | 2 | 2 | Sojan Jose |
| `app/javascript/dashboard/api/specs/inbox/message.spec.js` | Utility | 0 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/api/specs/helpCenter/categories.spec.js` | Utility | 0 | 2 | 3 | Sojan Jose |
| `app/javascript/dashboard/api/specs/channel/webChannel.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/channel/twitterClient.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/channel/twilioChannel.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/specs/channel/fbChannel.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/integrations/dyte.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/api/specs/integrations/linear.spec.js` | Utility | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/helpCenter/categories.js` | Utility | 3 | 1 | 2 | Sojan Jose |
| `app/javascript/dashboard/api/helpCenter/portals.js` | Utility | 5 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/helpCenter/articles.js` | Utility | 4 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/channel/fbChannel.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/channel/tiktokClient.js` | Utility | 3 | 1 | 1 | Mazen Khalil |
| `app/javascript/dashboard/api/channel/twilioChannel.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/channel/instagramClient.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/channel/googleClient.js` | Utility | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/api/channel/webChannel.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/channel/twitterClient.js` | Utility | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/api/channel/whatsappChannel.js` | Utility | 2 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/channel/microsoftClient.js` | Utility | 2 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/api/channel/voice/voiceAPIClient.js` | Utility | 2 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/api/channel/voice/twilioVoiceClient.js` | Utility | 3 | 1 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/channel/whatsapp/whatsappCallsAPI.js` | Utility | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/api/integrations/linear.js` | Utility | 4 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/api/integrations/shopify.js` | Utility | 1 | 1 | 1 | Pranav |
| `app/javascript/dashboard/api/integrations/dyte.js` | Utility | 3 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/i18n/index.js` | Utility | 4 | 41 | 2 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sl/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sl/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sl/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sk/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sk/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sk/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sk/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sk/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/integrationApps.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sk/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ur/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ur/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ur/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pl/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pl/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pl/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pl/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/pl/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pl/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pl/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pl/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/vi/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/vi/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/vi/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/webhooks.json` | Shared Component | 0 | 0 | 0 | ı ɑɷ ɖεɾεƙ |
| `app/javascript/dashboard/i18n/locale/vi/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/vi/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/vi/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/integrationApps.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/vi/bulkActions.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sq/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sq/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sq/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sv/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sv/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sv/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sv/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/sv/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sv/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sv/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sv/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/he/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/he/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/he/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/he/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/he/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ms/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ms/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ms/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ms/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ms/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hy/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hy/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/webhooks.json` | Shared Component | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/am/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/am/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/am/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/am/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/am/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/am/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/am/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/da/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/da/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/da/emoji.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/da/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/generalSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/da/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/da/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/da/bulkActions.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/no/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/no/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/no/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/no/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/no/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/no/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/no/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/no/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt_BR/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt_BR/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/webhooks.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt_BR/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt_BR/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/yearInReview.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/index.js` | Utility | 1 | 44 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt_BR/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt_BR/snooze.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt_BR/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt_BR/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt_BR/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/contentTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt_BR/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt_BR/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ja/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ja/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ja/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ja/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ja/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ja/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/el/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/el/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/el/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/el/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/el/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/el/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/el/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ur_IN/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/ur_IN/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ur_IN/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ur_IN/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lv/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lv/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lv/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/lv/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lv/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/lv/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lv/bulkActions.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/mfa.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/it/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/it/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/it/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/it/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/it/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ca/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ca/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/webhooks.json` | Shared Component | 0 | 0 | 0 | Fernando Verdugo |
| `app/javascript/dashboard/i18n/locale/ca/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ca/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ca/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ca/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_TW/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_TW/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/datePicker.json` | Shared Component | 1 | 0 | 0 | YJack0000 |
| `app/javascript/dashboard/i18n/locale/zh_TW/emoji.json` | Shared Component | 1 | 0 | 0 | YJack0000 |
| `app/javascript/dashboard/i18n/locale/zh_TW/webhooks.json` | Shared Component | 0 | 0 | 0 | snowild |
| `app/javascript/dashboard/i18n/locale/zh_TW/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/yearInReview.json` | Shared Component | 0 | 0 | 0 | YJack0000 |
| `app/javascript/dashboard/i18n/locale/zh_TW/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/index.js` | Utility | 1 | 41 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/snooze.json` | Shared Component | 1 | 0 | 0 | YJack0000 |
| `app/javascript/dashboard/i18n/locale/zh_TW/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/resetPassword.json` | Shared Component | 1 | 0 | 0 | YJack0000 |
| `app/javascript/dashboard/i18n/locale/zh_TW/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_TW/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/integrationApps.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_TW/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/is/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/is/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/is/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/is/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/index.js` | Utility | 1 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/is/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/is/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/is/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/is/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/is/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/is/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/cs/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/cs/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/cs/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/cs/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/cs/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/cs/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/cs/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ru/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ru/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ru/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ru/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ru/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ru/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ru/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tl/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tl/bulkActions.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ro/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ro/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ro/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_CN/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_CN/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/yearInReview.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_CN/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh_CN/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_CN/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh_CN/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh_CN/bulkActions.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sh/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sh/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sh/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/pt/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/pt/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/pt/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/zh/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/zh/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/report.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/index.js` | Utility | 0 | 15 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/integrations.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/chatlist.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/zh/login.json` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/i18n/locale/zh/generalSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/zh/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/uk/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/uk/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/uk/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sr/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/index.js` | Utility | 1 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sr/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sr/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sr/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/sr/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/sr/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/sr/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ml/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ml/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ml/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/webhooks.json` | Shared Component | 0 | 0 | 0 | Vishnu Narayanan |
| `app/javascript/dashboard/i18n/locale/ml/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ml/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/ml/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ml/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ml/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ml/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ar/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ar/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ar/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ar/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ar/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ar/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hr/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hr/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hr/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/hr/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hr/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hr/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/hu/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hu/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hu/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hu/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/nl/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/nl/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/nl/emoji.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/nl/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/nl/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/nl/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bg/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bg/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bg/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/bg/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/bg/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/bg/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bg/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bg/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bg/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/helpCenter.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/campaign.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/signup.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/attributesMgmt.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/mfa.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/onboarding.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/agentMgmt.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/general.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/datePicker.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/emoji.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/report.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/settings.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/contactFilters.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/search.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/conversation.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/inbox.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/teamsSettings.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/integrations.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/chatlist.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/sla.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/macros.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/login.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/generalSettings.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/customRole.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/resetPassword.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/auditLogs.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/companies.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/cannedMgmt.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/agentBots.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/components.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/automation.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/contact.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/inboxMgmt.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/whatsappTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/advancedFilters.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/csatMgmt.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/setNewPassword.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/bn/labelsMgmt.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/integrationApps.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/bn/bulkActions.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/index.js` | Utility | 0 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ne/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ne/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ne/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hi/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hi/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hi/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hi/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/hi/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/hi/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/hi/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ka/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/ka/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ka/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ka/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/de/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/de/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/webhooks.json` | Shared Component | 0 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/i18n/locale/de/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/de/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/de/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/de/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/integrationApps.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/de/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/helpCenter.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/index.js` | Utility | 0 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/az/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/sla.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/macros.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/customRole.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/az/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/az/bulkActions.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/emoji.json` | Shared Component | 1 | 0 | 0 | Jungu Lee |
| `app/javascript/dashboard/i18n/locale/ko/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/yearInReview.json` | Shared Component | 0 | 0 | 0 | Jungu Lee |
| `app/javascript/dashboard/i18n/locale/ko/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/snooze.json` | Shared Component | 0 | 0 | 0 | Jungu Lee |
| `app/javascript/dashboard/i18n/locale/ko/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/customRole.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/resetPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Jungu Lee |
| `app/javascript/dashboard/i18n/locale/ko/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ko/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ko/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ko/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fi/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fi/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fi/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/report.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fi/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fi/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fi/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fi/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/id/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/id/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/id/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/id/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/id/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/id/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/id/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/id/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fr/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fr/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fr/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fr/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fr/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fr/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fr/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/es/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/es/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/emoji.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/es/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/generalSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/es/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/es/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/es/bulkActions.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/et/helpCenter.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/campaign.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/signup.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/general.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/report.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/settings.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/yearInReview.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/conversation.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/index.js` | Utility | 1 | 43 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/et/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/snooze.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/integrations.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/chatlist.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/sla.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/macros.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/generalSettings.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/customRole.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/agentBots.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/components.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/automation.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/contact.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/contentTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/et/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/et/bulkActions.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/en/helpCenter.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/campaign.json` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/i18n/locale/en/signup.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/en/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/mfa.json` | Shared Component | 1 | 0 | 0 | Tanmay Deep Sharma |
| `app/javascript/dashboard/i18n/locale/en/onboarding.json` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/i18n/locale/en/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/general.json` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/i18n/locale/en/datePicker.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/emoji.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/webhooks.json` | Shared Component | 0 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/i18n/locale/en/report.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/en/settings.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/contactFilters.json` | Shared Component | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/i18n/locale/en/yearInReview.json` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/i18n/locale/en/search.json` | Shared Component | 1 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/i18n/locale/en/sessionLimit.json` | Shared Component | 1 | 0 | 0 | Vishnu Narayanan |
| `app/javascript/dashboard/i18n/locale/en/conversation.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/inbox.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/index.js` | Utility | 1 | 44 | 1 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/snooze.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/integrations.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/chatlist.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/en/sla.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/macros.json` | Shared Component | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/i18n/locale/en/login.json` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/i18n/locale/en/generalSettings.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/customRole.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/en/auditLogs.json` | Shared Component | 1 | 0 | 0 | Vishnu Narayanan |
| `app/javascript/dashboard/i18n/locale/en/companies.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/i18n/locale/en/agentBots.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/components.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/automation.json` | Shared Component | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/i18n/locale/en/contact.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/en/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/i18n/locale/en/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/i18n/locale/en/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Hricha Shandily |
| `app/javascript/dashboard/i18n/locale/en/contentTemplates.json` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/i18n/locale/en/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/integrationApps.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/i18n/locale/en/bulkActions.json` | Shared Component | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/i18n/locale/fa/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fa/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fa/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/datePicker.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/webhooks.json` | Shared Component | 0 | 0 | 0 | Ali Ghanavatian |
| `app/javascript/dashboard/i18n/locale/fa/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fa/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/companies.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fa/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/fa/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/fa/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/fa/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/campaign.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/signup.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lt/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lt/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lt/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/webhooks.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/settings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/conversation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/index.js` | Utility | 1 | 40 | 1 | Captain |
| `app/javascript/dashboard/i18n/locale/lt/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/lt/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/chatlist.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/contact.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/lt/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ta/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ta/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ta/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ta/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/ta/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/ta/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/ta/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/ta/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/mfa.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/th/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/th/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/th/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/contactFilters.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/th/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/resetPassword.json` | Shared Component | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/i18n/locale/th/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/th/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/th/integrationApps.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/th/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/helpCenter.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/campaign.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/signup.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/attributesMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/mfa.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/onboarding.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tr/agentMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/general.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/datePicker.json` | Shared Component | 1 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tr/emoji.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/webhooks.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/report.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/settings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/contactFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/yearInReview.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/search.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/conversation.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/inbox.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/index.js` | Utility | 1 | 40 | 1 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/teamsSettings.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/snooze.json` | Shared Component | 0 | 0 | 0 | Captain |
| `app/javascript/dashboard/i18n/locale/tr/integrations.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/chatlist.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/sla.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/macros.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/login.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/generalSettings.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/customRole.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/resetPassword.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/auditLogs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/companies.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/cannedMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/agentBots.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/components.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/automation.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/contact.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/inboxMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/whatsappTemplates.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/advancedFilters.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/csatMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/setNewPassword.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/i18n/locale/tr/contentTemplates.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/labelsMgmt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/integrationApps.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/i18n/locale/tr/bulkActions.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/dashboard/modules/contact/ContactMergeModal.vue` | Shared Component | 1 | 6 | 6 | Shivam Mishra |
| `app/javascript/dashboard/modules/contact/ContactDeleteModal.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/modules/contact/components/MergeContact.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/modules/contact/components/MergeContactSummary.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/search.routes.js` | Utility | 1 | 2 | 9 | Shivam Mishra |
| `app/javascript/dashboard/modules/search/components/SearchTabs.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchResultSection.vue` | Shared Component | 4 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchResultArticlesList.vue` | Shared Component | 1 | 3 | 3 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/components/SearchResultArticleItem.vue` | Shared Component | 1 | 5 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/components/SearchContactAgentSelector.vue` | Shared Component | 1 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchResultContactItem.vue` | Shared Component | 1 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/MessageContent.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchFilters.vue` | Shared Component | 1 | 4 | 6 | Khoa Nguyen |
| `app/javascript/dashboard/modules/search/components/SearchHeader.vue` | Shared Component | 1 | 6 | 7 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchView.vue` | Shared Component | 1 | 16 | 8 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/TranscribedText.vue` | Shared Component | 1 | 1 | 1 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationItem.vue` | Shared Component | 1 | 6 | 2 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/RecentSearches.vue` | Shared Component | 1 | 4 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/components/SearchResultConversationsList.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchDateRangeSelector.vue` | Shared Component | 1 | 3 | 5 | Khoa Nguyen |
| `app/javascript/dashboard/modules/search/components/SearchResultMessagesList.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchResultContactsList.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchInboxSelector.vue` | Shared Component | 1 | 4 | 5 | Khoa Nguyen |
| `app/javascript/dashboard/modules/search/components/SearchInput.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/modules/search/components/SearchResultMessageItem.vue` | Shared Component | 1 | 8 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/helpers/searchHelper.js` | Utility | 3 | 1 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/modules/search/helpers/specs/searchHelper.spec.js` | Utility | 0 | 1 | 2 | Vinay Keerthi |
| `app/javascript/dashboard/modules/conversations/components/ReportCaptainMessageDialog.vue` | Shared Component | 1 | 5 | 3 | Pranav |
| `app/javascript/dashboard/modules/conversations/components/MessageContextMenu.vue` | Shared Component | 1 | 10 | 7 | Sivin Varghese |
| `app/javascript/dashboard/modules/widget-preview/components/WidgetHead.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/modules/widget-preview/components/WidgetFooter.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/modules/widget-preview/components/Widget.vue` | Shared Component | 1 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/modules/widget-preview/components/WidgetBody.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/portalHelper.js` | Utility | 11 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/Timer.js` | Utility | 2 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/helper/auditlogHelper.js` | Utility | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/helper/snoozeHelpers.js` | Utility | 5 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/editorHelper.js` | Utility | 3 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/scriptHelpers.js` | Utility | 1 | 3 | 8 | Pranav Raj S |
| `app/javascript/dashboard/helper/customViewsHelper.js` | Utility | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/routeHelpers.js` | Utility | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/agentHelper.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/themeHelper.js` | Utility | 4 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/flag.js` | Utility | 1 | 0 | 0 | David Kubeš |
| `app/javascript/dashboard/helper/templateHelper.js` | Utility | 0 | 0 | 0 | Aguinaldo Tupy |
| `app/javascript/dashboard/helper/preChat.js` | Utility | 1 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/helper/states.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/helper/downloadHelper.js` | Utility | 11 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/helper/facebookScopes.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/helper/labelColor.js` | Utility | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/helper/emailQuoteExtractor.js` | Utility | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/actionQueryGenerator.js` | Utility | 3 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/helper/permissionsHelper.js` | Utility | 2 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/helper/sidebarSort.js` | Utility | 1 | 0 | 0 | Sony Mathew |
| `app/javascript/dashboard/helper/featureHelper.js` | Utility | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/helper/automationHelper.js` | Utility | 2 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/filterQueryGenerator.js` | Utility | 7 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/helper/validations.js` | Utility | 4 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/commons.js` | Utility | 10 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/quotedEmailHelper.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/voice.js` | Utility | 2 | 4 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/helper/uploadHelper.js` | Utility | 6 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/URLHelper.js` | Utility | 61 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/helper/APIHelper.js` | Utility | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/helper/pushHelper.js` | Utility | 0 | 3 | 2 | Pranav Raj S |
| `app/javascript/dashboard/helper/inbox.js` | Utility | 38 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/conversationHelper.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/actionCable.js` | Utility | 2 | 10 | 8 | Pranav Raj S |
| `app/javascript/dashboard/helper/DOMHelpers.js` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/ReconnectService.js` | Utility | 2 | 2 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/markdownEmbeds.js` | Utility | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/CacheHelper/version.js` | Utility | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/CacheHelper/DataManager.js` | Utility | 2 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/AudioNotificationStore.js` | Utility | 2 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/AudioAlerts/faviconHelper.js` | Utility | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/helper/AudioAlerts/AudioMessageHelper.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/DashboardAudioNotificationHelper.js` | Utility | 2 | 7 | 7 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/WindowVisibilityHelper.js` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/specs/WindowVisibilityHelper.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/specs/AudioMessageHelper.spec.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/AudioAlerts/specs/AudioNotificationStore.spec.js` | Utility | 0 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/templateHelper.spec.js` | Utility | 0 | 1 | 1 | Aguinaldo Tupy |
| `app/javascript/dashboard/helper/specs/conversationHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/macrosFixtures.js` | Utility | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/helper/specs/ReconnectService.spec.js` | Utility | 0 | 3 | 2 | Pranav |
| `app/javascript/dashboard/helper/specs/validations.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/themeHelper.spec.js` | Utility | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/helper/specs/editorHelper.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/routeHelpers.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/uploadHelper.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/specs/preChat.spec.js` | Utility | 0 | 1 | 1 | Surabhi Suman |
| `app/javascript/dashboard/helper/specs/flag.spec.js` | Utility | 0 | 1 | 1 | David Kubeš |
| `app/javascript/dashboard/helper/specs/customViewsHelper.spec.js` | Utility | 0 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/editorContentHelper.spec.js` | Utility | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/commons.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/snoozeDateParser.spec.js` | Utility | 0 | 0 | 0 | salmonumbrella |
| `app/javascript/dashboard/helper/specs/filterQueryGenerator.spec.js` | Utility | 0 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/helper/specs/downloadHelper.spec.js` | Utility | 0 | 1 | 1 | Pranav Raj S |
| `app/javascript/dashboard/helper/specs/URLHelper.spec.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/helper/specs/automationHelper.spec.js` | Utility | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/permissionsHelper.spec.js` | Utility | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/helper/specs/actionQueryGenerator.spec.js` | Utility | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/helper/specs/DOMHelpers.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/specs/auditlogHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/snoozeHelpers.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/macrosHelper.spec.js` | Utility | 0 | 2 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/helper/specs/sidebarSort.spec.js` | Utility | 0 | 0 | 0 | Sony Mathew |
| `app/javascript/dashboard/helper/specs/inbox.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/emailQuoteExtractor.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/specs/Timer.spec.js` | Utility | 0 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/helper/specs/actionCable.spec.js` | Utility | 0 | 1 | 9 | Sony Mathew |
| `app/javascript/dashboard/helper/specs/agentHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/quotedEmailHelper.spec.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/specs/portalHelper.spec.js` | Utility | 0 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/helper/specs/inboxFixture.js` | Utility | 1 | 0 | 0 | Surabhi Suman |
| `app/javascript/dashboard/helper/specs/CacheHelper/DataManger.spec.js` | Utility | 0 | 1 | 2 | Pranav |
| `app/javascript/dashboard/helper/specs/fixtures/conversationFixtures.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/fixtures/automationFixtures.js` | Utility | 0 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/specs/fixtures/agentFixtures.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/AnalyticsHelper/events.js` | Utility | 54 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/helper/AnalyticsHelper/index.js` | Utility | 16 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/helper/AnalyticsHelper/specs/events.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/helper/AnalyticsHelper/specs/helper.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/helper/commandbar/events.js` | Utility | 5 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/commandbar/icons.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/commandbar/actions.js` | Utility | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/helper/snoozeDateParser/tokenMaps.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/snoozeDateParser/index.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/snoozeDateParser/suggestions.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/helper/snoozeDateParser/localization.js` | Utility | 0 | 2 | 1 | salmonumbrella |
| `app/javascript/dashboard/helper/snoozeDateParser/parser.js` | Utility | 1 | 0 | 0 | salmonumbrella |
| `app/javascript/dashboard/routes/index.js` | Utility | 18 | 6 | 16 | Pranav Raj S |
| `app/javascript/dashboard/routes/index.spec.js` | Utility | 0 | 2 | 17 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/Dashboard.vue` | Shared Component | 1 | 12 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` | Utility | 1 | 15 | 15 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/SettingsSubPageHeader.vue` | Shared Component | 16 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/SettingsHeader.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/SettingsWrapper.vue` | Shared Component | 21 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/SettingsLayout.vue` | Layout | 31 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` | Utility | 1 | 23 | 12 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue` | Shared Component | 3 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/captain/Index.vue` | Shared Component | 1 | 10 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/captain/captain.routes.js` | Utility | 1 | 5 | 6 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelDropdown.vue` | Shared Component | 2 | 6 | 3 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/ModelSelector.vue` | Shared Component | 1 | 1 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/captain/components/FeatureToggle.vue` | Shared Component | 1 | 3 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Index.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/Settings.vue` | Shared Component | 1 | 39 | 8 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/InboxChannels.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` | Shared Component | 1 | 13 | 8 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/FinishSetup.vue` | Shared Component | 1 | 6 | 2 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/SmtpSettings.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/AddAgents.vue` | Shared Component | 1 | 6 | 6 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` | Utility | 1 | 11 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelList.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ImapSettings.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/Settings.vue` | Shared Component | 1 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/PreChatForm/PreChatFields.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/VoiceConfigurationPage.vue` | Shared Component | 1 | 7 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CustomerSatisfactionPage.vue` | Shared Component | 1 | 17 | 7 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/WhatsappCallingPage.vue` | Shared Component | 1 | 6 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/CollaboratorsPage.vue` | Shared Component | 1 | 10 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/ConfigurationPage.vue` | Shared Component | 1 | 10 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATStarInput.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/ConfirmTemplateUpdateDialog.vue` | Shared Component | 1 | 1 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATDisplayTypeSelector.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/settingsPage/components/CSATEmojiInput.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/LockToSingleConversationPreview.vue` | Shared Component | 1 | 1 | 2 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/InputRadioGroup.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/InboxReconnectionRequired.vue` | Shared Component | 6 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/SenderNameExamplePreview.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/ChannelName.vue` | Shared Component | 1 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/WeeklyAvailability.vue` | Shared Component | 1 | 8 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/BusinessDay.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/BotConfiguration.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/AccountHealth.vue` | Shared Component | 1 | 1 | 1 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/components/SingleSelectDropdown.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/facebook/Reauthorize.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/helpers/businessHour.js` | Utility | 2 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/helpers/timezones.json` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/helpers/specs/businessHour.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Website.vue` | Shared Component | 1 | 6 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Sms.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Instagram.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue` | Shared Component | 1 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Telegram.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/360DialogWhatsapp.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Twitter.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/WhatsappEmbeddedSignup.vue` | Shared Component | 2 | 6 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/BandwidthSms.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Tiktok.vue` | Shared Component | 1 | 5 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Twilio.vue` | Shared Component | 2 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Facebook.vue` | Shared Component | 1 | 8 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Api.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/CloudWhatsapp.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Line.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/WhatsappCall.vue` | Shared Component | 1 | 1 | 5 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Voice.vue` | Shared Component | 1 | 6 | 2 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue` | Shared Component | 1 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/Microsoft.vue` | Shared Component | 1 | 1 | 3 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/EmailInboxFinish.vue` | Shared Component | 1 | 0 | 0 | Vishnu Narayanan |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/ForwardToOption.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/OAuthChannel.vue` | Shared Component | 2 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/Google.vue` | Shared Component | 1 | 1 | 3 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/google/Reauthorize.vue` | Shared Component | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/microsoft/Reauthorize.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/tiktok/Reauthorize.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/instagram/DuplicateInboxBanner.vue` | Shared Component | 2 | 2 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/instagram/Reauthorize.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/utils.js` | Utility | 2 | 1 | 1 | Petterson |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/whatsapp/Reauthorize.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue` | Shared Component | 1 | 9 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/customRole.routes.js` | Utility | 1 | 5 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleTableBody.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRolePaywall.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/component/CustomRoleModal.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/security/Index.vue` | Shared Component | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/security/security.routes.js` | Utility | 1 | 5 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlAttributeMap.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlSettings.vue` | Shared Component | 1 | 7 | 3 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlInfoSection.vue` | Shared Component | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/security/components/SamlPaywall.vue` | Shared Component | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/canned/Index.vue` | Shared Component | 1 | 9 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/canned/AddCanned.vue` | Shared Component | 2 | 4 | 6 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/canned/canned.routes.js` | Utility | 1 | 4 | 8 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/canned/EditCanned.vue` | Shared Component | 1 | 4 | 6 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/labels/Index.vue` | Shared Component | 1 | 7 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/labels/AddLabel.vue` | Shared Component | 2 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/labels/EditLabel.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/labels/labels.routes.js` | Utility | 1 | 4 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/labels/validations.js` | Utility | 2 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/routes/dashboard/settings/labels/specs/validations.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/agents/Index.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/agents/AddAgent.vue` | Shared Component | 1 | 3 | 2 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/agents/EditAgent.vue` | Shared Component | 1 | 5 | 2 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/agents/agent.routes.js` | Utility | 1 | 4 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/Index.vue` | Shared Component | 1 | 8 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/agentBot.routes.js` | Utility | 1 | 4 | 6 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/agentBots/components/AgentBotModal.vue` | Shared Component | 1 | 9 | 4 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/Index.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/auditlogs/audit.routes.js` | Utility | 1 | 5 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Index.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/MultipleIntegrationHooks.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/SingleIntegrationHooks.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/IntegrationHooks.vue` | Shared Component | 1 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Shopify.vue` | Shared Component | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/ShowIntegration.vue` | Shared Component | 0 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Notion.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/hookMixin.js` | Utility | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Integration.vue` | Shared Component | 5 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/integrations.routes.js` | Utility | 1 | 11 | 5 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Linear.vue` | Shared Component | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/NewHook.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/IntegrationItem.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/specs/hookMixin.spec.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/Index.vue` | Shared Component | 1 | 7 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/DashboardAppModal.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/DashboardApps/DashboardAppsRow.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SelectChannelWarning.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Slack/SlackIntegrationHelpText.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/Index.vue` | Shared Component | 1 | 9 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookRow.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/NewWebHook.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/EditWebHook.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/integrations/Webhooks/WebhookForm.vue` | Shared Component | 2 | 6 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/constants.js` | Utility | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/Index.vue` | Shared Component | 1 | 9 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/EditAttribute.vue` | Shared Component | 1 | 5 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/attributes.routes.js` | Utility | 1 | 4 | 8 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/attributes/AddAttribute.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/constants.js` | Utility | 3 | 0 | 0 | Tejaswini Chile |
| `app/javascript/dashboard/routes/dashboard/settings/macros/Index.vue` | Shared Component | 1 | 8 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacrosTableRow.vue` | Shared Component | 2 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroForm.vue` | Shared Component | 1 | 3 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNode.vue` | Shared Component | 1 | 3 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroNodes.vue` | Shared Component | 1 | 3 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroProperties.vue` | Shared Component | 2 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/macroHelper.js` | Utility | 1 | 1 | 1 | Fayaz Ahmed |
| `app/javascript/dashboard/routes/dashboard/settings/macros/MacroEditor.vue` | Shared Component | 1 | 7 | 10 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/macros/macros.routes.js` | Utility | 1 | 6 | 11 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/macros/specs/MacroProperties.spec.js` | Utility | 0 | 1 | 3 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/macros/specs/MacrosTableRow.spec.js` | Utility | 0 | 1 | 3 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsListItem.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsHeader.vue` | Shared Component | 29 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/components/BasePaywallModal.vue` | Shared Component | 6 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/constants.js` | Utility | 0 | 0 | 0 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/Index.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/assignmentPolicy.routes.js` | Utility | 1 | 10 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityCreatePage.vue` | Page | 1 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentEditPage.vue` | Page | 1 | 8 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityEditPage.vue` | Page | 1 | 6 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentCreatePage.vue` | Page | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentCapacityIndexPage.vue` | Page | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/AgentAssignmentIndexPage.vue` | Page | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/ConfirmDeletePolicyDialog.vue` | Page | 2 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/ConfirmInboxDialog.vue` | Page | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentCapacityPolicyForm.vue` | Page | 2 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/InboxLinkDialog.vue` | Page | 1 | 2 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/assignmentPolicy/pages/components/AgentAssignmentPolicyForm.vue` | Page | 2 | 10 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/constants.js` | Utility | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/profile/Index.vue` | Shared Component | 1 | 22 | 10 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserProfilePicture.vue` | Shared Component | 1 | 1 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserLanguageSelect.vue` | Shared Component | 1 | 5 | 2 | micahmills |
| `app/javascript/dashboard/routes/dashboard/settings/profile/ChangePassword.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MessageSignature.vue` | Shared Component | 1 | 4 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertEvent.vue` | Shared Component | 1 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AccessToken.vue` | Shared Component | 3 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSetupWizard.vue` | Shared Component | 1 | 5 | 2 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSettings.vue` | Shared Component | 1 | 6 | 4 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/profile/NotificationPreferences.vue` | Shared Component | 1 | 6 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaStatusCard.vue` | Shared Component | 1 | 2 | 2 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/profile/UserBasicDetails.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/FontSize.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaManagementActions.vue` | Shared Component | 1 | 6 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/profile/ActiveSessions.vue` | Shared Component | 1 | 6 | 2 | Vishnu Narayanan |
| `app/javascript/dashboard/routes/dashboard/settings/profile/MfaSettingsCard.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioNotifications.vue` | Shared Component | 1 | 7 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/NotificationCheckBox.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertTone.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/AudioAlertCondition.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/Wrapper.vue` | Shared Component | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/profile/profile.routes.js` | Utility | 1 | 4 | 11 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Index.vue` | Shared Component | 1 | 9 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/FinishSetup.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/AgentSelector.vue` | Shared Component | 2 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` | Utility | 1 | 12 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/teams/TeamForm.vue` | Shared Component | 2 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/Index.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditTeam.vue` | Shared Component | 1 | 5 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditAgents.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Create/Index.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Create/AddAgents.vue` | Shared Component | 1 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` | Shared Component | 1 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/teams/helpers/validations.js` | Utility | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/routes/dashboard/settings/sla/Index.vue` | Shared Component | 1 | 8 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/sla/SlaTimeInput.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/sla/SLAPaywallEnterprise.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/sla/SlaForm.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/sla/sla.routes.js` | Utility | 1 | 5 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/sla/AddSLA.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/sla/validations.js` | Utility | 2 | 0 | 0 | Vishnu Narayanan |
| `app/javascript/dashboard/routes/dashboard/settings/automation/constants.js` | Utility | 3 | 0 | 0 | Tejaswini Chile |
| `app/javascript/dashboard/routes/dashboard/settings/automation/Index.vue` | Shared Component | 1 | 9 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AddAutomationRule.vue` | Shared Component | 1 | 3 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleRow.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/automation/operators.js` | Utility | 0 | 0 | 0 | Tejaswini Chile |
| `app/javascript/dashboard/routes/dashboard/settings/automation/AutomationRuleForm.vue` | Shared Component | 2 | 8 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/automation/automation.routes.js` | Utility | 1 | 4 | 10 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/automation/EditAutomationRule.vue` | Shared Component | 1 | 5 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/account/Index.vue` | Shared Component | 1 | 13 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/account/account.routes.js` | Utility | 1 | 3 | 6 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountId.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AccountDelete.vue` | Shared Component | 1 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AutoResolve.vue` | Shared Component | 1 | 7 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/AudioTranscription.vue` | Shared Component | 1 | 3 | 2 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/SectionLayout.vue` | Layout | 7 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/account/components/BuildInfo.vue` | Shared Component | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/conversationWorkflow/index.vue` | Shared Component | 1 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/conversationWorkflow/conversationWorkflow.routes.js` | Utility | 1 | 3 | 7 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/helper/settingsHelper.js` | Utility | 4 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/helper/spec/settingsHelper.spec.js` | Utility | 0 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/billing/Index.vue` | Shared Component | 1 | 11 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/billing/billing.routes.js` | Utility | 1 | 4 | 5 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/DetailItem.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/BillingMeter.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/PurchaseCreditsModal.vue` | Shared Component | 1 | 5 | 3 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/BillingCard.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/CreditPackageCard.vue` | Shared Component | 1 | 0 | 0 | Tanmay Deep Sharma |
| `app/javascript/dashboard/routes/dashboard/settings/billing/components/BillingHeader.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/constants.js` | Utility | 6 | 0 | 0 | Aswin Dev P.S |
| `app/javascript/dashboard/routes/dashboard/settings/reports/Index.vue` | Shared Component | 1 | 8 | 6 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReports.vue` | Shared Component | 1 | 1 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/AgentReportsShow.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/TeamReportsIndex.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/BotReports.vue` | Shared Component | 1 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/SLAReports.vue` | Shared Component | 1 | 7 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/TeamReportsShow.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/AgentReports.vue` | Shared Component | 1 | 1 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/LiveReports.vue` | Shared Component | 1 | 6 | 8 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/ReportContainer.vue` | Shared Component | 3 | 4 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/CsatResponses.vue` | Shared Component | 1 | 9 | 9 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/LabelReportsIndex.vue` | Shared Component | 1 | 3 | 7 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsShow.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/LabelReportsShow.vue` | Shared Component | 1 | 3 | 7 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/TeamReports.vue` | Shared Component | 1 | 1 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` | Utility | 1 | 20 | 10 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/AgentReportsIndex.vue` | Shared Component | 1 | 3 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/LabelReports.vue` | Shared Component | 1 | 1 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReportLink.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/WootReports.vue` | Shared Component | 8 | 7 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportHeader.vue` | Shared Component | 10 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/OverviewReportFilters.vue` | Shared Component | 1 | 3 | 5 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/AgentLiveReportContainer.vue` | Shared Component | 1 | 4 | 4 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatRatingDistribution.story.vue` | Shared Component | 0 | 1 | 2 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatMetrics.vue` | Shared Component | 2 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/TeamLiveReportContainer.vue` | Shared Component | 1 | 4 | 4 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatMetricCard.vue` | Shared Component | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportsWrapper.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatMetricCard.story.vue` | Shared Component | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/StatsLiveReportsContainer.vue` | Shared Component | 1 | 6 | 5 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportFilters.vue` | Shared Component | 3 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatReviewNotesPaywall.vue` | Shared Component | 1 | 2 | 3 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SummaryReports.vue` | Shared Component | 4 | 7 | 6 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/BotMetrics.vue` | Shared Component | 1 | 2 | 2 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTableLoader.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatTable.vue` | Shared Component | 1 | 11 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatContactCell.vue` | Shared Component | 1 | 1 | 4 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatRatingDistribution.vue` | Shared Component | 2 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportMetricCard.vue` | Shared Component | 2 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatExpandedRow.vue` | Shared Component | 1 | 7 | 7 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/CsatEmptyState.vue` | Shared Component | 1 | 0 | 0 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Filters/v3/ActiveFilterChip.vue` | Shared Component | 3 | 2 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Filters/v3/AddFilterChip.vue` | Shared Component | 2 | 4 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ChartElements/ChartStats.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/specs/ReportMetricCard.spec.js` | Utility | 0 | 1 | 1 | Vishnu Narayanan |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/specs/CSATMetrics.spec.js` | Utility | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilterHelpers.js` | Utility | 0 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/Csat/CsatFilters.vue` | Shared Component | 1 | 5 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportFilters.vue` | Shared Component | 1 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLATable.vue` | Shared Component | 1 | 4 | 5 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAReportItem.vue` | Shared Component | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAMetrics.vue` | Shared Component | 1 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAMetricCard.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAFilter.vue` | Shared Component | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/SLAViewDetails.vue` | Shared Component | 1 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/SLA/helpers/SLAFilterHelpers.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapTooltip.vue` | Shared Component | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmap.vue` | Shared Component | 1 | 2 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/ConversationHeatmapContainer.vue` | Shared Component | 1 | 1 | 7 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/ResolutionHeatmapContainer.vue` | Shared Component | 1 | 1 | 7 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/BaseHeatmapContainer.vue` | Shared Component | 2 | 8 | 6 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/HeatmapDateRangeSelector.vue` | Shared Component | 1 | 2 | 5 | Khoa Nguyen |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/heatmaps/composables/useHeatmapTooltip.js` | Hook | 1 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/AgentTable.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/TeamTable.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/MetricCard.vue` | Shared Component | 4 | 1 | 1 | Pranav |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/overview/AgentCell.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/helpers/reportFilterHelper.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/settings/reports/helpers/reportFilterHelper.spec.js` | Utility | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` | Utility | 1 | 16 | 10 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue` | Shared Component | 1 | 9 | 6 | Aakash Bakhle |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue` | Shared Component | 1 | 8 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue` | Shared Component | 1 | 11 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue` | Shared Component | 1 | 12 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/playground/Index.vue` | Shared Component | 1 | 2 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` | Shared Component | 1 | 7 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue` | Shared Component | 1 | 12 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue` | Shared Component | 1 | 12 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue` | Shared Component | 1 | 15 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue` | Shared Component | 1 | 16 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue` | Shared Component | 1 | 19 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/pages/CaptainPageRouteView.vue` | Page | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/captain/pages/AssistantsIndexPage.vue` | Page | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/upgrade/UpgradePage.vue` | Shared Component | 1 | 7 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` | Shared Component | 1 | 12 | 13 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxEmptyState.vue` | Shared Component | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/routes.js` | Utility | 1 | 4 | 14 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxList.vue` | Shared Component | 1 | 10 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxItemHeader.vue` | Shared Component | 1 | 10 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxContextMenu.vue` | Shared Component | 1 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxDisplayMenu.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxOptionMenu.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxListHeader.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/MenuItem.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/components/PaginationButton.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/inbox/helpers/InboxViewHelpers.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/contacts/routes.js` | Utility | 1 | 4 | 14 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/contacts/components/ContactsBulkActionBar.vue` | Shared Component | 1 | 4 | 6 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/contacts/contactFilterItems/index.js` | Utility | 2 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue` | Page | 1 | 11 | 11 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue` | Page | 1 | 11 | 13 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/helpcenter.routes.js` | Utility | 1 | 11 | 10 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/UpgradePage.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/SearchPopover.vue` | Shared Component | 1 | 7 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleView.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/SearchResults.vue` | Shared Component | 1 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/Header.vue` | Shared Component | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/components/ArticleSearch/ArticleSearchResultItem.vue` | Shared Component | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesIndexPage.vue` | Page | 1 | 4 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsCategoriesIndexPage.vue` | Page | 1 | 3 | 8 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesEditPage.vue` | Page | 1 | 5 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsLocalesIndexPage.vue` | Page | 1 | 3 | 8 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsIndexPage.vue` | Page | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsArticlesNewPage.vue` | Page | 1 | 4 | 9 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsNewPage.vue` | Page | 1 | 1 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/PortalsSettingsIndexPage.vue` | Page | 1 | 5 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/pages/HelpCenterPageRouteView.vue` | Page | 1 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/helpers/routeHelper.js` | Utility | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/helpcenter/helpers/specs/routeHelper.spec.js` | Utility | 0 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/customviews/DeleteCustomViews.vue` | Page | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/suspended/Index.vue` | Shared Component | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/noAccounts/Index.vue` | Shared Component | 1 | 4 | 2 | Pranav |
| `app/javascript/dashboard/routes/dashboard/commands/commandbar.vue` | Shared Component | 1 | 12 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/commands/CmdBarConversationSnooze.vue` | Shared Component | 2 | 7 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/campaigns/campaigns.routes.js` | Utility | 1 | 6 | 10 | Aman Kumar |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue` | Page | 1 | 7 | 7 | Aman Kumar |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/WhatsAppCampaignsPage.vue` | Page | 1 | 7 | 7 | Aman Kumar |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/CampaignsPageRouteView.vue` | Page | 1 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue` | Page | 1 | 8 | 9 | Aman Kumar |
| `app/javascript/dashboard/routes/dashboard/notifications/routes.js` | Utility | 1 | 3 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/notifications/components/NotificationsView.vue` | Shared Component | 1 | 4 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/routes/dashboard/notifications/components/NotificationTable.vue` | Shared Component | 1 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/companies/routes.js` | Utility | 1 | 5 | 9 | salmonumbrella |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompaniesIndex.vue` | Page | 1 | 6 | 8 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/companies/pages/CompanyDetailView.vue` | Page | 1 | 12 | 7 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/onboarding/constants.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/onboarding/Index.vue` | Shared Component | 1 | 15 | 4 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingLayout.vue` | Layout | 1 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingFormRow.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingFormSelect.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/onboarding/OnboardingSection.vue` | Shared Component | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationAction.vue` | Shared Component | 1 | 8 | 5 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/SharedFiles.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationInfo.vue` | Shared Component | 1 | 3 | 7 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactPanel.vue` | Shared Component | 1 | 17 | 11 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationParticipant.vue` | Shared Component | 1 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactConversations.vue` | Shared Component | 1 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/ContactDetailsItem.vue` | Shared Component | 2 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/conversation/ConversationView.vue` | Shared Component | 1 | 10 | 13 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/conversation/conversation.routes.js` | Utility | 1 | 3 | 14 | Sojan Jose |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfo.vue` | Shared Component | 1 | 12 | 10 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/EditContact.vue` | Shared Component | 1 | 4 | 4 | Pranav Raj S |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/SocialIcons.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactForm.vue` | Shared Component | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactNotes.vue` | Shared Component | 1 | 5 | 7 | Shivam Mishra |
| `app/javascript/dashboard/routes/dashboard/conversation/contact/ContactInfoRow.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/labels/LabelBox.vue` | Shared Component | 1 | 6 | 4 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/customAttributes/CustomAttributes.vue` | Shared Component | 2 | 6 | 6 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/search/SwitchLayout.vue` | Layout | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/MacroItem.vue` | Shared Component | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/List.vue` | Shared Component | 1 | 6 | 3 | Sivin Varghese |
| `app/javascript/dashboard/routes/dashboard/conversation/Macros/MacroPreview.vue` | Shared Component | 1 | 1 | 1 | Tejaswini Chile |
| `app/javascript/dashboard/services/TemplateTypeDetector.spec.js` | Utility | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/services/TemplateNormalizer.spec.js` | Utility | 0 | 1 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/services/TemplateTypeDetector.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/services/TemplateConstants.js` | Utility | 0 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/services/TemplateNormalizer.js` | Utility | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/constants.js` | Context / Store | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/store/index.js` | Context / Store | 7 | 60 | 6 | Pranav Raj S |
| `app/javascript/dashboard/store/mutation-types.js` | Context / Store | 130 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/storeFactory.js` | Context / Store | 11 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/store/storeFactoryHelper.js` | Context / Store | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/storeFactory.spec.js` | Context / Store | 0 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/assistant.js` | Context / Store | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/tools.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/copilotMessages.js` | Context / Store | 1 | 2 | 2 | Pranav |
| `app/javascript/dashboard/store/captain/response.js` | Context / Store | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/preferences.js` | Context / Store | 3 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/captain/inboxes.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/scenarios.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/bulkActions.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/copilotThreads.js` | Context / Store | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/customTools.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/captain/document.js` | Context / Store | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/utils/api.js` | Context / Store | 40 | 5 | 1 | Pranav Raj S |
| `app/javascript/dashboard/store/utils/specs/api.spec.js` | Context / Store | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/agentCapacityPolicies.js` | Context / Store | 4 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/csat.js` | Context / Store | 4 | 6 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversationPage.js` | Context / Store | 4 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/campaigns.js` | Context / Store | 4 | 7 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/agents.js` | Context / Store | 4 | 3 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversationWatchers.js` | Context / Store | 4 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/customRole.js` | Context / Store | 4 | 4 | 2 | Sojan Jose |
| `app/javascript/dashboard/store/modules/contactNotes.js` | Context / Store | 4 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/inboxes.js` | Context / Store | 4 | 12 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversationLabels.js` | Context / Store | 4 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/customViews.js` | Context / Store | 4 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/labels.js` | Context / Store | 4 | 5 | 4 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/auth.js` | Context / Store | 4 | 5 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversationMetadata.js` | Context / Store | 3 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/assignmentPolicies.js` | Context / Store | 4 | 4 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/accounts.js` | Context / Store | 4 | 7 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/attributes.js` | Context / Store | 4 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/bulkActions.js` | Context / Store | 4 | 2 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/cannedResponse.js` | Context / Store | 2 | 4 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/webhooks.js` | Context / Store | 4 | 3 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/draftMessages.js` | Context / Store | 4 | 4 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/inboxAssignableAgents.js` | Context / Store | 3 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/contactLabels.js` | Context / Store | 4 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/conversationStats.js` | Context / Store | 4 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/SLAReports.js` | Context / Store | 4 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/integrations.js` | Context / Store | 4 | 4 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/automations.js` | Context / Store | 4 | 4 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/inboxMembers.js` | Context / Store | 1 | 1 | 2 | Sojan Jose |
| `app/javascript/dashboard/store/modules/conversationUnreadCounts.js` | Context / Store | 4 | 2 | 2 | Sony Mathew |
| `app/javascript/dashboard/store/modules/contactConversations.js` | Context / Store | 3 | 3 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/auditlogs.js` | Context / Store | 1 | 4 | 2 | Vishnu Narayanan |
| `app/javascript/dashboard/store/modules/dashboardApps.js` | Context / Store | 4 | 3 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/sidebarSortPreferences.js` | Context / Store | 2 | 1 | 1 | Sony Mathew |
| `app/javascript/dashboard/store/modules/userNotificationSettings.js` | Hook | 4 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversationTypingStatus.js` | Context / Store | 4 | 2 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/conversationSearch.js` | Context / Store | 4 | 2 | 2 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/reports.js` | Context / Store | 2 | 8 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/summaryReports.js` | Context / Store | 2 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/macros.js` | Context / Store | 4 | 4 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/sla.js` | Context / Store | 4 | 6 | 2 | Vishnu Narayanan |
| `app/javascript/dashboard/store/modules/teamMembers.js` | Context / Store | 4 | 1 | 4 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/agentBots.js` | Context / Store | 4 | 5 | 4 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/helpCenterPortals/mutations.js` | Context / Store | 4 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/helpCenterPortals/actions.js` | Context / Store | 2 | 3 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterPortals/getters.js` | Context / Store | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterPortals/index.js` | Context / Store | 2 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterPortals/specs/actions.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterPortals/specs/fixtures.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/helpCenterPortals/specs/mutations.spec.js` | Context / Store | 0 | 2 | 2 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/helpCenterPortals/specs/getters.spec.js` | Context / Store | 0 | 2 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/summaryReports.spec.js` | Context / Store | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/agentCapacityPolicies/actions.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/agentCapacityPolicies/fixtures.js` | Context / Store | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/agentCapacityPolicies/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/agentCapacityPolicies/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/conversationLabels/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversationLabels/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversationLabels/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/inboxAssignableMembers/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/inboxAssignableMembers/fixtures.js` | Context / Store | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/inboxAssignableMembers/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/inboxAssignableMembers/getters.spec.js` | Context / Store | 0 | 2 | 5 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/cannedResponses/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/auth/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/auth/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/auth/getters.spec.js` | Context / Store | 0 | 1 | 3 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/teamMembers/actions.spec.js` | Context / Store | 0 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teamMembers/fixtures.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teamMembers/mutations.spec.js` | Context / Store | 0 | 2 | 5 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teamMembers/getters.spec.js` | Context / Store | 0 | 2 | 5 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/conversationTypingStatus/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/conversationTypingStatus/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/conversationTypingStatus/getters.spec.js` | Context / Store | 0 | 1 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/customRole/actions.spec.js` | Context / Store | 0 | 3 | 3 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/customRole/fixtures.js` | Context / Store | 3 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/customRole/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/customRole/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/contacts/actions.spec.js` | Context / Store | 0 | 4 | 4 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/contacts/filterApiResponse.js` | Context / Store | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/contacts/fixtures.js` | Context / Store | 2 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/contacts/mutations.spec.js` | Context / Store | 0 | 2 | 4 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/contacts/getters.spec.js` | Context / Store | 0 | 2 | 4 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/csat/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/csat/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/csat/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/conversationStats/actions.spec.js` | Context / Store | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/conversationStats/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/conversationStats/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversationUnreadCounts/actions.spec.js` | Context / Store | 0 | 2 | 3 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/conversationUnreadCounts/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/conversationUnreadCounts/getters.spec.js` | Context / Store | 0 | 1 | 3 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/labels/actions.spec.js` | Context / Store | 0 | 3 | 5 | Pranav |
| `app/javascript/dashboard/store/modules/specs/labels/fixtures.js` | Context / Store | 3 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/labels/mutations.spec.js` | Context / Store | 0 | 3 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/labels/getters.spec.js` | Context / Store | 0 | 2 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/agents/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/agents/fixtures.js` | Context / Store | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/agents/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/agents/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/assignmentPolicies/actions.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/assignmentPolicies/fixtures.js` | Context / Store | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/assignmentPolicies/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/assignmentPolicies/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/agentBots/agentBots.spec.js` | Context / Store | 0 | 3 | 5 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/agentBots/fixtures.js` | Context / Store | 3 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/agentBots/mutations.spec.js` | Context / Store | 0 | 3 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/agentBots/getters.spec.js` | Context / Store | 0 | 2 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/integrations/actions.spec.js` | Context / Store | 0 | 3 | 3 | Aakash Bakhle |
| `app/javascript/dashboard/store/modules/specs/integrations/fixtures.js` | Context / Store | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/integrations/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/integrations/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/attributes/actions.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/attributes/fixtures.js` | Context / Store | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/attributes/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/attributes/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/bulkActions/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/bulkActions/fixtures.js` | Context / Store | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/bulkActions/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/bulkActions/getters.spec.js` | Context / Store | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/macros/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/macros/fixtures.js` | Context / Store | 3 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/macros/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/macros/getters.spec.js` | Context / Store | 0 | 2 | 3 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/sidebarSortPreferences/actions.spec.js` | Context / Store | 0 | 1 | 1 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/sidebarSortPreferences/mutations.spec.js` | Context / Store | 0 | 0 | 0 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/sidebarSortPreferences/getters.spec.js` | Context / Store | 0 | 1 | 2 | Sony Mathew |
| `app/javascript/dashboard/store/modules/specs/inboxes/actions.spec.js` | Context / Store | 0 | 3 | 6 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/inboxes/templateFixtures.js` | Context / Store | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/inboxes/fixtures.js` | Context / Store | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/inboxes/mutations.spec.js` | Context / Store | 0 | 3 | 6 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/inboxes/getters.spec.js` | Context / Store | 0 | 3 | 6 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/contactConversations/actions.spec.js` | Context / Store | 0 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/contactConversations/fixtures.js` | Context / Store | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/contactConversations/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/contactConversations/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversations/helpers.spec.js` | Context / Store | 0 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/conversations/actions.spec.js` | Context / Store | 0 | 2 | 1 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversations/testConversationResponse.js` | Context / Store | 1 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/conversations/conversations.fixtures.js` | Context / Store | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversations/mutations.spec.js` | Context / Store | 0 | 3 | 5 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversations/getters.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/conversationMetadata/mutations.spec.js` | Context / Store | 0 | 2 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversationMetadata/getters.spec.js` | Context / Store | 0 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/dashboardApps/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/dashboardApps/fixtures.js` | Context / Store | 2 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/dashboardApps/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/dashboardApps/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/customViews/actions.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/customViews/fixtures.js` | Context / Store | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/customViews/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/customViews/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/contactNotes/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/contactNotes/fixtures.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/contactNotes/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/contactNotes/getters.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teams/actions.spec.js` | Context / Store | 0 | 2 | 5 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teams/fixtures.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teams/mutations.spec.js` | Context / Store | 0 | 2 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/teams/getters.spec.js` | Context / Store | 0 | 2 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/conversationWatchers/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/conversationWatchers/fixtures.js` | Context / Store | 1 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/conversationWatchers/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Sojan Jose |
| `app/javascript/dashboard/store/modules/specs/conversationWatchers/getters.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/automations/actions.spec.js` | Context / Store | 0 | 3 | 3 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/automations/fixtures.js` | Context / Store | 3 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/automations/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/automations/getters.spec.js` | Context / Store | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/sla/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/sla/fixtures.js` | Context / Store | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/sla/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/sla/getters.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/campaigns/actions.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/campaigns/fixtures.js` | Context / Store | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/campaigns/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/campaigns/getters.spec.js` | Context / Store | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/slaReports/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/slaReports/fixtures.js` | Context / Store | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/slaReports/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/slaReports/getters.spec.js` | Context / Store | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/userNotificationSettings/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/userNotificationSettings/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/userNotificationSettings/getters.spec.js` | Context / Store | 0 | 1 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/draftMessages/actions.spec.js` | Context / Store | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/draftMessages/fixtures.js` | Context / Store | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/draftMessages/mutations.spec.js` | Context / Store | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/draftMessages/getters.spec.js` | Context / Store | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/account/actions.spec.js` | Context / Store | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/account/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/account/getters.spec.js` | Context / Store | 0 | 2 | 3 | micahmills |
| `app/javascript/dashboard/store/modules/specs/webhooks/actions.spec.js` | Context / Store | 0 | 3 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/webhooks/fixtures.js` | Context / Store | 3 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/webhooks/mutations.spec.js` | Context / Store | 0 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/webhooks/getters.spec.js` | Context / Store | 0 | 2 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/specs/notifications/helpers.spec.js` | Context / Store | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/notifications/actions.spec.js` | Context / Store | 0 | 2 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/notifications/mutations.spec.js` | Context / Store | 0 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/specs/notifications/getters.spec.js` | Context / Store | 0 | 1 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/contactLabels/actions.spec.js` | Context / Store | 0 | 2 | 3 | Pranav |
| `app/javascript/dashboard/store/modules/specs/contactLabels/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/contactLabels/getters.spec.js` | Context / Store | 0 | 1 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/specs/reports/actions.spec.js` | Context / Store | 0 | 4 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/specs/conversationSearch/actions.spec.js` | Context / Store | 0 | 2 | 3 | Vinay Keerthi |
| `app/javascript/dashboard/store/modules/specs/conversationSearch/mutations.spec.js` | Context / Store | 0 | 2 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/conversationSearch/getters.spec.js` | Context / Store | 0 | 1 | 3 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/specs/conversationPage/actions.spec.js` | Context / Store | 0 | 2 | 2 | Pranav |
| `app/javascript/dashboard/store/modules/specs/conversationPage/mutations.spec.js` | Context / Store | 0 | 2 | 2 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/specs/conversationPage/getters.spec.js` | Context / Store | 0 | 1 | 2 | Niklas Haug |
| `app/javascript/dashboard/store/modules/contacts/mutations.js` | Context / Store | 1 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/contacts/actions.js` | Context / Store | 1 | 5 | 2 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/contacts/getters.js` | Context / Store | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/contacts/index.js` | Context / Store | 4 | 3 | 3 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/helpCenterCategories/mutations.js` | Context / Store | 2 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/store/modules/helpCenterCategories/actions.js` | Context / Store | 2 | 3 | 3 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterCategories/getters.js` | Context / Store | 2 | 0 | 0 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterCategories/index.js` | Context / Store | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterCategories/specs/actions.spec.js` | Context / Store | 0 | 3 | 4 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/helpCenterCategories/specs/fixtures.js` | Context / Store | 3 | 0 | 0 | Fayaz Ahmed |
| `app/javascript/dashboard/store/modules/helpCenterCategories/specs/mutations.spec.js` | Context / Store | 0 | 3 | 2 | Sojan Jose |
| `app/javascript/dashboard/store/modules/helpCenterCategories/specs/getters.spec.js` | Context / Store | 0 | 2 | 1 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/inboxes/channelActions.js` | Context / Store | 1 | 4 | 4 | Sojan Jose |
| `app/javascript/dashboard/store/modules/helpCenterArticles/mutations.js` | Context / Store | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/actions.js` | Context / Store | 2 | 4 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/getters.js` | Context / Store | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/index.js` | Context / Store | 1 | 3 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/specs/fixtures.js` | Context / Store | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/specs/action.spec.js` | Context / Store | 0 | 3 | 4 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/specs/mutation.spec.js` | Context / Store | 0 | 3 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/helpCenterArticles/specs/getters.spec.js` | Context / Store | 0 | 2 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/conversations/actions.js` | Context / Store | 1 | 7 | 3 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversations/getters.js` | Context / Store | 2 | 4 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversations/index.js` | Context / Store | 3 | 9 | 4 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversations/helpers.js` | Context / Store | 3 | 1 | 1 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/conversations/specs/helpers.spec.js` | Context / Store | 0 | 1 | 2 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/conversations/specs/mutations.spec.js` | Context / Store | 0 | 2 | 5 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/conversations/actions/messageReadActions.js` | Context / Store | 1 | 3 | 2 | Sojan Jose |
| `app/javascript/dashboard/store/modules/conversations/actions/messageTranslateActions.js` | Context / Store | 1 | 1 | 2 | Pranav Raj S |
| `app/javascript/dashboard/store/modules/conversations/helpers/filterHelpers.js` | Context / Store | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/conversations/helpers/actionHelpers.js` | Context / Store | 0 | 1 | 1 | Sojan Jose |
| `app/javascript/dashboard/store/modules/conversations/helpers/specs/filterHelpers.spec.js` | Context / Store | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/conversations/helpers/specs/actionHelpers.spec.js` | Context / Store | 0 | 0 | 0 | Sojan Jose |
| `app/javascript/dashboard/store/modules/teams/mutations.js` | Context / Store | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/dashboard/store/modules/teams/types.js` | Context / Store | 0 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/teams/actions.js` | Context / Store | 2 | 1 | 4 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/teams/getters.js` | Context / Store | 2 | 0 | 0 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/teams/index.js` | Context / Store | 1 | 3 | 5 | Nithin David Thomas |
| `app/javascript/dashboard/store/modules/notifications/mutations.js` | Context / Store | 2 | 1 | 1 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/notifications/actions.js` | Context / Store | 2 | 2 | 2 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/notifications/getters.js` | Context / Store | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/dashboard/store/modules/notifications/index.js` | Context / Store | 1 | 3 | 3 | Muhsin Keloth |
| `app/javascript/dashboard/store/modules/notifications/helpers.js` | Context / Store | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/v3/App.vue` | Shared Component | 1 | 1 | 2 | Sivin Varghese |
| `app/javascript/v3/components/Form/WithLabel.vue` | Shared Component | 8 | 0 | 0 | Nithin David Thomas |
| `app/javascript/v3/components/Form/CheckBox.vue` | Shared Component | 3 | 0 | 0 | Sivin Varghese |
| `app/javascript/v3/components/Form/Input.vue` | Shared Component | 7 | 2 | 2 | Shivam Mishra |
| `app/javascript/v3/components/Form/Select.vue` | Shared Component | 3 | 1 | 1 | Sivin Varghese |
| `app/javascript/v3/components/GoogleOauth/Button.vue` | Shared Component | 3 | 0 | 0 | Shivam Mishra |
| `app/javascript/v3/components/GoogleOauth/Button.spec.js` | Utility | 0 | 1 | 1 | Shivam Mishra |
| `app/javascript/v3/components/SnackBar/Container.vue` | Shared Component | 1 | 3 | 1 | Shivam Mishra |
| `app/javascript/v3/components/SnackBar/Item.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/v3/components/Divider/SimpleDivider.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/v3/api/apiClient.js` | Utility | 2 | 0 | 0 | Pranav Raj S |
| `app/javascript/v3/api/auth.js` | Utility | 6 | 1 | 1 | Vishnu Narayanan |
| `app/javascript/v3/api/testimonials.js` | Utility | 1 | 2 | 1 | Pranav Raj S |
| `app/javascript/v3/views/index.js` | Page | 1 | 3 | 6 | Shivam Mishra |
| `app/javascript/v3/views/routes.js` | Page | 1 | 8 | 5 | Shivam Mishra |
| `app/javascript/v3/views/auth/password/Edit.vue` | Page | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/v3/views/auth/signup/Index.vue` | Page | 1 | 3 | 4 | Sivin Varghese |
| `app/javascript/v3/views/auth/signup/components/Testimonials/Index.vue` | Page | 1 | 2 | 2 | Sivin Varghese |
| `app/javascript/v3/views/auth/signup/components/Testimonials/TestimonialCard.vue` | Page | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/v3/views/auth/signup/components/Signup/PasswordRequirements.vue` | Page | 1 | 1 | 1 | Pranav |
| `app/javascript/v3/views/auth/signup/components/Signup/Form.vue` | Page | 1 | 7 | 3 | Sivin Varghese |
| `app/javascript/v3/views/auth/reset/password/Index.vue` | Page | 1 | 5 | 3 | Sivin Varghese |
| `app/javascript/v3/views/auth/confirmation/Index.vue` | Page | 1 | 3 | 2 | Sivin Varghese |
| `app/javascript/v3/views/auth/verify-email/Index.vue` | Page | 1 | 3 | 2 | Shivam Mishra |
| `app/javascript/v3/views/login/Index.vue` | Page | 1 | 15 | 4 | Shivam Mishra |
| `app/javascript/v3/views/login/Saml.vue` | Page | 1 | 3 | 3 | Shivam Mishra |
| `app/javascript/v3/views/onboarding/OnboardingStep.vue` | Page | 0 | 0 | 0 | Sivin Varghese |
| `app/javascript/v3/helpers/RouteHelper.js` | Utility | 4 | 5 | 2 | Shivam Mishra |
| `app/javascript/v3/helpers/AuthHelper.js` | Utility | 2 | 2 | 1 | Pranav Raj S |
| `app/javascript/v3/helpers/CommonHelper.js` | Utility | 3 | 0 | 0 | Muhsin Keloth |
| `app/javascript/v3/helpers/specs/CommonHelper.spec.js` | Utility | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/v3/helpers/specs/RouteHelper.spec.js` | Utility | 0 | 3 | 3 | Pranav Raj S |
| `app/javascript/v3/helpers/specs/AuthHelper.spec.js` | Utility | 0 | 1 | 2 | Pranav |
| `app/javascript/v3/store/index.js` | Context / Store | 1 | 1 | 3 | Shivam Mishra |
| `app/javascript/sdk/constants.js` | Utility | 1 | 0 | 0 | Pranav Raj S |
| `app/javascript/sdk/bubbleHelpers.js` | Utility | 0 | 4 | 4 | Pranav Raj S |
| `app/javascript/sdk/IFrameHelper.js` | Utility | 3 | 6 | 2 | Pranav Raj S |
| `app/javascript/sdk/sdk.js` | Utility | 1 | 0 | 0 | Nithin David Thomas |
| `app/javascript/sdk/cookieHelpers.js` | Utility | 2 | 0 | 0 | Shivam Mishra |
| `app/javascript/sdk/settingsHelper.js` | Utility | 2 | 1 | 1 | Sivin Varghese |
| `app/javascript/sdk/DOMHelpers.js` | Utility | 1 | 2 | 3 | Shivam Mishra |
| `app/javascript/sdk/specs/cookieHelpers.spec.js` | Utility | 0 | 0 | 0 | Pranav |
| `app/javascript/sdk/specs/settingsHelpers.spec.js` | Utility | 0 | 0 | 0 | Pranav Raj S |
| `app/javascript/entrypoints/superadmin_pages.js` | Utility | 0 | 2 | 4 | Shivam Mishra |
| `app/javascript/entrypoints/survey.js` | Utility | 0 | 4 | 5 | Sivin Varghese |
| `app/javascript/entrypoints/superadmin.js` | Utility | 0 | 0 | 0 | Shivam Mishra |
| `app/javascript/entrypoints/sdk.js` | Utility | 0 | 3 | 3 | Shivam Mishra |
| `app/javascript/entrypoints/widget.js` | Utility | 0 | 6 | 10 | Shivam Mishra |
| `app/javascript/entrypoints/portal.js` | Utility | 0 | 1 | 6 | Alex |
| `app/javascript/entrypoints/v3app.js` | Utility | 0 | 6 | 7 | Shivam Mishra |
| `app/javascript/entrypoints/dashboard.js` | Utility | 0 | 10 | 17 | Sivin Varghese |
| `app/javascript/survey/App.vue` | Shared Component | 1 | 1 | 4 | Sivin Varghese |
| `app/javascript/survey/components/Banner.vue` | Shared Component | 1 | 0 | 0 | Sivin Varghese |
| `app/javascript/survey/components/Rating.vue` | Shared Component | 1 | 1 | 1 | Muhsin Keloth |
| `app/javascript/survey/components/Feedback.vue` | Shared Component | 1 | 3 | 1 | Shivam Mishra |
| `app/javascript/survey/api/survey.js` | Utility | 1 | 2 | 2 | Muhsin Keloth |
| `app/javascript/survey/api/endPoints.js` | Utility | 2 | 0 | 0 | Muhsin Keloth |
| `app/javascript/survey/api/specs/endPoints.spec.js` | Utility | 0 | 1 | 1 | Muhsin Keloth |
| `app/javascript/survey/i18n/index.js` | Utility | 1 | 40 | 1 | Muhsin Keloth |
| `app/javascript/survey/i18n/locale/hy.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/tr.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sl.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/hu.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/lt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/is.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/bn.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/nl.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ms.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/zh_CN.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ja.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/de.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ru.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/pl.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/uk.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/fi.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ta.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ur.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sk.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ml.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/az.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/pt.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/en.json` | Shared Component | 1 | 0 | 0 | Muhsin Keloth |
| `app/javascript/survey/i18n/locale/ka.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/it.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sr.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/survey/i18n/locale/hr.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/tl.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/et.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sq.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sh.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ur_IN.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ne.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/fr.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/am.json` | Shared Component | 0 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/el.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/bg.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ro.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/hi.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ca.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ko.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/he.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/vi.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/fa.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/cs.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/id.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/pt_BR.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/zh_TW.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/lv.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/no.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/da.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/th.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/sv.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/es.json` | Shared Component | 1 | 0 | 0 | Chatwoot Bot |
| `app/javascript/survey/i18n/locale/ar.json` | Shared Component | 1 | 0 | 0 | Sojan Jose |
| `app/javascript/survey/views/Response.vue` | Page | 1 | 10 | 3 | Sivin Varghese |
| `app/javascript/survey/helpers/axios.js` | Utility | 1 | 1 | 1 | Muhsin Keloth |
| `app/javascript/survey/store/index.js` | Context / Store | 1 | 1 | 3 | Shivam Mishra |
| `app/assets/config/manifest.js` | Utility | 0 | 0 | 0 | Sojan Jose |
| `app/assets/javascripts/secretField.js` | Utility | 0 | 0 | 0 | Sojan Jose |
| `swagger/swagger.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `swagger/tag_groups/other_swagger.json` | Shared Component | 0 | 0 | 0 | Shivam Mishra |
| `swagger/tag_groups/application_swagger.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `swagger/tag_groups/platform_swagger.json` | Shared Component | 0 | 0 | 0 | Shivam Mishra |
| `swagger/tag_groups/client_swagger.json` | Shared Component | 0 | 0 | 0 | Shivam Mishra |
| `config/llm_models.json` | Shared Component | 0 | 0 | 0 | Aakash Bakhle |
| `config/vite.json` | Shared Component | 0 | 0 | 0 | Shivam Mishra |
| `clevercloud/ruby.json` | Shared Component | 0 | 0 | 0 | Pranav Raj S |
| `tests/playwright/package.json` | Shared Component | 0 | 0 | 0 | dependabot[bot] |
| `tests/playwright/tsconfig.json` | Shared Component | 0 | 0 | 0 | Ajith KV |
| `tests/playwright/playwright.config.ts` | Utility | 0 | 0 | 0 | Ajith KV |
| `tests/playwright/tests/e2e/ui/login-flow-ui-validation.spec.ts` | Utility | 0 | 0 | 0 | Ajith KV |
| `tests/playwright/components/ui/login.component.ts` | Utility | 0 | 0 | 0 | Ajith KV |
| `tests/playwright/components/ui/index.ts` | Utility | 0 | 0 | 0 | Ajith KV |
| `.devcontainer/devcontainer.json` | Shared Component | 0 | 0 | 0 | Sojan Jose |
| `theme/icons.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `theme/colors.js` | Utility | 1 | 0 | 0 | Sivin Varghese |
| `.vscode/settings.json` | Shared Component | 0 | 0 | 0 | Muhsin Keloth |
| `.vscode/extensions.json` | Shared Component | 0 | 0 | 0 | Muhsin Keloth |

## 2. Dependency Loop Cycles Detected

| Component | Cycle Path |
|:---|:---|
| `app/javascript/widget/helpers/campaignTimer.js` | `app/javascript/widget/store/index.js` -> `app/javascript/widget/store/modules/campaign.js` -> `app/javascript/widget/helpers/campaignTimer.js` |
| `app/javascript/widget/store/index.js` | `app/javascript/widget/store/index.js` -> `app/javascript/widget/store/modules/campaign.js` -> `app/javascript/widget/helpers/campaignTimer.js` |
| `app/javascript/widget/store/modules/campaign.js` | `app/javascript/widget/store/index.js` -> `app/javascript/widget/store/modules/campaign.js` -> `app/javascript/widget/helpers/campaignTimer.js` |
| `app/javascript/dashboard/components-next/captain/PageLayout.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` |
| `app/javascript/dashboard/stores/calls.js` | `app/javascript/dashboard/stores/calls.js` -> `app/javascript/dashboard/helper/voice.js` |
| `app/javascript/dashboard/components/widgets/BackButton.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue` -> `app/javascript/dashboard/routes/dashboard/settings/SettingsHeader.vue` |
| `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` |
| `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` |
| `app/javascript/dashboard/helper/voice.js` | `app/javascript/dashboard/stores/calls.js` -> `app/javascript/dashboard/helper/voice.js` |
| `app/javascript/dashboard/routes/index.js` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/SettingsHeader.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue` -> `app/javascript/dashboard/routes/dashboard/settings/SettingsHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/Wrapper.vue` -> `app/javascript/dashboard/routes/dashboard/settings/SettingsHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Telegram.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/AddAgents.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/AddAgents.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/AddAgents.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Website.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Website.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Sms.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Sms.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Twilio.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/ForwardToOption.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Telegram.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Telegram.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/360DialogWhatsapp.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/360DialogWhatsapp.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/BandwidthSms.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Sms.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/BandwidthSms.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Twilio.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Sms.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Twilio.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Facebook.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Facebook.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Api.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Api.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/CloudWhatsapp.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/CloudWhatsapp.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Line.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Line.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Whatsapp.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/CloudWhatsapp.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/ForwardToOption.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/inbox.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/ChannelFactory.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/Email.vue` -> `app/javascript/dashboard/routes/dashboard/settings/inbox/channels/emailChannels/ForwardToOption.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/customRole.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue` -> `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/customRoles/customRole.routes.js` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/customRole.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue` -> `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsHeader.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/customRole.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/customRoles/Index.vue` -> `app/javascript/dashboard/routes/dashboard/settings/components/BaseSettingsHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditTeam.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditAgents.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Edit/EditAgents.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Create/AddAgents.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/AddAgents.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` | `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/teams.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/teams/Create/CreateTeam.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue` -> `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue` -> `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportHeader.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/settings.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` -> `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReportsIndex.vue` -> `app/javascript/dashboard/routes/dashboard/settings/reports/components/ReportHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/guardrails/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/playground/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/playground/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/assistants/guidelines/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue` |
| `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue` | `app/javascript/dashboard/components-next/captain/PageLayout.vue` -> `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` -> `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue` |
| `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/inbox/routes.js` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationBox.vue` -> `app/javascript/dashboard/components/widgets/conversation/ConversationHeader.vue` |
| `app/javascript/dashboard/routes/dashboard/inbox/components/InboxItemHeader.vue` | `app/javascript/dashboard/components/widgets/BackButton.vue` -> `app/javascript/dashboard/routes/index.js` -> `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/routes.js` -> `app/javascript/dashboard/routes/dashboard/inbox/InboxView.vue` -> `app/javascript/dashboard/routes/dashboard/inbox/components/InboxItemHeader.vue` |
| `app/javascript/dashboard/store/modules/helpCenterPortals/mutations.js` | `app/javascript/dashboard/store/modules/helpCenterPortals/index.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/actions.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/mutations.js` |
| `app/javascript/dashboard/store/modules/helpCenterPortals/actions.js` | `app/javascript/dashboard/store/modules/helpCenterPortals/index.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/actions.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/mutations.js` |
| `app/javascript/dashboard/store/modules/helpCenterPortals/index.js` | `app/javascript/dashboard/store/modules/helpCenterPortals/index.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/actions.js` -> `app/javascript/dashboard/store/modules/helpCenterPortals/mutations.js` |
