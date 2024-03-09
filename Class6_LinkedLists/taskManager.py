class Task:
    def __init__(self, title, description, priority):
        self.title = title
        self.description = description
        self.priority = priority


    def __str__(self):
        return f"{self.title} - {self.description} - {self.priority}"


class Node:
    def __init__(self, task):
        self.task = task
        self.next = None

class TaskManager:
    def __init__(self):
        self.head = None

    def add_task(self, title, description, priority):
        new_task = Task(title, description, priority)
        new_node = Node(new_task)

        # If list is emptuy or new task has higher priority than head
        if not self.head or self._compare_priority(new_task, self.head.task) > 0:
            new_node.next = self.head
            self.head = new_node
        else:
            # Traverse the list to find the insertion point
            current = self.head
            while current.next and self._compare_priority(new_task, current.next.task) <= 0:
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def complete_task(self, title):
        current = self.head
        prev = None

        while current and current.task.title != title:
            prev = current
            current = current.next

        if current:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def view_tasks(self):
        current = self.head
        while current:
            print(current.task)
            current = current.next

    def _compare_priority(self, task1, task2):
        priority_map = {"High": 3, "Medium": 2, "Low": 1}
        return priority_map[task1.priority] - priority_map[task2.priority]


task_manager = TaskManager()
task_manager.add_task(
    "Implement authentication", "Create user authentication logic", "High"
)
task_manager.add_task(
    "Design database schema", "Design the initial database schema", "Medium"
)
task_manager.add_task(
    "Set up CI/CD pipeline", "Set up continuous integration and deployment", "High"
)

task_manager.view_tasks()
task_manager.complete_task("Implement authentication")
print("\nAfter completing a task:\n")
task_manager.view_tasks()
