import requests
from bs4 import BeautifulSoup
import csv

class stock_info():
	def __init__(self):
		self.number = ""
		self.Company = ""
		self.Symbol = ""

response = requests.get("https://www.slickcharts.com/sp500").text

soup = BeautifulSoup(response, "lxml")

#Title of the webpage
headline = soup.find('h3', class_='text-center').text

#Description of the webpage
description_div = soup.find('div', class_='shadow p-3 mb-5 bg-white rounded')
description = (description_div.p.text)


#Table column names
column_html = soup.find('table', class_='table table-hover table-borderless table-sm')
column_head = column_html.thead
column_headers = []
for column in column_head.find_all('th'):
	column_headers.append(column.text.strip())