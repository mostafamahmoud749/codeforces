n=int(input())
a=list(map(int,input().split()))

res=0
for i in range(n):
    indx=i+1
    res+=a[i]*((indx*(n-indx+1)))

print(res)
