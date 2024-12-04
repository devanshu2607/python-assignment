##63.	Write a Python program that scrapes data from a website and processes it.

import requests
from bs4 import BeautifulSoup

url = "https://example.com"

response =  requests.get(url)
if response.status_code == 200:
    html_content=response.text
else :
    print("failed to retrieve the webpage")
    exit()

soup = BeautifulSoup(html_content,"html.parser")


data = []
for itrm in soup.find_all("a",href=True):
    title= item.text.strip()
    link = itrm['href']
    data.append({"title":title,"link":link})

for entry in data[:10]:
    print(f"title: {entry['title']},link :{entry['link']}")
