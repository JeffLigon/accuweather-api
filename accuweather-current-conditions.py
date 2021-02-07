import requests

key = 'UHo6YxqHHxBrei5DkAaEljGeCe4RdFOX'
location = '340969'
ApiUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + location + '?apikey=' + key

response = requests.get(ApiUrl) 
forecast = response.json() 

# weather = forecast[0]
# print ("The weather today is " + str(weather))
print ('The current weather in Plano is ' + str(forecast[0]['WeatherText']) + '.')
print ('The current temperature in Plano is ' + str(forecast[0]['Temperature']['Imperial']['Value']) + ' F.')
  
