#Model

class Task:
  def __init__(self, titulo, description, dateOpen, dateClose):
    self.titulo = titulo
    self.descricao = description
    self.dateOpen = dateOpen
    self.dateClose = dateClose

#View
class Taskview:
  def show_users(self, users):
    print("Usuários")
    for user in users:
      print(f"Nome: {user.name}, Email: {user.email}")

  def show_tasks(self, tasks):
    print("\nTarefas:")
    for task in tasks:
      print(f"Título: {task.titulo}, Descrição: {task.description}, Aberto em: {task.dateOpen}, Fechado em: {task.dateClose}")
