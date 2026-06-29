# Agent Instructions

This workspace contains rules governing the behavior of the DocScan and faults pipelines.

## /faults Command Behavior
* **Automatic Execution:** When the user runs the `/faults` command (e.g., `/faults workspace/codebase/chatwoot`), the agent must execute all 6 pipeline steps (Evidence Collection, Reasoning, Investigation, Risk Evaluation, Decision Support, and Executive Summary) automatically. Do not ask for user intervention or confirmation between stages.
* **Output Isolation:** Upon completing the execution of the pipeline:
  * Save `PROJECT_RISK_REGISTER.md`.
  * Open `PROJECT_RISK_REGISTER.md` in the editor and move focus to the tab.
  * Do not print the report contents in the chat.
  * Do not summarize the report in the chat.
  * Do not render tables from the report in the chat.
  * Do not duplicate markdown content in the chat.
  * Respond using the exact format:
    ```
    PROJECT_RISK_REGISTER generated successfully.

    Opened:
    proj/agents/docscan/docs/PROJECT_RISK_REGISTER.md

    Issues Found:
    Critical: X
    High: Y
    Medium: Z
    Low: N

    Use `/faults explain <issue-id>` for deeper investigation.
    ```
* **Risk Register Formatting:**
  * Use tables for each issue.
  * Every technical finding must explain the direct impact ("So what?").
  * Do not include confidence percentages, probability estimates, or speculative claims.
  * Define the executive summary with the top 3 immediate concerns, top 3 future concerns, top 3 acceptable risks, and the estimated engineering effort.
