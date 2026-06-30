l,r=map(int,input().split())
res=0
for i in range(r.bit_length()-1,-1,-1):
    if ((l>>i)&1)!=((r>>i)&1):
        res=((1<<(i+1))-1)
        break
print(res)