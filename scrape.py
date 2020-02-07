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

