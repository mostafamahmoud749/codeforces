import math

n,k=map(int,input().split())
res=0
p=[1,0,1,2,9]
for i in range(0,k+1):
    res+=(math.factorial(n)//(math.factorial(n-i)*math.factorial(i)))*p[i]

print(res)