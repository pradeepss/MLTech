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

##############################
# from bs4 import BeautifulSoup
# import urllib2
#
# resp = urllib2.urlopen("http://gibson.apple.com/ctbot103.html")
# soup = BeautifulSoup(resp)#, from_encoding=resp.info().getparam('charset'))
#
# for link in soup.find_all('a', href=True):
#     print link['href']

###########
import urllib2

import re
#connect to a URL
url = "http://gibson.apple.com/ctbot103.html"
website = urllib2.urlopen(url)

#read html code
html = website.read()

#use re.findall to get all the links
# links = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", html)
match = '"((https|testrun)s?://.*?[results]\w+)"'
links = re.findall(match, html)


print len(links)
for i in range(len(links)):
    match = '[results]\w+'
    if re.search(match, links[i]):
        print links[i]



# for link in links:
#     print('href: %s, HTML text: %s' % (link[0], link[1]))