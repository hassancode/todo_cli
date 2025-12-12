from task import TaskManager, Task
from utility import Utility, MenuOption, UpdateOption, TaskNotFound, Priority, TaskStatus, console

def _print_main_menu():
    """Prints the main menu options."""
    console.print()
    console.print('[bold yellow]Main Menu[/bold yellow]')
    console.print('[dim]──────────[/dim]')
    console.print('[cyan]1.[/cyan] Add task')
    console.print('[cyan]2.[/cyan] Update task')
    console.print('[cyan]3.[/cyan] Delete task')
    console.print('[cyan]4.[/cyan] View all tasks')
    console.print('[cyan]5.[/cyan] Delete all tasks')
    console.print('[cyan]0.[/cyan] Exit')

def _add_task(task_manager: TaskManager):
    """Handles the logic for adding a new task."""
    title = Utility.get_required_input('Enter title (required): ')
    description = input('Enter description (optional): ').strip()
    priority = Priority.LOW
    while True:
        priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; OR press enter to default as LOW): ').strip()
        if priority_input:
            try:
                priority = Priority(int(priority_input))
                break
            except ValueError:
                console.print('[red]Invalid priority. Please enter 1, 2, or 3.[/red]')
        else:
            break
    added_task = task_manager.add(title=title, description=description, priority=priority)
    console.print(f'[green]✓ Added {added_task.title} successfully![/green]')

def _update_task(task_manager: TaskManager):
    """Handles the logic for updating an existing task."""
    while True:
        try:
            console.print('[cyan]1.[/cyan] Update by id')
            console.print('[cyan]2.[/cyan] Update by index')
            console.print('[cyan]0.[/cyan] Return to main menu')
            update_by = UpdateOption(Utility.get_required_int('Choose an update option: '))
            break
        except ValueError:
            console.print('[red]Invalid option. Please enter 1, 2, or 0.[/red]\n')

    if update_by == UpdateOption.RETURN:
        return

    result = None
    if update_by == UpdateOption.ID:
        task_id = Utility.get_required_int('Enter id (required): ')
        result = task_manager.get_by_id(task_id)
    elif update_by == UpdateOption.INDEX:
        index = Utility.get_required_int('Enter index (required): ')
        result = task_manager.get_by_index(index)

    if result is None:
        console.print('[red]There is no task with the given id or index[/red]')
        return

    _, task = result
    console.print(f'[dim]Current title:[/dim] [bold]{task.title}[/bold]')
    new_title = input('Enter new title (leave blank to keep same): ').strip() or task.title

    console.print(f'[dim]Current description:[/dim] {task.description}')
    new_description = input('Enter new description (leave blank to keep same): ').strip() or task.description

    console.print(f'[dim]Current priority:[/dim] {task.priority.name}')
    while True:
        new_priority_input = input('Enter new priority (1=LOW, 2=MEDIUM, 3=HIGH; leave blank to keep same): ').strip()
        if not new_priority_input:
            new_priority = task.priority
            break
        try:
            new_priority = Priority(int(new_priority_input))
            break
        except ValueError:
            console.print('[red]Invalid priority. Please enter 1, 2, or 3.[/red]')

    console.print(f'[dim]Current status:[/dim] {task.status.name}')
    while True:
        new_status_input = input('Enter new status (pending/in_progress/completed; leave blank to keep same): ').strip().lower()
        if not new_status_input:
            new_status = task.status
            break
        try:
            new_status = TaskStatus(new_status_input)
            break
        except ValueError:
            console.print('[red]Invalid status. Please enter pending, in_progress, or completed.[/red]')

    if task_manager.update(id=task.id, new_title=new_title, new_description=new_description, new_priority=new_priority, new_status=new_status):
        console.print('[green]✓ Task has been updated successfully![/green]')
    else:
        console.print('[red]Sorry, task could not be updated, please try again[/red]')
    input('\nPress Enter to return to main menu...')

def _delete_task(task_manager: TaskManager):
    """Handles the logic for deleting a task."""
    try:
        task_id = Utility.get_required_int('Enter task id (required): ')
        if task_manager.delete(task_id):
            console.print(f'[green]✓ Task id {task_id} has been deleted successfully![/green]')
        else:
            console.print(f'[red]Sorry, Task id {task_id} could not be deleted, please try again[/red]')
    except TaskNotFound as te:
        console.print(f'[red]{te}[/red]\n')
    input('\nPress Enter to return to main menu...')

def _view_tasks(task_manager: TaskManager):
    """Displays all tasks."""
    task_manager.view()
    input('\nPress Enter to return to main menu...')

def _delete_all_tasks(task_manager: TaskManager):
    """Handles the logic for deleting all tasks."""
    if not task_manager.tasks:
        console.print('[yellow]There are no tasks to delete![/yellow]')
    else:
        confirmation = input(f'Are you sure you want to delete all {len(task_manager.tasks)} tasks? (yes/no): ').strip().lower()
        if confirmation == 'yes':
            task_manager.delete_all()
            console.print('[green]✓ All tasks have been deleted successfully![/green]')
        else:
            console.print('[yellow]Delete all operation cancelled.[/yellow]')
    input('\nPress Enter to return to main menu...')

def main():
    """Main function to run the TODO application."""
    task_manager = TaskManager()
    console.print()
    console.print('[bold cyan]═════ TODO APP ═════[/bold cyan]\n')

    while True:
        _print_main_menu()
        try:
            op_type = MenuOption(Utility.get_required_int('Choose a main menu option: '))
            
            if op_type == MenuOption.ADD:
                _add_task(task_manager)
            elif op_type == MenuOption.UPDATE:
                _update_task(task_manager)
            elif op_type == MenuOption.DELETE:
                _delete_task(task_manager)
            elif op_type == MenuOption.VIEW:
                _view_tasks(task_manager)
            elif op_type == MenuOption.DELETE_ALL:
                _delete_all_tasks(task_manager)
            elif op_type == MenuOption.EXIT:
                break
            else:
                console.print('[red]Invalid option selected. Please try again.[/red]')

        except ValueError:
            console.print('[red]Invalid input. Please enter a valid number for the menu option.[/red]')
        except Exception as e:
            console.print(f'[red]An unexpected error occurred: {e}[/red]')

if __name__ == "__main__":
    main()
