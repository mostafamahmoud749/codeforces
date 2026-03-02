t=int(input())
for _ in range(t):
    v=int(input())
    if v<2020:
        print("NO")
    else:
        n=v//2020
        if n*2020<=v and n*2020+n>=v:
            print("YES")
        else:
            print("NO")