y,x=map(int,input().split())
b=6-max(y,x)+1

if b==6:
    print("1/1")
elif b==5:
    print("5/6")
elif b==4:
    print("2/3")
elif b==3:
    print("1/2")
elif b==2:
    print("1/3")
elif b==1:
    print("1/6")
elif b==0:
    print("0/1")
    