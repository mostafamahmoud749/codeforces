t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()

    curres = s[:k].count("W")
    minres = curres

    for i in range(1, n-k+1):
        if s[i-1] == "W":
            curres -= 1
        if s[i+k-1] == "W":
            curres += 1
        minres = min(curres, minres)
        if minres == 0:
            break
    
    print(minres)