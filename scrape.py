import requests
import re
from bs4 import BeautifulSoup
page = requests.get("http://bom.gov.au")


soup = BeautifulSoup(page.content, 'html.parser')
# soup =soup.prettify().encode('utf-8')

# print(soup)
print(soup.title.get_text())


# capitals = []
# capitals = soup.find_all("div", {"class": "capital"})
# print(list(capitals))

sydney = soup.find("div", {"class": "capital"})
# print(sydney)

now = sydney.find("p", {"class": "now"})
# print(now)
sydney_now = list(now.children)[1]
# print(sydney_now)

temp = sydney_now.get_text().encode('utf-8')

print("The current temperature in Sydney is " + temp)
