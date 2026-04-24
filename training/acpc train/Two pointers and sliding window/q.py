t=int(input())
for _ in range(t):
    n,l,r=map(int,input().split())
    a=list(map(int,input().split()))
    la=a[0:l]
    ra=a[l:n]
    la.sort()
    ra.sort()
    dbla=[]
    for v in la:
        if dbla and dbla[-1][0]==v:
            dbla[-1][1]+=1
        else:
            dbla.append([v,1])
    dbra=[]
    for v in ra:
        if dbra and dbra[-1][0]==v:
            dbra[-1][1]+=1
        else:
            dbra.append([v,1])
    i=0
    j=0
    while i<len(dbla) and j<len(dbra):
        if dbla[i][0]==dbra[j][0]:
            v=min(dbla[i][1],dbra[j][1])
            dbla[i][1]-=v
            dbra[j][1]-=v
            i+=1
            j+=1
        elif dbla[i][0]<dbra[j][0]:
            i+=1
        else:
            j+=1
    sl=0
    sr=0
    for i in range(len(dbla)):
        sl+=dbla[i][1]
    for i in range(len(dbra)):
        sr+=dbra[i][1]
    pl=0
    pr=0
    for i in range(len(dbla)):
        pl+=dbla[i][1]//2
    for i in range(len(dbra)):
        pr+=dbra[i][1]//2
    if sl>sr:
        res=sl-min((sl-sr)//2,pl)
    else:
        res=sr-min((sr-sl)//2,pr)
    print(res)


    # la.sort()
    # ra.sort()
    # dbla={}
    # dbra={}
    # for i in range(len(la)):
    #     dbla[la[i]]=dbla.get(la[i],0)+1
    # for i in range(len(ra)):
    #     dbra[ra[i]]=dbra.get(ra[i],0)+1
    # for key,count in dbla.items():
    #     if key in dbra:
    #         v=min(count,dbra[key])
    #         dbla[key]-=v
    #         dbra[key]-=v

    # print(dbla,dbra)