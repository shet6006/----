from collections import deque

# deque 객체로 변환
array = deque(map(int, input().split()))

# 정렬
array = deque(sorted(array))
count=0
result=0
for i in array:
    count += 1
    if count >= i:
        result += 1
        count = 0
        
print(result)
