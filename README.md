# accuweather-api

Small project to test Accuweather APIs found at:  https://developer.accuweather.com/apis

From [Getting Started With Raspberry Pi, 3rd Edition, Ch. 10.](https://learning.oreilly.com/library/view/getting-started-with/9781680452457/ch10.html#chapid_12).

## Main app is "Current Conditions with Lights"

This app polls the Accuweather API every 30 minutes to retrieve the current weather conditions. 
It then takes the current temperature and lights one of three LEDs:
 - less than 40 degress F = red light
 - between 40 and 60 degrees F = yellow light
 - greater than 60 degress F = green light

Local files are stored on raspberry pi4 at: /home/pi/Python/accuweather-api
