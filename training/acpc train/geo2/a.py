t=int(input())
for _ in range(t):
    r,th=map(int,input().split())

    print("YES") if (360/th)%2==0 else print("NO")