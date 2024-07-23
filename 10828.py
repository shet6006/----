# 알고리즘
# push, pop, size, empty, top 명령어
#stack: lifo
import sys

N=int(sys.stdin.readline())
stack=[]
for i in range(N):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        order[1]=int(order[1])
    if order[0]=='push':
        stack.append(order[1])
    elif order[0]=='pop':
        if len(stack) >0:
            print(stack.pop())
        elif len(stack) == 0:
            print(-1)
    elif order[0]=='size':
        print(len(stack))
    elif order[0]=='empty':
        if len(stack)==0:
            print(1)
        elif len(stack)!=0:
            print(0)
    elif order[0]=='top':
        if len(stack) > 0:
            print(stack[-1])
        elif len(stack) == 0:
            print(-1)