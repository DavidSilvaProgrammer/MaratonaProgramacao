def contar_ocorrencias(lista):
    # Criando uma tabela hash para contar as ocorrências de cada elemento
    contador = {}

    # Iterando sobre os elementos da lista
    for elemento in lista:
        # Verificando se o elemento já está na tabela hash
        if elemento in contador:
            # Incrementando o contador se o elemento já existe na tabela hash
            contador[elemento] += 1
        else:
            # Inicializando o contador para o elemento se ele ainda não estiver na tabela hash
            contador[elemento] = 1

    return contador

# Lista de elementos
lista = [1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# Contando as ocorrências de cada elemento na lista
ocorrencias = contar_ocorrencias(lista)

# Exibindo o resultado
for elemento, quantidade in ocorrencias.items():
    print(f'O elemento {elemento} ocorre {quantidade} vezes na lista.')



**********************

Neste exemplo, a tabela hash (dicionário em Python) é usada para armazenar 
as contagens de cada elemento da lista. Isso permite que as contagens sejam 
atualizadas em tempo constante, independentemente do tamanho da lista, 
resultando em um tempo de execução mais eficiente em comparação com uma 
abordagem linear que teria uma complexidade de tempo de O(n^2).
