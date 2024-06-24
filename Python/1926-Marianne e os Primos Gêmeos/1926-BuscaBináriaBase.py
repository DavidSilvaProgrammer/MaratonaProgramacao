# Lista ordenada de números primos gêmeos
numeros_primos_gemeos = [
    3, 5, 5, 7, 11, 13, 17, 19, 29, 31,
    41, 43, 59, 61, 71, 73, 101, 103, 107, 109,
    137, 139, 149, 151, 179, 181, 191, 193, 197, 199,
    227, 229, 239, 241, 269, 271, 281, 283, 311, 313,
    347, 349, 419, 421, 431, 433, 461, 463, 521, 523,
    569, 571, 599, 601, 617, 619, 641, 643, 659, 661,
    809, 811, 821, 823, 827, 829, 857, 859, 881, 883,
    1019, 1021, 1031, 1033, 1049, 1051, 1061, 1063
]

# Função de busca binária para verificar se um número está na lista
def busca_binaria(lista, numero):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == numero:
            return True
        elif lista[meio] < numero:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False

# Função para contar números primos gêmeos no intervalo [x, y]
def contar_numeros_primos_gemeos(x, y):
    count = 0
    for num in range(x, y + 1):
        if busca_binaria(numeros_primos_gemeos, num):
            count += 1
    return count

# Função principal para solicitar entrada do usuário e realizar a contagem
def main():
    try:
        x = int(input("Digite o valor de x (inicio do intervalo): "))
        y = int(input("Digite o valor de y (fim do intervalo): "))
        if x > y:
            print("Intervalo inválido. x deve ser menor ou igual a y.")
            return
        quantidade = contar_numeros_primos_gemeos(x, y)
        print(f"A quantidade de números primos gêmeos no intervalo [{x}, {y}] é: {quantidade}")
    except ValueError:
        print("Entrada inválida. Por favor, digite números inteiros.")

# Executar a função principal
if __name__ == "__main__":
    main()
