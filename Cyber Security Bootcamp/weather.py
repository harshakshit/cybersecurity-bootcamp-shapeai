import requests
#import os
import pytz
from datetime import datetime

api_key = '87d845b0b6cf29baa1a73cc34b067a95'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
IST = pytz.timezone('Asia/Kolkata')
date_time = datetime.now(IST).strftime("%d %b %Y | %I:%M:%S %p")

design_1 = "-------------------------------------------------------------"
first_output = "Weather Stats for - {}  || {}".format(location.upper(), date_time)
design_2 = "-------------------------------------------------------------"

second_output = "Current temperature is: {:.2f} deg C".format(temp_city)
third_output = "Current weather desc  :",weather_desc
fourth_output = "Current Humidity      :",hmdt, '%'
fifth_output = "Current wind speed    :",wind_spd ,'kmph'

print(design_1)
print(first_output)
print(design_2)
print(second_output)
print(third_output)
print(fourth_output)
print(fifth_output)

with open("weatherreport.txt" ,mode = 'w' ,encoding ='utf-8')as f :
 f.write(design_1)
 f.write(first_output)
 f.write(design_2)
 f.write(second_output)
 f.write(third_output)
 f.write(fourth_output)
 f.write(fifth_output)
 f.close()
