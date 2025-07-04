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
| **Modeling**     | 🟩 Green  | Staging, SQL transformations         | `P3C-3`, `P3C-4`         |
| **Testing**      | 🟦 Blue   | dbt tests and validation             | `P3C-5`                  |
| **Orchestration**| 🟧 Orange | DAG development and Airflow logging  | `P3C-6`                  |
| **Final Review** | 🟪 Purple | Docs, screenshots, polish            | `P3C-8`                  |

---

## 🏷️ Label Reference Table

| Label               | Description                                                 |
|---------------------|-------------------------------------------------------------|
| `setup`             | Project scaffolding, secrets, repo config                   |
| `env`               | Tasks that involve managing `.env`, `.env.template`, or environment-specific variables |
| `secrets`           | Any sensitive credential configuration (Snowflake, AWS, dbt profiles) |
| `data-staging`      | Loading and preparing raw data                              |
| `transformation`    | dbt model development and enrichment                        |
| `data-validation`   | Schema checks, NULL filters, uniqueness                     |
| `testing`           | dbt tests, unit tests, pytest validation                    |
| `docs`              | README, screenshots, architecture, developer notes          |
| `dbt`               | Models, configs, profiles, tests                            |
| `snowflake`         | Snowflake account, schema, access                           |
| `airflow`           | DAG design, Airflow UI, task logic                          |
| `portfolio-deliverable` | Final visuals, CLI screenshots, documentation           |
| `core-feature`      | Tasks essential for MVP                                     |
| `blocked`           | Blocked by config, environment, or external decision        |
| `ready-for-review`  | Complete and staged for documentation                       |

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