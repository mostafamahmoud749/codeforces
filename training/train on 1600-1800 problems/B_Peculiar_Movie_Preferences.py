t=int(input())
for _ in range(t):
    n=int(input())
    a=[input().strip() for _ in range(n)]
    s=set()
    stat=False
    for i in range(len(a)):
        inv=a[i][::-1]
        if a[i]==inv:
            stat=True
        else:
            if len(inv)==3:
                if (inv in s) or inv[0:2] in s:
                    stat=True
            elif len(inv)==2:
                j=97
                while j<123:
                    if (inv+chr(j)) in s:
                        stat=True
                        break
                    j+=1
                if inv in s or inv[0] in s:
                    stat=True
            else:
                if inv in s:
                    stat=True
        s.add(a[i])
        if stat:
            break
    print("YES") if stat else print("NO")