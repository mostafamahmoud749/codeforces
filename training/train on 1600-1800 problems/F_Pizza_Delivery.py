import sys
from collections import defaultdict
sys.setrecursionlimit(10**8)
input=sys.stdin.readline

def solve(indx,y):
    if indx==len(keys):
        return abs(y-by) 
    if (indx,y) in dp:
        return dp[(indx,y)]
    ch1=float("inf")
    ch2=float("inf")
    maxy=max(goal[keys[indx]])
    miny=min(goal[keys[indx]])
    ch1=abs(y-miny)+abs(miny-maxy)+solve(indx+1,maxy)
    ch2=abs(y-maxy)+abs(miny-maxy)+solve(indx+1,miny)
    res=min(ch1,ch2)
    dp[(indx,y)]=res
    return res

t=int(input())
for _ in range(t):
    n,ax,ay,bx,by=map(int,input().split())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    goal=defaultdict(list)
    for i in range(n):
        goal[x[i]].append(y[i])
    keys=sorted(goal.keys())
    dp=defaultdict(list)
    res=(bx-ax)+solve(0,ay)
    print(res)