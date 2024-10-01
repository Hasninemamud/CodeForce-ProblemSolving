N = int(input())
A = list(map(int,input().split()))
min_index = A.index(min(A))
max_index = A.index(max(A))

A[min_index], A[max_index] = A[max_index], A[min_index]
print(" ".join(map(str, A)))