
file = "tasks.txt"
def load_tasks(filename=file):
    #Read tasks from file and returns a list like [task_description, done (or) not done] items.
    #File Format: each line is either "0 task_description" or "1 task_description"-->0-done and 1-not done
    tasks = []
    try:
        with open(filename,"r") as f:
            for line in f:
                line = line.rstrip("\n")
                if not line:
                    continue
                
                task_status = line[0]
                if len(line) > 2:
                    task_description = line[2:]
                else:
                    task_description = ""
                    
                if task_status == "1":
                    done = True
                else:
                    done = False
    except FileNotFoundError:
        pass 
    return tasks 

def view_tasks(tasks):
    #print all tasks with an index and status
    if len(tasks)==0:
        print("\nNo tasks added yet. Add the task....!\n")
        return 
    print("\nYour Tasks are: ")
    for i,(text,done) in enumerate(tasks,start=1):
        task_status = "[x]" if done else "[ ]"
        print(str(i)+" "+task_status+" "+text)
    print("")

def add_tasks(tasks):
    #Add task entered by user
    text = input("Enter task description: ").strip()
    if text:
        tasks.append([text,False])
        print("Task Added")
    else:
        print("Empty task cannot add")
        
def mark_task_as_done(tasks):
    #Mark task as done or not done
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to mark done: "))
        if 1<= task_number and task_number<=len(tasks):
            tasks[task_number - 1][1] = True
            print("Marked done: "+tasks[task_number-1][0])
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
        
def remove_task(tasks):
    #Remove task by index
    view_tasks(tasks)
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to remove: "))
        if 1<=task_number and task_number<=len(tasks):
            removed = tasks.pop(task_number-1)
            print("Removed: "+removed[0])
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
        
def edit_tasks(tasks):
    #Edit the description of existing task             
    view_tasks(tasks)
    if not tasks:
        return 
    try:
        task_number = int(input("Enter task number to edit: "))
        if 1 <= task_number and task_number<=len(tasks):
            task_to_edit = tasks[task_number-1][0]
            print("Current text: "+task_to_edit)
            new_task = input("Entyer new description: ").strip()
            if new_task:
                tasks[task_number-1][0] = new_task
                print("Task Added")
            else:
                print("Edit cancelled")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")
        
def clear_tasks(tasks):
    #clear all the task which are present in tasks list
    confirmation = input("Do you want to clear all the tasks(y/N): ").lower()
    if confirmation == "y":
        tasks.clear()
        print("All tasks deleted.")
    else:
        print("Cancelled")
        
def save_tasks(tasks,filename=file):
    #Save the tasks list to the file
    if not tasks:
        print("No task is added still....")
        return
    with open(filename,"w") as f:
        for text,done in tasks:
            line = ""
            if done:
                line = "1 "+text+"\n"
            else:
                line = "0 "+text+"\n"
            f.write(line)
    print("Tasks saved......") 

def show_menu():
    print("Simple To-Do List")
    print("------------------")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task done")
    print("4. Remove task")
    print("5. Edit task")
    print("6. Clear all tasks")
    print("7. Save and Exit")


def tasksToDo():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option from 1 to 7: ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_tasks(tasks)
        elif choice == '3':
            mark_task_as_done(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            edit_tasks(tasks)
        elif choice == '6':
            clear_tasks(tasks)
        elif choice == '7':
            save_tasks(tasks)
            break
        else:
            print("Invalid option. Please enter correct number from 1 to 7.")
            print("-"*30)
            
tasksToDo()