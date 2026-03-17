t = int(input())
for _ in range(t):
	n, k, p, m = map(int, input().split())
	a = list(map(int, input().split()))
	w = a[p - 1]

	n_f = max(0, p - k)
	if n_f > 0:
		l = sorted(a[:p - 1])
		s_c = sum(l[:n_f])
	else:
		s_c = 0
	n_c = n - k
	other = a[:p - 1] + a[p:]
	if n_c > 0:
		c_c = sum(sorted(other)[:n_c])
	else:
		c_c = 0
	f = s_c + w
	if f > m:
		print(0)
		continue
	each_next = w + c_c
	print((m - s_c + c_c) // each_next)
