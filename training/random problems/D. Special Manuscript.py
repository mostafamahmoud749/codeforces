s = input()
db = {0: 1}
p = 0
c = 0

for i in s:
    p += int(i) - 1
    c += db.get(p, 0)
    db[p] = db.get(p, 0) + 1

if c>=(len(s) + 1)//2:
    print("YES")
else:
    print("NO")
