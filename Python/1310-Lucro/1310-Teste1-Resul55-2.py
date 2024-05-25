n = int(input())
custoPorDia = int(input())

receita=[]

for i in range(n):
    receita.append(int(input()))
    
soma=0
for i in range(n):
    soma+=receita[i]
    
soma -= custoPorDia*n

print(soma)
