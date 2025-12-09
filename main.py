#add, update, delete todo
from task import add, update, delete, view

print()
print('Welcome to todo app', end='\n\n')

view()

while(True):
    print()
    print('-'*25)
    print('Type 1 to add task', 'Type 2 to update task', 'Type 3 to delete task', 'Type 4 to exit', sep='\n')
    print('-'*25)
    op_type = int(input('Enter your choice: '))

    if op_type == 1:
        task = input('Enter task: ')
        add(task)
    elif op_type == 2:
        task_id = int(input('Enter taskid: '))
        new_val = input('Enter new value: ')
        update(task_id, new_val)
    elif op_type == 3:
        task_id = int(input('Enter taskid: '))
        delete(task_id)
    elif op_type == 4:
        break
    else:
        print('Invalid choice')