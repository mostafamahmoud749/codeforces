n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
if sum(a)!=sum(b):
    print(-1)
    exit()
res=0
ac=0
bc=0
j=0
for i in range(n):
    ac+=a[i]
    while j<m and bc<ac:
        bc+=b[j]
        j+=1
    if ac==bc:
        res+=1
        ac+=0
        bc+=0
print(res)