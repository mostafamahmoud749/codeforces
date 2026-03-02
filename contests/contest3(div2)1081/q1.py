t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    
    if n == 1:
        print(1)
        continue
    
    blocks = 1
    double = 0
    for i in range(1, n):
        if s[i] != s[i-1]:
            blocks += 1
        else:
            double = 1
    
    if s[0] == s[n-1]:
        cyc = blocks - 1
    else:
        cyc = blocks

    l_cyc = double or (s[0] == s[n-1])
    
    print(cyc + (1 if l_cyc else 0))