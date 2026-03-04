import math
n,m=map(int,input().split())
nums=list(map(int,input().split()))
res={
    "iter":math.ceil(nums[0]/m),
    "index":0
}

for i in range(1,n):
    iters=math.ceil(nums[i]/m)
    if iters>=res["iter"]:
        res["iter"]=iters
        res["index"]=i
print(res["index"]+1)