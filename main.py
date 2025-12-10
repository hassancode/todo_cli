from task import TaskManager, Task
from utility import Utility, MenuOption, UpdateOption, TaskNotFound, Priority, TaskStatus

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
            if op_type == MenuOption.ADD:
                title = Utility.get_required_input('Enter title (required): ')
                description = input('Enter description (optional): ').strip()
                priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; default is LOW): ').strip()
                priority = Priority.LOW
                if priority_input:
                    try:
                        priority = Priority(int(priority_input))
                    except ValueError:
                        print('Invalid priority. Please enter 1, 2, or 3.')
                        return 
                added_task: Task = task_manager.add(title=title, description=description, priority=priority)
                print(f'Added {added_task.title} successfully!')
            elif op_type == MenuOption.UPDATE:
                print('1. Update by id', '2. Update by index', '0. Return', sep='\n')
                update_by = Utility.get_menu_choice('Choose an option: ')
                
                result = None
                if update_by == UpdateOption.ID:
                    task_id = Utility.get_required_int('Enter id (required): ')
                    result = task_manager.get_by_id(task_id)
                elif update_by == UpdateOption.INDEX:
                    index = Utility.get_required_int('Enter index (required): ')
                    result = task_manager.get_by_index(index)
                elif update_by == UpdateOption.RETURN:
                    continue
                else:
                    raise ValueError('Invalid option selected for update')
                
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
                    new_priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; leave blank to keep same): ').strip()
                    new_priority = task.priority
                    if new_priority_input:
                        try:
                            new_priority = Priority(int(new_priority_input))
                        except ValueError:
                            print('Invalid priority. Please enter 1, 2, or 3.')
                            return 

                    print(f'Current status: {task.status}')
                    new_status_input = input('Enter new status (pending/in_progress/completed; leave blank to keep same): ').strip().lower()
                    new_status = task.status
                    if new_status_input:
                        try:
                            new_status = TaskStatus(new_status_input)
                        except ValueError:
                            print('Invalid status. Please enter pending, in_progress, or completed.')
                            return  # or continue to skip update

                    task_manager.update(
                        id=task.id,
                        new_title=new_title,
                        new_priority=new_priority,
                        new_description=new_description,
                        new_status=new_status
                    )
            elif op_type == MenuOption.DELETE:
                task_id = Utility.get_required_int('Enter taskid (required): ')
                task_manager.delete(task_id)
            elif op_type == 0:
                break
            else:
                raise ValueError('Invalid option selected from menu option')
        except TaskNotFound as te:
            print(f'{te}')
        except ValueError as ve:
            print(f'Input error: {ve}')
        except Exception as e:
            print(f'Something went wrong, error: {e}')

if __name__ == "__main__":
    main()