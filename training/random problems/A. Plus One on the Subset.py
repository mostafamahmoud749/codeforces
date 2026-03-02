t=int(input())
for i in range(t):
    x=int(input())
    y=list(map(int,input().split()))
    print(max(y)-min(y))