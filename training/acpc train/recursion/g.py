def check(indx,c):
    global s
    if indx==n:
        if c%360==0:
            s=True
        return
    check(indx+1,c+a[indx])
    check(indx+1,c-a[indx])

n=int(input())
a=[]
s=False
for i in range(n):
    a.append(int(input()))
check(0,0)
print("YES") if s else print("NO")