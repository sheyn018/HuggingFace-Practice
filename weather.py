import os
from langchain_community.utilities import OpenWeatherMapAPIWrapper

os.environ["OPENWEATHERMAP_API_KEY"] = ""
weather = OpenWeatherMapAPIWrapper()
weather_data = weather.run("Delhi")
print(weather_data)