# Project 3C: Data Warehouse & Cloud Integration

This project automates ingestion and transformation of structured data from CSV sources (hosted on S3 or locally) into a **Snowflake data warehouse**. It uses **Apache Airflow** for orchestration, **dbt** for transformation and testing, and **Python** for supporting ETL utilities. The pipeline is modular, secure, and aligned with modern Data Engineering practices.

---

## 📁 Project Structure (Key Folders)

| Folder         | Purpose                                                  |
|----------------|----------------------------------------------------------|
| `dags/`        | Apache Airflow DAG definitions                           |
| `dbt/`         | dbt project structure, models, and configs               |
| `diagrams/`    | Pipeline architecture diagrams and lineage screenshots   |
| `docker/`      | Docker config for future containerization (optional)     |
| `docs/`        | Jira logs, screenshots, developer notes                  |
| `etl_pipeline/`| Python-based ETL logic, jobs, utils                      |
| `include/`     | Raw and lookup datasets (`/raw/`, `/lookup/`)           |
| `logs/`        | Runtime and Airflow logs (git-ignored)                   |
| `sandbox/`     | Scratch scripts, experiments, and test queries           |
| `tests/`       | Unit tests and dbt validation logic                      |

---

## ⚡ Tech Stack

- **Python 3.11** – Core scripting and ETL support  
- **Apache Airflow (2.8.1)** – Orchestration  
- **Snowflake** – Cloud data warehouse  
- **dbt Core** – SQL-based transformations and testing  
- **AWS S3** – Cloud object storage (planned integration)  
- **Git + Jira** – Version control and task tracking  

---

## 🎯 Objectives

- ✅ Ingest structured data from AWS S3 or local storage
- ✅ Load into Snowflake using native connectors (`COPY INTO`, dbt sources)
- ✅ Transform data via dbt models (staging → core → final)
- ✅ Orchestrate the full workflow using Apache Airflow
- ✅ Validate transformations via dbt tests and unit tests
- ✅ Secure secrets via `.env`, following production patterns
- ✅ Maintain clean, modular, job-ready Git repo and documentation

---

## 🔐 Secrets Management

Secrets are stored locally in a `.env` file and are **excluded from Git** using `.gitignore`. These include:

- Snowflake credentials (account, user, password, warehouse, schema)
- AWS credentials (for S3 integration — optional)
- dbt profile targets

✅ For production, secrets should be managed via **AWS Secrets Manager** or **Vault**.

---

## 🖼️ Visuals & Documentation

All visuals, diagrams, and outputs are stored in:

- `diagrams/` – Pipeline architecture and dbt lineage screenshots
- `docs/screenshots/` – Airflow UI, test results, CLI logs, and deliverables
- `docs/jira_sync_log.md` – Git ↔ Jira sync entries
- `developer_notes.md` – Lessons, blockers, and implementation notes

---

## 🏷️ Jira Epic Color Mapping

| Stage            | Color   | Description                         | Epics Included           |
|------------------|---------|-------------------------------------|--------------------------|
| **Setup**        | 🟨 Yellow | Git, Secrets, Scaffolding            | `P3C-1`, `P3C-2`, `P3C-36`, `P3C-7` |
| **Ingestion**    | 🟥 Red   | Data sourcing, integration, and pipelines feeding Snowflake | `P3C-56`         |
| **Modeling**     | 🟩 Green  | Staging, SQL transformations         | `P3C-3`, `P3C-4`         |
| **Testing**      | 🟦 Blue   | dbt tests and validation             | `P3C-5`                  |
| **Orchestration**| 🟧 Orange | DAG development and Airflow logging  | `P3C-6`                  |
| **Final Review** | 🟪 Purple | Docs, screenshots, polish            | `P3C-8`                  |


---
## 🏷️ Label Reference Table

| Label              | Description                                                              |
| ------------------ | ------------------------------------------------------------------------ |
| `setup`            | Initial scaffolding: Git repo, Docker, dbt, Airflow setup                |
| `env`              | Environment variables, `.env`, `.env.template`                           |
| `secrets`          | Secrets management (Snowflake creds, AWS Secrets Manager, dbt profiles)  |
| `cloud`            | Cloud-specific tools, services, or deployments                           |
| `aws`              | Tasks involving AWS services like S3, IAM, Secrets Manager               |
| `cli`              | Command-line tools (e.g., AWS CLI, SnowSQL, dbt CLI)                     |
| `python`           | Python-based ETL scripts, automation, or validation                      |
| `automation`       | Workflow automation using scripting, DAGs, or orchestration tools        |
| `data-staging`     | Loading and validating raw CSVs or source data                           |
| `modeling`         | dbt model logic across raw → staging → intermediate → final              |
| `transformation`   | Data enrichment or restructuring (can overlap with modeling)             |
| `sql`              | SQL scripts external to dbt (e.g., Snowflake DDLs, load scripts)         |
| `validation`       | Data quality checks, schema assertions, uniqueness, NULL filters         |
| `testing`          | dbt tests, unit tests, automated validation (e.g., pytest)               |
| `docs`             | Project documentation: README, dev notes, diagrams, screenshots          |
| `dbt`              | dbt-specific: models, configs, profiles, tests, docs                     |
| `snowflake`        | Snowflake configuration: database, schema, warehouse, integration        |
| `airflow`          | DAG development, scheduling, task orchestration, UI configuration        |
| `portfolio`        | Assets and documentation intended for job-seeking presentation           |
| `core-feature`     | Critical tasks required for MVP end-to-end flow                          |
| `refinement`       | Backlog refinement, subtask merging, re-sequencing, Jira cleanup         |
| `sprint-ready`     | Fully scoped, unblocked, and ready for execution in current sprint       |
| `stretch-goal`     | Optional but high-value additions that enhance the pipeline or portfolio |
| `blocked`          | Task is blocked due to external dependency, misconfiguration, or timing  |
| `ready-for-review` | Complete and staged for documentation or code review                     |


---

## 📝 Developer Notes

Challenges, fixes, and task-specific discoveries are logged in:

## Getting Started (Local Setup)

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/kmdawkins/portfolio-project3c.git
cd portfolio-project3c
```

2️⃣ **Create and Activate Virtual Environments**
- ETL + Apache Airflow
```bash
python -m venv C:venvs\etl_env
C:\venvs\etl_env\Scripts\Activate.ps1
```
- dbt + Snowflake
```bash
python -m venv C:\venvs\dbt_snowflake
C:\venvs\dbt_snowflake\Scripts\Activate.ps1
```

3️⃣ **Install Dependencies**
- From Airflow-compatible env:
```bash
pip install -r requirements.txt
```

- From dbt env:
```bash
pip install dbt-snowflake
```

4️⃣ **Configure `.env`**
Create `.env` based on `.env.template` and provide:
- Snowflake credentials
- AWS credentials (if needed)
- dbt target configs (for `profiles.yml`)