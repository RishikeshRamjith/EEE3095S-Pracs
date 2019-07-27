#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Rishikesh Ramjith
Student Number: RMJHRS001
Prac: 1
Date: 25/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
# Logic that you write
def main():
    ledPin = 4
    buttonPin = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)
    GPIO.output(ledPin, not GPIO.input(buttonPin))
    time.sleep(0.1)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
