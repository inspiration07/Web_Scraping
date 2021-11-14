from scrapy import Selector
import requests
import pandas as pd


url = 'https://en.wikipedia.org/wiki/Krishnadevaraya'
html = requests.get(url).text

sel = Selector(text=html)
name = sel.xpath(
    '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/table/tbody//text()').extract()
while (name.count('\n')):
    name.remove('\n')

reign = sel.xpath(
    '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]//text()').extract()
name = [x for x in name if x not in reign]
reign = list(map(lambda x: x.strip(), reign))

Sangama_dynasty = ['Sangama dysnasty'] * 12
Saluva_dynasty = ['Saluva dynasty'] * 3
Tuluva_dynasty = ['Tuluva dynasty'] * 6
Aravidu_dynasty = ['Aravidu dynasty'] * 8
dynasty = Sangama_dynasty + Saluva_dynasty + Tuluva_dynasty + Aravidu_dynasty
dynasty_old = ['Sangama dynasty', 'Saluva dynasty',
               'Tuluva dynasty', 'Aravidu dynasty']
name = [x for x in name if x not in dynasty_old]
print(len(name))
print(len(dynasty))
print(len(reign))

data = {'Name': name, 'Reign': reign, 'Dynasty': dynasty}

df = pd.DataFrame(data)
df.to_csv('Vijaynagar_Empire.csv')


# Ruins of Hampi

url_2 = "https://www.ghatroads.in/south-india-travel/historical-tourism-info/hampi-vijayanagaram"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
html_2 = requests.get(url_2, headers=headers).text
sel = Selector(text=html_2)
monument = sel.xpath('//*[@class="accordion-heading"]//p[1]//text()').extract()
monument = list(map(lambda x: x.strip(), monument))
while (monument.count('\n')):
    monument.remove('\n')
print(monument)

description = sel.xpath(
    '//*[@class="accordion-inner"]//p[1]//text()').extract()
while (description.count('\n')):
    name.remove('\n')
print(description)

data_2 = {'Monument': monument, 'Description': description}

df_2 = pd.DataFrame.from_dict(data_2, orient='index')
df_2 = df_2.transpose()
df_2.to_csv('Ruins of Hampi.csv')


tup = (1, 2, 3, ['Subodh', 'H'])
print(tup[3][0])
