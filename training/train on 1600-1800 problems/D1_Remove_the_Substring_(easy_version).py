t=list(input().strip())
s=list(input().strip())
res=0
for i in range(len(t)):
    for j in range(i,len(t)):
        newt=t[0:i]+t[j+1:]
        cur=0
        for k in range(len(newt)):
            if cur==len(s):
                break
            if newt[k]==s[cur]:
                cur+=1
        if cur==len(s):
            res=max(res,j-i+1)
print(res)