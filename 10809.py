# 알고리즘
# 단어 쪼개기
# a~z까지의 문자 중 어떤것에 해당하는지 찾기

# S=input()
# # for char in S:
# #     n.append(char)
# n=list(S) #위의 방법처럼 안하고 list(S)를 써서 한글자씩 넣을수있음
#더 줄여서
S=list(input()) #처럼 사용
alphabet='abcdefghijklmnopqrstuvwxyz'

# for i in range(len(S)):
#     char=S[i] #char에 n[i]번째 문자 저장
#     if char in alphabet: #알파벳 문자열에 char문자가 들어있다면
#         index=alphabet.index(char) #index라는 값에 알파벳에서 char문자가 들어있는 문자번호값 저장

for i in alphabet:
    if i in S:
        print(S.index(i), end = ' ')  ###문자에 대해 반복하고 있으므로 S[i]로하면 안됨(i가 문자임)
        #따라서 알파벳 i번째의 문자를 가지고있는 S의 index(위치)를 출력해줘야함
    else:
        print(-1, end = ' ')    