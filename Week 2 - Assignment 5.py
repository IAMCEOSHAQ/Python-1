


'''

Challenge: Implement error handling to ensure that the user enters a non-negative number for the time duration.

=======================================================
Input: Prompt the user to enter a time duration in hours.
Processing: Convert the time duration to minutes and seconds.
Output: Display the converted time duration in minutes and seconds.

'''

def convert_time():
    try:
        hours = float(input("Enter the time duration in hours: "))

        if hours < 0:
            raise ValueError("Time duration cannot be negative.")

        minutes = hours * 60
        seconds = hours * 3600

        print(f"\nTime Conversion:")
        print(f"{hours:.2f} hours = {minutes:.2f} minutes")
        print(f"{hours:.2f} hours = {seconds:.2f} seconds")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
convert_time()
