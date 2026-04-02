t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    res=0
    alicemode=a
    bobmode=a
    if a==0 and c+d+b==0:
        res=0
    elif a==0:
        res=1
    else:
        res+=a
        m=min(b,c)
        res+=2*m
        b-=m
        c-=m
        if b==0:
            cf= min(c,alicemode)
            res +=cf
            alicemode-= cf
            bobmode+=cf
            df=min(d,min(alicemode,bobmode))
            res+=df
        else:
            df=min(b, bobmode)
            res+=df
            bobmode-=df
            alicemode+=df
            df=min(d,min(alicemode, bobmode))
            res+=df
        
        if res<a+b+c+d+2*m:  
            res+=1
    print(res)