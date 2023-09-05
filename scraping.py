print("Start van de scraping applicatie")

from bs4 import BeautifulSoup
import requests

pagina = requests.get("https://bitcoinmeester.nl/")

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')

tabel = heeldehtml.find(".price1")

# print(tabel.prettify())

bitcoinprijs = heeldehtml.find(id = 'price1')

print(bitcoinprijs)