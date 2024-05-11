from math import sqrt

N = int(input())
for _ in range(N):
    X = int(input())
    is_prime = True
    if X <= 1:
        is_prime = False
    else:
        for j in range(2, int(sqrt(X)) + 1):
            if X % j == 0:
                is_prime = False
                break
    
    if is_prime:
        print("Prime")
    else:
        print("Not Prime")
