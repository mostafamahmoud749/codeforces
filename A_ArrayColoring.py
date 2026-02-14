t=int(input())
for _ in range(t):
    n=int(input())
    nums=list(map(int,input().split()))
    if sum(nums)%2==0:
        print("yes")
    else:
        print("no")
