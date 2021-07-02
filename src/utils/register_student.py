from src.mongo import add_student, check_if_student_exists


def register_student():
    s_id = input("Enter Student ID Number: ").upper()
    name = input("Enter Student Name: ").upper()
    year = input("Enter Year: ").upper()
    branch = input("Enter Branch: ").upper()
    section = input("Section: ").upper()


    if not(s_id and name and year and branch and section):
        print("Registration Failed. Some Feilds were empty.")
        return

    if check_if_student_exists(s_id):
        print("Student ID Already Exists!")
        exit()

    if add_student(s_id, name, year, branch, section):
        print("Registration Successful.")
    else:
        print("Registration Failed. Error adding to Database.")

    return
