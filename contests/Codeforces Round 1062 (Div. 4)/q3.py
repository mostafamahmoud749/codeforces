t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    even = False
    odd = False
    for num in a:
        if num % 2 == 0:
            even = True
        else:
            odd = True
    if even and odd:
        a.sort()
    print(*a)