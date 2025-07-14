# 📦 Project 3C: Data Warehouse & Cloud Integration

A modular, production-aligned data pipeline that automates the ingestion, transformation, and orchestration of structured CSV data into a **Snowflake cloud data warehouse**. It supports both **local and AWS S3** data sources, uses **dbt** for transformations and testing, and **Apache Airflow** for orchestration. Built for clarity, scalability, and security using **modern Data Engineering best practices**.

---

## 📁 Project Structure

| Folder         | Purpose                                                  |
|----------------|----------------------------------------------------------|
| `dags/`        | Apache Airflow DAG definitions                           |
| `dbt/`         | dbt project structure, models, and configs               |
| `diagrams/`    | Pipeline diagrams and dbt lineage screenshots            |
| `docker/`      | Docker config for containerization (optional)            |
| `docs/`        | Jira logs, screenshots, developer notes, architecture    |
| `etl_pipeline/`| Python-based ETL logic, jobs, utils                      |
| `include/`     | Raw and lookup datasets (`/raw/`, `/lookup/`)           |
| `logs/`        | Runtime logs (Airflow and ETL, git-ignored)              |
| `sandbox/`     | Scratch scripts, test queries, experimentation           |
| `tests/`       | Unit tests and dbt validation logic                      |

---

## ⚙️ Tech Stack

- **Python 3.11** – Core scripting and ETL support  
- **Apache Airflow 2.8.1** – DAG orchestration and automation  
- **Snowflake** – Cloud-based data warehouse  
- **dbt Core** – SQL modeling, testing, documentation  
- **AWS S3** – Cloud object storage for raw/staging datasets  
- **AWS Secrets Manager** – Production-grade secrets handling  
- **Git + Jira** – Version control and structured project tracking  

---

## 🎯 Project Goals

- ✅ Automate ingestion of CSV data from **S3** or local filesystem  
- ✅ Load into **Snowflake** via Python ETL and/or `COPY INTO`  
- ✅ Build dbt models to transform raw → staging → final  
- ✅ Validate using dbt tests and Python unit tests  
- ✅ Orchestrate full workflow using Apache Airflow DAGs  
- ✅ Store secrets securely using **AWS Secrets Manager**  
- ✅ Maintain clean, modular codebase and job-seeking artifacts  

---

## 🔐 Secrets Management

Secrets are managed in two stages to reflect development vs. production best practices.

### 1. Development (Local Only)
- Uses a `.env` file (excluded via `.gitignore`) to store environment-specific credentials.
- Supports Snowflake, AWS, and dbt configuration for local testing.
- Provides a simple fallback mechanism for rapid iteration during early-stage development.

### 2. Production-Ready (Cloud-Based)
- Leverages **AWS Secrets Manager** to securely store and retrieve secrets.
- Secrets are injected into:
  - Airflow connections dynamically (not stored in the UI)
  - Python utilities using `boto3` and `get_secret_value()`
  - dbt `profiles.yml` via environment variable substitution or CLI support
- Secrets are scoped via IAM roles and fine-grained access policies (e.g., `SecretsManagerReadWrite`, `AmazonS3FullAccess`) attached to a secure IAM user.
- AWS IAM user credentials (Access Key ID + Secret) are stored securely outside the repository.

---

## 🖼️ Visuals & Documentation

Project documentation and visual outputs are stored in:

| Folder                    | Contents                                          |
|---------------------------|---------------------------------------------------|
| `diagrams/`               | DAG flowcharts, dbt lineage screenshots           |
| `docs/screenshots/`       | Airflow UI, dbt CLI outputs, S3 console, test logs|
| `docs/jira_sync_log.md`   | Git ↔ Jira worklog sync                           |
| `developer_notes.md`      | Design rationale, blockers, lessons learned       |
| `dag_architecture.md`     | DAG task descriptions and orchestration logic     |

---

## 🏁 Jira Epic Color Mapping

| Stage            | Color    | Description                                     | Epics                                  |
|------------------|----------|-------------------------------------------------|----------------------------------------|
| **Setup**        | 🟨 Yellow | Git, scaffolding, secrets, Docker               | `P3C-1`, `P3C-2`, `P3C-36`, `P3C-7`, `P3C-65` |
| **Ingestion**    | 🟥 Red    | Data sourcing via S3, ingestion into Snowflake  | `P3C-56`                               |
| **Orchestration**| 🟧 Orange | DAG creation and Airflow task flow              | `P3C-6`                                |
| **Modeling**     | 🟩 Green  | dbt model logic and transformations             | `P3C-3`, `P3C-4`                        |
| **Testing**      | 🟦 Blue   | dbt tests and validation                        | `P3C-5`                                |
| **Final Review** | 🟪 Purple | Documentation, polish, GitHub release           | `P3C-8`                                |

---

## 🏷️ Label Reference Table

This project uses a structured label system across all Jira tasks to support traceability, sprint planning, and portfolio deliverables.

---

### 🎯 Core Execution Labels

| Label            | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| `core-feature`   | MVP-critical steps for pipeline success                                  |
| `sprint-ready`   | Fully scoped, unblocked tasks ready for execution                        |
| `blocked`        | Tasks blocked due to environment/setup dependencies                      |
| `ready-for-review` | Finalized and ready for testing, polish, or documentation             |

---

### 🧰 Portfolio-Grade Labels

| Label         | Description                                                              |
|---------------|--------------------------------------------------------------------------|
| `portfolio`   | Deliverables for job-seeking: visuals, docs, final polish                |
| `docs`        | Internal documentation, visuals, developer notes                         |
| `testing`     | dbt tests, Python unit tests, CI-style logic                             |
| `logging`     | Logging enhancements, retry strategies, observability instrumentation    |
| `refinement`  | Jira grooming: epic clarity, subtask decomposition                       |

---

### 🌱 Stretch & Enhancement Labels

| Label            | Description                                                              |
|------------------|--------------------------------------------------------------------------|
| `stretch-goal`   | Optional features that enhance the pipeline                              |
| `local-dev`      | Local development tasks: venv setup, CLI testing, config validation      |

---
### ☁️ Cloud Integration Labels

| Label         | Description                                                              |
| ------------- | ------------------------------------------------------------------------ |
| `aws`         | AWS-specific tasks (S3, IAM roles, Secrets Manager setup)                |
| `aws-secrets` | AWS Secrets Manager integration and secure retrieval logic               |
| `boto3`       | boto3-specific scripting, validation, upload/download logic              |
| `cloud`       | Cloud service setup (S3, Secrets Manager, Snowflake)                     |
| `infra`       | Infrastructure setup (CLI tools, user config, system-level dependencies) |

---

### 🧩 Full Label Reference (Alphabetical)

| Label              | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| `airflow`          | DAG development, orchestration logic, task-level tracking                |
| `automation`       | Scheduling and execution with Airflow DAGs                               |
| `aws`              | AWS-specific tasks (S3, IAM roles, Secrets Manager setup)                |
| `aws-secrets`      | AWS Secrets Manager integration and secure retrieval logic               |
| `boto3`            | boto3-specific scripting, validation, upload/download logic              |
| `cli`              | Command-line interfaces: AWS CLI, SnowSQL, dbt CLI                       |
| `cloud`            | Cloud service setup (S3, Secrets Manager, Snowflake)                     |
| `core-feature`     | MVP-critical steps for pipeline success                                  |
| `data-staging`     | Loading and validating structured source data                            |
| `dbt`              | dbt-specific logic (models, configs, tests, docs)                        |
| `docs`             | Internal documentation, visuals, developer notes                         |
| `env`              | Environment management: `.env`, `.env.template`                          |
| `infra`            | Infrastructure setup (CLI tools, user config, system-level dependencies) |
| `local-dev`        | Local development tasks: venv setup, CLI testing, config validation      |
| `logging`          | Logging enhancements, retry strategies, observability instrumentation    |
| `modeling`         | dbt model creation and transformation layers                             |
| `portfolio`        | Deliverables for job-seeking: visuals, docs, final polish                |
| `python`           | Custom ETL modules, validation logic, file ingestion                     |
| `ready-for-review` | Finalized and ready for testing, polish, or documentation                |
| `refinement`       | Jira grooming: epic clarity, subtask decomposition                       |
| `secrets`          | Secrets management with `.env` and AWS Secrets Manager                   |
| `setup`            | Initial scaffolding: Git, Docker, dbt, Airflow config                    |
| `snowflake`        | Snowflake object setup and integration                                   |
| `sprint-ready`     | Fully scoped, unblocked tasks ready for execution                        |
| `sql`              | Raw SQL scripts used outside dbt (DDL, `COPY INTO`, etc.)                |
| `stretch-goal`     | Optional features that enhance the pipeline                              |
| `testing`          | dbt tests, Python unit tests, CI-style logic                             |
| `transformation`   | Column renaming, normalization, NULL handling                            |
| `validation`       | Schema checks, row validation, quality assurance                         |


---

## 🚀 Getting Started (Local Setup)

> Ensure you have Python 3.11 and the necessary virtual environments created.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/kmdawkins/portfolio-project3c.git
cd portfolio-project3c
```

### 2️⃣ Setup Virtual Environments
**For Airflow + ETL**

```bash
python -m venv C:\venvs\etl_env
C:\venvs\etl_env\Scripts\Activate.ps1
pip install -r requirements.txt
```

**For dbt + Snowflake**

```bash
python -m venv C:\venvs\dbt_snowflake
C:\venvs\dbt_snowflake\Scripts\Activate.ps1
pip install dbt-snowflake
```

### 3️⃣ Configure Environment Variables
1. Duplicate `.env.template` > `.env`
2. Add credentials:
- Snowflake (`SF_ACCOUNT`, `SF_USER`, etc.)
- AWS (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- dbt target configs

### 4️⃣ Validate Setup
- Run basic Airflow DAGs via UI or CLI
- Test dbt connection:

```bash
dbt debug --target dev
```
- Confirm file ingestion via Python script or DAG

---

## Jira Sync Log
All tasks in this project are tracked using a structured **Jira Kanban board** with detailed task breakdowns, status changes, and label mappings. The file `docs/jira_sync_log.md` serves as a Git to Jira integration bridge, capturing:

| Log Type          | Description                                                                |
| ----------------- | -------------------------------------------------------------------------- |
| 🧩 Task Snapshots | Epic, subtask, and status logs captured at regular intervals               |
| 🔄 Change Logs    | Edits to summaries, descriptions, acceptance criteria, and labels          |
| 🚫 Blockers       | Temporarily paused or blocked tasks with reason and resolution             |
| 📌 Status Audits  | Manual progress updates for completed or sprint-ready items                |

This log supports project traceability, portfolio readiness, and demonstrates how tasks evolved through backlog refinement and sprint planning. All entries follow a standardized format for clarity and reproducibility.

## 💡 Future Enhancements

- Add S3 ➡️ Snowflake direct ingestion (`STAGE`, `COPY INTO`)
- Enable TaskGroups or decorators in Airflow DAGs
- Integrate dbt artifcats tracking into `docs/`
- Set up GitHub Actions for CI on push