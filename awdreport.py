import requests
from bs4 import BeautifulSoup
from pyrui import RUI
import re
from time import sleep

#
#
# # def Hparse(url):
r = requests.get("https://awd.apple.com/tracker3/577e6723690000f17ef9480a")
sleep(10)
soup = BeautifulSoup(r.content, "html.parser")
print r,soup
# links = []
# for link in soup.find_all('a'):
#     if "./ctbot" in link.get("href"):
#         links.append(link.get('href'))
#
# nLink = []
# rui = RUI('https://testautomation.apple.com', auth=("pradeep_sharma","Prashi33"))
# for i in range(len(links)):
#     r1 = links[i]
#     s1 = re.split("[, _?.]+", r1)
#     nLink.append("https://testautomation.apple.com/results/" +str(s1[3])+ "/")
#
#
# print nLink
#
# flinks = []
# print "Link Parser"
# for i in range(len(nLink)):
#     print nLink[i]
#     # r = RUI(nLink[i], auth=("pradeep_sharma","Prashi33"))
#     r2 = requests.get(nLink[i])
#     print r2
#     s2 = BeautifulSoup(r2.content, "html.parser")
#     for link in s2.findAll('a'):
#         # if "/results/" in link.get("href"):
#         print link
#             # flinks.append(link.get('href'))