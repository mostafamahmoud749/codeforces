import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))



n=input()

h=int(n[:2])
nh=str((h+5)%24)
if len(nh)==1:
    nh="0"+nh

print(nh+n[2:])