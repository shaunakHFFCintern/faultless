# Risk Assessment Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report evaluates the severity, Scope of Impact, and costs associated with the registered investigation candidates.

### Who should read this
* Engineering Managers
* Security Architects
* QA Directors

### Confidence Guide
Confidence is **HIGH** as assessments map to verified code patterns and files size distributions.

---

## Executive Summary
* Audited risks focus on store state mutations and endpoint clients.
* MFA client bypass holds High severity due to credentials security concerns.
* Calls store drift holds Medium severity due to potential layouts desync.
* Auto-dismiss timers hold Low severity.

---

## Key Findings
| Candidate ID | Claim | Severity | Likelihood (0-100) | Scope of Impact |
|:---|:---|:---:|:---:|:---|
| **FC_001** | Calls Store Mutation Drift | Medium | 65 | Medium |
| **FC_002** | Direct API Auth Wrapper Bypass | High | 40 | High |
| **FC_003** | Auto-Dismiss Timer Possible Timing Interaction | Low | 90 | Low |

---

## Detailed Analysis

### Step 1 — Preparation & Evaluation Criteria
We graded candidates based on Likelihood of occurrence, Severity of failure, and Scope of Impact (affected layouts).

### Step 2 — Analysis of Calls Store Risk (FC_001)
* **Severity**: Medium | **Likelihood**: 65 | **Confidence**: 82
* **Engineering Cost**: Medium | **Business Cost**: Low
* **Justification**: Update references are spread across 90+ files. If calls state variables are mutated unexpectedly, voice calling layouts can desynchronize.

### Step 3 — Analysis of MFA Wrapper Bypass (FC_002)
* **Severity**: High | **Likelihood**: 40 | **Confidence**: 78
* **Engineering Cost**: Low | **Business Cost**: High
* **Justification**: Bypassing centralized client instances skips authorization wrappers, potentially omitting CSRF tokens or custom auth headers in strict security settings.

### Step 4 — Analysis of Auto-Dismiss Timer (FC_003)
* **Severity**: Low | **Likelihood**: 90 | **Confidence**: 85
* **Engineering Cost**: Low | **Business Cost**: Low
* **Justification**: Validation warnings unmount automatically after 1.5 seconds. While this introduces user registration layout friction, it presents low business risk.

---

## Decision Guidance
Refer to the Recommended Actions and Leave-As-Is reports to authorize engineering resources.

---

## Evidence Sources
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`
* `evidence/event_inventory.json`

---

## Limitations
Risk assessment is a static evaluation of code structures and does not monitor real-time network attack vectors.
