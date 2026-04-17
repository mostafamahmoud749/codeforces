l,r=map(int,input().split())
if l==r:
    print(r.bit_count())
elif r.bit_length()>l.bit_length():
    print(max(r.bit_count(),r.bit_length()-1))
else:
    m=r.bit_count()
    rbin=bin(r)[2:]
    lbin=bin(l)[2:]
    s=True
    c=0
    so=0
    for i in range(1,len(rbin)):
        if s==True and rbin[i]!=lbin[i]:
            s=False
        elif s==False and rbin[i]=="0":
            c+=1
    print(max(m,c+m-1))