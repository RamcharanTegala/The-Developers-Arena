# grade_calculator.py
# Week 2 Project: Student Grade Calculator

def calculate_grade(marks):
    """Returns grade and message based on marks"""
    if marks >= 90:
        return "A", "Excellent work! 🌟 Keep shining!"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better!"
    elif marks >= 60:
        return "D", "You passed. Keep practicing!"
    else:
        return "F", "Don't give up! Practice makes perfect 💪"


print("📚 Student Grade Calculator")
print("----------------------------")

name = input("Enter student name: ")

# Input validation using while loop
while True:
    try:
        marks = int(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        else:
            print("❌ Marks must be between 0 and 100.")
    except ValueError:
        print("❌ Please enter a valid number.")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
