t=int(input())
for _ in range(t):
    s=input()
    seen=set()
    i=0
    j=0
    res=float('inf')
    one=-1
    two=-1
    three=-1
    while i<len(s):
        if s[i]=="1":
            one=i
        elif s[i]=="2":
            two=i
        else:
            three=i
        i+=1
        if one!=-1 and two!=-1 and three!=-1:
            res=min(res,max(one,two,three)-min(one,two,three)+1)
    if res == float('inf'):
        print(0)
    else:
        print(res)