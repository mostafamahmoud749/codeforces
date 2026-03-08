n=int(input())
db=[]
for _ in range(n):
    p,v=map(int,input().split())
    db.append((p,v))

db.sort(key=lambda x: x[0])
for i in range(1,n):
    if db[i-1][1]>=db[i][1]:
        print("Happy Alex")
        break
else:
    print("Poor Alex")

