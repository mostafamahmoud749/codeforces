import sys
sys.setrecursionlimit(10000)

def go(x,y):
    if x==n or y==n or grid[x][y]=="*":
        return 0
    if x==n-1 and y==n-1:
        return 1
    if seen[x][y]!=-1:
        return seen[x][y]
    ch1=go(x+1,y)
    ch2=go(x,y+1)
    res=(ch1+ch2)%(10**9+7)
    seen[x][y] = res
    return res

n=int(input())
grid=[]
seen=[]
for i in range(n):
    grid.append(list(input().strip()))
    seen.append([-1]*n)

res=go(0,0)
print(res)