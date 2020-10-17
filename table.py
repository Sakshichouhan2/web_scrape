import bs4
import requests

url = "https://webscraper.io/test-sites/tables"
data = requests.get(url)
soup = bs4.BeautifulSoup(data.text, 'html.parser')
file = open("copy.txt","w")
file.write(soup.get_text())

#This will Print all the html Source code.
#print(soup.prettify())
#This will print all the table tag data

#for table in soup.find('table'):
table = soup.find('table', class_ = 'table table-bordered')

print(table)

file.close()

#Find function will only print first Para but if we use .fine_all it will print all paragraph tag elements
#for para in soup.find_all('p'):
	#print(para.text)