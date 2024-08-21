# Activity: Python Function Practice Part 4

# Function to find the maximum of three numbers
def max_num(a, b, c):
    return max(a, b, c)

# Test cases
print(max_num(1, 2, 3))  # Outputs: 3
print(max_num(10, 5, 7))  # Outputs: 10
print(max_num(-1, -4, -3))  # Outputs: -1


# Function to multiply all the numbers in a list
def mult_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Test cases
print(mult_list([1, 2, 3]))  # Outputs: 6
print(mult_list([2, 4, 6]))  # Outputs: 48
print(mult_list([10, -2, 5]))  # Outputs: -100


# Function to reverse a string
def rev_string(s):
    return s[::-1]

# Test cases
print(rev_string("hello"))  # Outputs: "olleh"
print(rev_string("world"))  # Outputs: "dlrow"
print(rev_string("Python"))  # Outputs: "nohtyP"


# Function to check whether a number falls in a given range (inclusive)
def num_within(num, start, end):
    return start <= num <= end

# Test cases
print(num_within(3, 2, 4))  # Outputs: True
print(num_within(3, 1, 3))  # Outputs: True
print(num_within(10, 2, 5))  # Outputs: False


# Function to print out the first n rows of Pascal's triangle
def pascal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
        print(' '.join(map(str, row)))

# Test cases
pascal(1)
# Outputs:
# 1

pascal(5)
# Outputs:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
