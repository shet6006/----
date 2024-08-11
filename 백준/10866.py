import sys

N=int(sys.stdin.readline())
deque=[]
for i in range(N):
    order = sys.stdin.readline().split()
    if len(order) > 1:
        order[1]=int(order[1])
    if order[0]=='push_front':
        deque.insert(0,order[1])
    if order[0]=='push_back':
        deque.append(order[1])
    if order[0]=='pop_front':
        if len(deque)>0:
            print(deque.pop(0))
        else:
            print(-1)
    if order[0]=='pop_back':
        if len(deque)>0:
            print(deque.pop())
        else:
            print(-1)
    if order[0]=='size':
        print(len(deque))
    if order[0]=='empty':
        if len(deque)>0:
            print(0)
        else:
            print(1)
    if order[0]=='front':
        if len(deque)>0:
            print(deque[0])
        else:
            print(-1)
    if order[0]=='back':
        if len(deque)>0:
            print(deque[-1])
        else:
            print(-1)
    ##파이썬에는 추가적으로 appendleft, popleft등이 있다
