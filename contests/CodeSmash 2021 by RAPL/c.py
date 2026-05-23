t=int(input())
for i in range(t):
    x,l,r=map(int,input().split())
    s=False
    for i in range(l,r-1):
        if s!=True:
            for j in range(i+1,r):
                if s!=True:
                    for k in range(j+1,r+1):
                        if i*j*k==x:
                            print(i,j,k)
                            s=True
                        if s:
                            break
    if s!=True:
        print(-1)