N=int(input())
array=[]
for i in range(N):
    data=input().split()
    array.append([data[0], int(data[1])])  # 이름은 그대로, 숫자는 정수로 변환하여 리스트에 추가합니다.

array=sorted(array,key=lambda student: student[1])
for student in array:
    print(student[0], end=' ')