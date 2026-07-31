from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))

    freq={}
    for i in a:
        freq[i]=freq.get(i,0)+1

    