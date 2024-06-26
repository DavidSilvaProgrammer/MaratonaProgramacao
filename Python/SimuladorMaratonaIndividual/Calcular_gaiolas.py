def calcular_gaiolas(meses):
    casais = [1, 1]  # Inicialmente, temos um casal no primeiro mês e outro no segundo mês
    gaiolas = 1  # Iniciamos com uma gaiola
    
    for i in range(2, meses):
        novos_casais = casais[i - 1]  # Novos casais são iguais ao número de casais do mês anterior
        total_casais = casais[i - 1] + casais[i - 2]  # Total de casais é a soma dos casais dos dois meses anteriores
        casais.append(total_casais)
        
        # Verifica se é necessário uma nova gaiola
        if total_casais > gaiolas * 5:
            gaiolas += 1
    
    return casais[-1], gaiolas

meses = 6  # Altere para o número de meses desejado
casais_final, gaiolas_final = calcular_gaiolas(meses)
print(f"Após {meses} meses, haverá um total de {casais_final} casais de animais, requerendo {gaiolas_final} gaiolas.")



'''

Claro! Vou explicar a lógica passo a passo:

    Inicialização:
        Começamos com dois casais de animais: um casal no primeiro mês e outro no segundo mês, como especificado.
        Também iniciamos com uma única gaiola.

    Loop para cada mês após o segundo mês:
        Começamos o loop a partir do terceiro mês, já que nos dois primeiros meses já temos os casais iniciais.
        Para cada mês, calculamos o número de novos casais que serão produzidos. Isso é simplesmente o número de casais do mês anterior.
        Calculamos o total de casais para o mês atual, que é a soma dos casais do mês anterior e do mês retrasado.
        Adicionamos o total de casais calculado para o mês atual à lista de casais.

    Verificação de novas gaiolas:
        Verificamos se o número total de casais ultrapassou a capacidade atual de gaiolas (que abriga 5 casais cada).
        Se for necessário uma nova gaiola, incrementamos o contador de gaiolas.

    Resultado:
        Após o loop, temos a lista completa de casais em cada mês e o número total de gaiolas necessário para abrigá-los.

Espero que isso esclareça a lógica por trás do algoritmo!


########

Entendido! Vamos calcular a quantidade de casais de animais e o número de gaiolas necessárias com base nos pressupostos fornecidos:

    No primeiro mês, há apenas um casal.
    No segundo mês, esse casal atinge a maturidade sexual e pode produzir um novo casal.
    A partir do terceiro mês, cada casal existente produz um novo casal a cada mês.

Vamos criar uma tabela para visualizar melhor isso:

Mês	Casais	Novos Casais	Total Casais	Gaiolas
1	1	0	1	1
2	1	1	2	1
3	2	1	3	1
4	3	2	5	1
5	5	3	8	2
6	8	5	13	3


Você pode ajustar o valor de meses conforme necessário. Esse código calculará o número final de casais de animais 
e o número de gaiolas necessárias para abrigá-los após o número especificado de meses.


'''
