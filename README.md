# accuweather-api

Small project to test Accuweather APIs found at:  https://developer.accuweather.com/apis

From ["Getting Started With Raspberry Pi, 3rd Edition", Ch. 10.]
(https://learning.oreilly.com/library/view/getting-started-with/9781680452457/ch10.html#chapid_12).

##Main app is "Current Conditions with Lights"

This app polls the Accuweather API every 30 minutes to retrieve the current weather conditions. 
It then takes the current temperature and lights one of three LEDs:
 - < 40 degress = red light
 - > 40 and < 60 = yellow light
 - > 60 = green light

Local files stored on raspberry pi4 at: /home/pi/Python/accuweather-api
