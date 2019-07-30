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
#global variables
num = 0
numArr = [0,0,0]
#other functions
def render():
    global num
    global numArr

    x = num%8
    counter = 0
    if x == 0:
        numArr = [0,0,0]
    while x > 0:
        numArr[counter] = x%2
        x = x//2
        counter+=1
    GPIO.output(ledPin0, numArr[2])
    GPIO.output(ledPin1, numArr[1])
    GPIO.output(ledPin2, numArr[0])

def add(channel):
    global num
    num+=1
    render()

def subtract(channel):
    global num
    num-=1
    render()

# Logic that you write
def main():
    time.sleep(1)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        ledPin0 = 17
        ledPin1 = 27
        ledPin2 = 22
        buttonPin0 = 23
        buttonPin1 = 24
        GPIO.setmode(GPIO.BCM)

        #setup push button for incrementing
        GPIO.setup(buttonPin0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(buttonPin0, GPIO.FALLING, callback=add, bouncetime=200)

        #setup push button for decrementing
        GPIO.setup(buttonPin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(buttonPin1, GPIO.FALLING, callback=subtract, bouncetime=200)

        #setup LEDs
        GPIO.setup(ledPin0, GPIO.OUT)
        GPIO.setup(ledPin1, GPIO.OUT)
        GPIO.setup(ledPin2, GPIO.OUT)
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except Exception as e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e)
