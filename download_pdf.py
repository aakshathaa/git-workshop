import requests

url = "https://pdfobject.com/pdf/sample.pdf"

response = requests.get(url)

with open("sample.pdf", "wb") as file:
    file.write(response.content)

print("PDF downloaded successfully")
