import sys
sys.setrecursionlimit(400000)

def solve(prev,indx):
    cur=indx-prev
    of=cur-d+250
    if db[indx][of]!=-1:
        return db[indx][of]
    ch1=0
    ch2=0
    ch3=0
    if cur-1>0 and indx+cur-1<=maxisland:
        ch1=gems.get(indx+cur-1,0)+solve(indx,indx+cur-1)
    if cur>0 and indx+cur<=maxisland:
        ch2=gems.get(indx+cur,0)+solve(indx,indx+cur)
    if cur+1>0 and indx+cur+1<=maxisland:
        ch3=gems.get(indx+cur+1,0)+solve(indx,indx+cur+1)
    res=max(ch1,ch2,ch3)
    db[indx][of]=res
    return res

n,d=map(int,input().split())
gems={}
maxisland=0
for i in range(n):
    x=int(input())
    maxisland=max(maxisland,x)
    gems[x]=gems.get(x,0)+1
db=[[-1]*500 for _ in range(maxisland+1)]
if d<=maxisland:
    res=gems.get(d,0)+solve(0,d)
else:
    res=0
print(res)