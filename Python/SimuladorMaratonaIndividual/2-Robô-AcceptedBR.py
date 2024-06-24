# Receber o tamanho da matriz (número de linhas e colunas)
n, m = map(int, input().split())
start_i, start_j = map(int, input().split())

# Criar a matriz
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

# Função para encontrar o próximo movimento válido
def encontrar_proximo_movimento(i, j, visitados):
    # Verificar movimentos possíveis: cima, baixo, esquerda, direita
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for di, dj in direcoes:
        ni, nj = i + di, j + dj
        if 0 <= ni < n and 0 <= nj < m:  # dentro dos limites da matriz
            if matriz[ni][nj] == 1 and (ni, nj) not in visitados:  # movimento válido
                return ni, nj
    return None  # nenhum movimento válido encontrado

# Iniciar a busca a partir da posição inicial
posicao_atual_i, posicao_atual_j = start_i - 1, start_j - 1  # ajustar para índices base 0
visitados = set()
visitados.add((posicao_atual_i, posicao_atual_j))

while True:
    proximo_movimento = encontrar_proximo_movimento(posicao_atual_i, posicao_atual_j, visitados)
    if proximo_movimento is None:
        break
    posicao_atual_i, posicao_atual_j = proximo_movimento
    visitados.add((posicao_atual_i, posicao_atual_j))

# Ao final, imprimir a posição final do robô
print(f"{posicao_atual_i + 1} {posicao_atual_j + 1}")  # ajustar para índices base 1
