n=int(input())
s=set()
a=2
while a*a<=n:
    x=a*a
    while x<=n:
        s.add(x)
        x*=a
    a+=1
print(n-len(s))