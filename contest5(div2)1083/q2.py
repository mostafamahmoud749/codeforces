t = int(input())
for _ in range(t):
    n = int(input())
    k = 1
    tem = n
    i = 2
    while i * i <= tem:
        if tem % i == 0:
            k *= i
            while tem % i == 0:
                tem //= i
        i += 1
    if tem > 1:
        k *= tem
    print(k)