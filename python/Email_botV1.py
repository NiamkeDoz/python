import smtplib
import requests
import time
from bs4 import BeautifulSoup


#Request data from web 
page = requests.get("https://weather.com/weather/today/l/eeb123acf2414db84d8aeddccbb00775b33e4798ed789cd7a988ac709a698c37")
#Parse html data
soup = BeautifulSoup(page.text, 'html.parser')

count = int(0)


#Scrap forecast from weather.com
forecast = soup.find('div', attrs={'class': 'today_nowcard-temp'})
forecast_phrase = soup.find('div', attrs={'class': 'today_nowcard-phrase'})
forecast_today = soup.find('div', attrs={'class': 'today-daypart-top'})
location = soup.find('h1', attrs={'class': 'today_nowcard-location'})


#Clean Up data
curr_forecast = forecast.text
curr_forecast = curr_forecast[0:2] + "F"
forecast_phrase = forecast_phrase.text
forecast_today = forecast_today.text
location = location.text
weather = "\n" + curr_forecast + " " + forecast_phrase + "\n" + location + "\n"
print(weather)
print(forecast_today)

#Email Credentials
# server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#Replace login with your crendentials
#1. Recepient's Email
#2. Message
# server.login("example@gmail.com", "password")
# server.sendmail(
#     "ScootBot94", 
#     "1. receipent Email/Text", 
#     "2. {}".format(weather))
# server.quit()

# count += 1
