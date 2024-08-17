# Activity: Python Function Fun Part 3
# In this activity we are going to practice writing functions in Python. The prompts have been listed below. Work may be completed using a personal Replit or a local code editor. Be sure to retain access to your completed work so it can be checked by instructors.

# Python Function Fun: Part 3 Prompts
# Please complete the following functions.

# name_args - Accepts any number of named arguments and prints them in the pattern key : value one at a time.
print('----------------------')
def name_args(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage:
name_args(name="Alice", age=30, city="New York")
# Output:
# name: Alice
# age: 30
# city: New York



# all_true - Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.
print('----------------------')
def all_true(iterable):
    return all(iterable)

# Example usage:
print(all_true([True, True, True]))  # Output: True
print(all_true([True, False, True])) # Output: False



# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.
print('----------------------')
def one_true(iterable):
    return any(iterable)

# Example usage:
print(one_true([False, False, True])) # Output: True
print(one_true([False, False, False])) # Output: False



# recursive_factorial - Uses recursion to find the factorial of an integer.
print('----------------------')
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

# Example usage:
print(recursive_factorial(5))  # Output: 120



# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
## Input: AABBCCDD
## Output: ABCD
print('----------------------')
def recursive_deduplicate(s):
    if len(s) < 2:
        return s
    if s[0] == s[1]:
        return recursive_deduplicate(s[1:])
    else:
        return s[0] + recursive_deduplicate(s[1:])

# Example usage:
print(recursive_deduplicate("AABBCCDD"))  # Output: ABCD



# recursive_reverse - Uses recursion to reverse a string.
print('----------------------')
def recursive_reverse(s):
    if len(s) == 0:
        return s
    else:
        return recursive_reverse(s[1:]) + s[0]

# Example usage:
print(recursive_reverse("hello"))  # Output: olleh
