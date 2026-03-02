t=int(input())
for i in range(t):
    o=input()
    x=list(map(int,input().split()))
    y=[]
    for j in x:
        if j not in y:
            y.append(j)
        else:
            print("NO")
            break
    if len(y)==len(x):
        print("YES")