# Jira Sync Log – Project 3C

This file tracks synced updates between the Jira Kanban board and local Git activity.  
Used to record major changes in ticket such as: status updates (blocked), scope, acceptance criteria (AC), or timeline alignment.

---

## 🔎 Latest Activity  
🗓️ **2025-07-08**  
### Development
- ✅ **P3C-38**: `dbt_project.yml` scaffolded with project metadata, profile, and clean targets
- ✅ `.gitkeep` placeholder files added to all `dbt/models/` subfolders

### Visual Assets
- ✅ Screenshot: `2025-07-08-dbt-model-folder-structure-gitkeep.png` committed

### Jira Updates
- ✅ P3C-28 marked done
- ✅ P3C-39 marked done
- ✅ P3C-40 merged with **P3C-39**
- ✅ P3C-38 marked done


See full chronological log below ⬇️

---

## Legend

| Status     | Description       |
|------------|-------------------|
| 🟥 Red     | Blocked           |
| 🟨 Yellow  | In Progress       |
| 🟩 Green   | Done              |
| 🟪 Purple  | Merge             |
| 📌 Pin     | Backlogged        |
| 📝 Note    | Updated           |

---

## Chronological Log

| Date        | Jira ID | Summary                                                  | Action Taken (Git/Notes)                                                                      | Status         |
|-------------|---------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------|----------------|
| 2025-06-28  | P3C-35  | Install dbt CLI locally                                  | **Blocked** due to `venv` conflict; subtask **P3C-43** created                                | 🟥 Blocked     |
| 2025-07-02  | P3C-43  | Create clean virtual environment for `dbt-snowflake`     | Subtask completed; `venv` created, activated, and committed `.gitignore`                      | 🟩 Done        |
| 2025-07-03  | P3C-35  | Install dbt CLI locally                                  | Unblocked by **P3C-43**; proceeded with `pip install dbt-snowflake`                           | 🟨 In Progress |
| 2025-07-03  | P3C-35  | Install dbt CLI locally                                  | Installed dbt-snowflake in `dbt_snowflake` venv; verified versions                            | 🟩 Done        |
| 2025-07-03  | P3C-44  | Update `README.md` for dbt_snowflake venv setup          | Added modular venv instructions, revised folder structure, updated setup instructions         | 🟩 Done        |
| 2025-07-04  | P3C-45  | Capture dbt_snowflake venv setup and Git CLI screenshots | Subtask **P3C-45** created to document `dbt_snowflake` setup                                  | 🟨 In Progress |
| 2025-07-04  | P3C-45  | Capture dbt_snowflake venv setup and Git CLI screenshots | Saved visuals for deactivate/activate flow, `dbt --version`, commit/push to GitHub            | 🟩 Done        |
| 2025-07-04  | P3C-46  | Update Label Reference Table in `README.md`              | Added new `env` and `secrets` labels; committed changes to repository                         | 🟩 Done        |
| 2025-07-04  | P3C-29  | Duplicate subtask merged into **P3C-37**                 | Implementation completed under **P3C-37** context; no further action needed                   | 🟩 Done        |
| 2025-07-06  | P3C-47  | Create foundational Snowflake objects (Database, Schema, Warehouse)| **Blocked** due to missing `snowsql` CLI install; subtask **P3C-48** created        | 🟥 Blocked     |
| 2025-07-06  | P3C-48  | Install and configure `snowsql` CLI                      | Subtask **P3C-48** created to install `snowsql` CLI and unblock **P3C-47**                    | 🟨 In Progress |
| 2025-07-06  | P3C-48  | Install and configure `snowsql` CLI                      | Installed `snowsql` CLI; verified install and version (1.4.2)                                 | 🟩 Done        |
| 2025-07-06  | P3C-47  | Create foundational Snowflake objects (Database, Schema, Warehouse)| Unblocked by **P3C-48**; proceed with snowflake object creation                     | 🟨 In Progress | 
| 2025-07-06  | P3C-47  | Create foundational Snowflake objects (Database, Schema, Warehouse)| Created snowflake objects (database, schema, warehouse)                             | 🟩 Done        |
| 2025-07-07  | P3C-37  | Configure Snowflake credentials in `.env` and confirm integration | Connection test passed via `dbt debug`; screenshots captured and committed           | 🟩 Done        |
| 2025-07-08  | P3C-28  | Add `.env` to `.gitignore`                               | Updated description, AC, and labels to reflect GitHub history (completed 2025-06-10)          | 🟩 Done        |
| 2025-07-08  | P3C-40  | Test dbt connection to Snowflake                         | Merged into **P3C-39** to consolidate connection test with `profiles.yml` setup               | 🟪 Merge       |
| 2025-07-08  | P3C-39  | Configure `profiles.yml` for Snowflake + validate debug  | Updated summary + description to reflect both setup and connection validation                 | 🟩 Done        |
| 2025-07-08  | P3C-38  | Initialize dbt project folder and scaffold dbt_project.yml | Customize `dbt_project.yml` to match Project 3C conventions                                 | 🟩 Done        |
| 2025-07-08  | P3C-49  | Perform backlog refinement for Epics P3C-3 to P3C-5      | Review subtask summaries, descriptions, ac, labels for completeness, clarity, build logic     | 🟨 In Progress |
| 2025-07-09  | P3C-19  | Orchestrate raw-to-staging SQL Pipeline (PMO Table)      | Rewrote description and AC to reflect modular staging lifecycle; linked to P3C-18; P3C-50 to P3C-55 | 🟨 In Progress |
| 2025-07-09  | P3C-56  | Cloud Integration - AWS S3                               | Epic scaffolded; Added Epic Color Mapping (Ingestion 🟥); updated Label Reference Table with 4 new labels | 🟩 Done  |

---

## Update Protocol

**When to update**
- When a Jira ticket's **status, AC, or scope changes**
- When a new **subtask** is created due to a block or scope split
- After significant **README or docs alignment**

**Where to link**
- Screenshots: `docs/screenshots/portfolio-deliverables/`
- Git commits: Use semantic messages and track with `git log`
- Markdown updates: Mention if major edits to `README.md` or `developer_notes.md`

