N = int(input())
A = list(map(int,input().split()))
for i in A:
    if A[i] < 0:
        A[i] = 2
    elif A[i] > 0:
        A[i] = 1
    else:
        A[i] = 0
print(" ".join(map(str,A)))
