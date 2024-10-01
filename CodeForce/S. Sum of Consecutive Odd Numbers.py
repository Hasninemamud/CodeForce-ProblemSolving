
T = int(input())

for i in range(T):
    X, Y = map(int,input().split())
    if X > Y:
        X,Y = Y,X
    sum = 0
    for i in range(X+1,Y):
        if i % 2 != 0:
            sum += i
        else:
            pass
    print(sum) 
   