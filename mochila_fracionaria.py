def mochila_fracionaria(capacidade, itens):
    itens.sort(key=lambda x: x[1] / x[0], reverse=True)  # Ordena por valor/peso
    #  Item     Peso     valor     Valor/Peso
    #   A       10        60       6.0
    #   B       20        100      5.0
    #   C       30        120      4.0
    valor_total = 0
    peso_atual = 0

    for peso, valor in itens:
        if peso_atual + peso <= capacidade:
            peso_atual += peso
            valor_total += valor
        else:
            fracao = (capacidade - peso_atual) / peso  # Pegamos parte do item
            valor_total += valor * fracao
            break  # Mochila cheia

        # 30 kg na mochila
        # 20/30 = 0.6667
        # 120 * 0.6667 = 80

    return valor_total

# Exemplo de uso
itens = [(10, 60), (20, 100), (30, 120)]  # (peso, valor)
capacidade = 50
# 10 + 20 = 30

print("Valor máximo:", mochila_fracionaria(capacidade, itens))
