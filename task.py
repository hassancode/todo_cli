from utility import Priority, TaskStatus, TaskNotFound, TaskRepository

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
        t.title = new_title if new_title != '' else t.title
        t.description = new_description if new_description != '' else t.description
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
            print('-'*30)
            for t in self.tasks:
                print(f'Id={t.id}, Title={t.title}, Desc={t.description}, Priority={t.priority.name}, Status={t.status.name}')
            print('-'*30)
        else:
            print('There is no task yet!')

    def get_by_id(self, id):
        """Get task by id. Returns (index, task) if exists, None otherwise"""
        matches = [(i,tsk) for i, tsk in enumerate(self.tasks) if tsk.id == id]
        return matches[0] if matches else None
    
    def get_by_index(self, index):
        """Get task by index. Returns (index, task) if exists, None otherwise"""
        if 0 <= index < len(self.tasks):
            return (index, self.tasks[index])
        return None
