t=int(input())
for k in range(t):
    o=input()
    x=input()
    count=0
    if x :
        count+=2
    for i in range(1,len(x)):
        if x[i] in x[0:i]:
            count+=1
        else:
            count+=2
    print(count)
