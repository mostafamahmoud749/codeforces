L={
    "km":100000,
    "m":100,
    "cm":1,
}

W={
    "t":1000000,
    "kg":1000,
    "g":1,
}
numbs=["0","1","2","3","4","5","6","7","8","9"]
t=int(input())
for _ in range(t):
    wsum=0
    lsum=0
    n=int(input())
    items=input().split()
    for i in range(n):
        key=""
        value=""
        for j in items[i]:
            if j not in numbs:
                key+=j
            else:
                value+=j
        if key in L:
            lsum+=L[key]*int(value)
        else:
            wsum+=W[key]*int(value)

    print(f"{lsum/100:.2f}")
    print(f"{wsum/1000:.2f}")