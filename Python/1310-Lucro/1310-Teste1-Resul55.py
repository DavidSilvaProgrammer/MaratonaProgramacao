n = int(input())
custoPordia = int(input())

receita=[]

for i in range(n):
    receita.append(int(input()) - custoPordia)
    
soma=0
for i in range(n):
    soma+=receita[i]

print(soma)
