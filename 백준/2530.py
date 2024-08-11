hour,minute,second=map(int,input().split())
time_second=int(input())
# 초 업데이트
second += time_second
# 초가 60 이상일 때, 분으로 전환
minute += second // 60
second = second % 60
# 분이 60 이상일 때, 시간으로 전환
hour += minute // 60
minute = minute % 60
# 시간이 24 이상일 때, 24시간 형식으로 전환
hour = hour % 24
print(hour,minute,second)