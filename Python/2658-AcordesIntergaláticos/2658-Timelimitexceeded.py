import statistics

N, Q = map(int, input().split())
lista_notas = [1] * N

for _ in range(Q):
    A, B = map(int, input().split())
    lista_intervalo = lista_notas[A:B+1]
    f = statistics.mode(lista_intervalo)
    
    for i in range(A, B+1):  # Inclui B
        lista_notas[i] = (lista_notas[i] + f) % 9

for i in range(N):
    print(lista_notas[i])
