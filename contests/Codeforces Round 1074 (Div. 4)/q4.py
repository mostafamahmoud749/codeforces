import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    n,m,h=map(int,input().split())
    a=list(map(int,input().split()))
    new_a=a.copy()
    changes = []
    for i in range(m):
        b,c=map(int,input().split())
        new_a[b-1]=new_a[b-1]+c
        changes.append(b-1)
        if new_a[b-1]>h:
            for idx in changes:
                new_a[idx] = a[idx]
            changes.clear()
    print(*new_a)