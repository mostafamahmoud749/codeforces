n=int(input())
nums=list(map(int,input().split()))
cur_g=0
max_g=0
total_ones=0
for i in range(n):
    total_ones+=1 if nums[i]==1 else 0
    change=1 if nums[i]==0 else -1
    cur_g=max(change,change+cur_g)
    max_g=max(max_g,cur_g)
if total_ones==n:
    print(n-1)
else:
    print(total_ones+max_g)