from Operations.operations import add_student,view_students,search_student,update_student,delete_student
from Utility.display import show_menu,display_student,display_all_students,display_search_student,update_message,delete_message

students=[]
while True:

    show_menu()

    try:

        choice=int(input("Enter Your Choice :"))
    except ValueError:
        print("Please Enter Number Only.")
        continue
    if choice==1:
            student=add_student()
            students.append(student)
            display_student(student)
    elif choice == 2:
    
        students = view_students()

        display_all_students(students)
    elif choice == 3:
    
        student = search_student()

        display_search_student(student)
    elif choice == 4:
    
        status = update_student()

        update_message(status)
    elif choice == 5:
    
        status = delete_student()

        delete_message(status)
    elif choice==6:
        print("ThanK You For Using Student Management System")
        break
    else:
        print("Invalide Choice")