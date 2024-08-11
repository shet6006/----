# lists=[]
# row_mins=[]
# N,M=map(int,input().split())
# for i in range(N):
#     row=list(map(int,input().split()))
#     lists.append(row)  # 각 행을 lists에 추가
#     print(lists)
    
# for i in range(N):
#     row_min=min(lists[i])
#     row_mins.append(row_min)
# print(max(row_mins))

#모범답안
N,M=map(int,input().split())
result=0
for i in range(N):
    data=list(map(int,input().split()))
    min_value=min(data) #데이터를 입력받음과 동시에 가장 작은 수 찾기
    result=max(result,min_value) #result와 min_value를 비교하여 가장 큰 수 초기화
print(result)