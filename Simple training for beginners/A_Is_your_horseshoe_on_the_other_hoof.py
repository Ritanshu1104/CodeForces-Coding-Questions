# Read input and store colors in a set to find unique values
colors = set(map(int, input().split()))

# The number to buy is 4 minus the number of unique colors
print(4 - len(colors))
