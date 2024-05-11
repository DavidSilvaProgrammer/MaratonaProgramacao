from collections import defaultdict

N, Q = map(int, input().split())
lista_notas = [1] * N

# Dicionário para armazenar as frequências pré-calculadas dos intervalos
frequencias = defaultdict(dict)

# Pré-calcular as frequências para todos os intervalos possíveis
for A in range(N):
    for B in range(A, N):
        for i in range(A, B + 1):
            lista_notas[i] = (lista_notas[i] + 1) % 9
        moda = max(set(lista_notas[A:B + 1]), key=lista_notas[A:B + 1].count)
        frequencias[A][B] = moda

# Executar as iterações
for _ in range(Q):
    A, B = map(int, input().split())
    moda = frequencias[A][B]
    
    # Atualizar os valores da lista_notas com base na moda calculada
    for i in range(A, B + 1):
        lista_notas[i] = (lista_notas[i] + moda) % 9

# Imprimir o resultado
for nota in lista_notas:
    print(nota)
