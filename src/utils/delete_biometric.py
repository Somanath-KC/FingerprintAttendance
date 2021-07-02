from src.mongo import delete_biometric, check_person_in_biometrics


def delete_st_fc_biometric():
    p_id = input("Enter Student/Faculty ID: ").upper()

    if not check_person_in_biometrics(p_id):
        print("Invalid Student/Faculty ID. Please Try Again.")
        exit()
    else:
        if delete_biometric(p_id):
            print("Biometrics & Card Removed!")
        else:
            print("Error! Please try again.")
        exit(0)
