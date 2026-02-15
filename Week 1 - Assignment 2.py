


'''
Challenge: Implement error handling to ensure that the length and width entered by the user are positive numbers.

=================================
Input: Ask the user to enter the length and width of a rectangle.
Processing: Calculate the area of the rectangle using the formula: Area = Length * Width.
Output: Display the calculated area of the rectangle.
'''

def calculate_rectangle_area():
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers greater than zero.")

        area = length * width

        print(f"\nThe area of the rectangle is: {area:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
calculate_rectangle_area()
