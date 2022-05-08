import requests
import datetime
from pprint import pprint


API_key='6ea6206ef4a59f4f0996e4b4e81fafdb'
city=input("Enter the city: ")
base_url='https://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city

weather_data = requests.get(base_url).json()
city_temp=((weather_data['main']['temp'])-273.15)
country_code=((weather_data['sys']['country']))
clouds=(weather_data['weather'][0]['description'])
wind_speed=((weather_data['wind']['speed']))
humidity=(weather_data['main']['humidity'])
date_time=datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
print("---------------------------------------------------------------")
if(weather_data['cod'])=='404':
    print('invalid {city} name check the spelling ')
else:
    print(f'Date|Time : {date_time} ')
    print(f'city: {city} \ntemperature: {city_temp} degree celcius ')
    print(f'country code: {country_code} \nwindspeed: {wind_speed} meter/second ')
    print(f'Weather : {clouds} \nHumidity:{humidity} %')
print("---------------------------------------------------------------")
#pprint(weather_data)