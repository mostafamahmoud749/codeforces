t= int(input())
for _ in range(t):
    n=int(input())
    p1=input().split()
    p2=input().split()
    p3=input().split()

    scors={
        "p1":0,
        "p2":0,
        "p3":0
    }

    all_words = p1 + p2 + p3
    word_count = {}
    
    for w in all_words:
        if w in word_count:
            word_count[w] += 1
        else:
            word_count[w] = 1

    for i in range(n):
        for j, p in enumerate(["p1", "p2", "p3"]):
            w = [p1[i], p2[i], p3[i]][j]
            count = word_count[w]
            if count == 1:
                scors[p] += 3
            elif count == 2:
                scors[p] += 1

    print(scors["p1"],scors["p2"],scors["p3"])