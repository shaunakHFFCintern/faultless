/faults
/faultlens

## Workflow Objective
Analyze the target repository's frontend architecture, state relationships, component nesting, route patterns, and outgoing APIs. Run the 6-stage pipeline (Evidence Collection, Reasoning, Investigation, Risk Evaluation, Decision Support, and Executive Summary) to compile engineering reports and the primary decision-making register.

## Workflow Responsibilities & Expected Outputs
Generate the following deliverables:
* **Primary Executive Summary**:
  * `PROJECT_RISK_REGISTER.md`
* **Supporting Architectural Reports**:
  * `COMPONENT_REASONING.md`
  * `ROUTE_REASONING.md`
  * `API_REASONING.md`
  * `STATE_REASONING.md`
  * `EVENT_REASONING.md`

## Inheritance of Centralized Reasoning Specification
Every report listed above MUST be constructed in strict alignment with the FaultLens Shared Reasoning Specification:
proj/agents/docscan/prompts/reasoning_principles.md

The analytical pipeline (Observation, Role, Intent, Interpretation, Sufficiency, Impact, Recommendation, Trade-offs, Priority), engineering categories, and validation boundaries defined in reasoning_principles.md are the absolute single source of truth. If any requirement in this command prompt conflicts with reasoning_principles.md, the reasoning_principles.md specification SHALL always take precedence.
