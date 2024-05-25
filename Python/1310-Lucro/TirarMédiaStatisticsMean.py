def calcular_media(lista):
    if len(lista) == 0:
        return 0  # Retorna 0 se a lista estiver vazia para evitar divisão por zero
    soma = sum(lista)  # Calcula a soma dos elementos da lista
    media = soma / len(lista)  # Calcula a média
    return media

# Exemplo de uso:
valores = [10, 20, 30, 40, 50]
media = calcular_media(valores)
print("A média dos valores é:", media)

#################

from statistics import mean

valores = [10, 20, 30, 40, 50]
media = mean(valores)
print("A média dos valores é:", media)
