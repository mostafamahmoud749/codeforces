t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    maxx = 0
    ugly_indices = []
    
    for i in range(n):
        maxx = max(maxx, p[i])
        if maxx == i + 1:
            ugly_indices.append(i)

    if not ugly_indices:
        print(' '.join(map(str, p)))
        continue
    first_ugly = ugly_indices[0]
    
    b_candidate = -1
    b_pos = -1
    
    for j in range(first_ugly + 1, n):
        if p[j] > first_ugly + 1:
            if b_candidate == -1 or p[j] > b_candidate:
                b_candidate = p[j]
                b_pos = j
    
    if b_pos != -1:
        p[first_ugly], p[b_pos] = p[b_pos], p[first_ugly]
    
    print(' '.join(map(str, p)))