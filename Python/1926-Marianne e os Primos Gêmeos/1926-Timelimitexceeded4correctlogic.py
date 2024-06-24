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
    lista=[]
    conjunto=0
    quant=0
    for num in range(x, y):
        if eh_primo(num) and eh_primo(num + 2):
            lista.append(num)
            if num < y-2:
                lista.append(num+2)
    
    conjunto=set(lista)
    quant=len(conjunto)
    
    return quant

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
