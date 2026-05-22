def check(indx,c):
    global res
    if indx==len(n):
        if c==d:
            res+=1
        return
    if n[indx]=="+":
        check(indx+1,c+1)
    elif n[indx]=="-":
        check(indx+1,c-1)
    else:
        check(indx+1,c+1)
        check(indx+1,c-1)


s=input()
n=input()
d=0
t=1
c=0
for i in range(len(s)):
    if s[i]=="+":
        d+=1
    else:
        d-=1
for i in range(len(s)):
    if n[i]=="?":
        t+=2**c
        c+=1
res=0
check(0,0)
print(f"{res/t:.9f}")