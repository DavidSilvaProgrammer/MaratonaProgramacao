from math import sqrt

def is_prime(number):
    if number <= 1:
        return False
    for j in range(2, int(sqrt(number)) + 1):
        if number % j == 0:
            return False
    return True

def prime_twins_count(primes_list, k, p):
    count = 0
    for i in range(len(primes_list) - 1):
        if primes_list[i] >= k and primes_list[i + 1] <= p and primes_list[i + 1] - primes_list[i] == 2:
            count += 1
    return count

# Definindo um valor máximo fixo para a busca de primos
MAX_PRIME_SEARCH = 10**6

# Realizando a busca de primos até o valor máximo fixo
primes = []
for num in range(2, MAX_PRIME_SEARCH + 1):
    if is_prime(num):
        primes.append(num)
    
N = int(input("Digite o número de consultas: "))
for _ in range(N):
    k, p = map(int, input("Digite o intervalo [k, p] para a consulta: ").split())
    twins_count = prime_twins_count(primes, k, p)
    print(f"A quantidade de primos gêmeos no intervalo [{k}, {p}] é: {twins_count}")
