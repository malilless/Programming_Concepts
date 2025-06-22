import os

import requests
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

# Завдання 1
api_key = os.getenv('API_KEY')
location = os.getenv('LOCATION')
days = os.getenv('DAYS')
params = {
    "key": api_key,
    "q" : location,
    "days" : days
}
response = requests.get("https://api.weatherapi.com/v1/forecast.json", params = params)
data = response.json()

# Завдання 2
hourly_data = []

for day in data["forecast"]["forecastday"]:
    for hour in day["hour"]:
        hourly_data.append({
            "Time": pd.to_datetime(hour["time"]),
            "Temperature (°C)": hour["temp_c"],
            "Wind (km/h)": hour["wind_kph"]
        })

df = pd.DataFrame(hourly_data)
print(f"Загальний DataFrame:\n{df}")

# Завдання 3
tomorrow = (pd.Timestamp('today') + pd.Timedelta(days=1)).normalize()
filtered = df[(df["Time"] >= tomorrow) & (df["Time"] <= tomorrow + pd.Timedelta(days=2))]
max_temp = df["Temperature (°C)"].max()
print(f"Максимальна температура: {max_temp}")
min_temp = df["Temperature (°C)"].min()
print(f"Мінімальна температура: {min_temp}")
average_temp = df["Temperature (°C)"].mean()
print(f"Середня температура:  {average_temp}")

average_wind = df["Wind (km/h)"].mean()
windy_hours_count = df[df["Wind (km/h)"] > average_wind].shape[0]
print(f"Кількість годин, коли швидкість вітру перевищувала середню: {windy_hours_count}")