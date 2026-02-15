


'''
Challenge: Implement error handling to ensure that the user enters valid marks (between 0 and 100) for each subject.

=================================================
Input: Ask the user to enter their marks for three subjects.
Processing: Calculate the average of the marks. Determine the grade based on the average:
90 and above: A
80-89: B
70-79: C
60-69: D
Below 60: F
Output: Display the calculated grade.
'''

def calculate_grade():
    try:
        marks = []

        for i in range(1, 4):
            score = float(input(f"Enter marks for subject {i}: "))

            if score < 0 or score > 100:
                raise ValueError("Marks must be between 0 and 100.")

            marks.append(score)

        average = sum(marks) / len(marks)

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "F"

        print(f"\nAverage Score: {average:.2f}")
        print(f"Final Grade: {grade}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Run the program
calculate_grade()
