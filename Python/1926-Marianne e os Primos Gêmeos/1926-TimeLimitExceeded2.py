from math import sqrt

# Função para verificar se um número é primo
def eh_primo(num):
    if num <= 1:
        return False
    for j in range(2, int(sqrt(num)) + 1):
        if num % j == 0:
            return False
    return True

# Função para contar números gêmeos primos entre x e y
def contar_numeros_gemeos_primos(x, y):
    count = 0
    for num in range(x, y - 1):
        if eh_primo(num) and eh_primo(num + 2):
            count += 1
    return count

# Ler o número de casos de teste
N = int(input("Digite o número de casos de teste: "))

# Processar cada caso de teste
for _ in range(N):
    x, y = map(int, input().split())
    if x >= y:
        print("Entrada inválida: x deve ser menor que y")
        continue
    num_numeros_gemeos_primos = contar_numeros_gemeos_primos(x, y)
    print(num_numeros_gemeos_primos)

'''


Explicação:

    Função eh_primo: Esta função verifica se um número dado é primo, seguindo a lógica do código original.

    Função contar_numeros_gemeos_primos: Esta nova função conta o número de números gêmeos primos 
    entre xx e yy. Ela itera por cada número no intervalo de xx até y−1y−1 (inclusive) e verifica 
    se tanto o número quanto o número mais dois são primos. Se forem, incrementa o contador.

    Tratamento de Entrada:
        Primeiro, lemos o número de casos de teste NN.
        Para cada caso de teste, lemos xx e yy da entrada. Supomos que xx e yy sejam inseridos 
        na mesma linha e separados por espaço.
        Em seguida, chamamos contar_numeros_gemeos_primos(x, y) para obter o número de 
        números gêmeos primos entre xx e yy.
        Por fim, imprimimos o resultado para cada caso de teste.

    Tratamento de Casos Especiais:
        Garantimos que xx seja menor que yy. Se não for, exibimos uma mensagem de erro e 
        pulamos aquele caso de teste.

Este código modificado deve agora contar e imprimir corretamente o número de números gêmeos 
primos para cada caso de teste conforme especificado. Ajustes adicionais podem ser feitos 
dependendo de requisitos específicos ou restrições adicionais.
'''
