# 입력 받기
input_str = input()

# 입력 문자열을 공백을 기준으로 분리
date_str, time_str = input_str.rsplit(' ', 1)  # 뒤에서 한 번만 공백을 기준으로 분리
month_day, year = date_str.split(', ')

# 월과 일을 분리
month, day = month_day.split()
day = int(day)  # day에서 콤마 제거
year=int(year)
# 시간과 분을 ':' 기준으로 분리하고 정수로 변환
hour, minute = map(int, time_str.split(':'))
if (year%400==0) or (year%4==0 and year%100!=0):
    month_days = {
    'January': 31,
    'February': 29,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
    year_day=366
else:
    month_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
    year_day=365

# 월 리스트 순서대로
months_order = ['January', 'February', 'March', 'April', 'May', 'June', 
                'July', 'August', 'September', 'October', 'November', 'December']

# 누적 합 계산
total_days = 0
for m in months_order:
    if m == month:
        break
    total_days += month_days[m]

# 백분율 계산
days_ratio = ((total_days + day - 1) / year_day) * 100
hours_ratio = (hour / (year_day * 24)) * 100
minutes_ratio = (minute / (year_day * 24 * 60)) * 100

# 최종 백분율 합산
total_ratio = days_ratio + hours_ratio + minutes_ratio

print(total_ratio)