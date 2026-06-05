a=list(map(int,input().split()))
ch1=True
d=a[1]-a[0]
ch2=True
q=a[1]/a[0]
for i in range(2,4):
    if a[i]-a[i-1]!=d:
        ch1=False
        break
for i in range(2,4):
    if a[i]/a[i-1]!=q:
        ch2=False
        break
if ch1:
    print(a[3]+d)
elif ch2:
    v=a[3]*q
    if int(v)==v:
        print(int(v))
    else:
        print(42)
else:
    print(42)