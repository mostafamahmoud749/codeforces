
n=int(input())
a=list(map(int,input().split()))

c6=0
c7=0
for i in range(n):
    if a[i]==6:
        c6+=1
    elif a[i]==7:
        c7+=1

if c6==0 or c7==0:
    print(0)
elif c6==c7:
    print((c6*2)-1)
else:
    print(min(c6,c7)*2)