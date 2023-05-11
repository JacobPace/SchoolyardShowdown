import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
UpButton = 17
DownButton = 16
SelectButton = 13
GPIO.setup(UpButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(DownButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(SelectButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#need a change to commit nahudjkawbksjBDkjsAJKDASJ
