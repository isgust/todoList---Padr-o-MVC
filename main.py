from datetime import date

# Modelo (Model)
class Task:
    def __init__(self, titulo, descricao, dateOpen, dateClose=None, concluida=False):
        self.titulo = titulo
        self.descricao = descricao
        self.dateOpen = dateOpen
        self.dateClose = dateClose
        self.concluida = concluida


# Controlador (Controller)
class TaskController:
    def __init__(self):
        self.tasks = []

    def adicionar_tarefa(self, titulo, descricao):
        task = Task(titulo, descricao, date.today())
        self.tasks.append(task)

    def marcar_tarefa_como_concluida(self, indice_tarefa):
        if 0 <= indice_tarefa < len(self.tasks):
            self.tasks[indice_tarefa].concluida = True
            self.tasks[indice_tarefa].dateClose = date.today()

    def obter_lista_de_tarefas(self):
        return self.tasks

# Visão (View)
class TaskView:
    def mostrar_tarefas(self, tasks):
        print("Lista de Tarefas:")
        for index, task in enumerate(tasks):
            status = "Concluída" if task.concluida else "Pendente"
            dateOpen = task.dateOpen.strftime("%d/%m/%Y")  # Formata a data
            dateClose = task.dateClose.strftime("%d/%m/%Y") if task.dateClose else "N/A"
            print(f"{index + 1}. {task.titulo} - {status} - Início: {dateOpen} - Conclusão: {dateClose}")

    def solicitar_titulo_descricao(self):
        titulo = input("Digite o título da nova tarefa: ")
        descricao = input("Digite a descrição da nova tarefa: ")
        return titulo, descricao

    def mostrar_mensagem(self, mensagem):
        print(mensagem)

# Uso do MVC
if __name__ == "__main__":
    controller = TaskController()
    view = TaskView()

    while True:
        print("\n--- Menu ---")
        print("1. Adicionar Tarefa")
        print("2. Marcar Tarefa como Concluída")
        print("3. Exibir Lista de Tarefas")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            titulo, descricao = view.solicitar_titulo_descricao()
            controller.adicionar_tarefa(titulo, descricao)
            view.mostrar_mensagem("Tarefa adicionada com sucesso!")
        elif opcao == "2":
            indice_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: ")) - 1
            controller.marcar_tarefa_como_concluida(indice_tarefa)
            view.mostrar_mensagem("Tarefa marcada como concluída com sucesso!")
        elif opcao == "3":
            tasks = controller.obter_lista_de_tarefas()
            view.mostrar_tarefas(tasks)
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
