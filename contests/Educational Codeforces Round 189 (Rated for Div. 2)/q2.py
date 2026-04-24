t=int(input())
for _ in range(t):
    s=input()
    b2=0
    a2=0
    i=0
    while i<len(s)-1:
        if s[i]==s[i+1]:
            if s[i]+s[i+1]=="aa":
                a2+=1
            else:
                b2+=1
        i+=1
    print("YES") if a2+b2<=2 else print("NO")
