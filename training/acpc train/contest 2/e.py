t=int(input())
for _ in range(t):
    l,r=map(int,input().split())
    if r.bit_length()>l.bit_length():
        if r.bit_count()>r.bit_length()-1:
            print(r)
        else:
            print(int("1"*(r.bit_length()-1),2))
    else:
        rbits=bin(r)[2:]
        lbits=bin(l)[2:]
        s=False
        newnum=""
        for i in range(0,len(rbits)):
            if rbits[i]=="1" and lbits[i]=="0" and s ==False:
                s=True
                newnum=newnum+"0"
            elif s:
                newnum=newnum+"1"
            elif rbits[i]=="1":
                newnum=newnum+"1"
            else:
                newnum=newnum+"0"
        if int(newnum,2).bit_count() >= r.bit_count():
            print(int(newnum,2))
        else:
            print(r)





    # res=0
    # c=0
    # if l.bit_length()<r.bit_length():
    #     if r.bit_count()>r.bit_length()-1:
    #         res=r.bit_count()
    #         c=r
    #     else:
    #         res=r.bit_length()-1
    #         c=l
    # else:
    #     for i in range(l,r):
    #         if i.bit_count()>res:
    #             c=i
    #             res=i.bit_count()
    # print(c)