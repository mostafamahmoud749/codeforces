t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    s=set()
    for i in range(1,n):
        if a[i]==a[i-1]:
            continue
        elif a[i] in s:
            print("NO")
            break
        s.add(a[i-1])
    else:
        print("YES")