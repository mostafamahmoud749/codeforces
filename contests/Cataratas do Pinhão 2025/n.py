n=int(input())
a=list(map(int,input().split()))
o=0
t=0
for i in a:
    if i==1:
        o+=1
    else:
        t+=1

if o>t:
    print("Cataratas do Pinhao")
elif t>o:
    print("Pinhao das Cataratas")
else:
    print("Cascatiba?")