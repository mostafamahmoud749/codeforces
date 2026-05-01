import sys

sys.stdin = open("gates.in", "r")
sys.stdout = open("gates.out", "w")

n=int(input())
s=input()
visted_v=set()
visted_e=set()
x,y=0,0
visted_v.add((x,y))
for i in range(n):
    new_x,new_y=x,y
    if s[i]=="N":
        new_y+=1
    elif s[i]=="S":
        new_y-=1
    elif s[i]=="W":
        new_x-=1
    elif s[i]=="E":
        new_x+=1
    e=tuple(sorted(((x,y),(new_x,new_y))))
    visted_e.add(e)
    x,y=new_x,new_y
    visted_v.add((x,y))
print(len(visted_e)-len(visted_v)+1)