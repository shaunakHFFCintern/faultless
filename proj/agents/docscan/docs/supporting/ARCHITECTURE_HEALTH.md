# Architecture Health Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: MEDIUM  
**Evidence Quality**: MEDIUM (OVERCOLLECTION detected)  
**Report Version**: 1.0.0  

### Purpose
This report compiles global health diagnostics, modular complexities, state boundaries, and debugging risks.

### Who should read this
* Engineering Managers
* Frontend Architects
* Technical Project Managers

### Confidence Guide
Confidence is marked as **MEDIUM** because component coupling statistics are derived from overcollected file indexes.

---

## Executive Summary
* Architecture is structured around Vue 3 layouts and ActionCable real-time components.
* Modular density is concentrated in the dashboard folder directories.
* State boundary uses a hybrid of Vuex modules and Pinia stores.
* Client API requests total 186 resolved calls.

---

## Key Findings
| Finding | Why it matters | Severity | Confidence |
|:---|:---|:---:|:---:|
| **Hybrid State Complexity** | Tracking mutations across different stores is complex | Medium | HIGH |
| **Monolithic Layout Files** | Large layouts complicate localized testing | Medium | MEDIUM |
| **Dynamic URL Templates** | URL resolutions are hidden in dynamic evaluations | Low | HIGH |

---

## Detailed Analysis

### Step 1 — Preparation & Health Overview
We reviewed metrics from all collected inventories, identifying 4655 scanned files.

### Step 2 — Analysis of Modular Complexity
Modular density is high within `app/javascript/dashboard`, isolating administrative routes.

### Step 3 — State & Data Boundaries
State data flows through Pinia Call stores and the Vuex main store, presenting dual state setups.

---

## Decision Guidance

### Why would this repo be hard to debug?
Tracing data transitions requires checking multiple Pinia/Vuex actions alongside native browser localStorage setters.

### Where would debugging become expensive?
In integrations API wrappers and configuration mixins where changes can cascade and affect multiple dashboard components.

### Where would UI instability likely emerge?
In real-time dashboards under packet latency peaks if layout components trigger consecutive updates without debouncers.

---

## Evidence Sources
* `evidence/repo_index.json`
* `evidence/state_inventory.json`
* `evidence/api_inventory.json`

---

## Limitations
Static diagnostic metrics represent structural complexity and cannot predict runtime rendering performance.
