import requests
from bs4 import BeautifulSoup

def scrapper(stock):
    url = 'http://finance.google.com/finance/info?q=nse:'+stock
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html,"lxml")
    table = soup.find('p')
    data = table.prettify()
    final_string = data.split("\n")
    current_rate=final_string[6].split(":")
    return stock+current_rate[1]