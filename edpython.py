#utilizção das estruturas Lista, tupla e dicionário

#função para criar tarefas
def criar_task(nome, due_date, prioridade):
    task = {
        'tarefa' : nome,
        'data' : due_date,
        'prioridade' : prioridade
    }
    return task

def print_tasks(tasks):
    for task in tasks:
        print (task)

def search_task(tasks, name):
    for task in tasks:
        if task['nome'] == name:
            return task

    return None

def sort_tasks(tasks, by='due_date', ascending=True):
    # Classifica a lista de tarefas
    if by == 'due_date':
        tasks.sort(key=lambda task: task['due_date'], reverse=not ascending)
    elif by == 'priority':
        tasks.sort(key=lambda task: task['priority'], reverse=not ascending)

    return tasks

#lista para armazenar as tarefas
tasks = []

#adicionar tarefas à lisa
tasks.append(criar_task('Trabalho de e.d', '25-08', 'Média'))
tasks.append(criar_task('Fazer os brigadeiros', '19-08', 'Alta'))
tasks.append(criar_task('Lavar o banheiro' '20-08', 'Média'))

# Imprime a lista de tarefas
print_tasks(tasks)

# Pesquisa uma tarefa na lista de tarefas
task = search_task(tasks, 'Escrever um artigo')
if task is not None:
    print(task)

# Classifica a lista de tarefas por data de vencimento
tasks = sort_tasks(tasks, by='due_date')
print_tasks(tasks)
