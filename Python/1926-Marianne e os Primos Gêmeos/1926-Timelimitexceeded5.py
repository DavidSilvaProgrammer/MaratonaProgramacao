from math import isqrt

# Função para verificar se um número é primo
def eh_primo(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
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
    num_numeros_gemeos_primos = contar_numeros_gemeos_primos(x, y + 1)  # y + 1 para incluir y
    print(num_numeros_gemeos_primos)
