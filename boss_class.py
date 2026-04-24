import random as ra
import statistics as st

def get_number_only():
    while True:
        try:
            number = int(input("Enter a number:\n"))
            return number
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_option(op):
    print("Menu:\n")
    for i in range(len(op)):
        print(i, "- ", op[i], "press (", i, ")\n")
    while True:
        option = get_number_only()
        if 0 <= option < len(op):
            return option
        else:
            print("Invalid input. Please enter a valid option.")
    return option
def get_result(average_for_f):
    if average_for_f < 50:
        result = "Fail"
    elif 50 <= average_for_f < 70:
        result = "Pass"
    elif 70 <= average_for_f < 90:
        result = "Good"
    else:
        result = "Excellent"
    return result
def get_weakest_subject(math, english, programming):
    if math == 100 and english == 100 and programming == 100:
        return "None"
    else:
        weakest_subject = min([math, english, programming])
        if weakest_subject == math:
            weakest_subject = "Math"

        elif weakest_subject == english:
            weakest_subject = "English"

        else:  
            weakest_subject = "Programming"

        return weakest_subject
def no_data_message():
    print("There is not enough data! Add a student first.")