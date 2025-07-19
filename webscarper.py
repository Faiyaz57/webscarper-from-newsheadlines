import requests
from bs4 import BeautifulSoup

url = "https://www.ndtv.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

headline_tags = soup.find_all('h2', class_='newsHdng')

headlines = ["Probe Agency ED Files Chargesheet Against Congress Leader, Wife In Land Deal Case","Drugs, Steroids Found At Telangana Gym, Owner Arrested, Licence Cancelled","Nice Shirt”: US Border Patrol Mocks Arrested Migrant Wearing American Flag T‑Shirt","Probe Agency ED Files Chargesheet Against Congress Leader, Wife In Land Deal Case"]

for tag in headline_tags:
    a_tag = tag.find('a')
    if a_tag:
        text = a_tag.text.strip()
        if text and text not in headlines:
            headlines.append(text)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for headline in headlines:
        file.write(headline + "\n")

print(f"✅ {len(headlines)} headlines saved to headlines.txt")
