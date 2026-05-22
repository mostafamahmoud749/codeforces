import sys
sys.setrecursionlimit(10**5)
def buy(n):
    global s
    if n in seen:
        return
    seen.add(n)
    if n%1234==0:
        s=True
        return
    for i in range(2):
        if s:
            return
        if items[i]<=n:
            buy(n-items[i])
seen=set()
n=int(input())
s=False
items=[1234567,123456]
buy(n)
print("YES") if s else print("NO")