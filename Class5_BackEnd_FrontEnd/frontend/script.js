document.addEventListener("DOMContentLoaded", fetchTasks);
document.getElementById("taskForm").addEventListener("submit", addTask);

function fetchTasks() {
  fetch("/tasks")
    .then((response) => response.json())
    .then((data) => {
      const taskList = document.getElementById("taskList");
      taskList.innerHTML = "";
      data.forEach((task) => {
        const li = document.createElement("li");
        li.textContent = task.title;
        const deleteBtn = document.createElement("button");
        deleteBtn.textContent = "Delete";
        deleteBtn.addEventListener("click", function () {
          deleteTask(task.id);
        });
        li.appendChild(deleteBtn);
        taskList.appendChild(li);
      });
    })
    .catch((error) => console.error("Error:", error));
}

function addTask(e) {
  e.preventDefault();
  const taskTitle = document.getElementById("taskTitle").value; // Ensure this ID matches your HTML
  fetch("/tasks", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title: taskTitle }),
  }).then(() => {
    document.getElementById("taskTitle").value = "";
    fetchTasks();
  });
}

function deleteTask(taskId) {
  fetch(`/tasks/${taskId}`, {
    method: "DELETE",
  }).then(() => fetchTasks());
}
