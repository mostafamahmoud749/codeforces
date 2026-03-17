t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    d = [p[0]]
    stat=False
    for i in range(1, n - 1):
        d.append(p[i] - p[i - 1])

    s = set()
    ext= []
    for x in d:
        if x < 1 or x > n or x in s:
            ext.append(x)
        else:
            s.add(x)

    m = []
    for i in range(1, n + 1):
        if i not in s:
            m.append(i)

    if len(ext) == 0 and len(m) == 1:
        stat = True
    elif len(ext) == 1 and len(m) == 2 and ext[0] == m[0] + m[1]:
        stat = True

    if stat==True:
        print("YES")
    else:
        print("NO")
