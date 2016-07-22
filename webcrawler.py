#############
# simple script to download text from a web address
#
# import urllib
# import HTMLParser
#
# urlText = []
#
# #Define HTML Parser
# class parseText(HTMLParser.HTMLParser):
#
#     def handle_data(self, data):
#         if data != '\n':
#             urlText.append(data)
#
# #Create instance of HTML parser
# lParser = parseText()
#
# thisurl = "http://gibson.apple.com/ctbot103.html"
#
#
#
#
# # handle = urllib.urlopen(thisurl)
# # html_gunk =  handle.read()
#
# #Feed HTML file into parser
# lParser.feed(urllib.urlopen(thisurl).read())
# lParser.close()
# for item in urlText:
#     print item

# ##############################
# from bs4 import BeautifulSoup
# import urllib2
#
# resp = urllib2.urlopen("http://gibson.apple.com/ctbot103_14A294a.html")
# soup = BeautifulSoup(resp)#, from_encoding=resp.info().getparam('charset'))
#
# for link in soup.find_all('a', href=True):
#     print link['href']

###########
# import urllib2
#
# import re
# #connect to a URL
# url = "http://gibson.apple.com/ctbot103.html"
# website = urllib2.urlopen(url)
#
# #read html code
# html = website.read()
#
# #use re.findall to get all the links
# # links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", html)
# match = '"((https|testrun)s?://.*?)"'
# links = re.findall(match, html)
#
#
# print len(links)
# for i in range(len(links)):
#     match = '[results]\w+'
#     if re.search(match, links[i]):
#         print links[i]



# for link in links:
#     print('href: %s, HTML text: %s' % (link[0], link[1]))
#
# import requests
# import BeautifulSoup
#
#
# def trade_spider(max_pages):
#     page = 1
#     while page <= max_pages:
#         url = 'https://buckysroom.org/trade/search.php?page=' + str(page)
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text)
#         for link in soup.findAll('a', {'class': 'item-name'}):
#             href = "https://buckysroom.org" + link.get('href')
#             title = link.string
#             print(href)
#             print(title)
#         page += 1
#
# # trade_spider(1)
#
#
# def craw4href():
#
#     url = 'http://www.learn4good.com/kids/index.htm'
#     source_code = requests.get(url)
#     plain_text = source_code.text
#     soup = BeautifulSoup(plain_text)
#     for link in soup.findAll('a', {'class': 'kids_index_bl'}):
#         # href = "https://buckysroom.org" + link.get('href')
#         # title = link.string
#         print(href)
#         # print(title)
#
# craw4href()

#########working code##
# import requests
# from bs4 import BeautifulSoup
#
# r = requests.get("http://gibson.apple.com/ctbot103_14A294a.html")
# soup = BeautifulSoup(r.content)
# # print soup.prettify()
# # soup.find_all('a')
# for link in soup.find_all('a'):
#     if "testautomation" in link.get("href"):
#         print link.text,link.get('href')
#
#########



import requests
from bs4 import BeautifulSoup
from pyrui import RUI
import re
from HTMLParser import HTMLParser


# help(RUI)
# rui = RUI('https://testautomation.apple.com', auth=("pradeep_sharma","Prashi33"))
rui = RUI("https://testautomation.apple.com", auth=("pradeep_sharma","Prashi33"))
result = rui.resultForUUID("2e5161c0-c9bf-401d-992e-3933720115b3")
print result
# http://gibson.apple.com/ctbot103_14A297_c7fd8793-302d-4a0f-87bd-66fa6840ec31.html
# for a in result.attachments:
#     print a.filename
#     print a.url

# def Hparse(url):
r = requests.get("http://gibson.apple.com/ctbot103_14A294a.html")
soup = BeautifulSoup(r.content, "html.parser")
links = []
for link in soup.find_all('a'):
    if "./ctbot" in link.get("href"):
        links.append(link.get('href'))

nLink = []
rui = RUI('https://testautomation.apple.com', auth=("pradeep_sharma","Prashi33"))
for i in range(len(links)):
    r1 = links[i]
    s1 = re.split("[, _?.]+", r1)
    nLink.append("https://testautomation.apple.com/results/testrun/" +str(s1[3])+ "/")

# print nLink



###########

#############













flinks = []
print "Link Parser"
for i in range(len(nLink)):
    print nLink[i]
    rui = RUI(nLink[i], auth=("pradeep_sharma","Prashi33"))
    r2 = rui.get(nLink[i])
    print r2
    s2 = BeautifulSoup(r2.content, "html.parser")
    for link in s2.findAll('a'):
        # if "/results/" in link.get("href"):
        print link
            # flinks.append(link.get('href'))

print flinks





















