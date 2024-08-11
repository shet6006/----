n=int(input())
number=list(map(int,input().split()))
number=number[:n] #n개까지 슬라이싱
print(min(number), max(number))