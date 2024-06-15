NC = int(input())

def calculate_S(n):
    if n == 1:
        return 1
    
    if n % 2 == 0:
        k = n // 2
        return 2 * calculate_S(k) - 1
    else:
        k = (n - 1) // 2
        return 2 * calculate_S(k) + 1

for case_number in range(1, NC + 1):
    n, k = map(int, input().split())
    m = calculate_S(n)
    print(f"Case {case_number}: {m}")
