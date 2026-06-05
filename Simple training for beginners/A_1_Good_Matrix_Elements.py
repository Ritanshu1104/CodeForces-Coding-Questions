n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

total_sum = 0
mid = n // 2

for i in range(n):
    for j in range(n):
        # Check if the element is "good"
        if i == j or i + j == n - 1 or i == mid or j == mid:
            total_sum += matrix[i][j]

print(total_sum)
