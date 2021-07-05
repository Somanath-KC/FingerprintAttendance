
from RPLCD.i2c import CharLCD


lcd = CharLCD('PCF8574', 0x27, rows=2, cols=16)


def lcd_write(msg, space=0):
    lcd.clear()
    lcd.write_string(msg)

