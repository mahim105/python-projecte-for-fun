def task_management_app():
    tasks = []  # Renamed for clarity
    print('Welcome to the task management app')
    
    total_tasks = int(input('Enter how many tasks you want to add: '))
    for i in range(1, total_tasks + 1):
        task_name = input(f'Enter task {i}: ')
        tasks.append(task_name)
    
    print(f'Today\'s tasks are: {tasks}')
    
    while True:
        operation = int(input('Enter 1 - Add\n2 - Update\n3 - Delete\n4 - View\n5 - Exit: '))
        
        if operation == 1:
            add_task = input('Enter task you want to add: ')
            tasks.append(add_task)
            print(f'Task "{add_task}" has been successfully added.')
        
        elif operation == 2:
            update_task = input('Enter the task name that you want to update: ')
            if update_task in tasks:
                new_task = input('Enter new task: ')
                index = tasks.index(update_task)
                tasks[index] = new_task
                print(f'Updated task "{update_task}" to "{new_task}".')
            else:
                print(f'Task "{update_task}" not found.')
        
        elif operation == 3:
            delete_task = input('Enter the task name you want to delete: ')
            if delete_task in tasks:
                tasks.remove(delete_task)
                print(f'Task "{delete_task}" has been successfully deleted.')
            else:
                print(f'Task "{delete_task}" not found.')
        
        elif operation == 4:
            print(f'Current tasks: {tasks}')
        
        elif operation == 5:
            print('Exiting the app. Goodbye!')
            break
        
        else:
            print('Invalid operation. Please try again.')

# Call the function to run the app
task_management_app()
