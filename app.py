#Mini Flask Task API
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [
            {"id": 1, "title": "Learn Flask"},
            {"id": 2, "title": "Build API"}
        ]

tasks = load_tasks()

@app.route("/tasks")
def get_tasks():
    return jsonify(tasks)

@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json()
    if not data or not isinstance(data.get("title"), str) or not data["title"].strip():
        return jsonify({"error": "A valid title is required"}), 400 
    print(data)
    new_id = max((task["id"] for task in tasks), default=0) + 1
    new_task = {"id": new_id, "title": data["title"]}
    tasks.append(new_task)
    save_tasks()
    return jsonify(new_task), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks()
            return jsonify({"message": "Task successfully deleted"})
    return jsonify({"error": "Task not found"}), 404

app.run(debug=True, port=5001)