def create(crlist,crstring):
    if len(crstring)==len(n):
        r="".join(crstring)
        if r not in seen:
            seen.add(r)
        return
    for i in range(len(crlist)):
        ns=crstring.copy()
        nl=crlist.copy()
        ns.append(crlist[i])
        nl.pop(i)
        create(nl,ns)

seen=set()
n=list(input().strip())
create(n,[])
seen=sorted(list(seen))
print(len(seen))
for i in range(len(seen)):
    print(seen[i])
