t=int(input())
for _ in range(t):
    ang=int(input())
    if 360%(180-ang)==0:
        print("YES")
    else:
        print("NO")
