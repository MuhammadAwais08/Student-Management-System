from Student.student import Student
from Files.file_handler import save_data
from Files.file_handler import load_data,search_data,update_data,delete_data


def add_student():
    name=input("Enter Student Name:").strip()
    age=int(input("Enter Student Age:"))
    roll_number=int(input("Enter Student Roll Number:"))
    department=input("Enter Student Department:").strip()
    marks=float(input("Enter Student Marks:"))
    student=Student(
        name,
        age,
        roll_number,
        department,
        marks
        )

    save_data(student)
    
    return student

def view_students():
    
    students = load_data()

    return students

def search_student():
    
    roll_number = input("Enter Roll Number: ")

    student = search_data(roll_number)

    return student

def update_student():
    
    roll_number = input("Enter Roll Number To Update: ")

    name = input("Enter New Name: ").strip()

    age = int(input("Enter New Age: "))

    department = input("Enter New Department: ").strip()

    marks = float(input("Enter New Marks: "))

    student = Student(
        name,
        age,
        roll_number,
        department,
        marks
    )

    status = update_data(roll_number, student)

    return status

def delete_student():
    
    roll_number = input("Enter Roll Number To Delete: ").strip()

    status = delete_data(roll_number)

    return status

    