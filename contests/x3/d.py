t=int(input())
for i in range(t):
    a,b,c = map(int,input().split())

    tot = 0 
    x = a
    for i in range(c):
        tot += a % b
        a += x
    print(tot)