def check_input_number(input_number):
    """Function to check if input number contains 4 unique digits and first digit isn´t zero."""

    while True:
        if not input_number.isnumeric():
            print("Input isn't a number!")
            input_number = input("Enter a different number:\n>>> ")
            continue
        elif len(input_number) != 4:
            print("Input must have 4 digits!")
            input_number = input("Enter a different number:\n>>> ")
            continue
        elif input_number[0] == "0":
            print("First digit mustn't be 0!")
            input_number = input("Enter a different number:\n>>> ")
            continue
        elif len(set(input_number)) != 4:
            print("Digits must be unique!")
            input_number = input("Enter a different number:\n>>> ")
            continue
        else:
            break
    return input_number


def bulls_cows(input_number, random_number):
    """Function to count bulls(input_number and random_number have the same digit on the same position)
     and cows (input_number and random_number have the same digit on the different positions"""
    bulls = 0
    cows = 0
    for i in range(len(input_number)):
        if input_number[i] == random_number[i]:
            bulls+=1
        else:
            for j in random_number:
                if input_number[i] == j:
                    cows+=1
    return bulls, cows






