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
