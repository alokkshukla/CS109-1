from bs4 import BeautifulSoup
import requests
import pandas as pd

req = requests.get('http://charts.realclearpolitics.com/charts/1171.xml')
page = req.text

soup = BeautifulSoup(page, 'xml')


o = [];
r = [];
date = [];

for k in soup.find_all("value"):
	if k.parent.name == 'series':
		date.append(k.text)
	elif k.parent.name == 'graph':
		if k.parent.get("title") == "Obama":
			o.append(k.text)	
		if k.parent.get("title") == "Romney":
			r.append(k.text)	

#for v in soup.find_all("graph", {"title": "Obama"}):
	#o.append(v.text)
#for value in soup.find_all("graph"):
	#print value.text
print date
print o
print r
result = pd.DataFrame({'date': pd.to_datetime(date), 'Obama':o, 'Romney':r})