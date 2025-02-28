import streamlit as st 
import bs4 as bs 
import requests

html = requests.get("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
soup = bs.BeautifulSoup(html.text)

ticker = []

tables = soup.find('table')
data = tables.find_all('td')
# print(data.text)

tickers = []
for i in data : 
    ndata = i.find('a' , class_ = 'external text')
    if ndata : 
        tickers.append(ndata.get_text())

print(tickers)
