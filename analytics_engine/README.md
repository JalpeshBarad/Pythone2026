# Python2026: Enterprise ELT & Analytics Engineering Portfolio

## 🚀 Project Overview
An end-to-end Modern Data Stack (MDS) pipeline built to simulate enterprise data extraction, cleaning, modular transformation, and automated quality testing using local production tools.

## 🛠️ Tech Stack & Architecture
* **Language:** Python (Pandas, DuckDB)
* **Transformation & Modeling:** dbt (Data Build Tool)
* **Database / OLAP Engine:** DuckDB (Local in-process data warehouse)
* **Data Modeling:** Star Schema (Fact and Dimension separation)

## 📂 Repository Directory Structure
```text
Python2026/
├── 01_foundations/           # Core Python programming scripts & logic
├── 02_data_wrangling/        # Python ingestion, cleaning, & DuckDB SQL wrangling
├── data/
│   ├── raw/                  # Immutable, read-only raw enterprise datasets (CSV snapshots)
│   └── processed/            # Cleaned staging outputs
└── analytics_engine/         # dbt project workspace
    ├── models/               # Modular SQL transformations (Staging & Mart layers)
    └── tests/                # Automated data quality tests (unique, not_null)