t=int(input())
for _ in range(t):
    a,b,c,d=map(int,input().split())
    p1=min(a,c)
    p2=min(b,d)
    if p1>=p2:
        print("Gellyfish")
    else:
        print("Flower")