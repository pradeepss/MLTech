import requests
from bs4 import BeautifulSoup
stock = 'NFLX'
link = 'https://www.americanbulls.com/SignalPage.aspx?lang=en&Ticker=' + stock
r = requests.get(link)
soup = BeautifulSoup(r.content, "html.parser")
# print(soup)
for each_div in soup.findAll('span',{'class':'dxeBase vtoptext10a'}):
# for each_div in soup.findAll('td',{'class':'dxgv'}):
    print(stock + " ===> " + each_div.text)





#
# from BeautifulSoup import BeautifulSoup
# f = open()
# soup = BeautifulSoup(f)
# print(soup)
# for each_div in soup.findAll('div',{'class':'dxeBase vtoptexta'}):
#     print(each_div)









