n=int(input())
a=list(map(int,input().split()))
s=set()
new_a=[]
for i in range(n-1,-1,-1):
    if a[i] not in s:
        s.add(a[i])
        new_a.append(a[i])
print(len(new_a))
print(*new_a[::-1])