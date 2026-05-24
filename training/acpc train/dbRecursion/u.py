import sys
sys.setrecursionlimit(10**8)

def solve(l,remn1,remn2):
    if remn1+remn2==0:
        return 1
    if db[l][remn1][remn2]!=-1:
        return db[l][remn1][remn2]
    ch1=0
    ch2=0
    if l==0 or l==2:
        for i in range(1,min(k1,remn1)+1):
            ch1=(ch1+solve(1,remn1-i,remn2))%100000000
    if l==1 or l==2:
        for i in range(1,min(k2,remn2)+1):
            ch2=(ch2+solve(0,remn1,remn2-i))%100000000
    res=(ch1+ch2)%100000000
    db[l][remn1][remn2]=res
    return res

n1,n2,k1,k2=map(int,input().split())
db = [[[-1] * (n2+1) for _ in range(n1+1)] for _ in range(3)]
res=solve(2,n1,n2)
print(res)