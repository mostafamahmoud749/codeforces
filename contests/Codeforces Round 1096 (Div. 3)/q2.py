t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    o=0
    c=0
    for i in s:
        if i=="(":
            o+=1
        else:
            c+=1
    print("YES") if o==c else print("NO")