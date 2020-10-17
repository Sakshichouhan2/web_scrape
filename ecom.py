from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/e-commerce/allinone"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
#print(soup)

#Images
'''for a_tag in soup.findAll("img"):
	href = a_tag.attrs.get("src")
	if href !="":
		print(href)
		continue'''

#Image tag
div = soup.find('div',{'class': 'col-sm-4 col-lg-4 col-md-4'})
a = div.find('img')
link = a.attrs.get("src")
print(link)

