import sys

t = int(input())
for i in range(t):
    n = int(input())
    res = []
    for k in range(1, 19):
        div=(10**k)+1
        if div>n:
            break
        if n%div==0:
            res.append(n//div)
    res.sort()
    if not res:
        print("0")
    else:
        print(len(res))
        print(*res)
