# Frontend Overview Report

**Generated Date**: 2026-06-25  
**Repository**: workspace/codebase/chatwoot  
**Confidence**: MEDIUM (82/100)  
**Evidence Quality**: MEDIUM (OVERCOLLECTION detected)  
**Report Version**: 1.0.0  

### Purpose
This report integrates all static structural analyses, coupling hotspots, routing configurations, and architectural boundaries.

### Who should read this
* Engineering Managers
* Frontend Engineers
* Cross-functional Leaders

### Confidence Guide
Confidence is marked as **MEDIUM** because our parsing model classified every file as a separate component, which represents **OVERCOLLECTION** and reduces the fidelity of calculated coupling metrics.

---

## Executive Summary
* Consolidated structural analysis identifies dependencies clustering in the Vue 3 and ActionCable real-time modules.
* Core dashboard routing paths are highly concentrated under account configuration parameters.
* Direct endpoint calls exist that bypass global auth configurations, creating potential API drift.
* Store data mutations are highly distributed, risking state synchronization drift.

---

## Key Findings
| Finding | Why it matters | Severity | Confidence |
|:---|:---|:---:|:---:|
| **Vue & ActionCable Clustering** | Highlights largest production dependency groupings | Medium | HIGH |
| **Account Route Concentration** | Concentrates routing logic under account prefix | Medium | HIGH |
| **Distributed Calls Store Mutations** | Creates state drift risks across layouts | Medium | HIGH |
| **MFA HTTP Wrapper Bypass** | Skips global security/auth interceptors | High | MEDIUM |

---

## Detailed Analysis

### Step 1 — Preparation & Evidence Validation
We validated evidence across all inventory catalogs. The component model is classified as **OVERCOLLECTION** due to component count matching file count (4655). Route mapping (34) and API client mappings (186) show high completeness.

### Step 2 — Analysis of Dependency Clusters
The codebase production dependencies (80) and devDependencies (36) show high concentration in:
* Vue 3 Core (`vue`, `vue-router`, `pinia`, `vuex`)
* Live Communications (`@rails/actioncable`)
* Third-party integrations (`chart.js`, `dyte`, `linear`)

### Step 3 — Structural Coupling & Boundaries
Shared mixins (`configMixin.js`) and UI layouts serve as coupling hotspots. Because of overcollection, structural graphs show exaggerated fan-in metrics.

---

## Decision Guidance
* Enforce Pinia actions interfaces for calls store changes.
* Migrate dynamic MFA axios calls into the global HTTP client setup.
* Monitor error validation dialog dismissal timers.

---

## Evidence Sources
* `evidence/repo_index.json`
* `evidence/component_graph.json`
* `evidence/route_graph.json`
* `evidence/api_inventory.json`
* `evidence/state_inventory.json`

---

## Limitations
Static evaluation does not execute scripts or trace live lifecycle states, meaning dynamic import paths or conditional layout overrides cannot be resolved.
