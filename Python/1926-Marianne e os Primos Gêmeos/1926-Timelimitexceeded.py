from math import sqrt

def e_primo(numero):
    if numero <= 1:
        return False
    for j in range(2, int(sqrt(numero)) + 1):
        if numero % j == 0:
            return False
    return True

def contar_primos_gemeos(lista_primos, k, p):
    contador = 0
    for i in range(len(lista_primos) - 1):
        if lista_primos[i] >= k and lista_primos[i + 1] <= p and lista_primos[i + 1] - lista_primos[i] == 2:
            contador += 1
    return contador

# Definindo um valor máximo fixo para a busca de primos
MAXIMA_BUSCA_PRIMOS = 10**6

# Realizando a busca de primos até o valor máximo fixo
primos = []
for num in range(2, MAXIMA_BUSCA_PRIMOS + 1):
    if e_primo(num):
        primos.append(num)
    
N = int(input())
for _ in range(N):
    k, p = map(int, input().split())
    quantidade_primos_gemeos = contar_primos_gemeos(primos, k, p)
    print(quantidade_primos_gemeos+1)
