t=int(input())
for i in range(t):
    x=input()
    for k in range(0,len(x)-1):
        if x[k]==x[k+1]:
            print(1)
            break
    else:
        print(len(x))