n=input()
x=[]
if int(n[0])>=5 and int(n[0])!=9:
    x.append(9-int(n[0]))
else:
    x.append(int(n[0]))
for i in range(1,len(n)):
    if int(n[i])>=5 :
        x.append(9-int(n[i]))
    else:
        x.append(int(n[i]))
print(*x,sep="")
