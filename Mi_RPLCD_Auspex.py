#! /usr/bin/env python2.7

import RPi.GPIO as GPIO
from RPLCD import CharLCD, cleared, cursor
from time import sleep

# Auspex LCD for Warhammer 40,000 Victory Point and Turn Tracking

# wired as here: https://github.com/dbrgn/RPLCD

# Initialize display. All values have default values and are therefore optional.

lcd = CharLCD(pin_rs=15, pin_rw=18, pin_e=16, pins_data=[21, 22, 23, 24],
    numbering_mode=GPIO.BOARD, cols=20, rows=4, dotsize=8)

# create the aquila characters
aquila0 = (0b01111,0b00011,0b00001,0b00000,0b00000,0b00000,0b00000,0b00000)
lcd.create_char(0,aquila0)
aquila1 = (0b11101,0b11000,0b11111,0b11111,0b01101,0b00001,0b00011,0b00010)
lcd.create_char(1,aquila1)
aquila2 = (0b01011,0b10001,0b11111,0b11111,0b11011,0b11000,0b11100,0b10100)
lcd.create_char(2,aquila2)
aquila3 = (0b11111,0b11100,0b11000,0b10000,0b00000,0b00000,0b00000,0b00000)
lcd.create_char(3,aquila3)

# prep the LCD
lcd.clear()
lcd.home()

with cursor(lcd, 0, 2):
    lcd.write_string('AUSPEX 410014.M2')
    # test github editor for spaces

# draw the aquila centred on line 2
with cursor(lcd, 1,8):
    lcd.write_string(unichr(0))
    lcd.write_string(unichr(1))
    lcd.write_string(unichr(2))
    lcd.write_string(unichr(3))

with cursor(lcd,2,4):
    lcd.write_string('MET: 1:22:45')

with cursor(lcd,3,2):
    lcd.write_string('VP:03 <T2< VP:01')

# admire
sleep(10)

# close down, this is throwing error?
lcd.close(clear=True)
