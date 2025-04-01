def devolver_troco(valor, moedas):
    moedas.sort(reverse=True)
    resultado = {}
    for moeda in moedas:
        if valor >= moeda:
            resultado[moeda] = valor // moeda
            valor %= moeda
            # valor = 63 e usamos 1 moeda de 50, o 63 %= 50 = 13
    return resultado

moedas = [1, 5, 10, 25, 50]
valor =63
print(devolver_troco(valor, moedas))
    
# 63 // 50 = 1 => sobrar 13
# 25 => 13 não
# 10 --- 13 // 10 => sobra 3
# 5 => 3 não
# 1 --- 3 // 1 = 3 vamos usar 3 moedas de 1 centavo