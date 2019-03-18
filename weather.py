import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"4c9882268664d84df2bf30e5cbbf08b2"}

response = requests.get(endpoint, params=payload)
data = response.json()

print response.url
print response.status_code
print response.headers["content-type"]
temperature = data["main"]["temp"]
city = data["name"]
country = data["sys"]["country"]
weather = data["weather"][0]["description"]

print "It's {}C in {}, {} and there will be {}".format(temperature, city, country, weather)
