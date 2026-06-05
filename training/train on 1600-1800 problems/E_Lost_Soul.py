t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    s1=set()
    s2=set()
    res=0
    for i in range(n-1,0,-1):
        if a[i]==b[i]:
            res=i+1
            break
        elif a[i-1] in s2 or b[i-1] in s1 :
            res=i
            break
        if  i%2!=0:
            s1.add(a[i])
            s2.add(b[i])
        elif i%2==0: 
            s1.add(a[i])
            s2.add(b[i])
        if a[i-1] in s1 or b[i-1] in s2 :
            res=i
            break
    print(res)