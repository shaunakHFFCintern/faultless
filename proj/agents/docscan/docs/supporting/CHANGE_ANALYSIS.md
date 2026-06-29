# Change Impact Evaluation Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report evaluates the testing scopes, rollout complexities, and rollback risks associated with resolving the investigation candidates.

### Who should read this
* QA Managers
* Frontend Lead Engineers
* Release Managers

### Confidence Guide
Confidence is **HIGH** as affected files are located directly in the static module directory layout.

---

## Executive Summary
* Resolving the Calls store drift affects layout templates and Pinia store modules.
* Resolving the MFA HTTP client bypass affects `MfaVerification.vue` client requests.
* Resolving the auto-dismiss timer timing interactions modifies visual warning layouts.
* Rollback complexity across all options is low.

---

## Key Findings
| Candidate ID | Target Component | State / API Impact | Rollback Complexity | Release Risk |
|:---|:---|:---|:---|:---|
| **FC_001** | `FloatingCallWidget.vue` | Pinia calls store updates | Low | Low |
| **FC_002** | `MfaVerification.vue` | POST `/auth/sign_in` client calls | Low | Medium |
| **FC_003** | `Banner.vue` | Local error active flags | Low | Low |

---

## Detailed Analysis

### Step 1 — Impact Matrix: Resolving Calls Store Drift (FC_001)
* **Components Affected**: `FloatingCallWidget.vue`, `VoiceCallButton.vue`, call-control layout wrappers.  
  - *Classification*: **Derived**
* **Routes Affected**: None.  
  - *Classification*: **Observed**
* **APIs Affected**: None.  
  - *Classification*: **Observed**
* **State Affected**: `calls` Pinia store.  
  - *Classification*: **Observed**
* **Testing Scope**: Unit tests for calls store actions and integration tests for Webrtc voice call connections.  
  - *Classification*: **Predicted**
* **Deployment Risk**: Low.  
  - *Classification*: **Predicted**
* **Rollback Complexity**: Low.  
  - *Classification*: **Predicted**
* **Expected Stability Gain**: High (deterministic voice call states).  
  - *Classification*: **Predicted**
* **Unexpected Side Effects**: Locales and specs that directly mock state properties may fail to compile if properties are protected.  
  - *Classification*: **Predicted**

### Step 2 — Impact Matrix: Resolving MFA Wrapper Bypass (FC_002)
* **Components Affected**: `MfaVerification.vue`.  
  - *Classification*: **Observed**
* **Routes Affected**: `/auth/reset/password`.  
  - *Classification*: **Observed**
* **APIs Affected**: `POST /auth/sign_in`.  
  - *Classification*: **Observed**
* **State Affected**: Local credentials payload.  
  - *Classification*: **Observed**
* **Testing Scope**: Integration tests for login validation and Multi-Factor authentication flows.  
  - *Classification*: **Predicted**
* **Deployment Risk**: Medium.  
  - *Classification*: **Predicted**
* **Rollback Complexity**: Low.  
  - *Classification*: **Predicted**
* **Expected Stability Gain**: High (consistent headers transmission).  
  - *Classification*: **Predicted**
* **Unexpected Side Effects**: If centralized client interceptors intercept requests with unexpected redirection paths, authentication flows could trigger infinite redirection loops.  
  - *Classification*: **Predicted**

### Step 3 — Impact Matrix: Resolving Auto-Dismiss Timer (FC_003)
* **Components Affected**: `Banner.vue`.  
  - *Classification*: **Observed**
* **Routes Affected**: `/prechat-form`.  
  - *Classification*: **Observed**
* **APIs Affected**: None.  
  - *Classification*: **Observed**
* **State Affected**: Local error display status variables.  
  - *Classification*: **Observed**
* **Testing Scope**: Validation inputs error visual verification tests.  
  - *Classification*: **Predicted**
* **Deployment Risk**: Low.  
  - *Classification*: **Predicted**
* **Rollback Complexity**: Low.  
  - *Classification*: **Predicted**
* **Expected Stability Gain**: High (improved user registration flow).  
  - *Classification*: **Predicted**
* **Unexpected Side Effects**: Banners will persist indefinitely if users fail to click dismiss, potentially blocking other input areas.  
  - *Classification*: **Predicted**

---

## Decision Guidance
Ensure rollback procedures are documented prior to migrating authentication workflows.

---

## Evidence Sources
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`
* `evidence/event_inventory.json`

---

## Limitations
Impact claims are predicted based on static dependencies and actual rollout performance depends on client browser environments.
