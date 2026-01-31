import os
from time import strftime
import requests
from datetime import datetime

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
WEIGHT = 69
HEIGHT = 169
AGE = 21
GENDER = "male"
TOKEN = os.environ.get("TOKEN")

sheet_endpoint = "https://api.sheety.co/13dfcbe50c712a6ac5443a522f04580f/calTrackerData/workouts?raw=true"
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"

params = {
    "query": input("Tell me which exercises you did: "),
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
    "gender": GENDER
}


headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url = exercise_endpoint, json = params, headers = headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(sheet_endpoint, headers=bearer_headers, json = sheet_inputs)

    print(sheet_response.text)
    print(type(sheet_inputs["workout"]["time"]))
    print(type(now_time))

