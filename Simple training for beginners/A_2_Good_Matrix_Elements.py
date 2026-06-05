import sys

def solve():
    # Read n and the matrix
    try:
        input_data = sys.stdin.read().split()
        if not input_data:
            return
        
        n = int(input_data[0])
        matrix_elements = list(map(int, input_data[1:]))
        
        # Reshape flat list into a 2D list
        matrix = []
        for i in range(n):
            matrix.append(matrix_elements[i*n : (i+1)*n])
        
        total_sum = 0
        mid = n // 2  # Index of the middle row/column
        
        for i in range(n):
            for j in range(n):
                # Condition 1: Main diagonal (i == j)
                # Condition 2: Secondary diagonal (i + j == n - 1)
                # Condition 3: Middle row (i == mid)
                # Condition 4: Middle column (j == mid)
                if i == j or (i + j == n - 1) or i == mid or j == mid:
                    total_sum += matrix[i][j]
                    
        print(total_sum)
        
    except EOFError:
        pass

if __name__ == "__main__":
    solve()
