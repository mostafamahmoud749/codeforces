n=int(input())
res=0
n=list(map(int,input().split()))
while n:
    if len(n)==1:
        break
    res+=max(n)-min(n)
    n.remove(max(n))
    n.remove(min(n))
print(res)