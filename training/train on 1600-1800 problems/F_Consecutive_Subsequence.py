import sys
sys.setrecursionlimit(300000)

def solve(indx,l):
    if indx==n:
        return []
    if (indx,l) in db:
        return db[(indx,l)]
    ch1=[]
    ch2=[]
    ch3=[]
    if a[indx]-1==l:
        ch1=[indx+1]+solve(indx+1,a[indx])
    ch2=solve(indx+1,l)
    if l==-1:
        ch3=[indx+1]+solve(indx+1,a[indx])
    m=max(len(ch1),len(ch2),len(ch3))
    res=0
    if len(ch1)==m:
        res=ch1
    elif len(ch2)==m:
        res=ch2
    else:
        res=ch3
    db[(indx,l)]=res
    return res


n=int(input())
a=list((map(int,input().split())))
db={}
res=solve(0,-1)
print(len(res))
print(*res)