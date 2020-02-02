import requests
import re
from bs4 import BeautifulSoup

page = requests.get("http://bom.gov.au")
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

# Returns the soup for current values
now_soup = []
for now in capitals_soup:
    now_soup.append(now.find("p", {"class": "now"}))

# Returns the soup for for current temperatures
capitals_now_soup = []
for temp_soup in now_soup:
    capitals_now_soup.append(list(temp_soup.children)[1])

# Returns all the temperature values for cities
temps = []
for temp in capitals_now_soup:
    temps.append(temp.get_text().encode('utf-8'))

temp_in_city =[]
[temp_in_city.append("The current temperature in " + str(city) + " is " + temp) for city, temp in zip(list_of_capitals, temps)]

for weather_report in temp_in_city:
    print(weather_report)
