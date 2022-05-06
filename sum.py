import requests
from pprint import pprint


API_key='6ea6206ef4a59f4f0996e4b4e81fafdb'
city=input("Enter the city: ")
base_url='https://api.openweathermap.org/data/2.5/weather?appid='+API_key+'&q='+city

weather_data = requests.get(base_url).json()

pprint(weather_data)