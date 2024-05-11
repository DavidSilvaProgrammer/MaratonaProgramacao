import statistics

N, Q = map(int, input().split())
f=0
lista_notas = [1] * N

print(lista_notas)

for i in range(Q):
    A, B = map(int, input().split())
    lista_intervalo = lista_notas[A:B]
    print(lista_intervalo)
    f = statistics.mode(lista_intervalo)
    print(f)
    
    for i in range(A,B):
        lista_notas[i]=(lista_notas[i]+f)%9
        print(lista_notas[i])
print(lista_notas)



Quando você calcula lista_intervalo = lista_notas[A:B], isso não retorna uma nova lista contendo as notas 
dentro do intervalo [A, B). Em vez disso, ele retorna uma "fatia" da lista lista_notas, 
que é uma visão dos elementos da lista original. Isso significa que qualquer alteração feita em lista_intervalo 
também afetará lista_notas.

Portanto, ao modificar lista_intervalo dentro do loop for i in range(A, B):, você também estará alterando lista_notas, 
o que não é desejado.

Para resolver isso, você deve criar uma cópia da lista lista_intervalo antes de fazer qualquer modificação. 
Você pode fazer isso usando a função list() para criar uma nova lista com os mesmos elementos de lista_intervalo.


import statistics

N, Q = map(int, input().split())
lista_notas = [1] * N

for _ in range(Q):
    A, B = map(int, input().split())
    lista_intervalo = lista_notas[A:B+1]  # Inclui B
    f = statistics.mode(lista_intervalo)
    
    for i in range(A, B+1):  # Inclui B
        lista_notas[i] = (lista_notas[i] + f) % 9

print(*lista_notas)
