a=list(input().strip())
b=list(input().strip())
c=0
for i in range(min(len(a),len(b))):
    if a[-1-i]==b[-1-i]:
        c+=2
    else:
        break

print(len(a)+len(b)-c)