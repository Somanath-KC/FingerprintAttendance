from time import sleep
import sys
from mfrc522 import SimpleMFRC522
from RPi import GPIO

GPIO.setwarnings(False)

def read_rfid_card():
    reader = SimpleMFRC522()
    try:
        GPIO.cleanup()
        while True:
            print("Hold a tag near the reader")
            return reader.read()[0]
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Error Reading RFID Card")
        exit()