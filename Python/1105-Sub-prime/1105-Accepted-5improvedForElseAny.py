while True:
    try:
        B, N, *_ = map(int, input().split())
        
    except ValueError:
        break
    
    if B == 0 and N == 0:
        break
    
    R = list(map(int, input().split()))

    #(0 ≤ Ri ≤ 104, para 1 ≤ i ≤ B)
    if len(R) != B or any(0 > val > 10**4 for val in R):
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
