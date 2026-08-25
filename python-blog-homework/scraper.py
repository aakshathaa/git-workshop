import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/"

response = requests.get(url)
print("STATUS:", response.status_code)

soup = BeautifulSoup(response.text, "html.parser")

print("TITLE:", soup.title.get_text(strip=True))

print("ARTICLE COUNT:", len(soup.find_all("article")))
print("H2 COUNT:", len(soup.find_all("h2")))

for h2 in soup.find_all("h2"):
    print("H2:", h2.get_text(" ", strip=True))
