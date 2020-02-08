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


#Components of the S&P 500
stock_info_list = []

table = soup.find('table', class_='table table-hover table-borderless table-sm')
body = table.find('tbody')
for row in body.find_all('tr'):
	info_dict = {"#": None, "Company": None, "Symbol":None, "Weight":None, "Price":None, "Chg":None, "% Chg":None}
	info_item_lst = []
	for column in row.find_all('td'):
		a_tag = column.findChildren('a', recursive=True)
		img_tag = column.findChildren('img', recursive=True)
	if a_tag:
		for child in a_tag:
			info_item_lst.append(child.text.lstrip())
	if img_tag:
		for child in img_tag:
			info_item_lst.append(child['src'].text.lstrip())
	else:
		for column in row.find_all('td'):
			info_item_lst.append(column.text.lstrip())
	for info_item in info_dict.keys():
		txt = info_item_lst.pop(0)
		info_dict[info_item] = txt
	stock_info_list.append(info_dict)

csv_file = open('stocks_scrape.csv', 'w+', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(column_headers)

for stock_info in stock_info_list:
	csv_writer.writerow(stock_info.values())
'''
print(headline)
print(description)
print(column_headers)
print(stock_info_list)
'''