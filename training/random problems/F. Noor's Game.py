n=int(input())
y=list(map(int,input().split()))
noor=0
abdo=0
i = 0 
j = n - 1 
while i <= j:
    if len(y)==1:  
        noor += y[i]  
        break
    if y[i] > y[j]:
        noor += y[i]  
        i += 1  
        y[i],y[j]=y[j],y[i]
    else:
        abdo += y[j]  
        j -= 1  
        y[i],y[j]=y[j],y[i]
if noor >= abdo:
    print("YES")
else:
    print("NO")