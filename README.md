# Module 05 — Data Engineering and ETL Pipeline
## The Darko Method 2026 | Practice Task

---

## The Business Problem We Are Solving

**Company:** GlobalTech Solutions
**Team:** Data Engineering
**Your role:** Junior Data Engineer — first week on the job

GlobalTech Solutions is a technology company with 1,200 employees
across 8 departments: Engineering, Sales, Marketing, Finance, HR,
Operations, Data Science, and Product.

The HR Analytics team wants to answer questions like:
- Which departments have the highest salary inequity?
- Who is at risk of leaving in the next 6 months?
- Are high performers being paid fairly compared to their peers?

The data exists in a PostgreSQL database. But there is a problem.
After running the SQL extraction (Module 03), the raw data has:
- **Null values** — some employee records are incomplete
- **Duplicate rows** — a join error in the SQL created copies
- **Wrong types** — some salary values are stored as text strings
- **Outliers** — a few salaries are entered incorrectly (negative values)

**Before anyone can analyse this data or train a model on it,
it must be cleaned, validated, and standardised.**

That is our job this module.

---

## What We Are Building

An ETL (Extract, Transform, Load) pipeline that takes raw, messy data
and produces a clean, reliable, analysis-ready output.

```
raw-data.csv  (messy)
     │
     ▼
┌─────────────────────┐
│   DataValidator      │  — checks quality, reports problems
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│   DataTransformer    │  — fixes nulls, duplicates, types, adds flags
└─────────────────────┘
     │
     ▼
┌─────────────────────┐
│   ETLPipeline        │  — orchestrates everything, saves output
└─────────────────────┘
     │
     ▼
processed-data.csv  (clean, ready for analysis and ML)
```

---

## Project Structure

```
teaching-project/
├── README.md              ← you are here
├── .gitignore             ← files Git should never track
├── requirements.txt       ← Python packages needed
├── config.py              ← project settings (industry, paths, logging)
├── run.py                 ← entry point: run this to execute the pipeline
├── data/
│   ├── raw/               ← raw-data.csv goes here (from Module 03)
│   └── processed/         ← processed-data.csv appears here after running
├── src/
│   ├── validator.py       ← DataValidator class
│   ├── transformer.py     ← DataTransformer class
│   └── etl_pipeline.py    ← ETLPipeline class (the orchestrator)
└── tests/
    └── test_pipeline.py   ← unit tests for our classes
```

---

## Setup — Before You Run Anything

### Step 1: Copy raw-data.csv from Module 03
```bash
# Module 03 produced raw-data.csv — we need it here
cp ../../../module-03-sql-and-postgresql/data/raw-data.csv data/raw/
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Verify your config.py
Open `config.py` and confirm:
```python
INDUSTRY = "bootcamp_data"   # must match your database schema name
```

### Step 4: Run the pipeline
```bash
python run.py
```

---

## What You Will See When You Run It

```
2026-01-15 10:23:01 [INFO] ETLPipeline initialised
2026-01-15 10:23:01 [INFO] [EXTRACT] Loading raw-data.csv
2026-01-15 10:23:01 [INFO] [VALIDATE] Row count: 1,200 rows ✓
2026-01-15 10:23:01 [WARNING] [VALIDATE] WARNING | salary | 23 nulls (1.9%)
2026-01-15 10:23:01 [INFO] [TRANSFORM] Filled 23 nulls in 'salary' with median
...
══════════════════════════════════════════
  ETL PIPELINE COMPLETE
  Raw rows:      1,200
  Processed rows:1,187
  Nulls fixed:   47
  Duplicates removed: 13
  Output: data/processed/processed-data.csv
══════════════════════════════════════════
```

---

## Results and Findings
*(Fill this in after you run the pipeline)*

| Metric | Value |
|---|---|
| Raw rows | |
| Processed rows | |
| Nulls filled | |
| Duplicates removed | |
| Output file size | |

---

## What This Module Covers

By the end of this project you will understand:
- What ETL means and why every data team does it
- How to write a validator that catches data quality problems
- How to fix nulls, duplicates, and wrong types without corrupting data
- How OOP (classes) make pipelines reusable and testable
- How to write unit tests that run automatically
- How production data teams use logging and error handling
- How to structure a Python project like a professional engineer

---

## Connected Modules

- **Requires:** Module 03 (SQL extraction) — produces raw-data.csv
- **Feeds into:** Module 06 (EDA reads processed-data.csv)
- **Feeds into:** Module 09 (ML trains on processed-data.csv)
- **Feeds into:** Modules 11-15 (all downstream modules use processed-data.csv)
