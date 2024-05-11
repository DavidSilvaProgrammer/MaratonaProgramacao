# Dicionário de contagem de caracteres
contagem = {'a': 2, 'b': 3, 'c': 1}

# Valor a ser rastreado
valor = 3

# Verifica se o valor está presente nos valores do dicionário
if valor in contagem.values():
    print(f'O valor {valor} está presente nos valores do dicionário.')
else:
    print(f'O valor {valor} não está presente nos valores do dicionário.')
