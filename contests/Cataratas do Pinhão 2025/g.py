s=input()
db=[0]*26
for i in range(len(db)):
    db[i]=97+i
if s=="first":
    n=int(input())
    a=list(map(int,input().split()))
    s=[0]*n
    for i in range(n):
        s[i]=chr(db[a[i]-1])
    print("".join(s))
else:
    s=input()
    res=[0]*len(s)
    for i in range(len(s)):
        res[i]=ord(s[i])-97+1
    print(len(res))
    print(*res)