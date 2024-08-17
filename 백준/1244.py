n = int(input())  # 스위치 개수
student = []
switch = list(map(int, input().split()))  # 스위치 상태 입력받기
boolean_switch = [bool(x) for x in switch]  # Boolean 리스트로 변환
student_num = int(input())  # 학생 수

# 학생들 입력받기
for i in range(student_num):
    student.append(list(map(int, input().split())))  # 각 학생의 성별과 숫자

# 스위치 조작
for i in range(len(student)):
    if student[i][0] == 1:  # 남자 학생의 경우
        for j in range(1, len(boolean_switch) + 1):
            if j % student[i][1] == 0:
                boolean_switch[j - 1] = not boolean_switch[j - 1]
    else:  # 여자 학생의 경우
        index = student[i][1] - 1  # 여자 학생이 받은 숫자에 해당하는 인덱스
        boolean_switch[index] = not boolean_switch[index]  # 자기 자신을 먼저 뒤집기

        # # 좌우 대칭으로 뒤집기
        # left = index - 1
        # right = index + 1

        # while left >= 0 and right < len(boolean_switch):
        #     if boolean_switch[left] == boolean_switch[right]:
        #         boolean_switch[left] = not boolean_switch[left]
        #         boolean_switch[right] = not boolean_switch[right]
        #         left -= 1
        #         right += 1
        #     else:
        #         break

# 최종 결과 출력
result = [int(x) for x in boolean_switch]  # Boolean 리스트를 정수 리스트로 변환

for i in range(1, n + 1):
    print(result[i - 1], end=" ")  # 인덱스를 0부터 시작하게 조정
    if i % 20 == 0:
        print()  # 20번째마다 줄바꿈
