# Read n and k
n, k = map(int, input().split())

# Read the scores list
scores = list(map(int, input().split()))

# The score of the k-th place finisher (using 0-indexing)
threshold_score = scores[k-1]

count = 0
for score in scores:
    # Check if the score meets both conditions
    if score >= threshold_score and score > 0:
        count += 1
    else:
        # Since the list is sorted, we can stop early if conditions aren't met
        break

print(count)
