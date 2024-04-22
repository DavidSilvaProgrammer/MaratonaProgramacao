while True:
    try:
        B, N, *_ = map(int, input().split())
        
    except ValueError:
        break
    
    if B == 0 and N == 0:
        break
    
    R = list(map(int, input().split()))
    
    if len(R) != B or not all(0 <= val <= 10**4 for val in R):
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

# not all(0 <= val <= 10**4 for val in R): 
#Esta parte verifica se todos os valores em R 
#estão dentro do intervalo permitido de 0 a 104104. 
#Aqui, all() é uma função que verifica se todos os elementos 
#de um iterável são verdadeiros. 0 <= val <= 10**4 for val in R é 
#uma expressão geradora que verifica se todos os valores em R estão dentro 
#do intervalo permitido. O not antes disso inverte o resultado, então se qualquer 
#valor em R estiver fora do intervalo, a expressão como um todo será verdadeira.
