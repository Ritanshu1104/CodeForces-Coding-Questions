import sys

def solve():
    # Reading input values k, l, m, n, d
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        k = int(input_data[0])
        l = int(input_data[1])
        m = int(input_data[2])
        n = int(input_data[3])
        d = int(input_data[4])
        
        damaged_count = 0
        
        # Iterate through every dragon from 1 to d
        for i in range(1, d + 1):
            # Check if dragon 'i' is affected by any condition
            if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
                damaged_count += 1
        
        print(damaged_count)
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
