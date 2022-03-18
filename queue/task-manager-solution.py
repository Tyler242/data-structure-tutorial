print('Task Manager 1.0')
done = False

queue = []


def add_task(task):
    """
        Add a task to the end of the queue
    """
    queue.append(task)


def complete_task():
    """
        Remove the next task in the queue
    """
    if len(queue) < 1:
        print('No tasks to complete')
        return

    task = queue[0]
    del queue[0]

    print('Task \'{}\' complete'.format(task))


def total_tasks():
    """
        Return the size of the queue
    """
    return len(queue)


def display_queue():
    """
        Display each task in the queue
    """
    for task in queue:
        print(task)


while not done:
    print('1. Add task')
    print('2. Complete next task')
    print('3. View total number of tasks')
    print('4. View queue')
    print('5. Quit')

    option = int(input('Enter a number (1-4)\n> '))

    if option == 1:
        task_name = input('Enter name of task: ')
        add_task(task_name)
    elif option == 2:
        complete_task()
    elif option == 3:
        total = total_tasks()
        print(total)
    elif option == 4:
        display_queue()
    elif option == 5:
        print('goodbye')
        done = True

    print()
