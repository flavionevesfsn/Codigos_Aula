def mochila_gulosa(capacidade, itens):
  
    # Resolve o Problema da Mochila 0/1 usando um algoritmo guloso.
    # :param capacidade: Capacidade máxima da mochila.
    # :param itens: Lista de tuplas (peso, valor).
    # :return: Valor máximo que pode ser carregado na mochila.
    
    # Ordena os itens com base no valor por peso (estratégia gulosa)
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)
    
    valor_total = 0
    peso_atual = 0
    
    for peso, valor in itens:
        if peso_atual + peso <= capacidade:
            peso_atual += peso
            valor_total += valor
    
    return valor_total

# Definição da lista de itens no formato (peso, valor)
itens = [(10, 60), (20, 100), (30, 120), (40, 150)]  # Exemplo: (Peso, Valor)
capacidade = 70  # Capacidade máxima da mochila

# Chamando a função
resultado = mochila_gulosa(capacidade, itens)

print("Valor máximo possível na mochila:", resultado)
