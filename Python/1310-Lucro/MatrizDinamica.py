def preencher_matriz():
    matriz = []
    linhas = int(input("Digite o número de linhas da matriz: "))
    colunas = int(input("Digite o número de colunas da matriz: "))
    
    for i in range(linhas):
        linha = []
        print(f"Preencha os elementos da linha {i + 1}:")
        for j in range(colunas):
            elemento = int(input(f"Digite o elemento da coluna {j + 1}: "))
            linha.append(elemento)
        matriz.append(linha)
    
    return matriz

def imprimir_matriz(matriz):
    print("Matriz:")
    for linha in matriz:
        print(linha)

# Preencher a matriz
matriz = preencher_matriz()

# Imprimir a matriz
imprimir_matriz(matriz)


####################
