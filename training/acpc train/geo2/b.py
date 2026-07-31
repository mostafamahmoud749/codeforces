n=int(input())
pref=[0]*(n+1)

freq={}

for i in range(n):
    a,b=map(int,input().split())
    if a not in freq:
        freq[a]=1
    else:
        freq[a]+=1

res=0
c=0
for i in freq.keys():
    res+=freq[i]*(n-freq[i]-c)
    c+=freq[i]

print(res)