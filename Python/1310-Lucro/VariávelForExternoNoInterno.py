lista = [1, 2, 3, 4, 5, 6, 7]

for i in range(len(lista)):
    print(f"Posição atual do primeiro loop: {i}")
    print("Elementos registrados no segundo loop:")
    for j in range(i + 1, len(lista)):
        print(lista[j])
    print()


'''
Neste exemplo, o primeiro loop for itera sobre todos os índices da lista. Dentro dele, o segundo loop 
for começa do próximo índice após o índice atual do primeiro loop e itera até o final da lista, 
registrando cada elemento encontrado. Isso garante que apenas os elementos que aparecem após a 
posição atual do contador do primeiro loop sejam registrados no segundo loop.

Você pode ajustar o que fazer com esses elementos registrados dentro do segundo loop, dependendo 
dos requisitos do seu programa. Neste exemplo, estou apenas imprimindo-os, mas você pode armazená-los 
em outra lista, processá-los de alguma outra forma, etc.
'''
