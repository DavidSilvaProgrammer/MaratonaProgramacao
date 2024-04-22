while True:
    try:
        B, N, *_ = map(int, input().split())
        
    except ValueError:
        break
    
    if B == 0 and N == 0:
        break
    
    R = list(map(int, input().split()))
    
    if len(R) != B:
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
        
    
    s = True
    for i in range(B):
        if R[i] < 0:
            s = False
            print("N")
            break
            
    
    if s:
        print("S")
