from src.mongo import check_if_faculty_exists, check_if_student_exists
from src.mongo import add_biometric
from src.mongo import check_person_in_biometrics, check_if_card_exists
from src.rfid import read_rfid_card
from src.biometrics import read_fingerprint, compare_fingerprints


def add_card_num_biometric():
    card_num = read_rfid_card()
    
    if check_if_card_exists(card_num):
        print("Card Already Exists!")
        exit()
    else:
        bio1 = read_fingerprint()
        bio2 = read_fingerprint()
        if not compare_fingerprints(bio1, bio2, 40)[0]:
            print("Fingerprints did not matched. \n Place the same finger at same position next time.")
            print("Please try agian.")
            exit()
        return (card_num, bio1, bio2)
    

def add_student_to_biometrics():

    s_id = input("Enter Student ID: ").upper()
    if check_person_in_biometrics(s_id):
        print("BioMetric Already Registered!")
        exit()

    if check_if_student_exists(s_id):
        card_num, bio1, bio2 = add_card_num_biometric()
        return (s_id, card_num, bio1, bio2)
    else:
        print("Invalid Student ID.")
        exit()


def add_faculty_to_biometrics():
    s_id = input("Enter Facult ID: ").upper()
    if check_person_in_biometrics(s_id):
        print("BioMetric Already Registered!")
        exit()

    if check_if_faculty_exists(s_id):
        card_num, bio1, bio2 = add_card_num_biometric()
        return (s_id, card_num, bio1, bio2)
    else:
        print("Invalid Faculty ID.")
        exit()


def register_biometric(role):
    if role == "--student":
        s_id, card_num, bio1, bio2 = add_student_to_biometrics()
        add_biometric("student", s_id, card_num, bio1, bio2)
        print("Biometrics & Card Registration Successful.")
        return
    elif role == "--faculty":
        f_id, card_num, bio1, bio2 = add_faculty_to_biometrics()
        add_biometric("faculty", f_id, card_num, bio1, bio2)
        print("Biometrics & Card Registration Successful.")
        return
    else:
        print("Invalid Role Provied! Please try again.")
        exit()