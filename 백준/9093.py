T=int(input())
results=[]
for _ in range(T):
    S=input().split()
    for i in range(len(S)):
        S[i]=S[i][::-1]
    results.append(' '.join(S)) #나눠져있는 리스트 S(ex: ['i', 'ma', 'nowgnod']을 ' '를 기준으로 하나로 합침 ex: ['i ma nowgnod'])
for result in results:
    print(result)

#단어의 갯수마다 반복문 돌면서 뒤집기