
import requests, json
import pprint
# Enter your API key here
api_key = "6aae3f0f4fb4033d0dcd13fc9d59b3b4"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name
# city_name = input("Enter city name : ")

# complete_url variable to store
# complete url address


# get method of requests module
# return response object
def getWeather(city):
    complete_url = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()
    pprint.pprint(data)

    temp = data["main"]["temp"]
    status = data["weather"][1]["main"]

    res = {
        "temp":temp,
        "status": status
    }
    return res
# json method of response object
# convert json format data into
# python format data
# x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
# if x["cod"] != "404":
#
# 	# store the value of "main"
# 	# key in variable y
# 	y = x["main"]
#
# 	# store the value corresponding
# 	# to the "temp" key of y
# 	current_temperature = y["temp"]
#
# 	# store the value corresponding
# 	# to the "pressure" key of y
# 	current_pressure = y["pressure"]
#
# 	# store the value corresponding
# 	# to the "humidity" key of y
# 	current_humidity = y["humidity"]
#
# 	# store the value of "weather"
# 	# key in variable z
# 	z = x["weather"]

	# store the value corresponding
	# to the "description" key at
	# the 0th index of z
# 	weather_description = z[0]["description"]
#
# 	# print following values
# 	print(" Temperature (in kelvin unit) = " +
# 					str(current_temperature) +
# 		"\n atmospheric pressure (in hPa unit) = " +
# 					str(current_pressure) +
# 		"\n humidity (in percentage) = " +
# 					str(current_humidity) +
# 		"\n description = " +
# 					str(weather_description))
#
# else:
# 	print(" City Not Found ")

# get USERS json
url = "https://jsonplaceholder.typicode.com/users"
d = requests.get(url)
res = d.json()
# print(type(res))
names = []
for n in range(len(res)):
    for x in res[n].items():
        if x[0] == "name":
            names.append(x[1])
print(names)
# pprint.pprint(res)