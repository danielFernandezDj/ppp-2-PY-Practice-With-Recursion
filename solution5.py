# Write code for algorithm 5 below

# Write a function that checks whether a string is a palindrome or not.
# The program should take in a string and return True if the string is a palindrome and False if not.

# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
# Here is more information on palindromes.
def is_palindrome(s):
    # Remove any non-alphanumeric characters and convert to lowercase
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    # Check if the cleaned string is equal to its reverse
    return cleaned_str == cleaned_str[::-1]

# Example usage:
print(is_palindrome("madam"))      # Output: True
print(is_palindrome("radar"))      # Output: True
print(is_palindrome("hello"))      # Output: False
print(is_palindrome("A man, a plan, a canal, Panama"))  # Output: True
