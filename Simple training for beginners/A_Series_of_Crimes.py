import sys

def solve():
    # Read n and m
    try:
        line = sys.stdin.readline().split()
        if not line: return
        n, m = map(int, line)
    except ValueError:
        return

    rows = []
    cols = []

    # Find the coordinates of the three '*'
    for i in range(n):
        row_str = sys.stdin.readline().strip()
        for j in range(len(row_str)):
            if row_str[j] == '*':
                rows.append(i + 1)  # 1-based indexing
                cols.append(j + 1)

    # The missing coordinate is the one that occurs exactly once
    ans_r = 0
    ans_c = 0

    if rows[0] == rows[1]: ans_r = rows[2]
    elif rows[0] == rows[2]: ans_r = rows[1]
    else: ans_r = rows[0]

    if cols[0] == cols[1]: ans_c = cols[2]
    elif cols[0] == cols[2]: ans_c = cols[1]
    else: ans_c = cols[0]

    print(f"{ans_r} {ans_c}")

if __name__ == "__main__":
    solve()
