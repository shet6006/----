N = input().split()
N = [int(item) for item in N]
M = N[1]

importance = input().split()
importance = [int(item) for item in importance]

# 문서의 중요도와 인덱스를 함께 저장
queue = [(i, importance[i]) for i in range(len(importance))]
count = 0

while len(queue) != 0:
    while True:
        moved = False
        for i in ra햣nge(1, len(queue)):
            if queue[0][1] < queue[i][1]:
                queue.append(queue.pop(0))
                moved = True
                break
        else:
            break
    
    # 현재 가장 높은 중요도를 가진 문서 처리
    current = queue.pop(0)
    count += 1
    
    # 만약 이 문서가 우리가 찾는 문서라면 출력하고 종료
    if current[0] == M:
        print(count)
        break
