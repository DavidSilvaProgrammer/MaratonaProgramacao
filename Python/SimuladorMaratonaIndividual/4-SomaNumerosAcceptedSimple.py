calcula=0
n=-2
menosUm=False
while n != 0:
    n=int(input())
    if n == -1 and menosUm == False:
        menosUm=True
        continue
    if n == -1 and menosUm == True:
        menosUm=False
        continue
    
    if menosUm == False:
        calcula+=n 
    else:
        calcula-=n 

    
print(calcula)
        
    
