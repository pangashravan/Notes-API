# Notes-API

A simple FastAPI application for creating and reading notes, built with Python, SQLAlchemy, and SQLite.

## Project Overview

`Notes-API` is a lightweight web API that stores notes in a local SQLite database. It follows a clean structure with separate modules for:

- web routes and API logic (`app/main.py`)
- database configuration (`app/database.py`)
- data models (`app/models.py`)
- request/response schemas (`app/schemas.py`)
- database operations / CRUD logic (`app/crud.py`)

This structure helps keep code organized, easier to maintain, and easier to extend.

## Features

- Create notes via `POST /notes/`
- Read all notes via `GET /notes/`
- Uses FastAPI for automatic validation and documentation
- Uses SQLAlchemy ORM for database interaction
- Stores data locally using SQLite (`app.db`)

## Technology Stack

- Python 3
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite

## Setup

1. Open PowerShell and navigate to the project root:

```powershell
cd C:\projects\Notes-API
```

1. Create and activate the virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

1. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r app/requirements.txt
```

## Run the API

Start the application with Uvicorn:

```powershell
uvicorn app.main:app --reload
```

Then open `http://127.0.0.1:8000/docs` to explore the API documentation and test the endpoints interactively.

## API Endpoints

- `POST /notes/` - Create a new note
- `GET /notes/` - Retrieve all notes

### Example request body for `POST /notes/`

```json
{
  "title": "Shopping",
  "content": "Buy milk and eggs"
}
```

## Project Structure

```text
Notes-API/
├── app/
│   ├── main.py
│   ├── crud.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
├── app.db
└── README.md
```

## Why this README is written this way

This README focuses on clarity and practical setup. It tells someone exactly what the project does, how the code is organized, and how to run it. That is what employers and team members expect to see in a real project.

## How to write a good README

1. Start with a short project summary.
2. Describe the main features.
3. List the technologies used.
4. Provide clear setup and run instructions.
5. Explain the folder structure briefly.
6. Keep it short, but useful.

## Learning advice

- Read the project files in the order shown in this README.
- Practice adding one new endpoint at a time.
- Use the API docs at `/docs` to understand request and response formats.
- Update the README as you add features.
