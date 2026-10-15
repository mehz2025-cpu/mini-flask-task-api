# Mini Flask Task API

A simple REST API built with Flask to manage tasks using JSON persistence.

## Features
- Get all tasks
- Add tasks with POST
- Delete tasks with DELETE
- Validate task titles
- Store tasks in a JSON file

## Requirements
- Python 3
- Flask
- Requests

## Installation
```bash
pip install -r requirements.txt
```

## Run
```bash
python app.py
```

## Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Welcome message |
| GET | `/tasks` | Get all tasks |
| POST | `/tasks` | Add a task |
| DELETE | `/tasks/<task_id>` | Delete a task |