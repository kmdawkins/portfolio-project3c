# Jira Sync Log - Project 3C

This file tracks synced updates between the Jira Kanban board and local Git activity.
Used to record major changes in ticket such as: status changes (blocked), scope, acceptance criteria (ac), or timeline alignment.


## Log Format

**Legend**

|Status    | Description      |
|----------|------------------|
|🟥 Red   |Blocked           |
|🟨 Yellow|In Progress       |
|🟩 Green | Done             |
|📌 Pin   | Backlogged       |
|📝 Note  | Updated          |


|Date             | Jira ID | Summary                                               | Action Taken (Git/Notes)                         | Status                                 |
|-----------------|---------|-------------------------------------------------------|-------------------------------------------------|-----------------------------------------|
|2025-07-03       | P3C-35  | Install dbt CLI locally                               | Unblocked by **P3C-43**; Proceeding with `pip install dbt-snowflake`        | 🟨 In Progress |              
|2025-07-02       | P3C-43  | Create clean virtual environment for `dbt-snowflake`  | Subtask completed; `venv` created, activated, and committed `.gitignore`  | 🟩 Done        |
|2025-06-28       | P3C-35  | Install dbt CLI locally                               | Blocked due to `venv` conflict; subtask **P3C-43** created                         | 🟥 Blocked     |



## Update Protocol

**When to update**
- When a Jira ticket's **status, AC, or scope changes**
- When a new **subtask** is created due to a block or scope split
- After signigicant **README or docs alignment**

**Where to link**
- Sreenshots: `docs\screenshots\portfolio-deliverables\`
- Git commits: Semantic messages tracked in `git log`
- Markdown updates: Mention location if relevant


