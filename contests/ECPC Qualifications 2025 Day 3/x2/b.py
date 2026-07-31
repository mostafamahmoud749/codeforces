def sieve(n):
    p = [True] * (n + 1)
    p[0] = p[1] = False

    for i in range(2,int(n**.5)+1):
        if p[i] :
            for j in range(i*i , n + 1 , i):
                p[j] = False
    return p

n = int(input())
primes = sieve(n)

# print(primes)

ans = [-1]

if primes[n - 2]:
    ans = [2,n-2]
else:
    for i in range(3,n+1,2):
        if primes[i] and primes[n - i]:
            ans = [i,n-i]
print(*ans)

