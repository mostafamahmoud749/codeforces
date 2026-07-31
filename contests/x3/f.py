t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    zero=0
    chess=0
    lol=0

    for i in a:
        if i==1:
            chess+=1
        elif i==-1:
            lol+=1
        else:
            if zero%2==0:
                chess+=1
            else:
                lol+=1
            zero+=1
    
    if chess>lol:
        print("Chess")
    elif chess<lol:
        print("Lol")
    else:
        print("Go deploying")