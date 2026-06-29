# Project Risk Register

This document is the primary decision-making record for the DocScan frontend pipeline. It synthesizes structural analyses, coupling hotspots, and routing configurations into actionable engineering tasks. It is designed to stand alone, providing Engineering Managers, Senior Engineers, and team members with the context needed to decide what to fix, what to schedule, and what to accept without reading auxiliary reports.

---

## Issue 1: Direct API Wrapper Bypass during MFA Verification (FC_002)

| Parameter | Assessment & Details |
| :--- | :--- |
| **Priority** | **High** |
| **Severity** | **High** |
| **Recommended Action**| **Fix Immediately** |
| **Problem** | The Multi-Factor Authentication (MFA) verification layout (`MfaVerification.vue`) makes validation requests directly through the raw client library instead of using the central custom Axios wrapper. |
| **Affected Areas** | Authentication modules, sign-in flow (`/auth/sign_in`), password reset layouts, and user verification pages. |
| **Why This Happens** | The code directly imports and executes generic HTTP request methods, which bypasses the workspace's centralized request configuration rules. |
| **What Engineers Observe** | Authentication validation attempts fail with `401 Unauthorized` or `403 Forbidden` console warnings. This happens because the request lacks CSRF tokens and tracking cookies needed by the backend. |
| **What Happens If Left As Is** | If server-side routing or authentication policies are updated, user sign-in attempts will fail instantly. This locks users out of their dashboards. |
| **Business Impact** | **High Impact:** Support agents and administrators will be blocked from logging into the platform. This leads to immediate customer service interruptions and violates system availability agreements. |
| **Engineering Impact** | Direct calls bypass telemetry interceptors, which means developers cannot collect metrics on sign-in latency, monitor API drift, or trace authentication failures. |
| **Suggested Resolution** | Replace the direct Axios call in `MfaVerification.vue` with the shared HTTP client wrapper to ensure headers are added automatically. |
| **Implementation Complexity** | **Low:** Requires modifying a single file (`MfaVerification.vue`) to import and use the standard Axios wrapper. |
| **Expected Impact of Change** | Restores proper header injection for all MFA sign-in requests, ensuring login stability. |
| **Risk of Change** | **Low:** The shared Axios client is already well-tested and active across more than 180 other endpoints. |
| **Supporting Evidence** | `evidence/api_inventory.json` & `docs/API_REASONING.md` |

---

## Issue 2: Calls Store Mutation Drift (FC_001)

| Parameter | Assessment & Details |
| :--- | :--- |
| **Priority** | **Medium** |
| **Severity** | **Medium** |
| **Recommended Action**| **Schedule Refactor** |
| **Problem** | The calls state store (`calls.js`) is directly mutated by 98 different components, helpers, and files instead of restricting state changes to dedicated actions. |
| **Affected Areas** | Voice call widget (`FloatingCallWidget.vue`), start call trigger (`VoiceCallButton.vue`), and real-time dashboard elements. |
| **Why This Happens** | The codebase lacks rules to protect store properties, allowing any layout component to import and rewrite calls state variables directly. |
| **What Engineers Observe** | The calling interface shows active call widgets when a call is disconnected. In some cases, concurrent calling transitions fail due to values being overwritten mid-session. |
| **What Happens If Left As Is** | Calling layout components will continue to drift. This results in intermittent call state issues and increases the time developers spend debugging the widget. |
| **Business Impact** | **Medium Impact:** Support agents will experience visual bugs during calls. This leads to delayed ticket updates and lowers agent productivity. |
| **Engineering Impact** | Engineers cannot trace which module modified state variables. This increases the scope of regression testing and slows down store refactoring. |
| **Suggested Resolution** | Restructure the store to expose read-only state properties and enforce modifications exclusively through Pinia store actions. |
| **Implementation Complexity** | **Medium:** Requires auditing and updating references across multiple files to route mutations through store actions. |
| **Expected Impact of Change** | Eliminates race conditions and side-effects, making calling states predictable. |
| **Risk of Change** | **Medium:** Requires careful testing of WebRTC call handlers and integration test cases during the update. |
| **Supporting Evidence** | `evidence/state_inventory.json` & `docs/STATE_REASONING.md` |

---

## Issue 3: Auto-Dismiss Warning Banners (FC_003)

| Parameter | Assessment & Details |
| :--- | :--- |
| **Priority** | **Low** |
| **Severity** | **Low** |
| **Recommended Action**| **Monitor** |
| **Problem** | Form validation warning banners (`Banner.vue`) automatically close after a hardcoded 1.5-second timer. |
| **Affected Areas** | Pre-chat registration page (`/prechat-form`) and general form layouts. |
| **Why This Happens** | The component uses a simple JavaScript timer loop on mount that triggers the hide callback. |
| **What Engineers Observe** | Banners dismiss themselves before the user finishes reading, causing users to repeatedly submit incorrect details. |
| **What Happens If Left As Is** | Form submission usability issues will continue. However, this has no impact on data storage, network traffic, or security. |
| **Business Impact** | **Low Impact:** Creates minor friction during initial registration. This may slightly delay customer signup steps. |
| **Engineering Impact** | Minimal effect. It is a visual layout issue that does not impact server performance. |
| **Suggested Resolution** | Remove the hardcoded timer loop and add a clear close button so the banner remains open until dismissed. |
| **Implementation Complexity** | **Low:** Requires deleting the timer setup in the component template and rendering a close icon. |
| **Expected Impact of Change** | Ensures compliance with accessibility guidelines, allowing users to correct errors at their own pace. |
| **Risk of Change** | **Low:** Purely visual change that does not interact with backend APIs or global state. |
| **Supporting Evidence** | `evidence/event_inventory.json` & `docs/EVENT_REASONING.md` |

---

## Executive Summary

This summary maps the immediate and long-term concerns of the DocScan audit, providing estimate guidelines for engineering planning.

### Top 3 Immediate Concerns
1. **Direct Security Gate Bypass during Multi-Factor Authentication:** Raw API endpoints bypass centralized Axios interceptors, causing sign-in failures under corporate proxy servers that require authentication headers.
2. **Calls Store Mutation Drift:** Direct state overwrites across 98 components create random calling widget states, which make it difficult to determine call connections.
3. **Hybrid State Paradigms:** Splitting state variables between Vuex modules and Pinia stores increases developer cognitive load and increases the risk of state bugs during feature development.

### Top 3 Future Concerns
1. **Direct Browser Storage Access:** Direct reads and writes of keys like `impersonationUser` bypass centralized change tracking. This makes it difficult to manage storage values during user sessions.
2. **Access Control Routing Gate Density:** SPA routes are nested under account workspace prefixes. This increases the risk of breaking security access gates when editing route configurations.
3. **Watcher Cascades and Input Validation Loops:** Input wrappers lack debouncing, which can trigger infinite reactive calculations and slow down the main thread.

### Top 3 Acceptable Risks
1. **Auto-Dismiss Warning Banners:** The 1.5-second banner timer causes minor onboarding layout friction, but it has no impact on database integrity or security.
2. **Dynamic Endpoint Resolution:** API paths resolve at runtime. Although this cannot be verified via static code analysis, the risk is accepted as path changes are managed during API releases.
3. **Static Scanner Visibility Limits:** The static scanning process cannot resolve runtime dynamic components, which is accepted due to Vue’s fallback error boundaries.

### Estimated Engineering Effort
* **High-Priority Remediation (MFA Axios Wrapper Refactor):** **2 Engineering Days** (1 Developer for 2 days to refactor, test with proxy variables, and deploy).
