# Route Mapping Reasoning Analysis

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: HIGH  
**Evidence Quality**: HIGH  
**Report Version**: 1.0.0  

### Purpose
This report documents Single Page Application routing configurations, path concentration, and layout isolation.

### Who should read this
* Frontend Engineers
* Product Managers
* QA Engineers

### Confidence Guide
Confidence is **HIGH** because SPA routing is parsed directly and deterministically from router files.

---

## Executive Summary
* Single Page Application configs resolve 34 explicit routing paths.
* Routing paths are heavily concentrated under account workspace prefixes.
* Nested views isolate settings, SLA, and CRM details cleanly.
* Routing configurations map access flags dynamically.

---

## Key Findings
| Finding | Why it matters | Severity | Confidence |
|:---|:---|:---:|:---:|
| **Dashboard Concentration** | Modifying account layouts affects nested routes | Medium | HIGH |
| **Protected Access Constraints** | Access gates depend on account settings maps | High | HIGH |
| **Nested Page Isolation** | Isolates distinct layouts (SLA, reports, CRM) | Low | HIGH |

---

## Detailed Analysis

### Step 1 — Preparation & Route Extraction
We scanned configurations from router files, resolving 34 SPA paths.

### Step 2 — Analysis of Route Structures
Most routes (28 out of 34) reside under the `/accounts/:accountId/` prefix, representing dashboard feature components (reports, SLA views, campaigns, linear integration).

### Step 3 — Access Control Gates
Route metadata gates access flags, checking parameters such as enterprise settings or signup authorizations during navigation transitions.

---

## Decision Guidance
* Debugging is hard because nested routes globally inherit the account context.
* Debugging is expensive in router files where changes can break access rules across all dashboard layouts.
* UI instability is likely to emerge during route transitions if components fail to clean up event listeners or watchers.

---

## Evidence Sources
* `evidence/route_graph.json`

---

## Limitations
Static evaluation cannot capture runtime middleware redirects or session-driven path overrides.
