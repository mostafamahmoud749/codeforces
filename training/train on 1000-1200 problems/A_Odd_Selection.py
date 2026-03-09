t = int(input())
for _ in range(t):
    n, x = map(int,input().split())
    arr = list(map(int,input().split()))
    o = sum(1 for v in arr if v % 2 == 1)
    e = n - o
    if o == 0:
        print("No")
    elif x == n:
        print("Yes" if o % 2 == 1 else "No")
    elif x % 2 == 0 and o == n:
        print("No")
    else:
        print("Yes")