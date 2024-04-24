Boa tarde, colegas e professor. Consegui a aprovação no Beecrowd para a 1105 em Python. Vou postar.


while True:
    try:
        B, N, *_ = map(int, input().split())
        
    except ValueError:
        break
    
    if B == 0 and N == 0:
        break
    
    R = list(map(int, input().split()))

    if len(R) != B or any(0 > valor > 10**4 for valor in R):
        break
    for _ in range(N):
        try:
            D, C, V = map(int, input().split())
        except ValueError:
            break
        
        D-=1
        C-=1
        if D < 0 or D > B-1 or C < 0 or C > B-1:
            break
        
        R[D] -= V
        R[C] += V
        
    
  
    for i in range(B):
        if R[i] < 0:
            print("N")
            break
    else:  
        print("S")



Primeiro criei um loop while infinito para o código. Utilizei o método split para receber 
os valores de B e N em uma única linha com a função map para converter esses valores de 
strings para inteiros. Combinei isso com o tratamento de exceção para ValueError, 
que é acionado caso o valor recebido não possa ser convertido para um número inteiro. 
Também criei um if para dar um break no programa caso B e N sejam 0.

Obs: O '*_' serve para descartar valores além do necessário para as duas variáveis.

Depois disso, utilizei novamente o método split junto com map, mas dessa vez com a função list 
para criar uma lista com os elementos sendo inseridos nela tudo em uma única linha.

Em seguida, utilizei outro if para interromper o programa caso a quantidade de elementos 
na lista de reservas seja maior que a quantidade de B bancos, como solicitado pelo enunciado.

Também incluí nesse if, após o or, as restrições que garantem que os valores dos elementos 
de R não sejam menores que zero ou maiores que 10.000. Fiz isso usando a função any() 
que está retornando verdadeiro se houver qualquer valor em R que viole essas regras, 
assim ocorre um break no programa.

Após essa parte, criei outro loop for com range para lidar com as operações de debêntures 
N vezes e coloquei outro tratamento de exceção para ValueError.

Também está sendo verificado nesse loop por um if os critérios solicitados pelo enunciado 
de que C e D não podem ser menores que 0 ou maiores que a quantidade de B bancos, 
justamente para não que não ultrapassem o valor máximo do índice da lista R. 
Depois disso, ocorrem as operações de soma e subtração.

Obs: Antes das comparações do if, reduzi os valores das variáveis C e D em 1 para 
alinhar com o índice da lista R. Também fiz isso com o B no if para poder comparar com C e D.

Por fim, outro loop for com a função range, para percorrer a lista de reserva R e verificar 
se algum banco possui reserva negativa. 

Caso exista, o programa imprime "N" e dá um break. 
Caso contrário, o else após o loop é  acionado e imprime "S".

Agora vou tentar resolver os outros problemas.
