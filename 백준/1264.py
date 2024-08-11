while True:
    line=input()
    if line == "#":
        break
    vowels='aeiouAEIOU'
    count=0
    for char in line: #line의 문자열을 기준으로 탐색
        if char in vowels: #문자가 vowels에 있는 모음일 시
            count += 1 #count 1 더함
    print(count)