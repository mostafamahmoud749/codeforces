n=int(input())
a=sorted(map(int,input().split()))
s=set(a)
s=list(s)
res=0
cur=0
for i in range(1,len(s)):
    if s[i]==s[i-1]+1:
        cur+=1
    else:
        res=max(cur,res)
        cur=0
res=max(cur,res)
print(res+1)
