N = int(input())
A = list(map(int,input().split()))
X = int(input())
if X in range(A):
    print(A.index(X))
else:
    print("-1")