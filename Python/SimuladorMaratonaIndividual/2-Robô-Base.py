def main():
    # Receber o tamanho da matriz (número de linhas e colunas)
    n = int(input("Digite o número de linhas da matriz: "))
    m = int(input("Digite o número de colunas da matriz: "))
    
    # Criar a matriz
    matriz = []
    print("Digite a matriz (separe os valores por espaço):")
    for i in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    
    # Receber a posição inicial do robô
    print("Digite a posição inicial do robô (linha coluna):")
    start_i, start_j = map(int, input().split())
    
    # Função para encontrar o próximo movimento válido
    def find_next_move(i, j, visited):
        # Verificar movimentos possíveis: cima, baixo, esquerda, direita
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:  # dentro dos limites da matriz
                if matriz[ni][nj] == 1 and (ni, nj) not in visited:  # movimento válido
                    return ni, nj
        return None  # nenhum movimento válido encontrado
    
    # Iniciar a busca a partir da posição inicial
    current_i, current_j = start_i, start_j
    visited = set()
    visited.add((current_i, current_j))
    
    while True:
        next_move = find_next_move(current_i, current_j, visited)
        if next_move is None:
            break
        current_i, current_j = next_move
        visited.add((current_i, current_j))
    
    # Ao final, imprimir a posição final do robô
    print(f"Posição final do robô: ({current_i}, {current_j})")

if __name__ == "__main__":
    main()
