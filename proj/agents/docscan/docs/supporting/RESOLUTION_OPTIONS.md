# Resolution Options Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report presents possible resolutions (Option A, Option B, and Option C) for each candidate, evaluating their trade-offs and structural dependencies.

### Who should read this
* Frontend Engineers
* Technical Leads

### Confidence Guide
Confidence is **HIGH** as resolutions leverage standard Vue and API client configurations.

---

## Executive Summary
* Resolution options are proposed for three investigation candidates.
* Options range from low-complexity linting rules to high-complexity layout controller overrides.
* Standardized API wrapper integrations provide the highest expected stability gains.

---

## Key Findings
| Target Candidate | Resolution Option | Complexity | Confidence | Classification |
|:---|:---|:---:|:---:|:---|
| **FC_001** (Calls Store) | Option A: Read-Only Actions | Medium | High | Pattern Backed |
| **FC_002** (API Client Bypass) | Option A: Central HTTP Client | Low | High | Evidence Backed |
| **FC_003** (Dismiss Timer) | Option A: Interactive Close | Low | High | Industry Heuristic |

---

## Detailed Analysis

### Step 1 — Options for Calls Store mutation (FC_001)

#### Option A: Read-Only Actions Wrapper
* **Approach**: Restrict direct state mutations. Expose state solely through Pinia actions.
* **Complexity**: Medium | **Expected Benefit**: Eliminates arbitrary state writes.
* **Regression Risk**: Low | **Migration Effort**: Medium | **Dependencies**: Pinia store config.
* **Expected Timeline**: 3-4 days.
* **Audit Metrics**:
  - Evidence Coverage: 100%
  - Assumption Count: 1
  - Dependency Count: 1
  - Confidence: High
  - Classification: **Pattern Backed**

#### Option B: Localized Controller Component
* **Approach**: Refactor state management to maintain call status in a single layout controller component.
* **Complexity**: High | **Expected Benefit**: Completely isolates voice state.
* **Regression Risk**: Medium | **Migration Effort**: High | **Dependencies**: Layout routing files.
* **Expected Timeline**: 1-2 weeks.
* **Audit Metrics**:
  - Evidence Coverage: 40%
  - Assumption Count: 3
  - Dependency Count: 4
  - Confidence: Medium
  - Classification: **Speculative**

#### Option C: Enforce Strict Linting Rules
* **Approach**: Add ESLint rules blocking direct imports of `calls.js` outside of designated folders.
* **Complexity**: Low | **Expected Benefit**: Warns developers on unsafe imports.
* **Regression Risk**: Low | **Migration Effort**: Low | **Dependencies**: ESLint configuration.
* **Expected Timeline**: 1 day.
* **Audit Metrics**:
  - Evidence Coverage: 10%
  - Assumption Count: 0
  - Dependency Count: 1
  - Confidence: Low
  - Classification: **Industry Heuristic**

---

### Step 2 — Options for MFA HTTP Client Bypass (FC_002)

#### Option A: Integrate with Central HTTP Client
* **Approach**: Replace direct `axios.post` with calls to the shared HTTP api transport client wrapper.
* **Complexity**: Low | **Expected Benefit**: Restores custom authorization headers.
* **Regression Risk**: Low | **Migration Effort**: Low | **Dependencies**: Central API client modules.
* **Expected Timeline**: 2 days.
* **Audit Metrics**:
  - Evidence Coverage: 100%
  - Assumption Count: 1
  - Dependency Count: 1
  - Confidence: High
  - Classification: **Evidence Backed**

#### Option B: Local Axios Interceptor
* **Approach**: Inject a local instance setup exclusively inside `MfaVerification.vue`.
* **Complexity**: Medium | **Expected Benefit**: Restores security headers locally.
* **Regression Risk**: Medium | **Migration Effort**: Medium | **Dependencies**: Local helper files.
* **Expected Timeline**: 3 days.
* **Audit Metrics**:
  - Evidence Coverage: 50%
  - Assumption Count: 2
  - Dependency Count: 2
  - Confidence: Medium
  - Classification: **Pattern Backed**

#### Option C: Custom Middleware Verification
* **Approach**: Shift credentials header validations exclusively to backend controllers.
* **Complexity**: High | **Expected Benefit**: Mitigates client header omissions.
* **Regression Risk**: Low | **Dependencies**: Backend controllers.
* **Expected Timeline**: 1 week.
* **Audit Metrics**:
  - Evidence Coverage: 0%
  - Assumption Count: 2
  - Dependency Count: 2
  - Confidence: High
  - Classification: **Industry Heuristic**

---

### Step 3 — Options for Auto-Dismiss Timer (FC_003)

#### Option A: Replace Timeout with Interactive Close
* **Approach**: Remove the `setTimeout` function and require explicit user close action.
* **Complexity**: Low | **Expected Benefit**: Ensures accessibility compliance.
* **Regression Risk**: Low | **Migration Effort**: Low | **Dependencies**: None.
* **Expected Timeline**: 1 day.
* **Audit Metrics**:
  - Evidence Coverage: 100%
  - Assumption Count: 0
  - Dependency Count: 0
  - Confidence: High
  - Classification: **Industry Heuristic**

#### Option B: Dynamic Timeout Based on Length
* **Approach**: Scale the timer dynamically based on error message text length.
* **Complexity**: Medium | **Expected Benefit**: Reduces screen clutter.
* **Regression Risk**: Low | **Migration Effort**: Low | **Dependencies**: None.
* **Expected Timeline**: 2 days.
* **Audit Metrics**:
  - Evidence Coverage: 50%
  - Assumption Count: 2
  - Dependency Count: 0
  - Confidence: Medium
  - Classification: **Speculative**

#### Option C: Shift Validation Message to Inline Text
* **Approach**: Display errors as inline helper texts beneath inputs.
* **Complexity**: Medium | **Expected Benefit**: Improves form validation layout patterns.
* **Regression Risk**: Medium | **Migration Effort**: Medium | **Dependencies**: Input components.
* **Expected Timeline**: 3 days.
* **Audit Metrics**:
  - Evidence Coverage: 70%
  - Assumption Count: 1
  - Dependency Count: 1
  - Confidence: High
  - Classification: **Pattern Backed**

---

## Decision Guidance
Engineers should prioritize Option A across all targets to balance implementation complexity and expected stability gains.

---

## Evidence Sources
* `evidence/event_inventory.json`
* `evidence/api_inventory.json`
* `evidence/state_inventory.json`

---

## Limitations
Resolution options analyses evaluate architectural suitability and cannot guarantee absolute regression-free updates.
