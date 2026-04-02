t=int(input())
for _ in range(t):
    n=int(input())
    a=input()
    k=int(input())
    b=input()
    s=input()
    for i in range(k):
        if s[i]=="D":
            a=a+b[i]
        else:
            a=b[i]+a
    print(a)