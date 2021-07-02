from src.mongo import set_session_end_time
from src.send_email import send_email_report
import signal
import os

def say_goodbye():
    del os.environ['SESSION_ID']
    print("\nThanks for using our Application. \nGood Bye👋")
    exit()

def script_interrupt(signum, frame):
    set_session_end_time()
    if 'y' == input("\nDo you want to send the report to email? [Y/N] :").lower():
        try:
            send_email_report()
            print("Report sent successfully.✅")
        except Exception as e:
            print(e)
            print("❌Unable to send report.")
    say_goodbye()

def script_terminate(signum, frame):
    set_session_end_time()
    say_goodbye()

def set_interrupts():
    os.system("clear")
    signal.signal(signal.SIGINT, script_interrupt)
    signal.signal(signal.SIGTSTP, script_terminate)
