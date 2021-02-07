import requests
import RPi.GPIO as GPIO
import time

# initialize lights
GPIO.setmode(GPIO.BCM)
redLED = 17
yellowLED = 27
greenLED = 22
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)

while True:
   GPIO.output(redLED, GPIO.LOW)
   GPIO.output(yellowLED, GPIO.LOW)
   GPIO.output(greenLED, GPIO.LOW)
   
   currentTemp = float(input("What is the current temperature? "))
   print ('The current temperature in Plano is ' + str(currentTemp) + ' F.')
   
   if currentTemp <= 40: 
       GPIO.output(redLED, GPIO.HIGH)
       print ('red light')
   elif currentTemp > 40 and currentTemp < 80: 
       GPIO.output(yellowLED, GPIO.HIGH)
       print ('yellow light')
   else: 
       GPIO.output(greenLED, GPIO.HIGH)
       print ('green light')
   time.sleep(3) # 30 minutes = 1800 



