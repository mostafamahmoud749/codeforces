n=int(input())
a=list(map(str,input().split()))
count_1=a.count("1")
count_2=a.count("2")
new_a=[]
first=False
i=1
if count_2>0:
    new_a.append("2")
    count_2-=1
    i+=1
    first=True

while i<=n:
    if first==True and i<=2 and count_1>0:
        new_a.append("1")
        count_1-=1
    elif first==False and i<=3 and count_1>0:
        new_a.append("1")
        count_1-=1
    elif count_2>0:
        new_a.append("2")
        count_2-=1
    elif count_1>0:
        new_a.append("1")
        count_1-=1
    i+=1
print(*new_a)