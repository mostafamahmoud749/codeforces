def count(indx):
    if indx==len(n):
        return 0
    if n[indx]=="7" or n[indx]=="4":
        return 1+count(indx+1)
    return count(indx+1)

n=input()
res=count(0)
print("YES") if res==4 or res==7 else print("NO")