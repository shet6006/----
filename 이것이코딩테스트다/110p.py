# N=int(input())
# # array = [[0 for _ in range(N)] for _ in range(N)] #외우기
# x,y=1,1
# lists=input().split()
# #R일경우 array[0][+1]
# #L일경우 array[0][-1]
# #U일경우 array[-1][0]
# #D일경우 array[+1][0]
# print(len(lists))
# for i in range(len(lists)):
#     if lists[i]=='R':
#         y+=1
#     if lists[i]=='L':
#         y-=1
#     if lists[i]=='U':
#         x-=1
#     if lists[i]=='D':
#         x+=1
# print(x,y)
# #공간 벗어나는 경우에 대해 구현 힘드므로 다른방식

N=int(input())
x,y=1,1
plans=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]
move=['L','R','U','D']

for plan in plans:
    #문자열 그대로 비교
    for i in range(len(move)):
        if plan == move[i]: #'R'이라는 문자가 들어오면 move를 순회해서 R찾기
            nx=x+dx[i] #임시로 nx와 ny값 저장
            ny=y+dy[i]
    if nx<1 or ny <1 or nx > N or ny > N:
        continue
    x,y=nx,ny
print(x,y)