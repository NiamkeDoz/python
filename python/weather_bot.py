import smtplib
import requests
import time
from bs4 import BeautifulSoup


#Request data from web 
page = requests.get("https://weather.com/weather/today/l/eeb123acf2414db84d8aeddccbb00775b33e4798ed789cd7a988ac709a698c37")
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

