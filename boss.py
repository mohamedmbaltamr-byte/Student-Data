import random as ra
import statistics as st
from boss_class import *

students = []
Average_grades_for_class = []

while True:
    option = get_option(["Add Student", "Display class statistics", "Save to file and exit"])

    if option == 0:


        name = str(input("Adding name of student :\n"))

        a, b, c = get_grade(), get_grade(), get_grade()
        abc = a, b, c

        Average_grades = st.mean(abc)
        result = get_result(Average_grades)

        student = get_canvas(a, b, c, name, Average_grades, result)

        students.append(student)
        Average_grades_for_class.append(Average_grades)

    elif option == 1:

        if not Average_grades_for_class:
            print("There is not enough data! Add a student first.")
            continue 
            
    
        print(get_canvas_file(students))
        rate_class = st.mean(Average_grades_for_class)
        result = get_result(rate_class)
        print("The class success rate is: %.1f %% " % (rate_class), "The Result is : %s"%(result))



    elif option == 2:
        if not Average_grades_for_class:
            print("There is not enough data! Add a student first.")
            continue 
        aaa = students 
        bbb = Average_grades_for_class 
        x = open("students.txt", "w")
        x.write(str(get_canvas_file(aaa))+"\n\n\n")
        x.write(str(get_canvas_file_02(bbb)))
        x.close()
        exit()
 