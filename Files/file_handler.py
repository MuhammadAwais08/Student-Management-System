FILE_NAME = "students.txt"


def save_data(student):

    data = f"{student.name},{student.age},{student.roll_number},{student.department},{student.marks}\n"

    with open(FILE_NAME, "a") as file:
        file.write(data)

def load_data():
    
    students = []

    try:

        with open(FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                data = line.split(",")

                students.append(data)

    except FileNotFoundError:

        return []

    return students

def search_data(roll_number):
    
    try:

        with open(FILE_NAME, "r") as file:

            for line in file:

                line = line.strip()

                if line == "":
                    continue

                data = line.split(",")

                if data[2] == str(roll_number):

                    return data

    except FileNotFoundError:

        return None

    return None

def update_data(roll_number, new_student):
    
    try:

        students = []

        with open(FILE_NAME, "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[2] == str(roll_number):

                    students.append(
                        f"{new_student.name},{new_student.age},{new_student.roll_number},{new_student.department},{new_student.marks}\n"
                    )

                else:

                    students.append(line)

        with open(FILE_NAME, "w") as file:

            file.writelines(students)

        return True

    except FileNotFoundError:

        return False

def delete_data(roll_number):
    
    try:

        students = []

        deleted = False

        with open(FILE_NAME, "r") as file:

            for line in file:

                data = line.strip().split(",")

                if data[2] == str(roll_number):

                    deleted = True

                else:

                    students.append(line)

        with open(FILE_NAME, "w") as file:

            file.writelines(students)

        return deleted

    except FileNotFoundError:

        return False