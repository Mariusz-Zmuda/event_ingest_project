# Fitness Tracker API

This project is a simple CRUD backend for managing fitness tracker data using **Python**, **FastAPI**, and **PostgreSQL**.

## 📌 Features

- REST API for Create, Read, Update, and Delete tracker records
- Bulk CSV loader to import fitness tracker data
- Dockerized PostgreSQL database for easy setup
- Clean test automation with `pytest`

## ⚡ Quick Start

### 1️⃣ Install Python dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Start PostgreSQL using Docker

```bash
docker-compose up -d
```

### 3️⃣ Run the FastAPI app

```bash
uvicorn app.main:app --reload
```

Open your browser: http://127.0.0.1:8000/docs  
Test all endpoints interactively.

### 4️⃣ Bulk load the CSV data

```bash
python load_csv.py
```

### 5️⃣ Run API tests

```bash
pytest tests/
```

## 📂 Project Structure

```
fitness_tracker_api/
 ├── app/
 │   ├── db.py
 │   ├── models.py
 │   ├── schemas.py
 │   ├── main.py
 ├── data/
 │   └── Fitness_Tracker_Data.csv
 ├── tests/
 │   └── test_api.py
 ├── docker-compose.yml
 ├── load_csv.py
 ├── requirements.txt
 ├── .env.example
 ├── .gitignore
 ├── README.md
```

## Notes

This project does **not** use a real AWS SQS queue yet — it focuses on core CRUD and CSV ingestion.  
Easily extendable to real event-driven queues in production.

## ✅ Commit & Push

```bash
git add README.md
git commit -m "docs: add final single-block README"
git push
```
