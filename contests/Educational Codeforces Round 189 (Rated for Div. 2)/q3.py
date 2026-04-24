t=int(input())
for _ in range(t):
    n=int(input())
    a1=input()
    a2=input()
    redl=0
    redd=0
    for i in range(0,n):
        if i%2!=0:
            if a1[i]=="R":
                redl+=1
            if a2[i]=="R":
                redd+=1
        else:
            if a1[i]=="R":
                redd+=1
            if a2[i]=="R":
                redl+=1
    print(abs(redd-redl))