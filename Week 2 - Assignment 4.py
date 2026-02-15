


'''

Challenge: Implement error handling to ensure that the user enters numeric values for the coordinates.

============================================
Input: Prompt the user to enter the coordinates of two points in a 2D plane (x1, y1) and (x2, y2).
Processing: Calculate the distance between the two points using the distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
Output: Display the calculated distance between the two points.

'''

import math

def calculate_distance():
    try:
        x1 = float(input("Enter x1 coordinate: "))
        y1 = float(input("Enter y1 coordinate: "))
        x2 = float(input("Enter x2 coordinate: "))
        y2 = float(input("Enter y2 coordinate: "))

        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        print(f"\nThe distance between the two points is: {distance:.2f}")

    except ValueError:
        print("Input Error: Please enter valid numeric values for all coordinates.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
calculate_distance()
