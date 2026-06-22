t=int(input())
for _ in range(t):
    n,p=map(int,input().split())
    a=sorted(map(int,input().split()))
    res=0
    for i in a:
        if p>=i:
            res+=1
            if i%2==0:
                p+=2
            elif i%3==0:
                p+=3
            else:
                for j in range(5,(i**2)+1,6):
                    if i%j==0:
                        p+=j
                        break
                    elif (2+i)%j==0:
                        p+=j+2
                        break
        else:
            break
    print(res,p)