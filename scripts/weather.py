import json 
import requests

response = requests.get("http://api.openweathermap.org/data/2.5/weather?lat=34.0721664&lon=74.809344&appid=4e027d2fcccd807da22c4507d2dafed5")
data = response.json()

# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    json.dump(data, outfile)
