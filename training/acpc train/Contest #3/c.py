n=int(input())
tasks=[]
for _ in range(n):
    a,d=map(int,input().split())
    tasks.append([a,d])
tasks.sort()
t=0
res=0
for i in range(n):
    t+=tasks[i][0]
    res+=tasks[i][1]-t
print(res)