from src.mongo import add_faculty, check_if_faculty_exists


def register_faculty():
    s_id = input("Enter Faculty ID Number: ").upper()
    name = input("Enter Faculty Name: ").upper()
    branch = input("Enter Branch: ").upper()

    if check_if_faculty_exists(s_id):
        print("Faculty ID Already Exists!")
        exit()
    
    if not(s_id and name and branch):
        print("Registration Failed. Some Feilds were empty.")
        exit()
        return

    if add_faculty(s_id, name, branch):
        print("Registration Successful.")
    else:
        print("Registration Failed. Error adding to Database.")

    return
