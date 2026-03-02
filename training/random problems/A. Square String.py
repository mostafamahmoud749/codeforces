t=int(input())
for i in range(t):
    x=input()
    if len(x)%2!=0:
        print("NO")
    else:
        if x[0:len(x)//2]==x[len(x)//2:len(x)+1]:
            print("YES")
        else:
            print("NO")