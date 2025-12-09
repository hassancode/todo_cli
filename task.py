tasks = []
task_count=0

def add(task):
    global task_count
    task_count+=1
    tasks.append({'id': task_count, 'task': task})
    print(f'added {task}')

def update(task_id, new_value):
    result = get_by_id(task_id)
    if result is None:
        print(f'Task with id {task_id} not found')
        return
    i,t = result
    t['task'] = new_value
    tasks[i] = t
    print(f'updated {new_value} for taskid: {task_id}')

def delete(task_id):
    result = get_by_id(task_id)
    if result is None:
        print(f'Task with id {task_id} not found')
        return
    i,t = result
    tasks.remove(t)
    print(f'deleted taskid: {task_id}')

def view():
    if len(tasks) > 0:
        print(tasks)
    else:
        print('There is no task yet!')

def get_by_id(task_id):
    matches = [(i,tsk) for i, tsk in enumerate(tasks) if tsk.get('id') == task_id]
    return matches[0] if matches else None