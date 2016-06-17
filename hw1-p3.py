from bs4 import BeautifulSoup
import requests


req = requests.get('http://www.realclearpolitics.com/epolls/2010/governor/2010_elections_governor_map.html')
html = req.text

soup = BeautifulSoup(html, 'html.parser')

# print soup.find_all("option")
# print soup.option("value")
# print soup.body.option
print [t["value"] for t in soup.find_all("option") if (t.get("value") & "http" in t["value"])]