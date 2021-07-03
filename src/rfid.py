from time import sleep
import sys
from mfrc522 import SimpleMFRC522
from RPi import GPIO
from src.lcd import lcd


GPIO.setwarnings(False)

def read_rfid_card():
    reader = SimpleMFRC522()
    try:
        #GPIO.cleanup()
        while True:
            lcd.clear()
            lcd.write_string("Hold your tag \n near the reader")
            print("Hold a tag near the reader")
            return reader.read()[0]
    except KeyboardInterrupt:
        GPIO.cleanup()
        lcd.clear()
        lcd.write_string("Error Reading Card")
        print("Error Reading RFID Card")
        exit()

if __name__ == "__main__":
    print(read_rfid_card())
