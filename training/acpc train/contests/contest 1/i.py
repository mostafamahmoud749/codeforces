import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

n=II()
a=[]
for i in range(n):
  a.append(input())

c1={}
c2={}

for i in range(0,n,2):
  for c in range(65,92):
    ch=chr(c)
    if ch in c1:
      c1[ch]=max(c1[ch],a[i].count(ch))
    else:
      c1[ch]=a[i].count(ch)

for i in range(1,n,2):
  for c in range(65,92):
    ch=chr(c)
    if ch in c2:
      c2[ch]=max(c2[ch],a[i].count(ch))
    else:
      c2[ch]=a[i].count(ch)


res=0

for k in c1:
  res+=c1[k]

for k in c2:
  res+=c2[k]

print(res)