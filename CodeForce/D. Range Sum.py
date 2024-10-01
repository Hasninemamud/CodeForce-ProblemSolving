T = int(input())

for i in range(T):
    L, R = map(int,input().split())
    sum = 0
    for j in range(L,R):
        sum += j
    print(sum)


