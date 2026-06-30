n=input().strip()
if len(n)<=8:
    print(n+str(len(n)+1))
elif len(n)>=98:
    print(n+str(len(n)+3))
else:
    print(n+str(len(n)+2))
