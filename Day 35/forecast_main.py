import requests
import os
from twilio.rest import Client


account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")

MY_LAT = 53.488392
MY_LON = 26.731430



parameters = {
     "lat": MY_LAT,
     "lon": MY_LON,
     "appid": api_key,
     "cnt": 4
 }


response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
weather_data = response.json()


will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an Umbrella!  ",
        from_ = "+12707431240",
        to = "+375297584457"
    )
    print(message.status)
