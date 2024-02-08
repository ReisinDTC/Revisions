while True:

    first_number = int(input("Enter the first number"))
    if first_number == 0:
        break
    else:
        second_number = int(input("Enter the second"))


    if first_number == second_number:
        print(f"Both numbers were {first_number} and are therefore equal")
    elif first_number > second_number:
        print(f"{first_number} is greater than {second_number}")
    else:
        print(f"{second_number} is greater than {first_number}")


print("goodbye")
