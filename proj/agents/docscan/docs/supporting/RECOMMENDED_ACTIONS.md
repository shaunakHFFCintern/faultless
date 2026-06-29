# Recommended Actions Matrix

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This matrix summarizes priority actions, likelihood scores, and rationale to assist engineering decisions.

### Who should read this
* Engineering Directors
* Technical Leads

### Confidence Guide
Confidence is **HIGH** as suggestions align directly with audited risk severity rankings.

---

## Executive Summary
* Recommended actions are structured by severity and implementation difficulty.
* Immediate resolution is advised for the MFA client bypass.
* Auditing the calls store is scheduled for later cycles.
* User timing interactions on validation warnings are accepted with monitoring.

---

## Recommended Actions Registry

| Candidate | Severity | Likelihood | Confidence | Fix Now | Fix Later | Accept | Monitor | Rationale |
|:---|:---|:---|:---|:---:|:---:|:---:|:---:|:---|
| **FC_001** | Medium | 65 | 82 | | [X] | | | Calls store mutation structure has a wide scope of impact; audit during upcoming Pinia store cleanups. |
| **FC_002** | High | 40 | 78 | [X] | | | | Security-related bypass requires immediate alignment with global HTTP client interceptors. |
| **FC_003** | Low | 90 | 85 | | | [X] | [X] | Low operational impact. Banner dismissal can be accepted in the short term and monitored for user feedback. |

---

## Detailed Analysis

### Step 1 — Immediate Possible Resolution: FC_002
Integrate MFA API calls with the central Axios interceptors setup to ensure CSRF cookies and custom headers are consistently set.

### Step 2 — Scheduled Possible Resolution: FC_001
Restructure calls store updates to restrict direct mutations and funnel changes exclusively through store actions.

### Step 3 — Acceptance with Monitoring: FC_003
Accept the timing interaction but monitor form drop-offs.

---

## Decision Guidance
Obtain product management validation for Option A resolution on FC_002 prior to execution.

---

## Evidence Sources
* `docs/RISK_ASSESSMENT.md`
* `docs/RESOLUTION_OPTIONS.md`

---

## Limitations
The matrix acts as an advisory checklist and does not represent an executive engineering mandate.
