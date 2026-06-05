n=int(input())
a=sorted(map(int,input().split()))
res=1
for i in range(n):
    if a[i]==res:
        res+=1
    else:
        break
print(res)