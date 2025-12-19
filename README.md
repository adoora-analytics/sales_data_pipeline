#  Sales Data Pipeline – ETL with Python & PostgreSQL

This repository contains my **first data engineering project** : a simple but complete ETL (Extract–Transform–Load) pipeline for processing sales data.  
The pipeline extracts raw CSV files, cleans and transforms them using Python, validates the data, and loads the results into a PostgreSQL **staging table** and an optional **data warehouse** built using SQL scripts.

This project represents my starting point in data engineering, and I will continue improving it as I learn.


---

## What This Project Shows

**Skills demonstrated:**

- Python-based ETL orchestration (`main.py`)
- Modular pipeline design (`etl/` and `utils/` packages)
- Reading and combining multiple CSV files
- Minimal data cleaning and date conversion with pandas
- Basic data validation
- Loading into PostgreSQL using a reusable DB helper
- Config-driven design (`config.json` + `.env`)
- Logging to file for debugging and traceability

---

##  Project Structure

```text
sales_data_pipeline/
│
├── config/
│   ├── config.json             # Local config (ignored in git) 
│   └── config.example.json     # Template config for others
│
├── data/
│   ├── raw/                    # Input CSVs
│
├── dwh/
│   ├── dwh.sql                 # DWH star-schema (fact + dimensions) creation (includes indexing too)
│   ├─  dwh_population.sql      # Scripts to populate sales dimension and fact tables 
│   └── dwh_optimization.sql    # Basic performance tuning
│
├── etl/
│   ├── __init__.py
│   ├── extract.py              # Reads CSVs into DataFrames
│   ├── transform.py            # Cleans, normalises, enriches data (my cleaning was minimal though)
│   ├── validate.py             # Data quality checks
│   └── load.py                 # Loads into PostgreSQL staging table
│
├── logs/
│   └── pipeline.log            # Log output (ignored)
│
│
├── utils/
│   ├── __init__.py
│   ├── config.py               # Reads config + env variables
│   ├── db.py                   # DB connection & helpers
│   └── logger.py               # Logging configuration
│
├── .env                        # Local secrets (ignored)
├── .gitignore
├── main.py                     # Orchestrates the ETL steps
└── staging.sql                 # DDL for the staging table
├── requirements.txt
└── README.md
```

##  How to Use This Project

Follow these steps to run the ETL pipeline and reproduce the results on your own machine.

---

### 1️ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sales_data_pipeline.git
cd sales_data_pipeline
```

---

2️ Create and Activate a Virtual Environment (Recommended)
## For Windows OS
```bash
python -m venv .venv
```
---

3️ Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

4️ Set Up Database Credentials

Create a local .env file in the project root:

DB_PASSWORD=your_postgres_password



---

5️ Configure the Pipeline

Copy the example config file:

config/config.example.json -- rename as config.json

Then edit:

{
    "db_name": "your_database",
    "db_user": "postgres",
    "db_host": "localhost",
    "db_port": 5432,
    "raw_data_path": "data/raw"
}


---

6️ Add Raw CSV Files

Place your datasets inside:

data/raw/
    sales_2024.csv
    sales_2025.csv

Column names should match those expected in transform.py.


---

7️ Create the Staging Table

Run this SQL in PostgreSQL:
```psql
psql -U postgres -d your_database -f sql/day7/staging.sql
```

---

8️ Run the ETL Pipeline
```bash
python main.py
```

This will:

1. Extract raw CSVs


2. Clean and transform the data


3. Validate column types + nulls + duplicates


4. Load everything into w4d7_staging


5. Save logs to logs/pipeline.log




---

 Data Warehouse Layer

Inside the dwh/ folder:

dwh.sql – creates fact + dimension tables while indexing 

dwh_population.sql – populates dimensions and fact tables

dwh_optimization.sql – performance tuning


Run them in order:
```bash
psql -U postgres -d your_database -f dwh/dwh.sql
psql -U postgres -d your_database -f dwh/dwh_population.sql
psql -U postgres -d your_database -f dwh/dwh_optimization.sql
```

---

 Pipeline Architecture (Simple Diagram)

CSV Files
   │
   ▼
extract.py → transform.py → validate.py → load.py
                                          │
                                          ▼
                               PostgreSQL (staging)
                                          │
                                          ▼
                                       DWH Scripts
                                (fact + dimension tables)


---
