import requests
# import pprint
api = '6508c80d1115b29a5bb0e65c0009916d'
city = 'London'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'


def getWeather():
    data = requests.get(url).json()
    s = data['weather'][0]['description']
    t = int(data['main']["temp"])
    c = data['name']
    print(s,t-273,c)