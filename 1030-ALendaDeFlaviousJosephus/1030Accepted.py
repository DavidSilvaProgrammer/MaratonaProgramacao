# Lê o número de casos de teste
NC = int(input())

# Para cada caso de teste
for caso in range(1, NC + 1):
    # Lê os valores de n e k
    n, k = map(int, input().split())
    
    # Inicializa m como 0 (valor inicial arbitrário)
    m = 0
    sobrevivente = 0
    
    # Começa o processo de eliminar pessoas do círculo
    for i in range(2, n + 1):
        m = (m + k) % i
    
    # Calcula a posição do sobrevivente
    sobrevivente = m + 1
    
    # Imprime o resultado no formato solicitado
    print(f"Case {caso}: {sobrevivente}")
