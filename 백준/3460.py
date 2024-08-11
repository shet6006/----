T=int(input())

for _ in range(T):
    n=int(input())
    bin_n=bin(int(n))[2:] #13이면 1101
    for i in range(len(bin_n)):
        if bin_n[-i-1] == '1': #역순으로 탐색
            print(i, end =" ")
