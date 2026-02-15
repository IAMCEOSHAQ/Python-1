


'''
Challenge: Use nested loop structures to print the pattern efficiently and neatly. Allow the user to specify the character used for the pattern.

=========================================
Description: Develop a program that prompts the user to enter the number of rows for a pattern and then prints a pattern of asterisks (*) in the form of a right triangle.
'''


def print_triangle_pattern():
    try:
        rows = int(input("Enter the number of rows: "))

        if rows <= 0:
            raise ValueError("Number of rows must be a positive integer.")

        character = input("Enter a character to use for the pattern: ")

        if not character:
            raise ValueError("Pattern character cannot be empty.")

        print("\nGenerated Pattern:\n")

        for i in range(1, rows + 1):  # Outer loop for rows
            for j in range(i):  # Inner loop for characters
                print(character, end="")
            print()  # Move to next line

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
print_triangle_pattern()
