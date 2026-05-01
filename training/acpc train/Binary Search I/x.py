t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    print(int(k+((k-1)/(n-1))))