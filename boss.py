import random as ra
import statistics as st
from boss_class import *
import statistics as st

students_data = []


while True:
    option = get_option(["Add Student", "Display class statistics","Delete a student", "Save to file ", "exit"])


    if option == 0:
        name = input("Adding name of student :\n").title()

        print("Enter score for (Math)")
        math = get_number_only()

        print("Enter score for (English)")
        english = get_number_only()

        print("Enter score for (Programming)")
        programming = get_number_only()

        rate = st.mean([math, english, programming])
        result = get_result(rate)
        weakest_subject = get_weakest_subject(math, english, programming)
        students_data.append(
            {
            "name": name,
            "math": math,
            "english": english,
            "programming": programming,
            "rate": rate,
            "result": result,
            "weakest_subject": weakest_subject}
        )

    elif option == 1:
        if not students_data:
            no_data_message()
            continue 

        template = "N: %-25.25s | Math: %-3d | Englis: %-3d | Programming: %-3d | Rate: %-6.2f | Result: %-10s | Weakest: %s"

        output = "\n".join(template % (
            s["name"], 
            s["math"], 
            s["english"], 
            s["programming"], 
            s["rate"], 
            s["result"], 
            s["weakest_subject"]
        )
        for s in students_data)
        print(output)


    elif option == 2 :
        if not students_data:
            no_data_message()
            continue 

        name_delete_student = input("Enter The Name for a Student\n").title()
        for student in students_data:
            if student["name"] == name_delete_student:
                students_data.remove(student)
                print("Deleted successfully\n")
                break
            else:
                print("There is no student by that name!!\n")

    elif option == 3:
        if not students_data:
            no_data_message()
            continue 

        template = "N: %-25.25s | Math: %-3d | Englis: %-3d | Programming: %-3d | Rate: %-6.2f | Result: %-10s | Weakest: %s"

        output_print = "\n".join(template % (
            s["name"], 
            s["math"], 
            s["english"], 
            s["programming"], 
            s["rate"], 
            s["result"], 
            s["weakest_subject"]
        )
        for s in students_data)

        with open("students_data.txt", "w") as x:

            x.write(output_print)



    elif option == 4:
        exit()   