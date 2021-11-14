from scrapy import Selector
import requests


url = 'https://en.wikipedia.org/wiki/Krishnadevaraya'
html = requests.get(url).text

sel = Selector(text=html)
name = sel.xpath(
    '//*[@id="mw-content-text"]/div[1]/table[2]/tbody/tr[2]/td/table/tbody//text()').extract()
while (name.count('\n')):
    name.remove('\n')
print(name)
