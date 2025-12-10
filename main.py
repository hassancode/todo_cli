from task import TaskManager, Task
from utility import Utility

def main():
    task_manager = TaskManager()
    print()
    print('Welcome to todo app', end='\n\n')

    while(True):
        print()
        task_manager.view()
        print()
        print('='*5, 'TODO APP', '='*5)
        print('1. Add task', '2. Update task', '3. Delete task', '0. Exit', sep='\n')

        try:
            op_type = Utility.get_menu_choice('Choose an option: ')
            if op_type == 1:
                title = Utility.get_required_input('Enter title (required): ')
                description = input('Enter description (optional): ').strip()
                priority = input('Enter priority (optional): ').strip()
                added_task: Task = task_manager.add(title=title, description=description, priority=priority)
                print(f'Added {added_task.title} successfully!')
            elif op_type == 2:
                print('1. Update by id', '2. Update by index', '0. Return', sep='\n')
                update_by = Utility.get_menu_choice('Choose an option: ')
                
                result = None
                if update_by == 1:
                    task_id = Utility.get_required_int('Enter id (required): ')
                    result = task_manager.get_by_id(task_id)
                elif update_by == 2:
                    index = Utility.get_required_int('Enter index (required): ')
                    result = task_manager.get_by_index(index)
                elif update_by == 0:
                    continue
                else:
                    print('Invalid option')
                    continue
                
                if result is None:
                    print(f'There is no task with the given id or index')
                    continue
                else:
                    _, task = result
                    print(f'Current title: {task.title}')
                    new_title = input('Enter new title (leave blank to keep same): ').strip()
                    print(f'Current description: {task.description}')
                    new_description = input('Enter new description (leave blank to keep same): ').strip()
                    print(f'Current priority: {task.priority}')
                    new_priority = input('Enter new priority (leave blank to keep same): ').strip()
                    print(f'Current status: {task.status}')
                    new_status = input('Enter new status (leave blank to keep same):').strip()
                    task_manager.update(id=task.id, new_title=new_title, new_priority=new_priority, new_description=new_description, new_status=new_status)
            elif op_type == 3:
                task_id = Utility.get_required_int('Enter taskid (required): ')
                task_manager.delete(task_id)
            elif op_type == 0:
                break
            else:
                print('Invalid choice')
        except Exception as e:
            print(f'Something went wrong, error: {e}')

if __name__ == "__main__":
    main()