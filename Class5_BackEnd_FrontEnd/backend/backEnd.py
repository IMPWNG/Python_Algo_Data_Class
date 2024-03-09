from flask import Flask, jsonify, request, send_from_directory
import os

app = Flask(__name__, static_folder="frontend")

# Global variable to store tasks and a counter for unique task IDs
tasks = []
task_id_counter = 1


@app.route("/")
def serve_index():
    return send_from_directory("/frontend", "index.html")


@app.route("/<path:path>")
def serve_file(path):
    return send_from_directory("/frontend", path)


@app.route("/tasks", methods=["GET", "POST"])
def manage_tasks():
    global task_id_counter
    if request.method == "GET":
        return jsonify(tasks)
    elif request.method == "POST":
        task_title = request.json.get("title")
        task = {"id": task_id_counter, "title": task_title}
        tasks.append(task)
        task_id_counter += 1
        return jsonify(task), 201


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task removed"}), 200
    return jsonify({"error": "Task not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
