import math


n=int(input())
a=list(map(int,input().split()))
res=0
c=0
a.sort()
while c<=sum(a):
    c+=a.pop()
    res+=1
print(res)