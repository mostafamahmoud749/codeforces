t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    max_player_postion=0
    cur_postion=0
    i=0
    while i<n:
        if s[cur_postion]=="R":
            cur_postion+=1
        else:
            cur_postion-=1
        max_player_postion=max(max_player_postion,cur_postion)
        i+=1
    print(max_player_postion+1)