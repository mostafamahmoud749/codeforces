def count(indx,c,res):
    if indx<0:
        return res
    if n[indx]==1:
        c+=1
        res=res+(2**(len(n)-indx-1))
    return count(indx-1,c,res)


n=list(input().strip())
for i in range(len(n)):
    if int(n[i])>1:
        n[i:]=[1]*(len(n)-i)
        break
    else:
        n[i]=int(n[i])
res=count(len(n)-1,0,0)
print(res)