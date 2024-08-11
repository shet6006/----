dx=[-1,0,1,0]
dy=[0,1,0,-1]
N, M = map(int, input().split())
A, B, direc=map(int, input().split())
d = [[0] * M for _ in range(N)]
d[A][B] = 1
array=[]
for i in range(int(N)):
    array.append(list(map(int,input().split())))
    
#왼쪽으로 회전
def turn_left():
    global direc
    direc -= 1
    if direc == -1:
        direc = 3
#시뮬레이션 시작
count=1
turn_time=0
while True:
    turn_left()
    nx=A+dx[direc]
    ny=B+dy[direc]
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny]=1
        A=nx
        B=ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx=A-dx[direc]
        ny=B-dy[direc]
        if array[nx][ny] == 0:
            A=nx
            B=ny
        else:
            break
        turn_time = 0
print(count)
#왼쪽으로 회전
#회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#회전한 이후 정면에 가보지 않은 칸이 없거나 바다인경우
#네 방향 모두 갈 수 없는 경우
#뒤로 갈 수 있으면 이동하기
#뒤로 바다가 막혀있는경우

#정답 출력
