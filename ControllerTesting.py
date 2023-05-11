import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
UpButton = 17
DownButton = 16
SelectButton = 13
GPIO.setup(UpButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DownButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SelectButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
try:
    while True:
        print("-"*50)
        if GPIO.input(UpButton)==GPIO.HIGH:
            print("Up button on")
        if GPIO.input(DownButton)==GPIO.HIGH:
            print("Down button on")
        if GPIO.input(SelectButton)==GPIO.HIGH:
            print("Select button on")
        if GPIO.input(UpButton)==GPIO.LOW:
            print("Up button off")
        if GPIO.input(DownButton)==GPIO.LOW:
            print("Down button off")
        if GPIO.input(SelectButton)==GPIO.LOW:
            print("Select button off")
        print("-"*50)
        sleep(2)
except KeyboardInterrupt:
    GPIO.cleanup()