from task import TaskManager, Task
from utility import Utility, MenuOption, UpdateOption, TaskNotFound, Priority, TaskStatus

def main():
    task_manager = TaskManager()
    print()
    print('='*5, 'TODO APP', '='*5, end='\n\n')

    while(True):
        print()
        print('Main menu', 10*'-', '1. Add task', '2. Update task', '3. Delete task', '4. View all tasks', '5. Delete all tasks', '0. Exit', sep='\n')
        try:
            op_type = MenuOption(Utility.get_required_int('Choose a main menu option: '))
            if op_type == MenuOption.ADD:
                title = Utility.get_required_input('Enter title (required): ')
                
                description = input('Enter description (optional): ').strip()

                priority = Priority.LOW

                while(True):
                    priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; OR press enter to default as LOW): ').strip()
                    if priority_input:
                        try:
                            priority = Priority(int(priority_input))
                            break
                        except ValueError:
                            print('Invalid priority. Please enter 1, 2, or 3.')
                            continue
                    else:
                        break
                added_task: Task = task_manager.add(title=title, description=description, priority=priority)
                print(f'Added {added_task.title} successfully!')
            elif op_type == MenuOption.UPDATE:
                while(True):
                    try:
                        print('1. Update by id', '2. Update by index', '0. Return to main menu', sep='\n')
                        update_by = UpdateOption(Utility.get_required_int('Choose an update option: '))
                        break
                    except ValueError:
                        print('Invalid option. Please enter 1, 2, or 0.\n')
                        continue
                
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
                    new_title = new_title if new_title else task.title

                    print(f'Current description: {task.description}')
                    new_description = input('Enter new description (leave blank to keep same): ').strip()

                    print(f'Current priority: {task.priority}')
                    while True:
                        new_priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; leave blank to keep same): ').strip()
                        if not new_priority_input:
                            new_priority = task.priority
                            break
                        try:
                            new_priority = Priority(int(new_priority_input))
                            break
                        except ValueError:
                            print('Invalid priority. Please enter 1, 2, or 3.')

                    print(f'Current status: {task.status}')
                    while True:
                        new_status_input = input('Enter new status (pending/in_progress/completed; leave blank to keep same): ').strip().lower()
                        if not new_status_input:
                            new_status = task.status
                            break
                        try:
                            new_status = TaskStatus(new_status_input)
                            break
                        except ValueError:
                            print('Invalid status. Please enter pending, in_progress, or completed.')
                            
                    updated = task_manager.update(
                        id=task.id,
                        new_title=new_title,
                        new_priority=new_priority,
                        new_description=new_description,
                        new_status=new_status
                    )
                    if updated:
                            print('Task has been updated successfully!')
                    else:
                        print(f'Sorry,task could not be updated, please try again')
                    input('\nPress Enter to return to main menu...')
            elif op_type == MenuOption.DELETE:
                while(True):
                    try:
                        task_id = Utility.get_required_int('Enter taskid (required): ')
                        deleted = task_manager.delete(task_id)
                        if deleted:
                            print(f'Task id {task_id} has been deleted successfully!')
                        else:
                            print(f'Sorry, Task id {task_id} could not be deleted, please try again')
                        input('\nPress Enter to return to main menu...')
                        break
                    except ValueError as ve:
                        print(f'Error: {ve}\n')
                        continue
            elif op_type == MenuOption.VIEW:
                task_manager.view()
                input('\nPress Enter to return to main menu...')
            elif op_type == MenuOption.DELETE_ALL:
                if len(task_manager.tasks) == 0:
                    print('There are no tasks to delete!')
                else:
                    confirmation = input(f'Are you sure you want to delete all {len(task_manager.tasks)} tasks? (yes/no): ').strip().lower()
                    if confirmation == 'yes':
                        task_manager.delete_all()
                        print('All tasks have been deleted successfully!')
                    else:
                        print('Delete all operation cancelled.')
                input('\nPress Enter to return to main menu...')
            elif op_type == MenuOption.EXIT:
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