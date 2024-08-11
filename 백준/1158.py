# list=[1,3,4,5,6]
# list.pop(3)
# print(list)
S=[]
results=[]
N, K = map(int, input().split())
for i in range(N):
    S.append(i+1)
index = 0
while len(S) > 0:
    index = (index + K - 1) % len(S)  # 실제 제거할 인덱스를 계산
    results.append(S.pop(index))  # 제거하고 제거된 요소를 출력

output = "<" + ", ".join(map(str, results)) + ">"
print(output)
