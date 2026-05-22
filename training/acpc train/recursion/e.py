def genrate(n,indx):
    if indx==ln:
        if n!="":
            p.add(int(n))
        return
    genrate(n+"4",indx+1)
    genrate(n+"7",indx+1)
    genrate(n,indx+1)

n=input()
ln=len(n)
p=set()
p.add(int(n))
genrate("",0)
p=list(p)
p.sort()
print(p.index(int(n))+1)