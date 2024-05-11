# Lista de caracteres
lista = ['a', 'b', 'c', 'a', 'b', 'a', 'd']

# Dicionário para armazenar a contagem de cada caractere
contagem = {}

# Percorre a lista e conta a repetição de cada caractere
for caractere in lista:
    contagem[caractere] = lista.count(caractere)

# Exibe a contagem de repetição de cada caractere
for caractere, repeticao in contagem.items():
    print(f'O caractere "{caractere}" aparece {repeticao} vezes na lista.')
