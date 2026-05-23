t=int(input())
for i in range(t):
    n,s=map(int,input().split())
    res=360/s
    print("YES") if res%2==0 else print("NO")