a=list(input().strip())
q=int(input())
p=[0]*(len(a)+1)
c=0
for i in range(1,len(a)+1):
    if a[i-1]=="a":
        c+=1
    p[i]=c
for i in range(q):
    l,r=map(int,input().split())
    print(p[r]-p[l-1])