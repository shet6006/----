# import sys
# input = sys.stdin.readline

# N, M = map(int, sys.stdin.readline().split())
# array = []

# # 각 행의 요소를 입력 받아 2차원 배열에 추가
# for _ in range(N):
#     row = list(map(int, sys.stdin.readline().split()))
#     array.append(row)

# K = int(sys.stdin.readline())
# for _ in range(K):
#     i, j, x, y = map(int, sys.stdin.readline().split())
#     sum = 0
#     for c in range(i - 1, x):
#         for d in range(j - 1, y):
#             sum += array[c][d]
#     print(sum)
# import sys
# input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(N)]

# 누적 합 배열 계산
prefix_sum = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        prefix_sum[i][j] = array[i-1][j-1] + prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1]

# 쿼리 처리
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = (prefix_sum[x][y] 
              - prefix_sum[i-1][y] 
              - prefix_sum[x][j-1] 
              + prefix_sum[i-1][j-1])
    print(result)
#시간초과 문제 해결 위해 prefix sum 배열 생성