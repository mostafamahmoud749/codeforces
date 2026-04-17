n=input()
lower=0
upper=0
for i in n:
    indx=ord(i)
    if indx<=90 and indx>=65:
        upper+=1
    else:
        lower+=1
n=list(n)
if lower>=upper:
    for i in range(len(n)):
        cur=ord(n[i])
        if cur<=90 and cur>=65:
            n[i]=chr(cur+32)
else:
    for i in range(len(n)):
        cur=ord(n[i])
        if cur<=122 and cur>=97:
            n[i]=chr(cur-32)
print("".join(n))