# Write code for algorithm 2 below

# 2. Write a function that prints the natural numbers from 1 to n.
def natural_numbers(n, i=1):

  if i <= n:
    print(i)
    natural_numbers(n, i + 1)

natural_numbers(3)