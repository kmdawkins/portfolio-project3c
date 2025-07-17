# Jira Sync Log – Project 3C

This file tracks synced updates between the Jira Kanban board and local Git activity.  
Used to record major changes in ticket such as: status updates (blocked), scope, acceptance criteria (AC), or timeline alignment.

---

## 🔎 Latest Activity  
🗓️ 2025-07-13  

### Development  
- ✅ **P3C-104**: AWS account and IAM user for programmatic access successfully created
- ✅ **P3C-105**: AWS CLI installed and verified locally
- ✅ Named profile `project3c` securely configured using `~/.aws/credentials` and `~/.aws/config`
- ✅ Verified identity using `aws sts get-caller-identity`

### Documentation  
- ✅ Updated `README.md` under **Secrets Management** to reflect safest approach for configuring AWS CLI
- ✅ Logged changes for **P3C-104** and **P3C-105** in `jira_sync_log.md`
- ✅ Descriptions and AC updated for P3C-105 to reinfoce secure secrets handling

### Visual Assets  
- ✅ Screenshot added: `2025-07-13-aws-cli-installed-success.png`  
- ✅ Screenshot added: `2025-07-13-aws-cli-not-recognized-powershell-error.png`
- ✅ Screenshot added: `2025-07-13-aws-config-sts-verification-project3c.png`

### Jira Updates  
- ✅ **P3C-104** marked `Done`: AWS account + IAM user setup complete
- ✅ **P3C-105** marked `Done`: AWS CLI installed, verified, and securely configured




See full chronological log below ⬇️

---

## Legend

| Status     | Description       |
|------------|-------------------|
| 🟥 Red     | Blocked           |
| 🟨 Yellow  | In Progress       |
| 🟩 Green   | Done              |
| 🟪 Purple  | Merge             |
| ✅ Check   | Subtask creation  |
| 🔄️ Arrows  | Error correction  |
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
| 2025-07-10  | P3C-65  | Secrets Management - AWS Secrets Manager Integration     | Epic scaffolded; Added Epic Color Mapping (Setup 🟨); linked tasks P3C-66 to P3C-73          | 🟩 Done         |
| 2025-07-10  | P3C-49  | Perform backlog refinement for Epics P3C-3 to P3C-5, P3C-56, P3C-65 | Completed full backlog refinement for 3 core and 2 cloud/security epics; rewrote summaries, descriptions, AC, labels for all linked tasks | 🟩 Done      |
| 2025-07-10  | P3C-19  | Orchestrate raw-to-staging SQL Pipeline (PMO Table)      | Included in **P3C-49** full backlog refinement                                               | 🟩 Done         |
| 2025-07-10  | P3C-7   | Secrets & Config (Local)                                 | Sunset. Tasks completed (P3C-28, P3C-29), and P3C-30 merged into **P3C-65** (cloud transition). No further local config tasks remain | 🟩 Done      |
| 2025-07-10  | P3C-88  | Refine backlog for Epic P3C-6                            | Ensure cross-Epic dependencies are addressed; review Task scope, descriptions, AC, and labels for clarity and build sequence | 🟨 In Progress |
| 2025-07-11  | P3C-88  | Refine backlog for Epic P3C-6                            | Accounted for cross-Epic dependencies; reviewed Task scope, descriptions, AC, and labels for clarity and build sequence; captured visual assets for documentation | 🟩 Done        |
| 2025-07-13  | P3C-66  | Configure AWS Secrets Manager via Console or CLI           | 🔄 Scope update: Blocked due to missing AWS Account and uninstalled AWS CLI. Created subtasks **P3C-104** (Account + IAM setup) and **P3C-105** (CLI install & verification) to unblock. | 🟥 Blocked      |
| 2025-07-13  | P3C-67  | Create Python utility to retrieve secrets programmatically | 🔄 Scope update: Blocked due to missing AWS Account and uninstalled AWS CLI. Subtasks **P3C-104** and **P3C-105** now track prerequisites.                                               | 🟥 Blocked      |
| 2025-07-13  | P3C-68  | Refactor dbt `profiles.yml` to use AWS Secrets Manager     | 🔄 Scope update: Blocked due to missing AWS Account and uninstalled AWS CLI. Dependencies tracked in new subtasks **P3C-104** and **P3C-105**.                                           | 🟥 Blocked      |
| 2025-07-13  | P3C-104 | Create AWS Account + IAM user for programmatic access      | ✅ Subtask created to establish root AWS access and scoped IAM user required for Secrets Manager integration and CLI usage.                                                              | 🟨 In Progress  |
| 2025-07-13  | P3C-105 | Install and verify AWS CLI locally                         | ✅ Subtask created to install AWS CLI and configure project3c profile for local use across Airflow/dbt. CLI access required to proceed with secret retrieval utilities.                  | 🟨 In Progress  |
| 2025-07-13  | P3C-106 | Update requirements.txt to reflect new AWS dependencies    | ✅ Subtask created to update `requirements.txt` with `boto3`, `botocore`, and other AWS-related packages required for Secrets Manager integration (Epic P3C-65); linked to venv config and CLI | 🟨 In Progress  |
| 2025-07-13  | P3C-104 | Create AWS Account + IAM user for programmatic access      | AWS account created and IAM user provisioned with programmatic access; secure group permissions configured; access keys stored safely; updated `README.md` with rationale and workflow details | 🟩 Done    |
| 2025-07-13  | P3C-105 | Install and verify AWS CLI locally                         | AWS CLI installed and verified locally via `aws --version` and `aws sts get-caller-identity`. Profile `project3c` configured securely using safest approach for secrets management             | 🟩 Done    |
| 2025-07-14  | P3C-106 | Update requirements.txt to reflect new AWS dependencies    | 🔄 Scope update: Blocked due to missing `boto3` installation. Created subtask **P3C-107** (Install `boto3` in local Python environment) to unblock. | 🟥 Blocked     |
| 2025-07-14  | P3C-107 | Install `boto3` in local Python environment                | ✅ Subtask created to install `boto3`                                                                                                               | 🟨 In Progress |
| 2025-07-14  | P3C-107 | Install `boto3` in local Python environment                | `boto3` installed and version verified (v1.39.3); **P3C-106** (Update requirements.txt) unblocked                                                   | 🟩 Done         |
| 2025-07-14  | P3C-106 | Update requirements.txt to reflect new AWS dependencies    | Update `requirements.txt` with `boto3`, `botocore`, and other AWS-related packages required for Secrets Manager integration (**Epic P3C-65**); linked to venv config and CLI | 🟨 In Progress  |
| 2025-07-14  | P3C-106 | Update requirements.txt to reflect new AWS dependencies    | requirements.txt updated using `pip freeze > requirements.txt`; changes include `boto3`, `botocore`, and supporting packages for Secrets Manager integration                 | 🟩 Done         |
| 2025-07-14  | P3C-66  | Configure AWS Secrets Manager via Console or CLI | Unblocked by **P3C-104 – P3C-107**; proceeding with configuration via AWS Console | 🟨 In Progress |
| 2025-07-14  | P3C-67  | Create Python utility to retrieve secrets programmatically | Unblocked by **P3C-104 – P3C-107**; utility scaffold pending | 🟨 In Progress |
| 2025-07-14  | P3C-68  | Refactor dbt `profiles.yml` to use AWS Secrets Manager | Unblocked by **P3C-104 – P3C-107**; integration pending | 🟨 In Progress |
| 2025-07-15  | P3C-66  | Configure AWS Secrets Manager via Console or CLI          | 🔄 Scope update: Refactored into 5 child tasks for platform-specific secrets; original ticket repurposed for parent tracking; created subtasks **P3C-108 - P3C112** (Snowflake, PostgreSQL, S3, Airflow, dbt respectively) | 🟩 Done   |
| 2025-07-15  | P3C-108 | Create Snowflake secret in AWS Secrets Manager            | ✅ Secret created as `project3c/secrets/snowflake`; verified in Console or CLI                                            | 🟨 In Progress |
| 2025-07-15  | P3C-109 | Create dbt secret in AWS Secrets Manager                  | ✅ Secret created as `project3c/secrets/dbt`; verified in Console or CLI                                                  | 🟨 In Progress |
| 2025-07-15  | P3C-110 | Create PostgreSQL secret in AWS Secrets Manager           | ✅ Secret created as `project3c/secrets/postgres`; verified in Console or CLI                                             | 🟨 In Progress |
| 2025-07-15  | P3C-111 | Create S3 secret in AWS Secrets Manager                   | ✅ Secret created as `project3c/secrets/s3`; verified in Console or CLI                                                   | 🟨 In Progress |
| 2025-07-15  | P3C-112 | Create Airflow secret (fernet key) in AWS Secrets Manager | ✅ Secret created as `project3c/secrets/airflow`; verified in Console or CLI                                              | 🟨 In Progress |
| 2025-07-17  | P3C-108 | Create Snowflake secret in AWS Secrets Manager            | Secret created as `project3c/secrets/snowflake`; verified in Console and CLI using `describe-secret`                       | 🟩 Done         |
| 2025-07-17  | P3C-109 | Create PostgreSQL secret in AWS Secrets Manager           | Secret created as `project3c/secrets/postgresql`; verified in Console and CLI using `describe-secret`                      | 🟩 Done         |
| 2025-07-17  | P3C-110 | Create AWS S3 secret in AWS Secrets Manager               | 🔄 Corrected Jira summary to “AWS S3”; Secret will be stored as `project3c/secrets/s3`; verification via Console or CLI       | 🟨 In Progress  |
| 2025-07-17  | P3C-111 | Create Airflow secret (fernet key) in AWS Secrets Manager | 🔄 Corrected Jira summary to “Airflow”; Secret will be stored as `project3c/secrets/airflow`; verification via Console or CLI | 🟨 In Progress  |
| 2025-07-17  | P3C-112 | Create dbt secret in AWS Secrets Manager                  | 🔄 Corrected Jira summary to “dbt”; Secret will be stored as `project3c/secrets/dbt`; verification via Console or CLI         | 🟨 In Progress  |



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

