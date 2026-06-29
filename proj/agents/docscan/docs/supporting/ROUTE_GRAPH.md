# Route Mapping Discovery

## 1. Registered SPA Routes

| Route path | Route name | Entry Component | Protected? | Parent File |
|:---|:---|:---|:---|:---|
| `/unread-messages` | unread-messages | `Unknown` | False | `app/javascript/widget/router.js` |
| `/campaigns` | campaigns | `Unknown` | False | `app/javascript/widget/router.js` |
| `/prechat-form` | prechat-form | `Unknown` | False | `app/javascript/widget/router.js` |
| `/messages` | messages | `Unknown` | False | `app/javascript/widget/router.js` |
| `/article` | article-viewer | `Unknown` | False | `app/javascript/widget/router.js` |
| `accounts/:accountId` | accounts/:accountId | `app/javascript/dashboard/routes/dashboard/Dashboard.vue` | False | `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` |
| `no-accounts` | no_accounts | `app/javascript/dashboard/routes/dashboard/noAccounts/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/dashboard.routes.js` |
| `list` | sla_list | `app/javascript/dashboard/routes/dashboard/settings/sla/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/sla/sla.routes.js` |
| `agent` | agent_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/AgentReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `inboxes` | inbox_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/InboxReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `label` | label_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/LabelReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `teams` | team_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/TeamReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `overview` | account_overview_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/LiveReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `conversation` | conversation_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `sla` | sla_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/SLAReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `csat` | csat_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/CsatResponses.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `bot` | bot_reports | `app/javascript/dashboard/routes/dashboard/settings/reports/BotReports.vue` | False | `app/javascript/dashboard/routes/dashboard/settings/reports/reports.routes.js` |
| `accounts/:accountId/captain/:assistantId/faqs` | captain_assistants_responses_index | `app/javascript/dashboard/routes/dashboard/captain/responses/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/documents` | captain_assistants_documents_index | `app/javascript/dashboard/routes/dashboard/captain/documents/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/tools` | captain_tools_index | `app/javascript/dashboard/routes/dashboard/captain/tools/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/scenarios` | captain_assistants_scenarios_index | `app/javascript/dashboard/routes/dashboard/captain/assistants/scenarios/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/playground` | captain_assistants_playground_index | `app/javascript/dashboard/routes/dashboard/captain/assistants/playground/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/inboxes` | captain_assistants_inboxes_index | `app/javascript/dashboard/routes/dashboard/captain/assistants/inboxes/Index.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/faqs/pending` | captain_assistants_responses_pending | `app/javascript/dashboard/routes/dashboard/captain/responses/Pending.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:assistantId/settings` | captain_assistants_settings_index | `app/javascript/dashboard/routes/dashboard/captain/assistants/settings/Settings.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `accounts/:accountId/captain/:navigationPath` | captain_assistants_index | `app/javascript/dashboard/routes/dashboard/captain/pages/AssistantsIndexPage.vue` | False | `app/javascript/dashboard/routes/dashboard/captain/captain.routes.js` |
| `segments/:segmentId` | contacts_dashboard_segments_index | `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue` | False | `app/javascript/dashboard/routes/dashboard/contacts/routes.js` |
| `labels/:label` | contacts_dashboard_labels_index | `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue` | False | `app/javascript/dashboard/routes/dashboard/contacts/routes.js` |
| `active` | contacts_dashboard_active | `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactsIndex.vue` | False | `app/javascript/dashboard/routes/dashboard/contacts/routes.js` |
| `segments/:segmentId` | contacts_edit_segment | `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue` | False | `app/javascript/dashboard/routes/dashboard/contacts/routes.js` |
| `labels/:label` | contacts_edit_label | `app/javascript/dashboard/routes/dashboard/contacts/pages/ContactManageView.vue` | False | `app/javascript/dashboard/routes/dashboard/contacts/routes.js` |
| `live_chat` | campaigns_livechat_index | `app/javascript/dashboard/routes/dashboard/campaigns/pages/LiveChatCampaignsPage.vue` | False | `app/javascript/dashboard/routes/dashboard/campaigns/campaigns.routes.js` |
| `sms` | campaigns_sms_index | `app/javascript/dashboard/routes/dashboard/campaigns/pages/SMSCampaignsPage.vue` | False | `app/javascript/dashboard/routes/dashboard/campaigns/campaigns.routes.js` |
| `auth/reset/password` | auth_reset_password | `app/javascript/v3/views/auth/reset/password/Index.vue` | False | `app/javascript/v3/views/routes.js` |
