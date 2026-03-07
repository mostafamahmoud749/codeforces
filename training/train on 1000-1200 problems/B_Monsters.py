t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    nums=list(map(int,input().split()))
    db={}
    for i in range(n):
        if nums[i]<=k:
            if nums[i] in db:
                db[nums[i]].append(i+1)
            else:
                db[nums[i]]=[i+1]
        else:
            if nums[i]%k==0:
                if k in db:
                    db[k].append(i+1)
                else:
                    db[k]=[i+1]
            else:
                if (nums[i]-(nums[i]//k)*k) in db:
                    db[(nums[i]-(nums[i]//k)*k)].append(i+1)
                else:
                    db[(nums[i]-(nums[i]//k)*k)]=[i+1]
    res=[]
    for key in sorted(db.keys(),reverse=True):
        res.extend(db[key])
    print(*res)