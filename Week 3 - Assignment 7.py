


'''
Challenge: Handle cases where the user enters non-numeric input for the year and provide appropriate error messages.

===============================================
Input: Prompt the user to enter a year.
Processing: Determine whether the entered year is a leap year or not. A leap year is divisible by 4 but not by 100 unless it is also divisible by 400.
Output: Display whether the entered year is a leap year or not.

'''

def check_leap_year():
    try:
        year = int(input("Enter a year: "))

        if year <= 0:
            raise ValueError("Year must be a positive integer.")

        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"\n{year} is a leap year.")
        else:
            print(f"\n{year} is not a leap year.")

    except ValueError:
        print("Input Error: Please enter a valid numeric year (e.g., 2024).")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
check_leap_year()
