# Leave-As-Is Assessment

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report evaluates the operational and cost implications of accepting the registered investigation candidates without active resolution.

### Who should read this
* Engineering Managers
* QA Leads
* Technical Operations Leads

### Confidence Guide
Confidence is **HIGH** as assessments are derived from codebase structure size and dependencies metrics.

---

## Executive Summary
* Non-resolution of structural issues carries specific operational and developer maintenance costs.
* Direct HTTP client bypasses cannot be safely ignored long term.
* Calls store mutations drift risks call disconnect events under high volume.
* Layout timer timing interactions present low risk and are safe to ignore indefinitely.

---

## Key Findings
| Candidate ID | Claim | Safe to Ignore? | Maximum Safe Duration | Monitor Targets |
|:---|:---|:---:|:---:|:---|
| **FC_001** | Calls Store Mutation Drift | NO | 6 months | Calls state updates, activeCall resets |
| **FC_002** | Direct API Client Bypass | NO | 1 month | Auth error rates, connection drops |
| **FC_003** | Auto-Dismiss Timer Timing Interaction | YES | Indefinite | Form drop-off rates |

---

## Detailed Analysis

### Step 1 — Assessment: Calls Store Mutation Drift (FC_001)
* **Safe To Ignore**: NO
* **Short Term Impact**: Minor call status UI desynchronizations in dashboard layouts.
* **Long Term Impact**: Unpredictable Pinia store values during concurrent calls transitions.
* **Failure Growth Pattern**: Linear (increases as more modules import the store).
* **Operational Impact**: Voice call connections may occasionally drop or display incorrect status states.
* **Developer Cost**: High (increased regression checking time).
* **Business Cost**: Low.
* **Maximum Safe Duration**: 6 months.
* **What must be monitored if accepted**: Monitor calls store update events at runtime and watch for activeCall state resets during live voice channel sessions.

### Step 2 — Assessment: Direct API Auth Wrapper Bypass (FC_002)
* **Safe To Ignore**: NO
* **Short Term Impact**: Omission of custom request tracking telemetry headers on MFA requests.
* **Long Term Impact**: Security headers blockages at server gateways when security rules evolve.
* **Failure Growth Pattern**: Step-function (manifests immediately upon changes to backend security configurations).
* **Operational Impact**: MFA logins may fail for clients behind enterprise proxies that require specific custom headers.
* **Developer Cost**: Low.
* **Business Cost**: High.
* **Maximum Safe Duration**: 1 month.
* **What must be monitored if accepted**: Monitor authentication error rate (HTTP 401/403) specifically on `/auth/sign_in` endpoints under enterprise proxy settings.

### Step 3 — Assessment: Auto-Dismiss Timer (FC_003)
* **Safe To Ignore**: YES
* **Short Term Impact**: Validation banners close before users complete reading.
* **Long Term Impact**: Usability friction during user registrations.
* **Failure Growth Pattern**: Static (remains limited to Pre-Chat banner component limits).
* **Operational Impact**: None.
* **Developer Cost**: Low.
* **Business Cost**: Low.
* **Maximum Safe Duration**: Indefinite.
* **What must be monitored if accepted**: Monitor registration form submission drop-off rates and customer support queries concerning invalid pre-chat registrations.

---

## Decision Guidance
Ensure monitoring integrations are configured immediately for any accepted candidates.

---

## Evidence Sources
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`
* `evidence/event_inventory.json`

---

## Limitations
Leave-as-is risks are predicted based on static structures and can escalate under unexpected traffic spikes.
