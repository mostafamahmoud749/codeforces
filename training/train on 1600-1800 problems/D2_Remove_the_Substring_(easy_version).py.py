t=list(input().strip())
s=list(input().strip())
l=[]
r=[0]*len(s)
res=0

cur=0
for k in range(len(t)):
    if cur==len(s):
        break
    if t[k]==s[cur]:
        l.append(k)
        cur+=1
    if cur==len(s):
        break

cur=len(s)-1
for k in range(len(t)-1,-1,-1):
    if cur>=0 and t[k]==s[cur]:
        r[cur]=k
        cur-=1

res=max(len(t)-l[len(s)-1]-1,r[0])

for i in range(len(s)-1):
    res=max(res,r[i+1]-l[i]-1)
print(res)