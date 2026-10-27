import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n=II()
a=II()
b=II()


print(min(a*n,b))