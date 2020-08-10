import requests
baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID': 'e77f53292cfdb88635b821aa4c251486', 'q': 'Seattle, US'}
response = requests.get(baseUrl, params=parameters)

print(response.content)

