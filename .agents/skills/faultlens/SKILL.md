---
name: "/faultlens"
description: "Run the full DocScan intelligence pipeline on the target repository to automatically generate the Project Risk Register."
---

# /faultlens command

This command executes the full DocScan frontend intelligence pipeline. It runs all stages of analysis automatically to compile the primary risk register.

## Usage

```bash
/faultlens <target_repository_path>
```

Example:
```bash
/faultlens workspace/codebase/chatwoot
```

## Internal Execution Pipeline

When this command is run, execute the following steps in sequence:

1. **Step 1: Evidence Collection**
   * Update the target repository configuration file (`proj/agents/docscan/config/target_repo.txt`) to point to the supplied `<target_repository_path>`.
   * Execute the existing Python evidence collection pipeline by running:
     `python3 proj/agents/docscan/scanner/entry.py` (on macOS/Linux) or `python proj/agents/docscan/scanner/entry.py` (on Windows)
   * Ensure the following evidence inventories are generated or refreshed:
     * `repo_index.json`
     * `component_graph.json`
     * `route_graph.json`
     * `api_inventory.json`
     * `state_inventory.json`
     * `event_inventory.json`
     * `dependency_inventory.json`

2. **Step 2: Reasoning**
   * Use Antigravity reasoning to analyze the generated evidence files.
   * Compile individual reasoning reports:
     * Component reasoning (`COMPONENT_REASONING.md`)
     * Route reasoning (`ROUTE_REASONING.md`)
     * API reasoning (`API_REASONING.md`)
     * State reasoning (`STATE_REASONING.md`)
     * Event reasoning (`EVENT_REASONING.md`)

3. **Step 3: Investigation**
   * Pinpoint structural issues and layout concerns:
     * Investigation candidates (`INVESTIGATION_CANDIDATES.md`)
     * Cause and effect mapping (`CAUSE_EFFECT_MAP.md`)
     * Debug guidance (`DEBUG_GUIDE.md`)

4. **Step 4: Risk Evaluation**
   * Evaluate business and engineering costs of identified issues:
     * Severity analysis (`RISK_ASSESSMENT.md`)
     * Leave-as-is analysis (`LEAVE_AS_IS.md`)
     * Change impact analysis (`CHANGE_ANALYSIS.md`)
     * Resolution options (`RESOLUTION_OPTIONS.md`)

5. **Step 5: Decision Support**
   * Provide recommendations and trace support confidence:
     * Recommended actions (`RECOMMENDED_ACTIONS.md`)
     * Decision confidence (`DECISION_CONFIDENCE.md`)

6. **Step 6: Executive Summary**
   * Generate `PROJECT_RISK_REGISTER.md` as the primary decision-making output.

## Output Rules

* **Default Output:**
  * Save `PROJECT_RISK_REGISTER.md`.
  * Open `PROJECT_RISK_REGISTER.md` in the editor and move focus to the tab.
  * Do not print the report contents, summarize the report, render tables from it, or duplicate markdown content in the chat.
  * Use the exact Chat Response format:
    ```
    PROJECT_RISK_REGISTER generated successfully.

    Opened:
    proj/agents/docscan/docs/PROJECT_RISK_REGISTER.md

    Issues Found:
    Critical: X
    High: Y
    Medium: Z
    Low: N

    Use `/faultlens explain <issue-id>` for deeper investigation.
    ```
* **Internal Hiding:** Do not expose internal pipeline stages or intermediate reports unless the user explicitly requests them.

## Non-Goals

* Do not modify source code.
* Do not generate pull requests.
* Do not auto-fix issues.
* Do not execute runtime traces.
* Do not make production claims.
* Do not claim certainty without evidence.
