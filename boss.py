import random as ra
import statistics as st

students = []
Average_grades_for_class = []

def get_number_only():
        while True:
            try:
                number = int(input("Enter a number:\n"))
                return number
            except ValueError:
                print("Invalid input. Please enter a valid number.")
def get_option(op):
    print("menu:\n")
    for i in range(len(op)):
        print(i, "- ", op[i], "press (", i, ")\n")
    while True:
        option = get_number_only()
        if 0 <= option < len(op):
            return option
        else:
            print("Invalid input. Please enter a valid option.")
    return option
def get_grade():
    return ra.randint(0, 100)
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
def get_canvas(a101, b101, c101, name101, Average_grades101, result101):
    edit = ((name101.ljust(20)).lower()).title(), {"math": a101}, {"english": b101}, {"programming": c101}
    student = [(str(edit)).ljust(85),"Score Rate (%.1f %%)"%(Average_grades101) ," Result : %s"%(result101)]
    return student
def get_canvas_file(students):
    return "\n".join(str(s) for s in students)
def get_canvas_file_02(Average_grades_for_class):
    mean_class = st.mean(Average_grades_for_class)
    return "The class success rate is: %.1f %% " % (mean_class), "The Result is : %s"%(get_result(mean_class))



while True:
    option = get_option(["Add Student", "Display class statistics", "Save to file and exit"])

    if option == 0:


        name = str(input("Adding name of student :\n"))

        a, b, c = get_grade(), get_grade(), get_grade()
        abc = a, b, c

        Average_grades = st.mean(abc)
        result = get_result(Average_grades)

        student = get_canvas(a, b, c, name, Average_grades, result)
#       edit = ((name.ljust(20)).lower()).title(), {"math": a}, {"english": b}, {"programming": c}
#       student = [(str(edit)).ljust(85),"Score Rate (%.1f %%)"%(Average_grades) ," Result : %s"%(result)]


        students.append(student)
        Average_grades_for_class.append(Average_grades)

    elif option == 1:
        print(get_canvas_file(students))
        rate_class = st.mean(Average_grades_for_class)
        result = get_result(rate_class)
        print("The class success rate is: %.1f %% " % (rate_class), "The Result is : %s"%(result))










    elif option == 2:

        aaa = students 
        bbb = Average_grades_for_class 
        x = open("students.txt", "w")
        x.write(str(get_canvas_file(aaa))+"\n\n\n")
        x.write(str(get_canvas_file_02(bbb)))
        x.close()
        exit()
 