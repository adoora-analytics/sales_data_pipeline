# 📊 Sales Data Pipeline – ETL with Python & PostgreSQL

This repository contains a small but realistic **ETL (Extract–Transform–Load) pipeline** for sales data, built as part of my Data Engineering learning track.

The pipeline reads raw CSV files, cleans and transforms the data, validates basic quality rules, and loads the result into a **PostgreSQL staging table**.

---

## 🚀 What This Project Shows

**Skills demonstrated:**

- Python-based ETL orchestration (`main.py`)
- Modular pipeline design (`etl/` and `utils/` packages)
- Reading and combining multiple CSV files
- Data cleaning and type conversion with pandas
- Basic data validation
- Loading into PostgreSQL using a reusable DB helper
- Config-driven design (`config.json` + `.env`)
- Logging to file for debugging and traceability

---

## 🧱 Project Structure

```text
sales_data_pipeline/
│
├── config/
│   ├── config.json             # Local config (ignored) 
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
│   ├── transform.py            # Cleans, normalises, enriches data
│   ├── validate.py             # Data quality checks
│   └── load.py                 # Loads into PostgreSQL staging table
│
├── logs/
│   └── pipeline.log            # Log output (ignored in git)
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
