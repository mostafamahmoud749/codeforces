import sys
sys.setrecursionlimit(100000)

def genrate(c,x,y):
    if c!="":
        if int(c)>0 and int(c)<=n:
            vnumbers.add(int(c))
        numbers.add(c)
    if c!="" and (int(c)>n or len(c)>10):
        return
    if c+x not in numbers:
        genrate(c+x,x,y)
    if c+y not in numbers:
        genrate(c+y,x,y)

n=int(input())
vnumbers=set()

for i in range(10):
    for j in range(i,10):
        numbers=set()
        genrate("",str(i),str(j))
print(len(vnumbers))