# Project 3C: Data Warehouse & Cloud Integration

This project automates data ingestion and transformation from raw files in AWS S3 into a Snowflake data warehouse. It leverages Apache Airflow for orchestration and dbt for data transformation and testing.

---

## 📁 Project Structure (Key Folders)

| Folder       | Purpose                                              |
|--------------|------------------------------------------------------|
|`dags/`       | Airflow DAGSs                                        |
|`data/`       | Data files (raw, processed, staging)                 |
|`dbt/`        | dbt project and models                               |
|`diagrams/`   | Architecture diagrams and lineage screenshots        |
|`docker/`     | Docker config (if applicable)                        |
|`docs/`       | Documentation and project notes                      |
|`logs/`       | Airflow and pipeline logs                            |
|`sandbox/`    | Experimental scripts / tests                         |
|`tests/`      | dbt and Airflow validation tests                     |
|`.gitignore/` | Git ignore rules                                     |
|`README.md/`  | This file                                            |


## ⚡Tech Stack

- **AWS S3** - Data staging and file storage
- **Snowflake** - Cloud-based data warehouse
- **dbt** - Data transformation and testing framework
- **Apache Airflow** - Orchestration and automation of data workflows
- **Python** - Supporting data processing scripts (as needed)

## 🚀 Objectives

- ✅ Ingest raw data from S3 into Snowflake using native `COPY INTO` commands
- ✅ Transform data in Snowflake using dbt models (`staging`, `intermediate`, `final`)
- ✅ Orchestrate the entire workflow in Airflow, ensuring reliability and modularity
- ✅ Practice secrets management (locally via `.env` files, with awareness of AWS Secret Manager for production)
- ✅ Create a clear, modular, and professional Git repo structure
- ✅ Document challenges and solutions to showcase real-world Data Engineering logic

## 🔐 Secrets Management

Sensitive credentials (Snowflake, AWS, dbt profiles) are stored in local `.env` files and **excluded from version control** via `.gitignore`. For production environments, integration with **AWS Secrets Manager** or **HashiCorp Vault** is recommended for enhanced security.

---

## 🎨 Visuals

- Architecture diagrams (`/diagrams/`)
- dbt model lineage screenshots
- Airflow DAG graph screenshots

|Stage|Color| Description |Epics |
|-----|-----|-------|------------|
|**Setup**| 🟨 Yellow|Tooling, Git, Secrets, Project Scaffolding|`P3C-1`, `P3C-2`,`P3C-36`,`P3C-7`|
|**Modeling**| 🟩 Green |Ingestion & Transformation | `P3C-3`,`P3C-4` |
|**Testing**| 🟦 Blue |Data Quality, dbt Tests |`P3C-5` |
|**Orchestration**| 🟧 Orange |Airflow DAGs, Logging| `P3C-6` |
|**Final Review**| 🟪 Purple |Documentation, Screenshots, Acceptance| `P3C-8`|

---

## Label Reference Table
|Label|Description|
|-----|-----------|
|`setup`|Initial environment, tooling, scaffolding, and repo configuration tasks|
|`data-staging`|Loading, cleaning, or structuring raw data into staging tables|
|`transformation`|Any dbt or SQL logic that reshapes or enriches data|
|`data-validation`|Manual or automated checks to verify data integrity|
|`testing`|Pytest, dbt tests, or debug-related activities|
|`docs`|README updates, screenshots, architecture diagrams, or inline documentation|
|`dbt`|Task related to dbt models, congigs, tests, or docs|
|`snowflake`|Tasks involving Snowflake setup, configs, schema, or access|
|`airflow`|DAGs, logging, scheduling, or Airflow UI setup|
|`portfolio-deliverable`|Tasks contributing to README, screenshots, or final documentation|
|`core-feature`|Tasks required for MVP of the pipeline|
|`blocked`| Tasks cannot proceed without external/unresolved input|
|`ready-for-review`|Task is complete and needs review or final signoff|

---

## 📝 Developer Notes

Document challenges, solutions, and future improvements in: `docs/developer_notes.md`

---

## 🚀 Getting Started (Local)

- 1️⃣ Clone this repo:

```bash
git clone https://github.com/kmdawkins/portfolio-project3c.git
cd portfolio-project3c
```

- 2️⃣ Create and activate a virtual environment:

```bash
python -m venv .venv
.\.venv\Scripts\Activate
```

- 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

- 4️⃣ Customize `.env` file with local environemnt variables
