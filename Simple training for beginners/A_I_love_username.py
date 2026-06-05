def solve():
    n = int(input())
    scores = list(map(int, input().split()))
    
    if n <= 1:
        print(0)
        return

    min_score = scores[0]
    max_score = scores[0]
    amazing_count = 0
    
    for i in range(1, n):
        if scores[i] > max_score:
            amazing_count += 1
            max_score = scores[i]
        elif scores[i] < min_score:
            amazing_count += 1
            min_score = scores[i]
            
    print(amazing_count)

solve()
