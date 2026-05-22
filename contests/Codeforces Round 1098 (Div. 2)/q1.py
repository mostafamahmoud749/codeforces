import sys
input = lambda: sys.stdin.readline().strip()
from collections import defaultdict, Counter
for _ in range(int(input())):
    n = int(input())
    ls = list(map(int, input().split()))

    mp = Counter(ls)
    # print(mp)
    res = 0
    if 1 in mp and 2 in mp:
        res += min(mp[1],mp[2])
        m=min(mp[1],mp[2])
        mp[1] -= m
        mp[2] -= m
        if mp[2]:
            res += mp[2]//3
        if mp[1]:
            res += mp[1]//3
    elif 1 in mp:
        res += mp[1]//3
    elif 2 in mp:
        res += mp[2]//3

    res += mp[0]
    print(res)