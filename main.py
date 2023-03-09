import requests

# api key to log in

api_key = "f3e0471c2c044dd7b2193207230903"

# a user input the name of the city
city = input("Enter name of the City :")

# URL to and passed the key

url_Weather = 'https://api.weatherapi.com/v1/current.json?key='+api_key+"&q="+city+'&aqi=no'

# make HTTPS request

weather_data = requests.get(url_Weather)

# convert the data into Json
weather = weather_data.json()

# Assign the data from Json to variable
c = weather['current']['temp_c']
country_name = weather['location']['country']

# finally print 
print(country_name,c)