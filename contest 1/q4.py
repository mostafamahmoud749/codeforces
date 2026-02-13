t=int(input())
for _ in range(t):
    solved={}
    n=int(input())
    s=input()
    res=0
    for i in s:
        if i in solved:
            res+=1
        else:
            solved[i]=1
            res+=2
    print(res)