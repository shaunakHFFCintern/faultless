---
name: "/faultlens"
description: "Run the full DocScan intelligence pipeline on the target repository to automatically generate the Project Risk Register."
---

# FaultLens Engineering Intelligence Pipeline (v1.5.1)

Welcome to the FaultLens project! This document serves as the onboarding guide and technical reference for engineers working on or contributing to the FaultLens architecture.

---

# 1. Project Overview

FaultLens is an AI-assisted frontend debugging and engineering intelligence system. It statically analyzes frontend codebases, extracts rich structured information, and applies advanced engineering reasoning to help team members understand complex configurations and trace architectural hotspots.

### Key Objectives:
- **Static Analysis**: Extract component declarations, data flows, routing models, and dependencies directly from repository source code.
- **Deterministic Evidence**: Generate structured JSON reports representing the facts of the repository without speculation.
- **Engineering Reasoning**: Apply an evidence-based reasoning pipeline to identify technical debt, map causes-and-effects, and construct remediations.
- **Actionable Documentation**: Compile executive summaries and technical registries to accelerate developer onboarding and facilitate engineering design decisions.

> [!IMPORTANT]
> **No Runtime Dependencies**: FaultLens operates strictly as a static analysis engine. It does not perform runtime profiling, execute tests, load production logging, or hook browser environments.

---

# 2. Architecture Overview

FaultLens consists of three distinct layers:

1. **Deterministic Evidence Collection (Python Scanners)**: Traverses the target repository, parsing AST-like syntax patterns, dependencies, and configuration definitions to produce structured JSON documents.
2. **Engineering Reasoning (Antigravity LLM)**: Consumes the JSON evidence files to perform semantic engineering analysis. This layer is strictly governed by the centralized, canonical reasoning specification:
   `proj/agents/docscan/prompts/reasoning_principles.md`
   All reasoning, assessments, prioritization, and recommendations inherit directly from this specification.
3. **Report Generation**: Consolidates the findings into supporting reports and compiles the master decision-making registry.

```
Repository Source Code
        │
        ▼ (Python Scanners)
[ 1. Deterministic Evidence Collection ]
        │
        ▼ (Structured JSON Inventories)
[ 2. Engineering Reasoning (Governed by reasoning_principles.md) ]
        │
        ▼ (Semantic Syntheses)
[ 3. Report Generation ]
        │
        ▼
[ PROJECT_RISK_REGISTER.md ]
```

---

# 3. Evidence Layer

The evidence collector runs at the start of the pipeline and produces the following JSON artifacts:

* **Repository Index** (`repo_index.json`): Maps all scanned files, locations, extensions, and file sizes.
* **Technology Stack Inventory** (`framework_inventory.json`): Lists observed frameworks, libraries, build tools, package managers, and testing libraries with categorizations (e.g. `Frontend Framework`, `State Management`, `Build Tool`).
* **Component Graph** (`component_graph.json`): Traces import-export declarations to map modular structural relationships.
* **Route Graph** (`route_graph.json`): Maps routing configuration objects, path matching expressions, and components bound to each route.
* **API Inventory** (`api_inventory.json`): Records outgoing API calling structures, matching paths, HTTP methods, and source locations, assigning deterministic `API_XXXX` IDs.
* **Dependency Inventory** (`dependency_inventory.json`): Maps third-party modules and external libraries consumed across files.
* **Complexity Inventory** (`complexity_inventory.json`): Stores metrics (lines, import counts, render tree nesting depth, conditional render counts, reactive logic counts, etc.) and risk signals, assigning deterministic `COMP_XXXX` IDs.
* **Interaction Flow Inventory** (`interaction_inventory.json`): Documents static event-to-handler-to-API chains, assigning deterministic `FLOW_XXXX` IDs.
* **State Relationship Inventory** (`state_relationship_inventory.json`): Traces stores and contexts to their declaring files and consumer components, assigning deterministic `STORE_XXXX` IDs.
* **Component Dependency Inventory** (`component_dependency_inventory.json`): Documents static parent-child component structures resolved from imports and template elements.

---

# 4. Evidence Principles

All collectors must adhere to the following core principles:

- **Deterministic**: Given the same codebase state, the scanner must always output identical, reproducible inventories.
- **Framework-Aware**: Collectors parse different syntax models (React, Vue, Angular) and map them to generalized, framework-agnostic schemas.
- **Configuration-Driven**: Matching patterns and complexity rules are loaded dynamically from JSON config files (`api_rules.json` and `complexity_rules.json`).
- **Based on Observable Code**: FaultLens collects only what is explicitly written. It never guesses or speculates.

---

# 5. Reasoning Layer

Once the evidence layer generates the JSON inventories, the reasoning layer (Antigravity LLM) consumes the files to perform semantic engineering analysis under the guidance of the centralized `reasoning_principles.md` specification.

The reasoning layer is responsible for:
- **Architectural Understanding**: Mapping module decoupling, layouts, and component structures.
- **Issue Localization**: Pinpointing files responsible for bad practices, bypassed abstractions, or design violations.
- **Severity Assessment**: Evaluating how findings impact maintainability, stability, and scale.
- **Remediation Suggestions**: Providing concrete step-by-step guidance for refactoring.
- **Engineering Summaries**: Building developer-friendly explanations of codebase health.

> [!IMPORTANT]
> **No Hallucinations**: Recommendations and findings must trace directly back to observable facts in Tiers 1 and 2 of the evidence hierarchy. The reasoning layer is strictly forbidden from fabricating files, components, or issues.

---

# 6. Engineering Reports

The pipeline translates its findings into markdown documents saved under the `proj/agents/docscan/docs/` directory:

* **Investigation Candidates** (`INVESTIGATION_CANDIDATES.md`): Lists components containing potential hotspots or anti-patterns.
* **Cause & Effect Map** (`CAUSE_EFFECT_MAP.md`): Traces how changes in specific files propagate to dependent modules.
* **Risk Assessment** (`RISK_ASSESSMENT.md`): Estimates technical debt and maintenance issues.
* **Resolution Options** (`RESOLUTION_OPTIONS.md`): Discusses alternative refactoring strategies.
* **Change Analysis** (`CHANGE_ANALYSIS.md`): Predicts how system modifications will impact the existing structure.
* **Recommended Actions** (`RECOMMENDED_ACTIONS.md`): Lists prioritized engineering refactoring items.
* **PROJECT_RISK_REGISTER** (`PROJECT_RISK_REGISTER.md`): The master document that serves as the single source of truth for decision-making.

---

# 7. Engineering Health Indicators

The master `PROJECT_RISK_REGISTER.md` rates codebase health against eight distinct categories:

1. **Code Practices**: Evaluates coding standards, architectural compliance, and consistency.
2. **Architecture**: Assesses modular coupling, circular imports, and structure.
3. **Code Quality**: Evaluates complexity, file sizes, and readability.
4. **Maintainability**: Measures ease of modifications and technical debt load.
5. **Production Readiness**: Static assessment of bundler configs, build rules, and package dependencies.
6. **Scalability**: Static evaluation of state sharing architectures and module sizes.
7. **Reliability**: Static analysis of data error boundaries and retry fallbacks.
8. **Safety**: Static check of inputs sanitization, route guards, and direct browser API bypasses.

### Assessment Format:
Each indicator must contain:
- **Rating**: (e.g. HIGH, MEDIUM, LOW) derived directly from evidence metrics.
- **Evidence Summary**: Bullet points listing the exact evidence items (like `lines_of_code > 300` or `multiple_api_clients = true`).
- **Why it Matters**: A concise explanation of the engineering impact ("So what?").
- **Recommended Action**: The direct refactoring steps to resolve the issue.

---

# 8. Current Scope (v1.5.1)

FaultLens v1.5.1 introduces a standardized, disciplined engineering reasoning framework while keeping functionality focused and the pipeline frozen.

### Frozen Components:
- **Scanners**: Unchanged and feature complete.
- **Evidence**: Unchanged schemas and JSON inventories.
- **Report Formats**: Output structures and registers remain unchanged.

*Objective*: Release v1.5.1 focuses entirely on improving the quality of engineering decisions and reasoning accuracy rather than expanding features.

### Unsupported:
- Runtime instrumentation or profiling.
- Production log monitoring or server diagnostics.
- Database analysis or backend codebase scans.
- Git revision history traversal.
- MaxKB, Supabase, PostgreSQL, or RAG databases.
- MCP (Model Context Protocol) tool integration.

---

# 9. Design Principles

- **Evidence First**: All scans start with deterministic code collection. No reasoning is applied during gathering.
- **Reasoning Second**: Antigravity evaluates the collected files using the 9-step reasoning pipeline. It never invents files or endpoints.
- **Recommendations Third**: Remediations are generated and linked directly back to specific metrics and classifications.
- **Memory Later**: The collector outputs raw facts. Future persistence layers (V2) will track historical scans without modifying the underlying analyzer.

---

# 10. Roadmap

* **✓ V1.0**: Static Frontend Scanner
* **✓ V1.5**: Evidence Quality Improvements
* **✓ V1.5.1**: Engineering Reasoning Framework (Current)
* **V2 (Planned)**: Persistent Knowledge Layer. Storing scan history, calculating drift/diffs over time, tracking stable findings, and building a local knowledge repository.
* **V3 (Planned)**: Knowledge Retrieval Layer. Integrating local search engines (MaxKB or equivalent), RAG-based context, and conversational developer assistants.
* **V4 (Planned)**: Platform Integrations. PostgreSQL analytics reports, GitHub actions integration, Model Context Protocol (MCP) servers, Jira ticket generation, Slack hooks, and CI/CD quality gate checks.
