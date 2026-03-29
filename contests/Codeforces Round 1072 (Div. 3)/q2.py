import math 
t=int(input())
for _ in range(t):
    s,k,m=map(int,input().split())
    flips = m // k
    rem = m % k
    if flips % 2 == 0:
        print(max(0, s - rem))
    else:
        print(max(0, min(s, k) - rem))
