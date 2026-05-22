def genrate(cnums,a,count):
    global res
    if count>k or res!=-1:
        return
    if len(a)==10:
        res=a
        return
    for i in range(len(cnums)):
        genrate(cnums[:i]+cnums[i+1:],a+[cnums[i]],count+(cnums[i]*n[len(a)]))


t=int(input())
for _ in range(t):
    n=list(map(int,input().split()))
    k=int(input())
    res=-1
    nums=list(range(10))
    genrate(nums,[],0)
    print(*res) if res!=-1 else print(res)

#     def genrate(a,count):
#     global res
#     if count>k or res!=-1:
#         return
#     if len(a)==10:
#         res=list(a)
#         return
#     for i in range(10):
#         if not used[i]:
#             used[i]=True
#             a.append(i)
#             genrate(a,count+i*n[len(a)-1])
#             a.pop()
#             used[i]=False

# t=int(input())
# for _ in range(t):
#     n=list(map(int,input().split()))
#     k=int(input())
#     res=-1
#     used=[False]*10
#     genrate([],0)
#     print(*res) if res!=-1 else print(res)