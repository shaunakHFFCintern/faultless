# Investigation Candidates Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report registers and evaluates high confidence investigation candidates representing structural vulnerability risks.

### Who should read this
* Frontend Engineers
* QA Leads
* Security Engineers

### Confidence Guide
Confidence is **HIGH** as the listed candidates represent direct code structure anomalies supported by explicit inventory entries.

---

## Executive Summary
* Audited codebase shows structural anomalies that present potential runtime risks.
* The Calls store is mutated by over 90 different files, creating state drift.
* MFA validation invokes axios directly, bypassing global interceptor configurations.
* Validation warning layouts unmount after fixed timers, creating Timing Interactions.

---

## Key Findings
| Candidate ID | Claim | Severity | Confidence | Classification |
|:---|:---|:---:|:---:|:---|
| **FC_001** | Calls Store Mutation Drift | Medium | 0.82 | Hypothesis |
| **FC_002** | Direct API Auth Wrapper Bypass | High | 0.78 | Derived |
| **FC_003** | Auto-Dismiss Timer Possible Timing Interaction | Low | 0.85 | Derived |

---

## Detailed Analysis

### Step 1 — Preparation & Candidate Registration
We evaluated file inventories to isolate patterns presenting deviations from core design standards.

### Step 2 — Analysis of Calls Store Drift (FC_001)
* **Area**: Dashboard calls state module.
* **Trigger**: Triggering calls actions or mutations from helper and locales modules.
* **Evidence**: `calls.js` registers **98 mutator reference locations** (`state_inventory.json` line 312-412).
* **Counter Evidence**: Pinia namespaces isolate states.
* **Why It Matters**: Arbitrary state mutations can lead to desynchronized call statuses.

### Step 3 — Analysis of MFA HTTP Wrapper Bypass (FC_002)
* **Area**: Authentication & MFA modules.
* **Trigger**: Multi-Factor Authentication initialization.
* **Evidence**: `MfaVerification.vue` invokes `/auth/sign_in` (POST) directly (`api_inventory.json` line 7).
* **Counter Evidence**: Axios instances might be configured globally.
* **Why It Matters**: Bypassing client wrappers skips auth token setups and tracking headers.

### Step 4 — Analysis of Auto-Dismiss Timer (FC_003)
* **Area**: Common Layout UI elements (Banners / Tooltips).
* **Trigger**: validation warning banner mount.
* **Evidence**: `Banner.vue:18` implements `setTimeout` with a hardcoded `1500ms` dismiss limit (`event_inventory.json` line 252).
* **Counter Evidence**: Layout unmount clears active timers.
* **Why It Matters**: Auto-dismissing banners can remove error messages before users finish reading.

---

## Decision Guidance
Refer to the Debug Guide and Resolution Options reports to plan corrective actions for these candidates.

---

## Evidence Sources
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`
* `evidence/event_inventory.json`

---

## Limitations
Investigation candidates represent potential structural vulnerabilities and do not confirm runtime failures.
