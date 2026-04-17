
n=int(input())
a=list(map(int,input().split()))
curs=set()
m=0
l=0
for i in range(0,n):
    while a[i] in curs:
        curs.remove(a[l])
        l+=1
    curs.add(a[i])
    m=max(len(curs),m)

print(m)