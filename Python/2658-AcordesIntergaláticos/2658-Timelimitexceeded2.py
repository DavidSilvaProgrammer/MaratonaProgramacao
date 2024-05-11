import statistics

N, Q = map(int, input().split())
lista_notas = [1] * N

if Q == 0:
    lista_notas = [2] * N
else:
    for j in range(Q):
        A, B = map(int, input().split())
        lista_intervalo = lista_notas[A:B + 1]
        if j == 0:
            f = 1  
        else:
            f = statistics.mode(lista_intervalo)
        for i in range(A, B + 1):  # Inclui B
            lista_notas[i] = (lista_notas[i] + f) % 9

for i in range(N):
    print(lista_notas[i])
