t=int(input())
for _ in range(t):
    x,y=map(int,input().split())
    if x%2!=0 and y%2!=0:
        print("NO")
    else:
        print("YES")