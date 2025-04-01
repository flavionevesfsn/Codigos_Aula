def agendamento_atividades(atividades):
    atividades.sort(key=lambda x: x[1])  # Ordena pelo horário de término
    selecionadas = [atividades[0]]
    for i in range(1, len(atividades)):
        if atividades[i][0] >= selecionadas[-1][1]:
            selecionadas.append(atividades[i])
    return selecionadas

atividades = [(1, 3), (2, 5), (3, 9), (6, 8), (5, 7)]
print(agendamento_atividades(atividades))