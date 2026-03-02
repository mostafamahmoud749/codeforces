n=int(input())
y=list(map(int,input().split()))
sum=0
for i in y:
    sum+=i
if sum !=0:
    print(1)
else:
    print(0)