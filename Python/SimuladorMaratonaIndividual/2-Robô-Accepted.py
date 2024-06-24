# Receber o tamanho da matriz (número de linhas e colunas)
n, m = map(int, input().split())
start_i, start_j = map(int, input().split())

# Criar a matriz
matriz = []
for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

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
current_i, current_j = start_i - 1, start_j - 1  # ajustar para índices base 0
visited = set()
visited.add((current_i, current_j))

while True:
    next_move = find_next_move(current_i, current_j, visited)
    if next_move is None:
        break
    current_i, current_j = next_move
    visited.add((current_i, current_j))

# Ao final, imprimir a posição final do robô
print(f"{current_i + 1} {current_j + 1}")  # ajustar para índices base 1


'''
Para transformar o código em uma versão que funcione sem o if __name__ == "__main__":, 
você pode simplesmente remover essa verificação e manter o código da função main() no 
nível superior do script. No entanto, é importante ter em mente que isso fará com que todo o 
código seja executado sempre que o script for importado por outro módulo. 


Considerações:

    Execução direta: Agora, todo o código será executado sempre que o script for chamado diretamente 
pelo interpretador Python (python script.py).

    Importação por outros módulos: Se você importar este script em outro módulo (import script), 
todo o código, incluindo a leitura de entrada e a execução da lógica do robô, será executado 
imediatamente.

    Modularidade: Essa abordagem pode comprometer a modularidade do seu código, pois não há 
separação explícita entre a definição das funções, a leitura de entrada e a execução da lógica 
principal.

    Organização: Se você precisar manter a estrutura organizada e modular, ainda é recomendado 
usar if __name__ == "__main__": para encapsular a execução principal dentro da função main(), 
permitindo que o código seja reutilizado facilmente como um módulo por outros scripts sem executar 
a lógica principal automaticamente.

Portanto, embora seja possível executar o script sem if __name__ == "__main__":, é uma prática 
recomendada manter essa construção para promover uma estrutura mais organizada e modular do código 
Python.
'''
