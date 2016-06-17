from bs4 import BeautifulSoup
import requests


req = requests.get('http://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html')
page = req.text

soup = BeautifulSoup(page, 'html.parser')

print type(soup)
print type(soup.th)
#print dir(soup.th)
print soup.th.name
print len(soup.th)

th = soup.body
print body.attr



x = [];
for i in soup.find_all('th'):
 	x.append(i.text)
print x[3:5]
