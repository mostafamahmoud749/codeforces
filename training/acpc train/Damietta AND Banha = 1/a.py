
a=list(map(int,input().split()))
s=0
maxo=0
for i in range(14):
    if a[i]%2==0:
        s+=a[i]
    else:
        maxo=max(maxo,a[i])
print(s+(maxo//2))