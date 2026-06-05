import sys

def solve():
    # Read n from input
    line = sys.stdin.read().split()
    if not line:
        return
    n = int(line[0])

    # If n is odd, no perfect permutation exists
    if n % 2 != 0:
        print("-1")
    else:
        # Generate pairs (2, 1), (4, 3), (6, 5)...
        result = []
        for i in range(1, n + 1, 2):
            result.append(str(i + 1))
            result.append(str(i))
        
        print(" ".join(result))

if __name__ == "__main__":
    solve()
