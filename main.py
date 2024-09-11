class ToDoApp:

    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        return f"Task '{task}' added!"

    def view_tasks(self):
        return self.tasks

    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"Task '{task}' completed!"
        else:
            return f"Task '{task}' not found!"


# Test the application
if __name__ == "__main__":
    app = ToDoApp()
    app.add_task("Finish GitHub profile ASAP")
    print(app.view_tasks())
