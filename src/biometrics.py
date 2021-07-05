from pyfingerprint.pyfingerprint import PyFingerprint
from pyfingerprint.pyfingerprint import FINGERPRINT_CHARBUFFER1
from pyfingerprint.pyfingerprint import FINGERPRINT_CHARBUFFER2
#from src.mongo import check_person_in_biometrics
from time import sleep
from src.lcd import lcd_write


f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
def read_fingerprint():
    try:

        if ( f.verifyPassword() == False ):
            raise ValueError('The given fingerprint sensor password is wrong!')

    except Exception as e:
        lcd_write("System Error")
        print('The fingerprint sensor could not be initialized!')
        print('Exception message: ' + str(e))
        exit(1)

    # Start reading fingerpirnt
    print("Put your finger on sensor")
    lcd_write("Put your finger on sensor")
    while ( f.readImage() == False ):
        pass
    
    sleep(3)
    
    f.convertImage(FINGERPRINT_CHARBUFFER1)
    fingerprint_data = f.downloadCharacteristics(1)

    return fingerprint_data


def compare_fingerprints(bio1, bio2, accuracy=40):
    #f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)
    f.uploadCharacteristics(1, bio1)
    f.uploadCharacteristics(2, bio2)
    match = f.compareCharacteristics()
    #print(match)
    return (match >= accuracy, match)


if __name__ == "__main__":
    print(read_fingerprint())
