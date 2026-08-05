import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

t=II()
for _ in range(t):
    n=II()
    print(10) if n>0 else print(0)