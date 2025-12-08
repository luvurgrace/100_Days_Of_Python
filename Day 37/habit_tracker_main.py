import requests
import os
from datetime import datetime, timedelta

USERNAME = "hulkenberg"
TOKEN = os.environ.get("TOKEN")
now = datetime.now()
yesterday = now - timedelta(days=1)
today_date = f"{now.strftime("%Y%m%d")}"
yesterday_date = f"{yesterday.strftime("%Y%m%d")}"


pixela_endpoint = "https://pixe.la/v1/users"
user_params = { # user created
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url = pixela_endpoint, json = user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "GYM Graph",
    "unit": "Min",
    "type": "float",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint,json=graph_config,headers = headers)
# print(response.text)


pix_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}"
pix_config_crt = {
    "date": today_date,
    "quantity": input("How many minutes have you trained today? ")
}
# response = requests.post(url=pix_endpoint,json=pix_config_crt,headers=headers)
# print(response.text)
# print(yesterday_date)


pix_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{today_date}"

pix_config_upd = {
    "quantity": "50"
}
# response = requests.put(url=pix_update_endpoint,json=pix_config_upd,headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config["id"]}/{yesterday_date}"

# response = requests.delete(url=delete_endpoint,headers=headers)
# print(response.text)
