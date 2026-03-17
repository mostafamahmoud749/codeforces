t = int(input())
for _ in range(t):
	n = int(input())
	c = [0] * n
	p = [0] * n
	for i in range(n):
		c[i], p[i] = map(int, input().split())
	dp=0.0
	for i in range(n-1,-1,-1):
		q=1.0-p[i]/100.0
		do=c[i]+q*dp
		skip= dp
		if do > skip:
			dp = do
		else:
			dp = skip
	print(f"{dp:.10f}")