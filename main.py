#Model

class Task:
  def __init__(self, titulo, description, dateOpen, dateClose):
    self.titulo = titulo
    self.descricao = description
    self.dateOpen = dateOpen
    self.dateClose = dateClose

#View
class Taskview:
  def show_tasks(self, tasks):
    print("Tarefas:")
    for task in tasks:
      print(f"Título: {task.titulo}, Descrição: {task.descricao}, Aberto em: {task.dateOpen}, Fechado em: {task.dateClose}")


#Controller
class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, titulo, descricao, dateOpen, dateClose):
        task = Task(titulo, descricao, dateOpen, dateClose)
        self.model.add_task(task)
        self.update_view()

    def mark_task_as_completed(self, task_index):
        self.model.mark_task_as_completed(task_index)
        self.update_view()

    def get_task_list(self):
        return self.model.get_task_list()

    def update_view(self):
        tasks = self.get_task_list()
        self.view.show_tasks(tasks)
      