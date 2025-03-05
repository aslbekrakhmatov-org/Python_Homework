import requests

API_KEY = "91ea15ce3900a85486798375ee12b1a0" 
city = input("Write your city's name to know weather in there:\n")
if (city.capitalize() == "Tashkent"):
    lat  = 41.2646
    lon = 69.2163


URL = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Description: {description.capitalize()}")
else:
    print("Error fetching weather data")