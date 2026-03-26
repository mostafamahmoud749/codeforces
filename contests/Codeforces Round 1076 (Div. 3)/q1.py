t=int(input())
for _ in range(t):
    n,s,x=map(int,input().split())
    a=sum(map(int,input().split()))
    while a<s:
        a+=x
    if a==s:
        print("YES")
    else:
        print("NO")
