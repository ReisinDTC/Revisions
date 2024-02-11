def number_checker(question):
    error = "\nSorry, you must enter a valid number\n"
    while True:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)

def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    elif 85 <= mark < 90:
        return "A"
    elif 80 <= mark < 85:
        return "A-"
    elif 75 <= mark < 80:
        return "B+"
    elif 70 <= mark < 75:
        return "B"
    elif 65 <= mark < 70:
        return "B-"
    elif 60 <= mark < 65:
        return "C+"
    elif 55 <= mark < 60:
        return "C"
    elif 50 <= mark < 55:
        return "C-"
    elif 40 <= mark < 50:
        return "D"
    else:
        return "F"

total_marks = 0
marks_list = []

while True:
    name = input("Student name (enter 'X' to finish): ").title()

    if name == "X":
        break

    if len(name) < 2:
        print("A person's name must be at least 2 characters long!")
        continue

    mark = number_checker(f"{name}'s mark: ")

    while not 0 <= mark <= 100:
        print("Marks can only be between 0 and 100!")
        mark = number_checker(f"{name}'s mark: ")

    total_marks += mark
    marks_list.append([name, mark])

# Calculate average marks
average_marks = total_marks / len(marks_list) if len(marks_list) > 0 else 0

# Find the best mark and student
best_student = max(marks_list, key=lambda x: x[1]) if marks_list else None

# Display results
print("\n----- Results -----")
print(f"Total number of students: {len(marks_list)}")
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks:.2f}")

if best_student:
    print(f"Best student: {best_student[0]} with a mark of {best_student[1]}")
else:
    print("No students entered.")

# Display University-style grades
print("\n----- University-style Grades -----")
for student in marks_list:
    name, mark = student
    grade = calculate_grade(mark)
    print(f"{name} - Mark: {mark}, Grade: {grade}")
