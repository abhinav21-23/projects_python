import requests
import json
import pyttsx3

city = input("Enter the name of the city\n")
url = f"http://api.weatherapi.com/v1/current.json?key=a5b528410e484d3d8e3160520230607&q={city}"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
print(w)
pyttsx3.speak(f"The current weather in {city} is {w} degree celsius")
