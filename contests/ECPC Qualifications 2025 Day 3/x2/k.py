def genrate(i,c):
    if i==n:
        p.append(c)
        return
    genrate(i+1,c|a[i])
    genrate(i+1,c)



n = int(input())
a= list(map(int,input().split()))


p=[]
genrate(0,0)
# print(p)
# all = a[0]
# print(p)
res=0
for i in p:
    res+=i
# print(20|1)
print(res)