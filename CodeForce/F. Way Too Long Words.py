T = int(input())
for i in range(T):
    S = input()
    if len(S) > 10:
        print(S[0])
        abbreviation = S[0] + str(len(S) - 2) + S[-1]
        print(abbreviation)
        print(S[-1])
    elif len(S) < 10:
        print(S)