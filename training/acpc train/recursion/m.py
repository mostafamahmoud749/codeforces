db={}
def count(indx,la,crest):
    global res
    if (indx,la) in db and db[(indx,la)]<=crest:
        return
    db[(indx,la)]=crest
    if indx==n:
        res=min(res,crest)
        return
    if a[indx]==3:
        if la==1:
            count(indx+1,2,crest)
        elif la==2:
            count(indx+1,1,crest)
        else:
            count(indx+1,2,crest)
            count(indx+1,1,crest)
    elif a[indx]==0 or la==a[indx]:
        count(indx+1,0,crest+1)
    elif a[indx]==1:
        count(indx+1,1,crest)
    elif a[indx]==2:
        count(indx+1,2,crest)
    
n=int(input())
a=list(map(int,input().split()))
res=float("inf")
count(0,0,0)
print(res)