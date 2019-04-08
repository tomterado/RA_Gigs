import requests
import re
from bs4 import BeautifulSoup

url = "https://www.residentadvisor.net/events/au/sydney"
response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# content = soup.find_all('a', href=True, )

# for a in content:
#     if a['href'].startswith('/events/1'):
#         print(a['title'])

for h1 in soup.find_all('h1', {'class': 'event-title'}):
    for each in h1.find_all('a'):
        title = each.get('href')
        print each.string
