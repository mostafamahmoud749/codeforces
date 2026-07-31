from collections import deque
import heapq
import math

t=int(input())
for _ in range(t):
    n=int(input())
    print(*range(n,0,-1))