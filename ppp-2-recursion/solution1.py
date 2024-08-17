# Write code for algorithm 1 below

# 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero.
def positive_num(num):

  # base case
  if num == 1:
    return 1

  # recursive case
  else:
    return (num * positive_num(num - 1))

print(positive_num(4))


# Other example:
def count_down(n):
  #inherent base case
  #(will stop if n <= 0)
  if n>0:
      #recursive case
      print(n)
      count_down(n-1)

#test case
n=8
count_down(n)
