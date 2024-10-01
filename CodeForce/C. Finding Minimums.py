N, K =map(int,input().split())
numbers = list(map(int,input().split()))
for i in range(1,N,K):
    group = numbers[i:i+K]
    print(min(group))