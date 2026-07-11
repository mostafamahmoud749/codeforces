n=int(input())
a=sorted(map(int,input().split()))

res=0
for i in range(n//2):
    res+=((a[i]+a[n-i-1])**2)

print(res)
