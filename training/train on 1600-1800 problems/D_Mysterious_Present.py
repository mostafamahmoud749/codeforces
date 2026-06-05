n,w,h=map(int,input().split())
a=[0]*n
for i in range(n):
    cw,ch=map(int,input().split())
    a[i]=[cw,ch,i]
a.sort(reverse=True)

if a[0][0]>w and a[0][1]>h:
    res=[a[0][2]+1]
    cw=a[0][0]
    ch=a[0][1]
    for i in range(n):
        if w<a[i][0]<cw and h<a[i][1]<ch:
            cw=a[i][0]
            ch=a[i][1]
            res.append(a[i][2]+1)

    print(len(res))
    print(*res[::-1])
else:
    print(0)