from utility import Priority, TaskStatus, TaskNotFound

class Task:
    def __init__(self, id: int, title: str, description: str, priority: Priority):
        self.id: int = id
        self.title: str = title
        self.description: str = description
        self.priority: Priority = priority
        self.status: TaskStatus = TaskStatus.PENDING

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_count = 0

    def add(self, title: str, description: str, priority: Priority):
        self.task_count+=1
        new_task = Task(self.task_count, title, description, priority)
        self.tasks.append(new_task)
        return new_task

    def update(self, id: int, new_title: str, new_description: str, new_priority: Priority, new_status: TaskStatus):
        result = self.get_by_id(id)
        if result is None:
            raise TaskNotFound(f'Task with id {id} not found')
        i,t = result
        t.title = new_title if new_title != '' else t.title
        t.description = new_description if new_description != '' else t.description
        t.priority = new_priority if new_priority != '' else t.priority
        t.status = new_status if new_status != '' else t.status
        self.tasks[i] = t
        return True

    def delete(self, id):
        result = self.get_by_id(id)
        if result is None:
            raise TaskNotFound(f'Task with id {id} not found')
        i, _ = result
        self.tasks.pop(i)
        return True

    def view(self):
        if len(self.tasks) > 0:
            print('-'*10)
            #print('|\tTask Id\t|\t|\tTitle\t|')
            for t in self.tasks:
                print(f'Id={t.id}, Title={t.title}, Desc={t.description}, Priority={t.priority.value}, Status={t.status.value}')
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