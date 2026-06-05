def solve():
    # Read the length of the ticket
    n = int(input())
    # Read the ticket number as a string to handle leading zeros easily
    ticket = input().strip()
    
    # Condition 1: Check if all digits are lucky (4 or 7)
    for digit in ticket:
        if digit != '4' and digit != '7':
            print("NO")
            return

    # Condition 2: Check if sums of both halves are equal
    half = n // 2
    # Convert digits to integers and calculate sums
    sum_first_half = sum(int(d) for d in ticket[:half])
    sum_second_half = sum(int(d) for d in ticket[half:])
    
    if sum_first_half == sum_second_half:
        print("YES")
    else:
        print("NO")

# Execute the function
solve()
