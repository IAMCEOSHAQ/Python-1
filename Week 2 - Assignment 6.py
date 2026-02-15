


'''

Challenge: Allow the user to choose from multiple currency pairs and implement appropriate error handling for invalid currency inputs.

==============================================
Input: Ask the user to enter an amount in one currency (e.g., USD).
Processing: Convert the amount to another currency (e.g., EUR) using a fixed exchange rate.
Output: Display the converted amount in the target currency.

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
