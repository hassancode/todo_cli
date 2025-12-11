import json
from enum import Enum

class TaskNotFound(Exception):
    """Exception raised when a task is not found."""
    pass

class Priority(Enum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class TaskStatus(Enum):
    PENDING = 'pending'
    IN_PROGRESS = 'in_progress'
    COMPLETED = 'completed'

class MenuOption(Enum):
    ADD = 1
    UPDATE = 2
    DELETE = 3
    VIEW = 4
    DELETE_ALL = 5
    EXIT = 0

class UpdateOption(Enum):
    ID = 1
    INDEX = 2
    RETURN = 0

class Utility:
    @staticmethod
    def get_menu_choice(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                raise ValueError("Invalid input. Please enter a number.")
                #print("Invalid input. Please enter a number.")

    @staticmethod
    def get_required_int(prompt: str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a number.")

    @staticmethod
    def get_required_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Input cannot be empty.")

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
        from task import Task  # Local import to prevent circular dependency
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
