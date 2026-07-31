# from collections import deque



# n=int(input())
# s=input()

# res=[0]*(n+1)
# q=deque([])

# curo=0
# i=0
# while i<len(s):
#     if s[i].isdigit():
#         cur=""
#         while s[i].isdigit() and  i<len(s):
#             cur=cur+s[i]
#             i+=1
        
#         if q:
#             res[int(cur)]=q[-1]
#         q.append(int(cur))

#         if i==len(s):
#             break

#     elif s[i]=="(":
#         curo+=1
#         i+=1
#     elif s[i]==")":
#         if len(q)-1==curo:
#             q.pop()
#         curo-=1
#         i+=1

# print(*res[1:])

# from collections import deque



# n=int(input())
# s=input()

# j=0
# i=0

# l=[]
# while i<len(s):
#     if not s[i].isdigit():
#         if i!=j:
#             l.append(int(s[j:i]))
#         l.append(s[i])
#         j=i
#         i+=1
#     else:
#         i+=1

# print(l)

# res=[0]*(n+1)
# q=deque([])

# curo=0
# for i in range(len(s)):
#     if s[i].isdigit():
#         if q:
#             res[int(s[i])]=q[-1]
#         q.append(int(s[i]))
#     if s[i]=="(":
#         curo+=1
    
#     if s[i]==")":
#         if len(q)-1==curo:
#             q.pop()
#         curo-=1

# print(*res[1:])

from collections import deque
 
n=int(input())
s=input()
 
res=[0]*(n+1)
q=deque([])
 
curo=0
i = 0

while len(s) > i:

    num = ""
    while len(s) > i and s[i].isdigit()  :
        num += s[i]
        i += 1
        
    if num :
        if q:
            res[int(num)]=q[-1]
        q.append(int(num))

    if i == len(s):
        break
    
    if s[i]=="(":
        curo+=1
    
    if s[i]==")":
        if len(q)-1==curo:
            q.pop()
        curo-=1
    i += 1
print(*res[1:])