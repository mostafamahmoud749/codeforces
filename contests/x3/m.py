t=int(input())
for i in range(t):
    l,r=input().split()
    

    res=0

    for i in range(len(l)+1,len(r)):
        lnum=int("1"+("0"*(i-1)))
        rnum=int("9"*i)
        res+=i*(rnum-lnum+1)
    
    if len(l)==len(r):
        res=(int(r)-int(l)+1)*len(l)
    else :
        lnum=int(l)
        rnum=int("9"*len(l))
        res+=len(l)*(rnum-lnum+1)


        rnum=int(r)
        lnum=int("1"+("0"*(len(r)-1)))
        res+=len(r)*(rnum-lnum+1)

    print(res)
