import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

for i in range(100):
    # Turn on blue LED connected to BCM pin 23
    GPIO.output(23, True)
    time.sleep(1)
    # Switch to green LED connected to BCM pin 24
    GPIO.output(23, False)
    GPIO.output(24, True)
    time.sleep(1)
    
    # Switch back to blue
    GPIO.output(24, False)