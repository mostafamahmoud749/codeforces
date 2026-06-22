s=list(input().strip())
t=list(input().strip())
for i in range(len(s)-1,-1,-1):
    if s[i]!="z":
        s[i]=chr(ord(s[i])+1)
        break
    else:
        s[i]="a"
print("".join(s)) if "".join(s)<"".join(t) else print("No such string")
