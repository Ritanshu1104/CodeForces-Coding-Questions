# Read input string
username = input()

# Use a set to find distinct characters
distinct_chars = set(username)

# Check if the number of distinct characters is even or odd
if len(distinct_chars) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
