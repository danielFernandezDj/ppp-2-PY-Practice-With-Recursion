# Write code for algorithm 3 below

# Write a function that returns the nth elements in the Fibonacci Sequence.

# The Fibonacci Sequence is the series of numbers where the next number is found
# by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
# For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
# Here is more information on the Fibonacci Sequence.
# Hint: Look back at the factorial example as the structure of the algorithm may help you.

def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])

    return fib_seq

# Example usage:
print(fibonacci_iterative(10))
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
