from bs4 import BeautifulSoup

with open("weather.html", 'r', encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

weather_data = []
rows = soup.find("tbody").find_all("tr")
for tr in rows:
    tds = tr.find_all('td')
    day = tds[0].text.strip()
    temp = int(tds[1].text.strip().replace('°C', ''))
    cond = tds[2].text.strip()
    weather_data.append((day, temp, cond))
   

#printing datas
title = soup.find("h4")
print(f"{title.text}\n")
for item in weather_data:
    print(f"{item[0]} - {item[1]}°C - {item[2]}")

#specific data
temps = []
max_temp = max(weather_data, key=lambda x:x[1])
print("Highest Temp:")
print(f"{max_temp[0]} - {max_temp[1]}°C")

sunny_days = [day for day, temp, cond in weather_data if cond == "Sunny"]
print("Sunny days:")
print(", ".join(sunny_days))  

#average temperature
temp_sum = sum(temp for day, temp, cond in weather_data)
avg_temp = temp_sum/len(weather_data)
print(f"Average temp: {avg_temp}°C")
