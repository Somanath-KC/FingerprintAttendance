from .mongo import check_if_card_exists, get_card_details
from .mongo import log_attendance
from .rfid import read_rfid_card
from .biometrics import read_fingerprint, compare_fingerprints
from time import sleep
from src.lcd import lcd_write


def check_attendance():
    print("Started Accepting Attendance..\n")
    while True:
        card_num = read_rfid_card()

        if not check_if_card_exists(card_num):
            print("Card not registered.")
            lcd_write("Card not registered.")
            sleep(2)
        else:
            card_data = get_card_details(card_num)
            #print(card_data)
            ip_bio = read_fingerprint()
            
            compare = []
            compare.append(compare_fingerprints(ip_bio, card_data['bio1'])[1])
            compare.append(compare_fingerprints(ip_bio, card_data['bio2'])[1])

            if max(compare) >= 40:
                log_attendance(card_data['card_num'], card_data['_id'], card_data['role'])
                print("Present")
                lcd_write("Success!")
                sleep(3)
            else:
                lcd_write("Biometrics not matched!")
                sleep(3)
                print("Biometrics dose not matched! Please try again.")
