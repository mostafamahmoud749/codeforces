import math

t=int(input())
for _ in range(t):
    n=int(input())
    traps=[]
    for i in range(n):
        d,s=map(int,input().split())
        traps.append([d,s])
    traps.sort()
    r=(traps[-1][1]-1)//2
    for i in range(n-2,-1,-1):
        r+=traps[i+1][0]-traps[i][0]
        r=min(r,(traps[i][1]-1)//2)
    print(r+traps[0][0])