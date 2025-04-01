import random
import math

def calcular_distancia(caminho, matriz_distancias):
    return sum(matriz_distancias[caminho[i-1]][caminho[i]] for i in range(len(caminho)))

# matriz = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

def simulated_annealing(matriz_distancias, temperatura=1000, resfriamento=0.99):
    num_cidades = len(matriz_distancias)
    caminho_atual = list(range(num_cidades))
    random.shuffle(caminho_atual)
    melhor_caminho = caminho_atual[:]
    melhor_distancia = calcular_distancia(melhor_caminho, matriz_distancias)

    while temperatura > 1:
        i, j = sorted(random.sample(range(num_cidades), 2))  
        novo_caminho = caminho_atual[:]
        novo_caminho[i:j] = reversed(novo_caminho[i:j])  # Faz uma pequena alteração no caminho

        nova_distancia = calcular_distancia(novo_caminho, matriz_distancias)
        if nova_distancia < melhor_distancia or random.random() < math.exp((melhor_distancia - nova_distancia) / temperatura):
            caminho_atual = novo_caminho[:]
            melhor_distancia = nova_distancia
            melhor_caminho = caminho_atual[:]

        temperatura *= resfriamento  # Reduz a temperatura

    return melhor_caminho, melhor_distancia

# Exemplo: Matriz de distâncias entre 4 cidades
matriz = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0],
    [20, 25, 30, 0]
]

rota, distancia = simulated_annealing(matriz)
print("Melhor Rota:", rota)
print("Distância Total:", distancia)
