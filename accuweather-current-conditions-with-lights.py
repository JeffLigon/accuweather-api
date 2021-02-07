import requests
from gpiozero import LED
import time

key = 'UHo6YxqHHxBrei5DkAaEljGeCe4RdFOX'
location = '340969'
ApiUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + location + '?apikey=' + key

redLED = LED(17)
yellowLED = LED(27)
greenLED = LED(22)

while True:
   response = requests.get(ApiUrl) 
   weather = response.json() 
   currentTemp = weather[0]['Temperature']['Imperial']['Value']
   
   print ('The current weather in Plano is ' + str(weather[0]['WeatherText']) + '.')
   print ('The current temperature in Plano is ' + str(currentTemp) + ' F.')
   print (currentTemp)
   
   if currentTemp <= 40: 
       redLED.on()
       print ('red')
   elif 61 > currentTemp > 80: 
       yellowLED.on()
       print ('yellow')
   else: 
       greenLED.on()
       print ('green')
   time.sleep(1800) # 30 minutes 

  
