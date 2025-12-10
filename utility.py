from enum import Enum, IntEnum

class MenuOption:
    ADD = 1
    UPDATE = 2
    DELETE = 3
    EXIT = 0

class UpdateOption:
    ID = 1
    INDEX = 2
    RETURN = 0

class TaskStatus(Enum):
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

class Utility:
    @staticmethod
    def get_required_input(prompt: str)->str:
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print('This field is required. Please try again.')

    @staticmethod
    def get_required_int(prompt: str) -> int:
        """Get required integer input with validation"""
        while True:
            value = input(prompt).strip()
            if not value:
                print('This field is required. Please try again.')
                continue
            try:
                return int(value)
            except ValueError:
                print('Invalid input. Please enter a valid integer.')

    @staticmethod
    def get_menu_choice(prompt: str) -> int:
        """Get menu choice with validation"""
        while True:
            try:
                value = input(prompt).strip()
                if not value:
                    print('Please enter a choice.')
                    continue
                return int(value)
            except ValueError:
                print('Invalid input. Please enter a valid number.')

class TaskNotFound(Exception):
    """Raised when a task lookup fails."""
    def __init__(self, message: str = "No Task Found"):
        super().__init__(message)

