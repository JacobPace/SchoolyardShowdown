################################################
#Name: Jacob Pace
#Date: 10/23/2022
#Description: Blinking Light
################################################

import RPi.GPIO as GPIO
from time import sleep

led = 17
button = 25

#Board Type (mode)
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.output(led, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(led, GPIO.LOW)
    sleep(0.5)
    if (GPIO.input(button)==GPIO.HIGH):
        GPIO.output(led, GPIO.HIGH)
        sleep(0.1)
        GPIO.output(led, GPIO.LOW)
        sleep(0.1)




        output =str(value) + "\t"
    num = 0
    while (num <= 9):
        output += f"{log10(float(str(value) + str(num)))}"
        num += 1
    print(output)