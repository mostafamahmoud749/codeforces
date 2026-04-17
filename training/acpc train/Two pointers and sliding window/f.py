n=int(input())
a=list(map(int,input().split()))
s=set()
m=0
j=0
for i in range(n):
    while a[i] in s:
        s.remove(a[j])
        j+=1
    s.add(a[i])
    m=max(len(s),m)
print(m)