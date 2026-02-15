


'''
Challenge: Provide feedback to the user based on their BMI category (e.g., underweight, normal weight, overweight, obese).

===============================
Input: Prompt the user to enter their weight in kilograms and height in meters.
Processing: Calculate the BMI using the formula: BMI = Weight / (Height^2).
Output: Display the calculated BMI.
'''

def calculate_bmi():
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive numbers.")

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
            feedback = "You may need to gain weight. Consider consulting a healthcare professional."
        elif bmi < 25:
            category = "Normal weight"
            feedback = "You are within a healthy weight range. Keep up the good habits!"
        elif bmi < 30:
            category = "Overweight"
            feedback = "You may benefit from a balanced diet and regular physical activity."
        else:
            category = "Obese"
            feedback = "Health risks may be increased. Consider speaking with a healthcare professional."

        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"BMI Category: {category}")
        print(f"Feedback: {feedback}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
calculate_bmi()
