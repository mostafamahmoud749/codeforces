import math

n=input()
k=int(input())
l=len(n)
if k==0:
    print(1)
elif k==1:
    print(l-1)
else:
    c=[[0]*1001 for _ in range(1001)]

    for i in range(1001):
        c[i][0]=1
        for j in range(1,i+1):
            c[i][j]=(c[i-1][j-1]+c[i-1][j])%1000000007

    a=[0]*(l+1)
    for i in range(1,l+1):
        res=0
        ones=0
        for j in range(l):
            if n[j]=="1":
                need=i-ones
                if 0<=need<=l-j-1:
                    res+=c[l-j-1][need]
                ones+=1
        if ones==i:
            res+=1
        a[i-1]=res

    dp=[0]*(l+1)
    res=0
    for i in range(2,l+1):
        dp[i]=1+dp[i.bit_count()]
        if dp[i]+1==k:
            res=(res+a[i-1])%((10**9)+7)

    print(res)

































# import math

# n=int(input(),2)
# k=int(input())
# if k==0:
#     print(1)
# elif k==1:
#     print(n.bit_length()-1)
# else:
#     l=n.bit_length()
#     a=[0]*(l+1)
#     for i in range(1,l+1):
#         res=0
#         ones=0
#         for j in range(l-1,-1,-1):
#             if ((n>>j)&1)==1:
#                 need=i-ones
#                 if 0<=need<=j:
#                     res+=math.comb(j,need)
#                 ones+=1
#         if ones==i:
#             res+=1
#         a[i-1]=res

#     dp=[0]*(l+1)
#     res=0
#     for i in range(2,l+1):
#         dp[i]=1+dp[i.bit_count()]
#         if dp[i]+1==k:
#             res=(res+a[i-1])%((10**9)+7)

#     print(res)
