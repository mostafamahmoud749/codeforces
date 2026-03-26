n=int(input())
s=input()
x=[]
for i in range(len(s)-1):
    x.append(s[i]+s[i+1])
res=x[0]
freq=1
for i in x:
    cur_freq=x.count(i)
    if cur_freq>freq:
        res=i
        freq=cur_freq
print(res)