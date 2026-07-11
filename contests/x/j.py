# TEST

n,q=map(int,input().split())
a=list(map(int,input().split()))

for _ in range(q):
    inp=list(input().split())
    l=int(inp[1])
    r=int(inp[2])
    if inp[0]=="P":
        c1=0
        cb=0
        for i in range(l-1,r):
            if a[i]==1:
                c1+=1
            else:
                cb+=1
        # if c1%2==0:
        #     c1="e"
        # else:
        #     c1="o"
        # if cb%2==0:
        #     cb="e"
        # else:
        #     cb="o"
        if cb>0:
            if cb%2!=0:
                print("FRANK")
            else:
                print("JUAN")
        else:
            if c1%2!=0:
                print("FRANK")
            else:
                print("JUAN")
    else:
        a[r-1]=a[r-1]+l