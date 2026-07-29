def show_menu():
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6.Exit")


def display_student(student):

    print("\n=== Student Information ===")
    print(f"Name Of Stuent : {student.name}")
    print(f"Age            : {student.age}")
    print(f"Roll Number    : {student.roll_number}")
    print(f"Department     : {student.department} ")
    print(f"Marks          : {student.marks}")

def display_all_students(students):
    
    if len(students) == 0:

        print("\nNo Student Record Found.")

        return

    print("\n=========== STUDENTS ===========")

    for student in students:

        print("-------------------------------")

        print(f"Name       : {student[0]}")
        print(f"Age        : {student[1]}")
        print(f"Roll No    : {student[2]}")
        print(f"Department : {student[3]}")
        print(f"Marks      : {student[4]}")

    print("-------------------------------")

def display_search_student(student):
    
    if student is None:

        print("\nStudent Not Found.")

        return

    print("\n====== Student Found ======")

    print(f"Name       : {student[0]}")
    print(f"Age        : {student[1]}")
    print(f"Roll No    : {student[2]}")
    print(f"Department : {student[3]}")
    print(f"Marks      : {student[4]}")


def update_message(status):
    
    if status:

        print("\nStudent Updated Successfully.")

    else:

        print("\nStudent Not Found.")

def delete_message(status):
    
    if status:

        print("\nStudent Deleted Successfully.")

    else:

        print("\nStudent Not Found.")