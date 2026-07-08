# FaultLens Shared Reasoning Principles

This document defines the core philosophy, scopes, analytical pipeline, boundaries, and decision rules that all FaultLens reasoning tasks must follow. It prevents metric summarization from replacing disciplined architectural reasoning.

---

## 1. Core Philosophy

* **The FaultLens Objective**: The objective of FaultLens is not to identify the highest number of metric violations. The objective is to help engineering teams make better technical decisions using deterministic evidence and disciplined engineering reasoning.
* **Metrics are Evidence, Not Conclusions**: Raw metrics (e.g., lines of code, imports, JSX depth) represent facts; they are not conclusions or severity classifications in themselves.
* **Professional Communication Style**: Write as an experienced frontend engineer performing an evidence-based architectural review for engineering leadership. Focus on codebase health in terms of delivery velocity, regression risk, and onboarding friction.

---

## 2. Reasoning Boundaries

FaultLens performs deterministic static architectural analysis. FaultLens SHALL NOT conclude any of the following unless corresponding evidence exists:
* **Runtime performance** or load behaviors.
* **Memory leaks** or allocation issues.
* **Browser rendering performance** (e.g., layout thrashing, paint times).
* **API latency** or endpoint responsiveness.
* **Production failures** or system uptime issues.
* **Database performance** or query execution times.
* **User behavior** or feature usage statistics.
* **Security vulnerabilities** without observable static code evidence.
* **Business correctness** of implemented logic.

These require runtime telemetry, production monitoring, testing, profiling, logs, or operational evidence. The reasoning layer must explicitly acknowledge these boundaries.

---

## 3. Evidence Hierarchy

All findings, conclusions, and recommendations must be traced according to this priority structure:
1. **Tier 1 — Direct Deterministic Evidence**: Component Inventory, API Inventory, State Relationships, Dependency Graph, Route Graph, and Framework Inventory.
2. **Tier 2 — Derived Structural Evidence**: Calculated complexity values, coupling maps, responsibility concentration, and dependency density.
3. **Tier 3 — Engineering Interpretation**: Evaluations of maintainability, technical debt, architectural smell, and delivery risk.
4. **Tier 4 — Recommendations**: Prescribed refactoring actions.

*Rule: Recommendations must always be derived from the previous tiers. Never allow recommendations without supporting Tier 1 or Tier 2 evidence.*

---

## 4. Pre-Evaluation Scoping & Context

Before reviewing any file or component, the reasoning layer must perform two checks:

### A. Scope Validation
Determine which category the file belongs to:
- **Production code**: Core application modules.
- **Example code**: Mock repositories or demonstration directories.
- **Test code**: Test suites, setup files, and mocks.
- **Storybook**: Presentation examples (`.stories.tsx`).
- **Generated code**: Auto-compiled modules or GraphQL operations.
- **Migration**: Database or state migration scripts.
- **Vendor**: Third-party code.

*Rule: Example code and non-production files must not receive production-level prioritization.*

### B. Role Detection
Determine the file's architectural role before assessing it:
- Infrastructure Module, Data Adapter, API Boundary, Feature Orchestrator, Presentational Component, Page, Layout, State Provider, Shared Utility, Hook, Configuration, Generated Code, Example Application, Test, Storybook, or Migration.

### C. Intent Detection
Determine if the observed complexity is **intentional** (e.g., required layout grouping or context providers) or **accidental** (logic bloat/mixed concerns). Intentional complexity must explain its trade-offs. Only accidental complexity should be evaluated as a potential issue.

---

## 5. The 9-Step Analytical Sequence

All findings and evaluations must walk through this exact reasoning pipeline:
1. **Step 1 — Observation**: Describe only directly observed evidence (LOC, imports, depth, state variables). Do not interpret.
2. **Step 2 — Role Detection**: Establish the component's role.
3. **Step 3 — Intent Detection**: Determine if the observed complexity is intentional. Intentional complexity must explain its trade-offs. Only accidental complexity should be evaluated as a potential issue.
4. **Step 4 — Engineering Interpretation**: Translate metrics into software patterns (e.g., "This module combines transport, data mapping, and validation concerns").
5. **Step 5 — Evidence Sufficiency**: Verify if evidence is *Sufficient*, *Partially Supported*, *Insufficient*, or *Unknown*. Use "Unknown" when the available deterministic evidence is insufficient to determine whether a conclusion can reasonably be evaluated. Do not treat "Unknown" as a defect; it simply indicates that the available evidence does not allow a meaningful engineering conclusion. Do not speculate.
6. **Step 6 — Engineering & Business Impact**:
   - **Engineering Impact**: maintainability, ownership, coupling, readability, testing, onboarding.
   - **Business Impact**: delivery velocity, regression risk, future feature cost, engineering effort.
   - *Note: Keep these impacts in distinct sections; do not mix them.*
7. **Step 7 — Recommendation**: Detail a structural solution. Recommendations must preserve external interfaces unless explicitly justified.
8. **Step 8 — Trade-offs**:
   - **If implemented**: benefits, migration effort, testing scope, regression considerations.
   - **If deferred**: acceptable duration, engineering consequences, situations where priority should increase.
9. **Step 9 — Priority**: Assigned LAST. Never prioritize directly from raw metrics.

---

## 6. Recommendation Basis

Each recommendation must explicitly indicate its basis:
- `Observed Evidence` (resolves a direct metric or file structure alert)
- `Engineering Best Practice` (implements general modular patterns)
- `Framework Convention` (aligns with Next.js/React standard styles)
- `Architectural Pattern` (conforms to core decoupled structures)

The report must explain *why* a recommendation exists rather than assigning a vague confidence percentage.

---

## 7. Prioritization Decision Test

Before assigning a **Medium** or **High** priority to any finding, ask:
> *"Would an Engineering Manager realistically create a Jira ticket for this?"*

If the answer is probably not, the finding must remain **Informational** rather than prioritized.

---

## 8. Engineering Classifications

Every finding must include exactly one independent engineering category:
- `Responsibility Concentration`
- `State Coupling`
- `Maintainability Hotspot`
- `Technical Debt`
- `Architectural Smell`
- `API Boundary`
- `Configuration Risk`
- `Framework Convention`
- `Positive Engineering Pattern`

---

## 9. Alternative Interpretation Analysis

For significant findings, the agent must consider and compare at least one alternative explanation:
- State the raw observations.
- Evaluate the primary interpretation.
- Detail the alternative explanation.
- Justify which explanation requires the fewest assumptions and is most strongly supported by the evidence.

---

## 10. Symmetry of Strengths and Weaknesses

Codebase strengths must be analyzed with the exact same depth as issues. Instead of generic compliments, use:
* **Observation**: State the raw design/structure pattern observed.
* **Engineering Benefit**: Detail the structural benefit (e.g., decoupled modules).
* **Long-term Impact**: Explain how this decision benefits velocity, onboarding, or future changes.

---

## 11. The Golden Rule

**When multiple valid engineering interpretations exist, FaultLens must prefer the interpretation that requires the fewest assumptions while remaining fully supported by deterministic evidence.**

---

## 12. Permanent Actionability Principle

The reasoning layer exists to support engineering decisions, not to maximize the number of findings. A smaller number of highly actionable, evidence-backed findings is preferred over a larger number of speculative observations.
