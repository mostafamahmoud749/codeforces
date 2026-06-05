n=int(input())
a=list(map(int,input().split()))
a.sort()
res=1
cs=a[0]
for i in range(1,n):
    if a[i]>=cs:
        res+=1
        cs+=a[i]
print(res)