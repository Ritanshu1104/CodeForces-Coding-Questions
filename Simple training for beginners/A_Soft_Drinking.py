# Read input values
n, k, l, c, d, p, nl, np = map(int, input().split())

# Calculate toasts possible by each resource
drink_toasts = (k * l) // nl
lime_toasts = c * d
salt_toasts = p // np

# Find the overall minimum and divide by the number of friends
ans = min(drink_toasts, lime_toasts, salt_toasts) // n

print(ans)
