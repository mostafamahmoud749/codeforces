import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
    n,k=LII()
    a=LII()


    allb=[]
    bits=[0]*10

    res=a[0]
    cres=a[0]
    for i in range(a[0].bit_length()):
        if ((a[0]>>i)&1)==1:
            bits[i]=1
    
    i=0
    j=0
    while i<n-1:
        i+=1
        l=a[i].bit_length()
        if bits[l-1]==1:
            allb.append(bits)
            bits=[0]*10
            j=i
        else:
            for p in range(a[i].bit_length()):
                if ((a[0]>>i)&1)==1:
                    if bits[p]==0:
                        bits[p]=1
                    else:
                        bits[p]=0
                
    allb.append(bits) 

    res=0
    for i in allb:
        curk=k
        cres=0
        for j in range(len(i)-1,-1,-1):
            if curk>0 and i[j]==0:
                curk-=1
                cres|=(1<<j)
            elif i[j]==1:
                cres|=(1<<j)
                
        res=max(res,cres)

    print(res)
    # print(bits)




