n=int(input())
l=[True]*26
s=input()
s=set(s)
for i in s:
    l[ord(i)-97]=False
print(n//(l.index(True)+97)) if len(s)<26 else print(0)