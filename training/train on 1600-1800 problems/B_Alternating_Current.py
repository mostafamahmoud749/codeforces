a=list(input().strip())
s=[]
for i in range(len(a)):
    if s and s[-1]==a[i]:
        s.pop()
    else:
        s.append(a[i])
print("YES") if not s else print("NO")