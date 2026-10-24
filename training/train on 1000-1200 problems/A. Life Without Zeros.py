a=int(input())
b=int(input())

c=a+b

newa=str(a).replace("0","")
newb=str(b).replace("0","")
newc=str(c).replace("0","")

print("YES") if int(newa)+int(newb)==int(newc) else print("NO")