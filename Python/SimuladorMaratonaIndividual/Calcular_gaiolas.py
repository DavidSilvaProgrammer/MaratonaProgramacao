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
