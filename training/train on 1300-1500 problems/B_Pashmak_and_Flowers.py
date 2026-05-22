n=int(input())
a=sorted(map(int,input().split()))
s=1
e=1
for i in range(1,n):
    if a[0]==a[i]:
        s+=1
for i in range(n-2,-1,-1):
    if a[-1]==a[i]:
        e+=1
if a[0]!=a[-1]:
    print(a[-1]-a[0],s*e)
else:
    print(a[-1]-a[0],n*(n-1)//2)
