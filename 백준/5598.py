##############틀린 풀이############
# # 알고리즘
# # 딕셔너리 a키에d입력 입력에 해당하는 value출력
# caesar={'A':'D', 'B':'E'}
# n=input()
# value=[caesar[char] for char in n] #입력받은 n을 char단위로 끝까지 caesar의 key를 순회하여 value를 얻는다
# print(''.join(map(str, value)))
##############맞은 풀이############
n=input()
ans=''
for i in n: #각 문자열 순회
    if i in 'ABC':
        ans+=chr(ord(i)+23) #ord:아스키 코드 값 반환, chr:아스키코드 값 문자 변환
    else:                   #아스키코드 3개만큼 빼주면 D가 A가 될 수 있으므로 변환 후 
        ans+=chr(ord(i)-3)
print(ans)
