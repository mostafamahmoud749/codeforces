import sys
sys.setrecursionlimit(100000)

def count(indx,lc,cres):
    global res
    if indx==n-1:
        res=max(res,cres)
        return
    rc=trees[indx+1][0]-trees[indx][0]
    if lc>trees[indx][1]:
        count(indx+1,rc,cres+1)
    elif rc>trees[indx][1]:
        count(indx+1,rc-trees[indx][1],cres+1)
    else:
        count(indx+1,rc,cres)

n=int(input())
trees=[]
for i in range(n):
    x,h=map(int,input().split())
    trees.append([x,h])
if n<=2:
    print(n)
    exit()
res=0
count(1,trees[1][0]-trees[0][0],0)
print(res+2)