import json
from utility import Priority, TaskStatus, TaskNotFound, console
from rich.table import Table

class Task:
    def __init__(self, id: int, title: str, description: str, priority: Priority, status: TaskStatus = TaskStatus.PENDING):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.priority: Priority = priority
        self.status: TaskStatus = status

    def to_dict(self):
        """Converts the Task object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority.value,
            "status": self.status.value
        }

    @staticmethod
    def from_dict(data: dict):
        """Creates a Task object from a dictionary."""
        return Task(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            priority=Priority(data["priority"]),
            status=TaskStatus(data["status"])
        )

class TaskManager:
    def __init__(self):
        self._repository = TaskRepository()
        self.tasks = self._repository.read_tasks()
        self.task_count = max([task.id for task in self.tasks]) if self.tasks else 0

    def _save_tasks(self):
        self._repository.write_tasks(self.tasks)

    def add(self, title: str, description: str, priority: Priority):
        self.task_count += 1
        new_task = Task(self.task_count, title, description, priority)
        self.tasks.append(new_task)
        self._save_tasks()
        return new_task

    def update(self, id: int, new_title: str, new_description: str, new_priority: Priority, new_status: TaskStatus)->bool:
        result = self.get_by_id(id)
        if result is None:
            raise TaskNotFound(f'Task with id {id} not found')
        i, t = result
        t.title = new_title
        t.description = new_description
        t.priority = new_priority
        t.status = new_status
        self.tasks[i] = t
        self._save_tasks()
        return True

    def delete(self, id)->bool:
        result = self.get_by_id(id)
        if result is None:
            raise TaskNotFound(f'Task with id {id} not found')
        i, _ = result
        self.tasks.pop(i)
        self._save_tasks()
        return True

    def delete_all(self)->bool:
        """Deletes all tasks from the list."""
        self.tasks.clear()
        self.task_count = 0
        self._save_tasks()
        return True

    def view(self):
        if len(self.tasks) > 0:
            table = Table(title="[bold cyan]Your Tasks[/bold cyan]", show_header=True, header_style="bold magenta")
            table.add_column("ID", style="cyan", justify="center", width=6)
            table.add_column("Title", style="bold", justify="left")
            table.add_column("Description", style="dim", justify="left")
            table.add_column("Priority", justify="center", width=10)
            table.add_column("Status", justify="center", width=12)

            for t in self.tasks:
                # Color code priority
                if t.priority == Priority.HIGH:
                    priority_str = f"[red]{t.priority.name}[/red]"
                elif t.priority == Priority.MEDIUM:
                    priority_str = f"[yellow]{t.priority.name}[/yellow]"
                else:
                    priority_str = f"[green]{t.priority.name}[/green]"

                # Color code status
                if t.status == TaskStatus.COMPLETED:
                    status_str = f"[green]{t.status.name}[/green]"
                elif t.status == TaskStatus.IN_PROGRESS:
                    status_str = f"[blue]{t.status.name}[/blue]"
                else:
                    status_str = f"[yellow]{t.status.name}[/yellow]"

                table.add_row(
                    str(t.id),
                    t.title,
                    t.description or "[dim]No description[/dim]",
                    priority_str,
                    status_str
                )

            console.print(table)
        else:
            console.print('[yellow]There is no task yet![/yellow]')

    def get_by_id(self, id):
        """Get task by id. Returns (index, task) if exists, None otherwise"""
        matches = [(i,tsk) for i, tsk in enumerate(self.tasks) if tsk.id == id]
        return matches[0] if matches else None
    
    def get_by_index(self, index):
        """Get task by index. Returns (index, task) if exists, None otherwise"""
        if 0 <= index < len(self.tasks):
            return (index, self.tasks[index])
        return None

class TaskRepository:
    """
    Handles reading and writing tasks to a file.
    """
    def __init__(self, filename="tasks.json"):
        self._filename = filename

    def read_tasks(self):
        """
        Reads tasks from a JSON file and returns a list of Task objects.
        """
        try:
            with open(self._filename, 'r') as f:
                tasks_data = json.load(f)
            return [Task.from_dict(task_data) for task_data in tasks_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_tasks(self, tasks):
        """
        Writes a list of Task objects to a JSON file.
        """
        with open(self._filename, 'w') as f:
            json.dump([task.to_dict() for task in tasks], f, indent=4)