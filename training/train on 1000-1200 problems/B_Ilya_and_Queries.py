s=input()
t=int(input())
db={1:0}
count=0

for i in range(1,len(s)):
    if s[i-1]==s[i]:
        count+=1
    db[i+1]=count

for _ in range(t):
    l,r=map(int,input().split())
    print(db[r]-db[l])