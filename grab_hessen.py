import requests
from bs4 import BeautifulSoup

# default bs4 stuff
url = "https://soziales.hessen.de/gesundheit/infektionsschutz/coronavirus-sars-cov-2/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle-hessen"
r = requests.get(url)
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'lxml')

# navigate to table (diiiirty)
div = soup.findAll('div', {'class': ["he_content_body"]})
table = div[0].findAll('table')

# extract data from table
table_rows = table[0].findAll('tr')
results = []
for tr in table_rows:
	td = tr.findAll('td')
	result = (td[0].text, td[1].text)
	results.append(result)

# remove headers
results = results[1:]

#convert to int and sort
results = [(location, int(amount)) for location, amount in results]
results.sort(key=lambda x:x[1], reverse=True)

# output
print("Kreis/Stadt,bestätigte Fälle")
for result in results:
	print(result[0][1:-1] + "," + str(result[1]))
