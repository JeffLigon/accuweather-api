import requests
import RPi.GPIO as GPIO
import time

key = 'UHo6YxqHHxBrei5DkAaEljGeCe4RdFOX'
location = '340969'
ApiUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + location + '?apikey=' + key

# initialize lights
GPIO.setmode(GPIO.BCM)
redLED = 17
yellowLED = 27
greenLED = 22
GPIO.setup(redLED, GPIO.OUT)
GPIO.setup(yellowLED, GPIO.OUT)
GPIO.setup(greenLED, GPIO.OUT)

while True:
   response = requests.get(ApiUrl) 
   weather = response.json() 
   currentTemp = weather[0]['Temperature']['Imperial']['Value']
   
   # reset all lights off
   GPIO.output(redLED, GPIO.LOW) 
   GPIO.output(yellowLED, GPIO.LOW)
   GPIO.output(greenLED, GPIO.LOW)
   
   print ('The current weather in Plano is ' + str(weather[0]['WeatherText']) + '.')
   print ('The current temperature in Plano is ' + str(currentTemp) + ' F.')
      
   if currentTemp <= 40: 
       GPIO.output(redLED, GPIO.HIGH)
       print ('red light')
   elif currentTemp > 40 and currentTemp < 60: 
       GPIO.output(yellowLED, GPIO.HIGH)
       print ('yellow light')
   else: 
       GPIO.output(greenLED, GPIO.HIGH)
       print ('green light')
   time.sleep(1800) # 30 minutes = 1800 

