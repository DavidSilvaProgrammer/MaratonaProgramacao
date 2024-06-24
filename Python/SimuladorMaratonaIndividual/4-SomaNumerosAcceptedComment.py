calcula = 0  # Inicializa a variável 'calcula' com zero.
n = -2  # Inicializa a variável 'n' com -2 para não interferir no inicio do while.
menosUm = False  # Inicializa a variável booleana 'menosUm' como falso.

while n != 0:
    n = int(input())  # Lê um valor inteiro do usuário.
    
    # Verifica se o usuário digitou -1 e se 'menosUm' é falso.
    if n == -1 and not menosUm:
        menosUm = True
        continue  # Pula para a próxima iteração do loop.
    
    # Verifica se o usuário digitou -1 e se 'menosUm' é verdadeiro.
    if n == -1 and menosUm:
        menosUm = False
        continue  # Pula para a próxima iteração do loop.
    
    # Se 'menosUm' for verdadeiro, subtrai 'n' do cálculo.
    if menosUm:
        calcula -= n
    
    # Se 'menosUm' for falso, adiciona 'n' ao cálculo.
    else:
        calcula += n

# Imprime o resultado final.
print(calcula)
