import sys
input = lambda: sys.stdin.readline().rstrip()  
II = lambda: int(input())
LII = lambda: list(map(int, input().split()))

for _ in range(II()):
  a=[]
  for i in range(10):
    a.append(input())

  res=0

  for i in range(10):
    for j in range(10):
      if a[i][j]=="X":
        if i==0 or j==0 or i==9 or j==9:
          res+=1
        elif i==1 or j==1 or i==8 or j==8:
          res+=2
        elif i==2 or j==2 or i==7 or j==7:
          res+=3
        elif i==3 or j==3 or i==6 or j==6:
          res+=4
        else:
          res+=5
  print(res)