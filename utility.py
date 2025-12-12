import json
from enum import Enum
from rich.console import Console

console = Console()

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
                console.print("[red]Invalid input. Please enter a number.[/red]")

    @staticmethod
    def get_required_input(prompt: str) -> str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            console.print("[red]Input cannot be empty.[/red]")

