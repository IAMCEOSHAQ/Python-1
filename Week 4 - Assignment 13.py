


'''
Challenge: Use a loop structure to compare characters from both ends of the string to determine whether it is a palindrome.

===================================
Description: Write a program that prompts the user to enter a string and then checks whether it is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
'''

def check_palindrome():
    try:
        user_input = input("Enter a string: ")

        if not user_input:
            raise ValueError("Input cannot be empty.")

        # Normalize input: lowercase and remove non-alphanumeric characters
        cleaned = "".join(char.lower() for char in user_input if char.isalnum())

        left = 0
        right = len(cleaned) - 1
        is_palindrome = True

        # Loop to compare characters from both ends
        while left < right:
            if cleaned[left] != cleaned[right]:
                is_palindrome = False
                break
            left += 1
            right -= 1

        if is_palindrome:
            print("\nThe entered string is a palindrome.")
        else:
            print("\nThe entered string is not a palindrome.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
check_palindrome()
