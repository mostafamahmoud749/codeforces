n,t=map(int,input().split())
m=list(map(int,input().split()))
count=0
for i in m:
    if i>t:
        break
    count+=1
    t-=i
print(count)