s=input()
if len(s)<26:
    print(-1)
else:
    i=0
    j=0
    c=0
    db={}
    seen=set()
    m=0
    mindxs=[0,0]
    while i<len(s):
        if s[i]=="?":
            c+=1
            i+=1
        elif s[i] not in seen:
            seen.add(s[i])
            i+=1
            c+=1
        else:
            while s[i] in seen:
                if s[j]!="?":
                    seen.remove(s[j])
                j+=1
                c-=1
            seen.add(s[i])
            c+=1
            i+=1
        if c>m:
            mindxs[0]=j
            mindxs[1]=i
            m=c
        if m==26:
            break
    s=list(s)
    if m<26:
        print(-1)
    else:
        letters=[-1]*26
        for i in range(mindxs[0],mindxs[1]):
            if s[i]!="?":
                letters[ord(s[i])-65]=s[i]
        for i in range(mindxs[0],mindxs[1]):
            if s[i]=="?":
                s[i]=chr(letters.index(-1)+65)
                letters[letters.index(-1)] = s[i]
        for i in range(len(s)):
            if s[i]=="?":
                s[i]="A"
        print("".join(s))
