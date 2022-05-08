import requests
import datetime
import webbrowser
from pprint import pprint
API_key='6ea6206ef4a59f4f0996e4b4e81fafdb'
def getstats():
      city=input("Enter the city: ")
      base_url='https://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city
      weather_data = requests.get(base_url).json()
      date_time=datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
      print("---------------------------------------------------------------")
      print(f'Date|Time : {date_time} ')
      if(weather_data['cod'])=='404':
          print(f'invalid name: \'{city}\' check the spelling ')
      else:
          city_temp=((weather_data['main']['temp'])-273.15)
          country_code=((weather_data['sys']['country']))
          clouds=(weather_data['weather'][0]['description'])
          wind_speed=((weather_data['wind']['speed']))
          humidity=(weather_data['main']['humidity'])
          print(f'city: {city} \ntemperature: {city_temp} degree celcius ')
          print(f'country code: {country_code} \nwindspeed: {wind_speed} meter/second ')
          print(f'Weather : {clouds} \nHumidity: {humidity} %')
      print("---------------------------------------------------------------")

getstats()

#pprint(weather_data)