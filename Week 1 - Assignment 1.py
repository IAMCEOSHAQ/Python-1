


'''
Challenge: Handle cases where the user enters non-numeric input for the principal amount, interest rate, or time period, and provide appropriate error messages.

=============================
Input: Prompt the user to enter the principal amount, interest rate (in percentage), and the time period (in years).
Processing: Calculate the simple interest using the formula: Simple Interest = (Principal * Rate * Time) / 100.
Output: Display the calculated simple interest.
'''

def calculate_simple_interest():
    try:
        principal = float(input("Enter the principal amount: "))
        rate = float(input("Enter the interest rate (in %): "))
        time = float(input("Enter the time period (in years): "))

        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if time <= 0:
            raise ValueError("Time period must be greater than zero.")

        simple_interest = (principal * rate * time) / 100

        print(f"\nSimple Interest: {simple_interest:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
calculate_simple_interest()
