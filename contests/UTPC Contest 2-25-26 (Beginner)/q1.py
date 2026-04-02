n,c1,c2=map(str,input().split())
n=int(n)
r1=c1[0]
c1=int(c1[1:])
r2=c2[0]
c2=int(c2[1:])
if r1==r2:
	print(abs(c1-c2))
else:
	print(abs(ord(r1)-ord(r2))+min(c1+c2,n+1-c1+n+1-c2))