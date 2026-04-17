t=int(input())
for _ in range(t):
    n=int(input())
    s,t=map(str,input().split())
    s=list(s)
    t=list(t)
    s.sort()
    t.sort()
    for i in range(n):
        if s[i]!=t[i]:
            print("NO")
            break
    else:
        print("YES")

    