import math
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(math.ceil((max(a)-min(a))/2))