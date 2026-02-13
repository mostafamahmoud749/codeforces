n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*n)
else:
    if n%m==0:
        print((n//m)*b)
    else:
        if (n%m)*a<b:
            print((n//m)*b+(n%m)*a)
        else:       
            print((n//m)*b+b)