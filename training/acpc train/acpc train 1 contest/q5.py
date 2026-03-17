s=input()
h=0
res=0
for i in range(len(s)-4):
    word=s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]
    if word=="heavy":
        h+=1
    elif word=="metal":
        res+=h
print(res)