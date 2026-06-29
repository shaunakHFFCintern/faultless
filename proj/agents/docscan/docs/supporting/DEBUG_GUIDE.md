# Debug Guide Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report registers priority targets and guides engineers on debugging strategies based on risk impact scores.

### Who should read this
* Frontend Engineers
* QA Engineers
* Support Developers

### Confidence Guide
Confidence is **HIGH** as scoring calculations rely on verified code location metrics.

---

## Executive Summary
* Debugging efforts are prioritized by difficulty and Scope of Impact.
* Auto-dismiss timer check is the highest priority due to low complexity.
* Calls store audit holds high priority due to wide mutation scope.
* MFA auth bypass audit holds medium priority.

---

## Key Findings
| Target Candidate | Debug Priority | Difficulty | Scope of Impact | Confidence |
|:---|:---:|:---:|:---:|:---:|
| **FC_003** (Auto-Dismiss Timer) | **8.5** | Low | Low | 0.85 |
| **FC_001** (Calls Store Drift) | **8.2** | High | High | 0.82 |
| **FC_002** (Direct API Bypass) | **7.8** | Medium | Medium | 0.78 |

---

## Detailed Analysis

### Step 1 — Priority Registry Table
The following matrix ranks candidates based on difficulty (cost to verify/refactor) and Scope of Impact (system failure scope of impact).

| Candidate ID | Claim | Difficulty | Scope of Impact | Confidence | Priority Score | Recommendation |
|:---|:---|:---|:---|:---|:---|:---|
| **FC_003** | Auto-Dismiss Timer Possible Timing Interaction | Low | Low | 0.85 | **8.5** | Check `Banner.vue:18` and evaluate dismiss callback triggers |
| **FC_001** | Calls Store Mutation Drift | High | High | 0.82 | **8.2** | Audit Pinia store import references in dashboard helper modules |
| **FC_002** | Direct API Auth Wrapper Bypass (API Drift) | Medium | Medium | 0.78 | **7.8** | Verify Axios client integration inside `MfaVerification.vue:70` |

---

## Decision Guidance
* Review `Banner.vue:18` first (low effort, high priority).
* Plan Pinia calls store refactoring alongside upcoming dashboards cleanup cycles.

---

## Evidence Sources
* `evidence/event_inventory.json`
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`

---

## Limitations
Debug prioritization is based on structural metrics and is not an assessment of active bug occurrences.
