def number_checker(question):
    error = "\nSorry, you must enter a valid number\n"
    number = ""
    while not number:
        try:
            number = float(input(question))
            return number
        except ValueError:
            print(error)


total_marks = 0
marks_list = []
best_mark = 0
best_student = []

while True:
    name = input("Student name: ").title()
    if name == "X":
        break
    else:
        if len(name) < 2:
            print("A person's name must be at least 2 characters long!")
            continue
        else:
            mark = number_checker(f"{name}'s mark: ")
            while not 0 <= mark <= 100:
                print("Marks can only be between 0 and 100!")
                mark = number_checker(f"{name}'s mark: ")
            else:
                total_marks += mark
                marks_list.append([name, mark])
