import math
n,k=map(int,input().split())

res=[1]

b=n//k
x=n%k
l=1
c=0
# for i in range(k):
#     if i==0:
#         res.append(1)
#     else:
#         res.append(1+((10**5)*i))
while len(res)<k:
    if c<x:
        res.append(l+b+1)
        c+=1
        l+=b+1
    else:
        res.append(l+b)
        l+=b

j=1
while len(res)<n:
    for i in range(k):
        res.append(res[i]+j)
        if len(res)==n:
            break
    j+=1

# print(res)

# curk=k
# j=0

# while len(res)<n:
#     for i in range(1,n+1,math.ceil(n/k)):
#         res.append(j+i)
#         if len(res)>=n:
#             break
#     j+=1



# while len(res)<n:


print(*res)