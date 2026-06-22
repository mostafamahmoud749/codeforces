n=int(input())
a=list(input().strip())
gc=a.count("G")
s=False
i=0
j=0
res=0
while i<n:
    if a[i]=="G":
        i+=1
    elif a[i]=="S":
        if s:
            while a[j]!="S":
                j+=1
            j+=1
        else:
            s=True
        i+=1
    res=max(res,min(gc,i-j))
print(res)
