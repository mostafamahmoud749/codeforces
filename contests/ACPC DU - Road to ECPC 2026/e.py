t=int(input())
for _ in range(t):
    a=list(input().strip())
    b=list(input().strip())
    i=1
    j=1
    s=True

    if b[0]!=a[0]:
        s=False
    
    while j<len(b) and i<len(a):
        if b[j]!=a[i]:
            while j<len(b) and b[j]==a[i-1]:
                j+=1
        if j>=len(b) or a[i]!=b[j]:
            s=False
            break
        i+=1
        j+=1
        
    while j<len(b) and i<=len(a) and b[j]==a[i-1]:
        j+=1
    
    if i!=len(a) or j!=len(b):
        s=False
    print("YES") if s else print("NO")