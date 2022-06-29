# https://openweathermap.org/api
# pip install colorama
import requests
from colorama import Fore, Back, Style
import json
city = input("Enter city name :")  # tashkent

API_KEY = "YOUR API KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
response = requests.get(url)
# print(response.status_code)  # agar 200 bo'lsa demak OK
# kelgan json ko'rinishidagi malumotlarni python dict ga olish
data = response.json()


temp_f = data.get("main").get("temp")
temp_c = round(temp_f - 273, 2)
city_name = data.get("name")
status = data.get("weather")[0].get("main")
desc = data.get("weather")[0].get("description")
print(Fore.RED + f"city : {city_name}")
print(Fore.CYAN + f"Temperature F : {temp_f}")
print(Fore.YELLOW + f"Temperature C : {temp_c}")
print(Fore.MAGENTA + f"status : {status}")
print(Fore.BLUE + f"description : {desc}")
