
#  O(1) - Constant Time
# -----------------------------------------------
# Constant time complexity: execution time is independent of input size.
# Example: Simple arithmetic operation or accessing an element by index.

def add_items(n):
    # Only one operation regardless of n
    return n + n + n

print("O(1) example:", add_items(10))


# -----------------------------------------------
#  O(n) - Linear Time
# -----------------------------------------------
# Linear time complexity: directly proportional to input size.
# Example: Single loop over the input.

def print_linear_items(n):
    for i in range(n):  # Runs n times
        print("O(n) example:", i)

print_linear_items(10)


# -----------------------------------------------
#  O(n^2) - Quadratic Time
# -----------------------------------------------
# Nested loop: each loop runs n times, total = n * n = n^2

def print_quadratic_items(n):
    for i in range(n):
        for j in range(n):
            print("O(n^2) example:", i, j)

print_quadratic_items(5)


# -----------------------------------------------
#  Drop Constants Rule
# -----------------------------------------------
# O(n + n) becomes O(2n), and then we drop constants to simplify to O(n)

def print_with_constants(n):
    for i in range(n):
        print("First loop:", i)
    for j in range(n):
        print("Second loop:", j)
    # Even though there are two loops, time is still linear in n.

print_with_constants(5)


# -----------------------------------------------
#  Drop Non-Dominant Terms
# -----------------------------------------------
# O(n^2 + n) becomes O(n^2) because n^2 dominates for large input

def print_non_dominant(n):
    for i in range(n):
        for j in range(n):
            print("Dominant loop:", i, j)  # O(n^2)
    
    for k in range(n):
        print("Non-dominant loop:", k)  # O(n), which we drop in Big O

print_non_dominant(3)


# -----------------------------------------------
#  Different Terms for Inputs (O(a + b))
# -----------------------------------------------
# When the loops run based on different inputs, they are separate terms.
# This gives O(a + b), not O(n^2) or similar.

def print_items_different_inputs(a, b):
    for i in range(a):
        print("First input loop:", i)

    for j in range(b):
        print("Second input loop:", j)

print_items_different_inputs(2, 3)


# -----------------------------------------------
#  THEORETICAL SUMMARY 
# -----------------------------------------------
"""
Big O Notation - Worst case runtime
Omega (Ω) - Best case runtime
Theta (Θ) - Average case runtime

Time Complexities:
• O(1): Constant - array access, arithmetic
• O(log n): Logarithmic - binary search
• O(n): Linear - single loop
• O(n log n): Merge sort, Quick sort
• O(n^2): Bubble sort, nested loops

Rules:
• Drop Non-Dominant Terms: O(n^2 + n) => O(n^2)
• Drop Constants: O(3n) => O(n)
"""
