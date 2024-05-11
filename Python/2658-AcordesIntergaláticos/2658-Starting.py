import statistics

N, Q = map(int, input().split())
f=0
lista_notas = [1] * N

conta= {}

for i in range(Q):
    A, B = map(int, input().split())
    lista_intervalo = lista_notas[A:B]
    moda_intervalo = statistics.mode(lista_intervalo)
    
    
    
    
        for k in range(A,B):
            if k in conta:
                conta[k] +=1:
            else:
                conta[k]=1
        
        
    
