n=int(input())
s=input()
cfreq=[0]*26
i=0
j=0
res=0
while i<n:
    v=ord(s[i])-97
    cfreq[v]+=1
    maxr=25
    while maxr>0:
        if cfreq[maxr]!=0:
            break
        maxr-=1
    while (v+1)*cfreq[v]<(maxr+1)*((i-j)+1):
        cfreq[ord(s[j])-97]-=1
        j+=1
        maxr=25
        while maxr>0:
            if cfreq[maxr]!=0:
                break
            maxr-=1
    i+=1
    res=max(res,i-j)
print(res)
