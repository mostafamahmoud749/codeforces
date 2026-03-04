def elsepart():
    for i in range(lenBA):
        for j in range(lenAB):
            if abs(db["BA"][i] - db["AB"][j]) >= 2:
                return True
    return False

res=False
s=input()
db={"AB":[],"BA":[]}
for i in range(len(s)-1):
    curstr=s[i]+s[i+1]
    if curstr in ["AB","BA"]:
        db[curstr].append(i)
lenAB=len(db["AB"])
lenBA=len(db["BA"])
if lenAB==0 or lenBA==0:
    res=False
else:
    res=elsepart()

if res:
    print("YES")
else:
    print("NO")