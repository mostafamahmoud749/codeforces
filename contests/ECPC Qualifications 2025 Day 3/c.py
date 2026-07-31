import sys
input = lambda: sys.stdin.readline().rstrip()  # strip the trailing newline
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))


n,m=LII()
a=LII()
b=LII()

b.sort()

seg=[]
j=0
st=set()
for i in range(n):
    st.add(a[i])
    if j<m and i==b[j]-1:
        seg.append(len(st))
        st.clear()
        j+=1
seg.append(len(st))

p=[0]*(len(seg)+1)
for i in range(1,len(seg)+1):
    p[i]=seg[i-1]+p[i-1]


b=[0]+b+[n]
res=p[-1]

for i in range(m):
    x=len(set(a[b[i]:b[i+2]]))
    cur=p[-1]-seg[i]-seg[i+1]+x
    res=min(res,cur)

# print(p)
# print(b)

print(res)