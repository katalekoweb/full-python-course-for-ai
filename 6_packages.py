# Python's ecosystem
""" 
Web Scrapping
Data analysis
AI/ML
APIs
Automation
"""
from math import sqrt, pi
import random
import datetime
import requests
# Import entire module
# import math

# Import specific functions
# from math import sqrt

# Import with alias
# import pandas as pd

sqrt(18)
number = random.randint(1,10)
choice = random.choice(['Apple', 'Banana', 'Orange'])

today = datetime.date.today()
# print(today)
# print(choice)

# Where to find py packages
""" 
Pypi
Awesome python
"""

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
def get_weather (latitude, longitude):
    response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m")
    data = response.json()
    return data['current']['temperature_2m']

# Get temperature for different cities
paris_temp = get_weather(48.85, 2.35)
london_temp = get_weather(51.50, -0.12)
tokyo_temp = get_weather(35.60, 139.69)

print(f"Paris: {paris_temp}@C")
print(f"London: {london_temp}@C")
print(f"Tokyo: {tokyo_temp}@C")