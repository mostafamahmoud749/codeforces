n,k=map(int,input().split())
s=input()
maxa=0
maxb=0
i=0
j=0
k2=k
while i<=n-1:
    if s[i]=="b":
        k-=1
    while k<0:
        if s[j]=="b":
            k+=1
        j+=1
    maxa=max(maxa,i-j+1)
    i+=1
i=0
j=0
while i<=n-1:
    if s[i]=="a":
        k2-=1
    while k2<0:
        if s[j]=="a":
            k2+=1
        j+=1
    maxb=max(maxb,i-j+1)
    i+=1
print(max(maxa,maxb))
