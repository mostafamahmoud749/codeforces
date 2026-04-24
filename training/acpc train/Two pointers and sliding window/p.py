import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    freqb={}
    freqc={}
    curk=0
    res=0
    for i in range(m):
        freqb[b[i]]=freqb.get(b[i],0)+1
    for i in range(m):
        if a[i] in freqb:
            freqc[a[i]]=freqc.get(a[i], 0) + 1
            if freqc[a[i]]<=freqb[a[i]]:
                curk+=1
    i=m
    j=0
    if curk>=k:
        res+=1
    while i<n:
        if a[j] in freqb:
            if freqc[a[j]]<=freqb[a[j]]:
                curk-=1
            freqc[a[j]]-=1
        if a[i] in freqb:
            freqc[a[i]]=freqc.get(a[i],0)+1
            if freqc[a[i]]<=freqb[a[i]]:
                curk+=1
        if curk>=k:
            res+=1
        i+=1
        j+=1
    print(res)