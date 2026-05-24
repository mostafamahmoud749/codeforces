import sys
sys.setrecursionlimit(100005)

def go(v):
    if v<=0:
        return 0
    if v==1:
        return freq[1]
    if v in db:
        return db[v]
    ch1=go(v-1)
    ch2=v*freq[v]+go(v-2)
    res=max(ch1,ch2)
    db[v]=res
    return res

n=int(input())
a=list(map(int,input().split()))
db={}
max_v=max(a)
freq=[0]*(max_v+1)
for i in range(n):
    freq[a[i]]+=1
res=go(max_v)
print(res)