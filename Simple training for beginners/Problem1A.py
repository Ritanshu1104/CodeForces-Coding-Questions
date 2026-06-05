# Read the number of problems
n = int(input())
count = 0

for _ in range(n):
    # Read the three views (0 or 1) and sum them
    views = sum(map(int, input().split()))
    
    # If two or more are sure, increment the count
    if views >= 2:
        count += 1

# Print the final total
print(count)
