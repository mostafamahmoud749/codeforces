
primes=[]

for i in range(2,1001):
    s=True
    for j in range(2,i):
        if i%j==0:
            s=False
    if s:
        primes.append(i)

print(primes)