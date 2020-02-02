import requests
import re
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

page = requests.get("http://www.bom.gov.au")
soup = BeautifulSoup(page.content, 'html.parser')
# soup = soup.prettify().encode('utf-8')
# print(soup)

print(soup.title.get_text())

# Returns the soup for all capital cities
capitals_soup = soup.find_all("div", {"class": "capital"})


# Returns a list of capital cities
list_of_capitals = []
for capital in capitals_soup:
    list_of_capitals.append(capital.find("h3").get_text())

# Returns the soup for current weather values
now_weather_soup = []
for now in capitals_soup:
    now_weather_soup.append(now.find("p", {"class": "now"}))

# Returns the soup for for current temperatures
capitals_now_weather_soup = []
for temp_soup in now_weather_soup:
    capitals_now_weather_soup.append(list(temp_soup.children)[1])

# Returns all the temperature values for cities
temps = []
for temp in capitals_now_weather_soup:
    temps.append(temp.get_text())

temp_in_city =[]
[temp_in_city.append("The current temperature in " + city + " is " + temp) for city, temp in zip(list_of_capitals, temps)]

for weather_report in temp_in_city:
    print(weather_report)

temp_nums =[]
for val in temps:
    temp_nums.append(float(val.replace("°", "")))

##=======================##
## Plotting the data

y_pos = np.arange(len(list_of_capitals))

plt.bar(y_pos, temp_nums)
plt.xticks(y_pos, list_of_capitals)
plt.xticks(rotation=45)
plt.ylabel('Temperature (°C)')
plt.title('Temperatures of Capital Cities')
plt.tight_layout()

plt.show()
