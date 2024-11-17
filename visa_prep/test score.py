def is_possible_to_score(N,X,Y):
    for i in range(2 ** N):
        total_score = 0
        for j in range(N):
            if i & (1 << j):
                total_score += X
        if total_score == Y:
            return "YES"
    return "NO"
N,X,Y = map(int, input().split())
print(is_possible_to_score(N,X,Y))
