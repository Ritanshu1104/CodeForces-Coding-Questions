s = input().strip()

# Find the lexicographically largest character
max_char = max(s)

# Count its occurrences
count = s.count(max_char)

# Print that character repeated 'count' times
print(max_char * count)
