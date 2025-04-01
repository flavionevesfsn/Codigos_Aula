def organiza_tarefas(tempo_disponivel, tarefas):
    # Ordena as tarefas do menor para o maior tempo de duração (estratégia gulosa)
    tarefas.sort()
    
    tempo_atual = 0
    tarefas_realizadas = []
    
    for tarefa in tarefas:
        if tempo_atual + tarefa <= tempo_disponivel:
            tarefas_realizadas.append(tarefa)
            tempo_atual += tarefa
        else:
            break  # Não há mais tempo para novas tarefas

    return tarefas_realizadas, tempo_atual

# Lista de tarefas com seus tempos de duração (em minutos)
tarefas = [30, 9, 10, 1, 20, 5, 15, 40, 50]  
tempo_maximo = 90  # Tempo total disponível

resultado, tempo_utilizado = organiza_tarefas(tempo_maximo, tarefas)

print("Tarefas escolhidas:", resultado)
print("Tempo total utilizado:", tempo_utilizado)
