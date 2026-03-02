n,t=map(int,input().split())
y=list(map(int,input().split()))
index=0
while index+1<t:
    index+=y[index]
if index+1==t:
    print("YES")
else:
    print("NO")