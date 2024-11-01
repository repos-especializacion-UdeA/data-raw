import requests
from bs4 import BeautifulSoup

## https://realpython.com/beautiful-soup-web-scraper-python/

URL = "https://ninapro.hevs.ch/instructions/DB1.html"
page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
