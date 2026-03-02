n=int(input())
y=list(map(int,input().split()))
res=0
min=0
for i in y:
    res+=i
    if res<min:
        min=res
print(-min)