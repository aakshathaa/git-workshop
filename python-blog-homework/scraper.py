import requests
from bs4 import BeautifulSoup

url = "https://blog.python.org/"

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("article")

print("Number of articles:", len(articles))

for article in articles:
    title = article.find("h3").get_text(strip=True)

    author = article.find("span", class_="font-medium").get_text(strip=True)

    date = article.find("time").get_text(strip=True)

    link = article.find("a")["href"]

    if link.startswith("/"):
        link = "https://blog.python.org" + link

    print("Title:", title)
    print("Author:", author)
    print("Date:", date)
    print("URL:", link)
    print("-" * 80)
