def decimal_para_octal(decimal):
    if decimal == 0:
        return "0"
    
    octal = ""
    while decimal > 0:
        resto = decimal % 8
        octal = str(resto) + octal
        decimal //= 8
    
    return octal


numeros = []
while True:
    num = int(input().strip())
    if num == 0:
        break
    numeros.append(num)

for num_decimal in numeros:
    octal_str = decimal_para_octal(num_decimal)
    soma_parcelas = sum(int(digito) for digito in octal_str)
    print(soma_parcelas)

'''
xplicação da Implementação:

    Função decimal_para_octal(decimal):
        Esta função converte um número decimal em sua representação octal. Ela usa um loop 
        while para dividir o número decimal por 8 repetidamente, capturando os restos e 
        construindo o número octal da direita para a esquerda.

    Função main():
        No início, inicializa uma lista numeros para armazenar os números decimais fornecidos.
        Usa um loop para ler números decimais até que o número 0 seja inserido, 
        indicando o fim da entrada.
        Para cada número decimal lido, calcula sua representação octal usando a 
        função decimal_para_octal() e em seguida calcula a soma das parcelas octais.
        Imprime a soma das parcelas octais para cada número decimal processado.

'''
