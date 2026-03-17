n,m=map(int,input().split())
arr=list(map(int,input().split()))
pref=[0]*n
n_set=set()
for i in range(n-1,-1,-1):
    n_set.add(arr[i])
    pref[i]=len(n_set)

for i in range(m):
    o=int(input())
    print(pref[o-1])
