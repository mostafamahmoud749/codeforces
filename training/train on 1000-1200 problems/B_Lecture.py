n,m=map(int,input().split())
words={}
for i in range(m):
    w1,w2=map(str,input().split())
    if len(w1)>len(w2):
        words[w1]=w2
    else:
        words[w2]=w1
sentence=list(map(str,input().split()))
new_sentence=[]
for i in sentence:
    if i in words:
        new_sentence.append(words[i])
    else:
        new_sentence.append(i)
print(*new_sentence)