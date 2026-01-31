import requests
from datetime import datetime

MY_LAT = 53.488392
MY_LONG = 26.731430
F = 0

# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
#
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data")
# response.raise_for_status()
#
# data = response.json()["timestamp"]
# print(data)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": F
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)