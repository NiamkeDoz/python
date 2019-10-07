import smtplib
import requests
import time
from bs4 import BeautifulSoup

#List of cities
cities = [
    'Glen Carbon, IL',
    'Edwardsville, IL',
    'Decatur, IL',
    'Chicago, IL',
    'St. Louis, MO'
]

#Dictionary of city urls
city_url = {
    'Glen Carbon, IL': 'https://weather.com/weather/today/l/6aac383f81800632ef5ac912703b9ad03fc1c483d9d340c9ceea3b527f9d6c25',
    'Edwardsville, IL': 'https://weather.com/weather/today/l/eeb123acf2414db84d8aeddccbb00775b33e4798ed789cd7a988ac709a698c37',
    'Decatur, IL': 'https://weather.com/weather/today/l/4f3cdad7aac4a702031dd6d797e9225e37d054b615d9f3fbe24e9571f5aa1010',
    'St. Louis, MO': 'https://weather.com/weather/today/l/7d11e61b33b7d790573f8183cf3280fc8158bfa60ef3f3a96d426a427f0ccd0c',
    'Chicago, IL': 'https://weather.com/weather/today/l/e0abde3003a88dedecad92fedc96375000c16843287a51dbf2cd92f062217180' 
}

#Number of cities in list
NumOfCities = len(cities)
NumOfCities = int(NumOfCities)

for x in range(NumOfCities):
    print(str(x) + '. ' + cities[x])

user_input = input()
user_input = int(user_input)
city = cities[user_input]

#Request data from web 
page = requests.get(city_url[city])
#Parse html data
soup = BeautifulSoup(page.text, 'html.parser')


#Scrap forecast from weather.com

#Weather Location
location = soup.find('h1', attrs={'class': 'today_nowcard-location'})

#Timestamp
timestamp = soup.find('p', attrs={'class': 'today_nowcard-timestamp'})

#Current weather conditions
forecast = soup.find('div', attrs={'class': 'today_nowcard-temp'})
forecast_phrase = soup.find('div', attrs={'class': 'today_nowcard-phrase'})
#Future weather conditions

#Same Day Future Forecast
forecast_today = soup.find('span', attrs={'class': 'today-daypart-title'})
forecast_today_cond = soup.find('span', attrs={'class': 'today-daypart-wxphrase'})
forecast_today_hilo = soup.find('div', attrs={'id': 'dp0-highLow'})
forecast_today_temp = soup.find('div', attrs={'class': 'today-daypart-temp'})
precip = soup.find('span', attrs={'class': 'precip-val'})


#Clean Up data
curr_forecast = forecast.text
curr_forecast = curr_forecast[0:2] + "F"

forecast_phrase = forecast_phrase.text
forecast_today = forecast_today.text + ": "
forecast_today_cond = forecast_today_cond.text + "\n"
forecast_today_hilo = forecast_today_hilo.text + ": "
forecast_today_temp = forecast_today_temp.text
forecast_today_temp = forecast_today_temp[0:2] + 'F'


precip = precip.text
timestamp = timestamp.text + "\n"
location = location.text
weather = "\n" + curr_forecast + " " + forecast_phrase + "\n" + location + '\n' + timestamp + '\n' + forecast_today + forecast_today_cond + forecast_today_hilo + forecast_today_temp
print(weather)
print('Chance of precipitation: ' + precip)

