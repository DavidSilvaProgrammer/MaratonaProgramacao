lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

lista1.extend(lista2)

print(lista1)  # Output: [1, 2, 3, 4, 5, 6]


##############

O método extend() é usado para adicionar os elementos de uma lista (ou qualquer iterável) 
ao final de outra lista. Ele modifica a lista original, adicionando os elementos do iterável 
fornecido como argumento.

Neste código, extend() adiciona os elementos da lista2 ao final da lista1, 
resultando em uma única lista contendo todos os elementos de ambas as listas.
