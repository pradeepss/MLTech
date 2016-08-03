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



# import requests
# from bs4 import BeautifulSoup
# from pyrui import RUI
# import re
#
#
#
# # def Hparse(url):
# r = requests.get("http://gibson.apple.com/ctbot103_14A294a.html")
# soup = BeautifulSoup(r.content, "html.parser")
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
#
# print flinks

import pyrui
# import ResultQuery
import datetime
import os
import argparse
import subprocess

import zipfile

def read_zip_file(filepath):
    zfile = zipfile.ZipFile(filepath)
    for finfo in zfile.infolist():
        ifile = zfile.open(finfo)
        line_list = ifile.readlines()
        print line_list




rui = pyrui.RUI('https://testautomation.apple.com', auth=("pradeep_sharma","Prashi33"))

def getDateString(days=7):
    date = datetime.datetime.now()-datetime.timedelta(days=days)
    return date.strftime('%b. %d, %Y, %I:%M %p')

def getPredicates(days=7, hostname='', failed=None):
    print 'Querying RDB results in last %d days...' % days
    predicates = []

    predicates.append(("test_category", "starts with", "WAF"))
    predicates.append(("result_code", "not equals", "None"))

    if days:
        predicates.append(("result_started", "greater than", getDateString(days)))
    if hostname:
        predicates.append(("result_source", "starts with", hostname))
    if failed:
        predicates.append(("is_failed", "equals", failed))

    print('predicates:\n', predicates)
    return predicates

def showStats(results):
    print '\nTotal results:', len(results)
    print 'Total passed:', len([r for r in results if r['simple_status']=='Passed'])
    print 'Total failed:', len([r for r in results if r['simple_status']=='Failed'])
    print 'Total skipped:', len([r for r in results if r['simple_status']=='Skipped'])

# def downloadLog(result, logPath='.', filter='log'):
#     # print result.attachments
#     for attach in result.attachments:
#         path = os.path.join(logPath, result.result_source)
#         name = '%d_%s_%s' % (result.started_epoch, result.test_id, attach.filename)
#         if attach.filename.endswith('.%s' % filter):
#             p = '%s/%s' % (result.result_source, name)
#             print '%s%s' % (p.ljust(85), result.simple_status)
#             print 'size: %s' % attach.size
#             log = None
#             try:
#                 text = rui._get(attach.url, json=False, cache=True)
#                 log = text.encode('UTF-8')
#             except Exception, e:
#                 print 'Error: %s' % e
#                 continue
#
#             if not os.path.isdir(path):
#                 os.makedirs(path)
#
#             with open(os.path.join(path, name), 'w') as f:
#                 f.write(log)

def UnzipAWD(path2zip, path2metric):
    try:
        cmd = "unzip -j '" + pathzzip + "' '*/*.metriclog' -x '" + path2metric + "'"
        subprocess.call(cmd, shell=True)
    except Exception, e:
        print 'Error: %s' % e



def downloadLog(result, logPath='.', filter='log'):
    # print result.attachments
    for attach in result.attachments:
        path = os.path.join(logPath, result.result_source)
        name = '%d_%s_%s' % (result.started_epoch, result.test_id, attach.filename)


        if os.path.exists(os.path.join(path, name)):
            continue
        if attach.filename.endswith('.%s' % filter):
            p = '%s/%s' % (result.result_source, name)
            print '%s%s' % (p.ljust(85), result.simple_status)
            print 'size: %s' % attach.size

            if not os.path.isdir(path):
                os.makedirs(path)

            try:
                attach.download(path)
                # UnzipAWD(path , '/Volumes/Navjot/AWD/C09/Metric/')
            except Exception, e:
                print 'Error: %s' % e
                continue


def extractMetricLogsFromArchive(zippath, metricloglocation="/Volumes/Navjot/AWD/C09/Metric/"):
    cmd = "unzip -Z -1 " + zippath+ " |grep -i metric"
    run1 = subprocess.call(cmd, shell=True)
    print run1

def downloadLogs(results, path='Log', filter='log'):
    print '%s Start downloading %s logs %s' % ('='*25, len(results), '='*25)
    for result in results:
        downloadLog(result, path, filter)
    print '%s Finish download %s\n' % ('='*25, '='*35)


if __name__=='__main__':
    # predicates = getPredicates(days=1, hostname='C09', failed=None)
    # results = rui.resultsForPredicates(predicates)
    # showStats(results)
    # downloadLogs(results,path='/Volumes/Navjot/AWD/',filter='zip')

    # extractMetricLogsFromArchive("/Volumes/Navjot/AWD/C09/Siri_utterances_garage_door_2016-08-02_16-41_20267", "/Volumes/Navjot/AWD/C09/Metric/")
    # read_zip_file('/Volumes/Navjot/AWD/C09/Home_sharing_admin_to_shared_user_while_remote_2016-08-02_03-40_11322.zip')
    zip = zipfile.ZipFile('/Volumes/Navjot/AWD/C09/Home_sharing_admin_to_shared_user_while_remote_2016-08-02_03-40_11322.zip')
    zip.extractall("/Volumes/Navjot/AWD/C09/Metric/")




























































