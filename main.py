from src.welcome_banner import print_banner, loading
from src.interrupts import set_interrupts
from src.mongo import generate_attendance_session_id, set_session
import os
import sys
from src.utils.register_student import register_student
from src.utils.register_faculty import register_faculty
from src.utils.register_biometric import register_biometric
from src.utils.delete_biometric import delete_st_fc_biometric
from src.check_attendance import check_attendance
from RPLCD.i2c import CharLCD


args = sys.argv
print(args)

if len(args) > 1:
    if args[1].lower() == 'register-student':
        register_student()
    elif args[1].lower() == 'register-faculty':
        register_faculty()
    elif args[1].lower() == 'register-biometric':
        if len(args) == 3:
            register_biometric(args[2].lower())
        else:
            print("Role flag not found!")
            exit()
    elif args[1].lower() == 'delete-biometric':
        delete_st_fc_biometric()
    else:
        print("Invalid command! Please try again.")
else:
    # Attendace Session ID for Mongo
    os.environ['SESSION_ID'] = generate_attendance_session_id()
    set_session(os.environ['SESSION_ID'])
    set_interrupts()
    print_banner()
    loading()
    check_attendance()

