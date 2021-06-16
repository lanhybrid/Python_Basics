import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0'}
page = requests.get("https://www.google.com/search?client=firefox-b-d&q=dolar", headers=header)
soup = BeautifulSoup(page.content, 'html.parser')


valor_dollar = soup.find_all('span', class_='DFlfde SwHCTb')[0]

print(valor_dollar)
print(valor_dollar.text)
