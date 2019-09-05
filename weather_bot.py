import smtplib
import requests
import time
from bs4 import BeautifulSoup


#Request data from web 
page = requests.get("https://weather.com/weather/today/l/eeb123acf2414db84d8aeddccbb00775b33e4798ed789cd7a988ac709a698c37")
#Parse html data
soup = BeautifulSoup(page.text, 'html.parser')


#Scrap forecast from weather.com
#Current weather conditions
forecast = soup.find('div', attrs={'class': 'today_nowcard-temp'})
forecast_phrase = soup.find('div', attrs={'class': 'today_nowcard-phrase'})
#Future weather conditions

#Same Day Future Forecast
forecast_today = soup.find('span', attrs={'class': 'today-daypart-title'})
forecast_today_cond = soup.find('span', attrs={'class': 'today-daypart-wxphrase'})

#Next Day Forcast
nextday_name = soup.find('span', attrs={'id': 'dp1-daypartName'})
nextday_phrase = soup.find('span', attrs={'id': 'dp1-phrase'})
location = soup.find('h1', attrs={'class': 'today_nowcard-location'})


#Clean Up data
curr_forecast = forecast.text
curr_forecast = curr_forecast[0:2] + "F"
forecast_phrase = forecast_phrase.text
forecast_today = forecast_today.text + ": "
forecast_today_cond = forecast_today_cond.text + " "
nextday_name = nextday_name.text + ": "
nextday_phrase = nextday_phrase.text
location = location.text
weather = "\n" + curr_forecast + " " + forecast_phrase + "\n" + location + "\n"
print(weather)
print(forecast_today + forecast_today_cond)
print(nextday_phrase)