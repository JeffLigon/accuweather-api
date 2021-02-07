import requests

key = 'UHo6YxqHHxBrei5DkAaEljGeCe4RdFOX'
location = '340969'
ApiUrl = 'http://dataservice.accuweather.com/currentconditions/v1/' + location + '?apikey=' + key

response = requests.get(ApiUrl) 
forecast = response.json() 

weather = forecast[0]
# print ("The weather today is " + str(weather))
print (forecast[0]['Epochtime'])

  
