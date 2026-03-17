n,k=map(int,input().split())
a=list(map(int,input().split()))
min_h=float("inf")
indx=0
window_sum=0
p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=a[i-1]+p[i-1]
for i in range(k,n+1):
    cur=p[i]-p[i-k]
    if cur<min_h:
        indx=i-k+1
        min_h=cur
print(indx)
