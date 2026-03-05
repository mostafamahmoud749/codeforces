n,t=map(int,input().split())
a=list(map(int,input().split()))
cur=0
last_index=0

while last_index<n and t>=a[last_index]:
    t-=a[last_index]
    cur+=1
    last_index+=1
max_a=cur
for i in range(1,n):
    if i-1 < last_index:
        t+=a[i-1]
        cur-=1
    if last_index < i:
        last_index = i
    while last_index<n and t>=a[last_index]:
        t-=a[last_index]
        cur+=1
        last_index+=1
    if cur>max_a:
        max_a=cur

print(max_a)