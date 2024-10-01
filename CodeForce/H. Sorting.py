N = int(input())
A = list(map(int,input().split()))
B = []
for i in range(N):
    B.append(A[i])
print(sorted(B))

