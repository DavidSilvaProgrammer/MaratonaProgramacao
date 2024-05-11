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




################################

A linha de código if caractere in contagem: verifica se a chave caractere está presente 
no dicionário contagem. Em outras palavras, ela verifica se o dicionário já possui uma entrada 
para o caractere atual.

Se o caractere já estiver presente no dicionário contagem, isso significa que ele já foi 
encontrado anteriormente na lista e sua contagem de repetição já está sendo rastreada. 
Nesse caso, o programa incrementa o valor da contagem para esse caractere em 1.

Se o caractere não estiver presente no dicionário contagem, isso significa que ele ainda 
não foi encontrado anteriormente na lista. Nesse caso, o programa cria uma nova entrada 
no dicionário para o caractere e define sua contagem inicial como 1.

Essa linha de código é uma maneira de verificar se um caractere já foi encontrado 
antes na lista e, se sim, atualizar sua contagem de repetição; ou, se não, iniciar 
uma nova contagem para esse caractere.

