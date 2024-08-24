x=-1
y=-1
lista_x=[]
lista_y=[]

while x != 0 and y != 0:
    x, y = map(int, input().split())
    print(x)
    print(y)
    for i in range(1,1,x+1):
        lista_x.append(i)
    print(lista_x)
    for i in range(1,1,y+1):
        lista_x.append(y)
    print(lista_y)
