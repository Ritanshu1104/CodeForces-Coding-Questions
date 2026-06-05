import sys

def solve():
    # Read n and m from input
    line = sys.stdin.readline()
    if not line:
        return
    n, m = map(int, line.split())
    
    count = 0
    # Iterate through all possible values of 'a'
    # Since n <= 1000, a won't exceed 32 (32^2 = 1024)
    for a in range(1001):
        b = n - (a**2)
        if b >= 0:
            if a + (b**2) == m:
                count += 1
                
    print(count)

if __name__ == "__main__":
    solve()
