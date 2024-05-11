import sys

def get_input():
    return map(int, sys.stdin.readline().split())

N, Q = get_input()
lista_notas = [1] * N
contadores = {}

for _ in range(Q):
    A, B = get_input()
    for i in range(A, B + 1):
        if (A, B) not in contadores:
            contadores[(A, B)] = {}
        lista_notas[i] += 1
        contadores[(A, B)][lista_notas[i]] = contadores[(A, B)].get(lista_notas[i], 0) + 1

for intervalo, contador in contadores.items():
    moda = max(contador, key=contador.get)
    A, B = intervalo
    for i in range(A, B + 1):
        lista_notas[i] = (lista_notas[i] + moda) % 9

for nota in lista_notas:
    print(nota)
