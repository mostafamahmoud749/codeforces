import math

n,k=map(int,input().split())

a=list(map(int,input().split()))
# res=math.prod(a)**(1/k)
# # maxv=(10**5)**51
# # cur=1


# # for i in a:
# #     cur=(cur*i)%maxv
    
# # res=cur**(1/k)

# if res%1==0:
#     print("YES")
# else:
#     print("NO")

cur=0
for i in range(1,(10**5)+1):
    c=0
    for j in a:
        cur=(cur*j)%k



print("YES") if cur==0 else print("NO")

