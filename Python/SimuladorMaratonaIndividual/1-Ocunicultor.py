import math

def calculaCasal(m):
    #no primeiro mês, há apenas um casal e nasce somente um casal
    casais = [1, 1]
    total_casais = 0
    gaiolas = 0
    total =2;
    for i in range(2, m):
        
        #sempre vai nascer a quantidade de casais
        #com o mesmo valor da soma dos 2 
        #meses anteriores
        
        total_casais = casais[i - 1] + casais[i - 2] 
        
        #incrementa a a lista com a quantidade de casais do mês
        casais.append(total_casais)
        
    
    gaiolas = math.ceil(total_casais/5)

    
    

    print(f"{total_casais} {gaiolas} ")
            
        
n = int(input())
for i in range(n):
    m = int(input())
    calculaCasal(m)

    
