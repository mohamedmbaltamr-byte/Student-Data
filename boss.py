import random as ra
import statistics as st
from boss_class import *

students = []
Average_grades_for_class = []


while True:
    option = get_option(["Add Student", "Display class statistics", "Save to file and exit"])

    if option == 0:
        name = input("Adding name of student :\n")
        a, b, c = get_grade(), get_grade(), get_grade()
        abc = [a, b, c]

        Average_grades = st.mean(abc)

        result = get_result(Average_grades)
        student = get_canvas(a, b, c, name, Average_grades, result)

        students.append(student)
        Average_grades_for_class.append(Average_grades)


    elif option == 1:
        if not students:
            no_data_message()
            continue 

        student_data = str(get_canvas_file(students))+"\n\n\n"
        class_data = str(get_canvas_file_02(Average_grades_for_class))

        print(student_data)
        print(class_data)



    elif option == 2:
        if not students:
            no_data_message()
            continue 

        student_data = str(get_canvas_file(students))+"\n\n\n"
        class_data = str(get_canvas_file_02(Average_grades_for_class))  

        with open("students_data.txt", "w") as x:
            x.write(student_data)
            x.write(class_data)
        exit()