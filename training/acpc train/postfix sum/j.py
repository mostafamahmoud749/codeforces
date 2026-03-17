
import sys
input = lambda: sys.stdin.readline().strip()
sys.stdin = open("maxcross.in")
sys.stdout = open("maxcross.out", "w")

n,k,b=map(int,input().split())
broken=[0]*(n+1)

for i in range(b):
    indx=int(input())
    broken[indx]=1

p=[0]*(n+1)
for i in range(1,n+1):
    p[i]=p[i-1]+broken[i]

min_r=float("inf")
for i in range(k,n+1):
    cur=p[i]-p[i-k]
    min_r=min(min_r,cur)

print(min_r)