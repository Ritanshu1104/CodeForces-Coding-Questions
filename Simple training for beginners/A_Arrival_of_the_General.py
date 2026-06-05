def solve():
    n = int(input())
    heights = list(map(int, input().split()))

    # Find max height and its leftmost index
    max_h = max(heights)
    max_idx = heights.index(max_h)

    # Find min height and its rightmost index
    min_h = min(heights)
    # Reverse the list to find the first occurrence from the right
    min_idx = (n - 1) - heights[::-1].index(min_h)

    # Calculate swaps
    # max_idx is swaps needed to reach index 0
    # (n - 1 - min_idx) is swaps needed to reach the last index
    swaps = max_idx + (n - 1 - min_idx)

    # If max was to the right of min, they cross, reducing total swaps by 1
    if max_idx > min_idx:
        swaps -= 1

    print(swaps)

if __name__ == "__main__":
    solve()
