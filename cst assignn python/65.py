##65.	Create a ToDo application using classes and file handling to save tasks.

class ToDoApp:
    def __init__(self,filename="tasks.txt"):
        self.filename=filename

    def add_task(self,task):
        with open(self.filename,"a")as file:
            file.write(task + "\n")

    def show_tasks(self):
       
        try:
            with open(self.filename,"r")as file:
                tasks=file.readlines()
                print("your tasks:")
                for i, task in enumerate(tasks,1):
                    print(f"{i}.{task.strip()}")
        except FileNotFoundError:
            print("no tasks found.")

app = ToDoApp()
app.add_task("learn python")
app.add_task("build a to do app")
app.show_tasks()