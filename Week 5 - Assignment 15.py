


'''
Challenge: Write the function using recursion.

===================================
Description: Create a function named is_palindrome that takes a string as input and returns True if it is a palindrome, and False otherwise.

'''


def is_palindrome(text):
    # Normalize the string (optional but recommended)
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    def recursive_check(s):
        # Base case: empty or single character
        if len(s) <= 1:
            return True

        # If first and last characters don't match
        if s[0] != s[-1]:
            return False

        # Recursive call on substring without first and last characters
        return recursive_check(s[1:-1])

    return recursive_check(cleaned)


# Example usage
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
