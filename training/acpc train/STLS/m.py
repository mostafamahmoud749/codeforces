# wrong
n,k=map(int,input().split())
a=list(map(int,input().split()))
done=0
for i in range(n):
	s = False
	for j in range(0, n - i - 1):
		if a[j] > a[j + 1]:
			a[j], a[j + 1] = a[j + 1], a[j]
			s = True
	done+=1
	if not s or done==k:
		break

print(*a)
