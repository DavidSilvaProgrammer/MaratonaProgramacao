#S(1) = 1
#S(2k) = 2S(k) − 1    =   n = 2k
#S(2k + 1) = 2S(k) + 1  =  n = 2k+1
#Case 1: 3

m=0

NC = int(input())

for i in range(NC):
    n, k = map(int, input().split())
    if n == 1:
        print(f"Case {NC}: 1")
    else:
        if n % 2 == 0:
            m = n%(2*k-1)
            print(f"Case {NC}: {m}")
        else:
            if n % 2 == 0:
                m = n%(2*k+1)
                print(f"Case {NC}: {m}")

        
    
