def solve():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    
    for i in range(1, n):
        # If the gap between sorted elements is > 1, 
        # we can't reduce the array to one element.
        if a[i] - a[i-1] > 1:
            print("NO")
            return
            
    print("YES")

t = int(input())
for _ in range(t):
    solve()
