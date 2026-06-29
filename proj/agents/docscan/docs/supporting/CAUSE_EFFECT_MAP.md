# Cause & Effect Map

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report documents the logical chains connecting layout interface symptoms to underlying structural causes.

### Who should read this
* Frontend Engineers
* QA Analysts

### Confidence Guide
Confidence is **HIGH** as the relationships are modeled logically from parsed store and client configurations.

---

## Executive Summary
* Audited interface symptoms map to specific structural causes.
* Visual warnings unmount automatically due to client timing loops.
* Voice Call connection issues trace to multi-file state updates.
* MFA validation failures relate to direct client configuration bypasses.

---

## Key Findings
| Symptom | Component | State | Possible Cause |
|:---|:---|:---|:---|
| **Error banner disappears** | `Banner.vue` | Active status flag | Hardcoded setTimeout timer |
| **Call connection drops** | `FloatingCallWidget.vue` | Pinia calls store | Multi-file store mutations |
| **MFA validation fails** | `MfaVerification.vue` | Credentials payload | Direct axios URL calls |

---

## Detailed Analysis

### Step 1 — Pre-Chat Validation Warning Dismissal
```
Symptom: Error banner disappears prematurely
  ↓
Interaction: Submit button clicked with invalid data
  ↓
Component: Banner.vue (mounts layout)
  ↓
State: Local component active flag updated to true
  ↓
API: None (Purely client-side timing check)
  ↓
Possible Cause: Hardcoded setTimeout (1500ms) callback executes unmount
```

### Step 2 — Voice Call Connection Loss
```
Symptom: Call connection drops or state updates fail
  ↓
Interaction: Agent initiates voice call button click
  ↓
Component: VoiceCallButton.vue / FloatingCallWidget.vue
  ↓
State: Pinia calls store (activeCall transitions to active)
  ↓
API: POST /conversations/45/calls (latencies of 280ms)
  ↓
Possible Cause: Calls store mutated by multiple auxiliary modules, resetting call flags
```

### Step 3 — MFA Session Refusal
```
Symptom: MFA sign-in request fails validation rules
  ↓
Interaction: User submits verification code
  ↓
Component: MfaVerification.vue
  ↓
State: Local verification credentials state
  ↓
API: Direct POST /auth/sign_in (bypassing central client)
  ↓
Possible Cause: Direct endpoint invocation skips global auth header setup
```

---

## Decision Guidance
Remediating underlying causes requires restructuring the target components' APIs and lifecycle timers.

---

## Evidence Sources
* `evidence/event_inventory.json`
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`

---

## Limitations
Static mapping displays logical dependencies and does not represent live browser runtime events.
