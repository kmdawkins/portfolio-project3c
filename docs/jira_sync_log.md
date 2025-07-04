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


|Date             | Jira ID | Summary                                                  | Action Taken (Git/Notes)                                                                      | Status          |
|-----------------|---------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------|-----------------|
|2025-07-04       | P3C-45  | Capture dbt_snowflake venv setup and GIT CLI screenshots | Saved visuals for deactivate/activate flow, `dbt-version`, and commit/push to GitHub          | 🟩 Done        | 
|2025-07-04       | P3C-45  | Capture dbt_snowflake venv setup and GIT CLI screenshots | Subtask **P3C-45** created to document `dbt_snowflake` setup                                    | 🟨 In Progress |
|2025-07-03       | P3C-44  | Update README.md for dbt_snowflake venv setup            | Added modular venv instructions, revised folder structure, updated setup instructions         | 🟩 Done        |
|2025-07-03       | P3C-35  | Install dbt CLI locally                                  | Installed dbt-snowflake in `dbt_snowflake` venv; verified versions                            | 🟩 Done        |
|2025-07-03       | P3C-35  | Install dbt CLI locally                                  | Unblocked by **P3C-43**; Proceeding with `pip install dbt-snowflake`                          | 🟨 In Progress |              
|2025-07-02       | P3C-43  | Create clean virtual environment for `dbt-snowflake`     | Subtask completed; `venv` created, activated, and committed `.gitignore`                      | 🟩 Done        |
|2025-06-28       | P3C-35  | Install dbt CLI locally                                  | Blocked due to `venv` conflict; subtask **P3C-43** created                                    | 🟥 Blocked     |



## Update Protocol

**When to update**
- When a Jira ticket's **status, AC, or scope changes**
- When a new **subtask** is created due to a block or scope split
- After signigicant **README or docs alignment**

**Where to link**
- Sreenshots: `docs\screenshots\portfolio-deliverables\`
- Git commits: Semantic messages tracked in `git log`
- Markdown updates: Mention location if relevant


