from bs4 import BeautifulSoup
import requests
from pattern import web


# req = requests.get('http://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html')
# page = req.text

# soup = BeautifulSoup(page, 'html.parser')

# print type(soup)
# print type(soup.th)
# #print dir(soup.th)
# print soup.th
# print len(soup.th)

# print soup.th['class']

# print soup.th

# print soup.find_all('th')

# x = [];
# for i in soup.find_all('th'):
#  	x.append(i.text)
# print x[3:5]

# #print soup.find(id="l")
# # for link in soup.find_all('th'):
# #     print(link.get('class'))
# for i in soup.find_all('th'):
# 	print i.attrs

# for i in soup.find_all('a'):
# 	print i.contents
# # for i in soup.find_all('a'):
# # 	print i.value
# # 	if i.value == 'Final Results':
# # 		print no
# print '================================================='
# for i in soup.a.children:
# 	print i


dom = web.Element(requests.get('http://www.realclearpolitics.com/epolls/2010/governor/ca/california_governor_whitman_vs_brown-1113.html').text)

table = dom.by_tag('div#polling-data-rcp')[0]
result_data = table.by_tag('tr.final')[0]
td = result_data.by_tag('td')

results = [float(t.content) for t in td[3:-1]]
tot = sum(results) / 100

#get table headers
headers = table.by_tag('th')
labels = [str(t.content).split('(')[0].strip() for t in headers[3:-1]]

print labels
print headers
