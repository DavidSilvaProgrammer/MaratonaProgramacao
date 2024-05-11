# Lista de caracteres
lista = ['a', 'b', 'c', 'a', 'b', 'a', 'd']

# Dicionário para armazenar a contagem de cada caractere
contagem = {}

# Percorre a lista e conta a repetição de cada caractere
for caractere in lista:
    if caractere in contagem:
        contagem[caractere] += 1
    else:
        contagem[caractere] = 1

# Exibe a contagem de repetição de cada caractere
for caractere, repeticao in contagem.items():
    print(f'O caractere "{caractere}" aparece {repeticao} vezes na lista.')
 
################ Código semelhante ##################

# Lista de números inteiros
lista = [1, 2, 3, 4, 2, 1, 3, 4, 5, 5, 5]

# Dicionário para armazenar a contagem de cada número
contagem = {}

# Percorre a lista e conta a repetição de cada número
for numero in lista:
    if numero in contagem:
        contagem[numero] += 1
    else:
        contagem[numero] = 1

# Exibe a contagem de repetição de cada número
for numero, repeticao in contagem.items():
    print(f'O número "{numero}" aparece {repeticao} vezes na lista.')

