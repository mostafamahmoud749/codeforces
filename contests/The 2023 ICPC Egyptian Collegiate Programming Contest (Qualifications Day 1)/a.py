t = int(input())
for _ in range(t):
    s=input()
    rs=s[::-1]
    print("YES" if s>=rs else "NO")