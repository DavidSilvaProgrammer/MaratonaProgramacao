def decimal_para_octal(decimal):
    if decimal == 0:
        return ""
    else:
        resto = decimal % 8
        quociente = decimal // 8
        return decimal_para_octal(quociente) + str(resto)


numeros = []
while True:
    num = int(input().strip())
    if num == 0:
        break
    numeros.append(num)

for num_decimal in numeros:
    octal_str = decimal_para_octal(num_decimal)
    if octal_str == "":
        octal_str = "0"
    soma_parcelas = sum(int(digito) for digito in octal_str)
    print(soma_parcelas)


'''

Explicações das Alterações:

    Função decimal_para_octal(decimal) Recursiva:
        A função decimal_para_octal() agora usa recursão para converter um número decimal em 
        sua representação octal.
        Ela baseia-se na ideia de dividir o número decimal por 8 repetidamente até que o 
        quociente seja zero, construindo assim a representação octal a partir 
        dos restos das divisões.

    Condição Base e Passo Recursivo:
        Se o número decimal fornecido for zero, a função retorna uma string vazia "".
        Caso contrário, a função calcula o resto da divisão por 8 (resto) e chama 
        recursivamente a si mesma com o quociente da divisão inteira por 8 (quociente), 
        concatenando o resto convertido em string.

    Função main() Atualizada:
        A função main() permanece essencialmente a mesma, com exceção de verificar 
        se octal_str está vazia (caso o número seja zero, para o qual a função recursiva 
        retorna "") e atribuir "0" nesse caso para corrigir a representação octal.

'''
