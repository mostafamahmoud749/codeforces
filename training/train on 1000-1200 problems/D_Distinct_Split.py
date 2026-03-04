t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    left=[0]*n
    right=[0]*n
    seen=set()
    for i in range(n):
        seen.add(s[i])
        left[i]=len(seen)
    seen=set()
    for i in range(n-1,-1,-1):
        seen.add(s[i])
        right[i]=len(seen)
    res=0
    for i in range(n-1):
        res=max(res,left[i]+right[i+1])
    print(res)



    # maxval=0
    # count=0
    # added={}
    # for j in range(n):
    #     added[s[j]]=False
        
    # for i in range(0,n):
    #     existafter=s[i] in s[i+1:]
    #     existbeffor=s[i] in s[:i]
    #     if existafter and not added[s[i]]:
    #         count+=2
    #         added[s[i]]=True

    #     if not existafter and not existbeffor:
    #         count+=1
    #     if count>maxval:
    #         maxval=count
            
    #     if existbeffor and not existafter :
    #         count-=1
    # print(maxval)