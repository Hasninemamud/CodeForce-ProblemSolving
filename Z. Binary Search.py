N, Q = map(int,input().split())
A = list(map(int,input().split()))
A_set = set(A)
for j in range(Q):
    X = int(input())
    if X in A:
        print("found")
    else:
        print("not found")
    