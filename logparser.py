import os
import sys
import collections
import re
import numpy
import datetime
from xlwt import *
from xlrd import open_workbook
from xlutils import *
from time import strftime, sleep


messageList=['Received incoming message','Answering incoming message','Starting write for accessory','Completed write for accessory','Relaying message']
keyLists=['kAddAccessoryRequestKey','kCharacteristicReadRequestKey','kCharacteristicWriteRequestKey','kSiriCommandRequestKey', 'kMultipleCharacteristicReadRequestKey','kMultipleCharacteristicWriteRequestKey','kCharacteristicEnableNotificationRequestKey']

font0 = Font()
font0.name = 'Times New Roman'
font0.bold = True
font0.size='16'
styleHeader = XFStyle()
styleHeader.font = font0
try:
    book = open_workbook(r'Homekit_Performance.csv')
    HKBook = copy(book)
    HKSheet = HKBook.add_sheet(strftime('Local'))
    HKSheet = HKBook.add_sheet(strftime('Remote'))
except:
    HKBook = Workbook()
    HKSheet1 = HKBook.add_sheet(strftime('Local'))
    HKSheet2 = HKBook.add_sheet(strftime('Remote'))

def timeCalculator(args, filename, col):
    row = 0
    startKey=None
    stopKey=None
    remoteIndicator= False
    successRate=0
    timeList=[]
    localTime=[]
    remoteTime=[]
    LOCATION = os.path.expanduser("~/Desktop/HK/")
    srcFile = os.path.join(LOCATION, filename)
    output= open(srcFile, 'r')
    for line in output:
        for key in messageList:
            #print key
            searchobj=re.search(key, line)
            if searchobj:
                #print line #for debugging
                if (('Received' in line) and (args in line)):
                    startTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{6}', line)
                    startKey=re.findall(r'\(([0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})\)', line)
                elif (('Answering' in line) and (args in line)):
                    stopTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{6}', line)
                    stopKey=re.findall(r'\(([0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})\)', line)
                elif (('Starting' in line) and (args in line)):
                    startTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{6}', line)
                    startKey=re.findall(r'\(([0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})\)', line)
                elif (('Completed' in line) and (args in line)):
                    stopTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{6}', line)
                    stopKey=re.findall(r'\(([0-9A-F]{8}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{4}-[0-9A-F]{12})\)', line)
                elif ('Relaying message' in line) :
                    remoteIndicator = True
        if ((startKey is not None) and (stopKey is not None) and (startKey==stopKey)):
            delta=(datetime.datetime.strptime("".join(stopTime), "%H:%M:%S.%f")-datetime.datetime.strptime("".join(startTime),"%H:%M:%S.%f")) #Join command to convert list to string.
            timeList.append((remoteIndicator,float(delta.total_seconds())))
            startKey=None
            stopKey=None
            remoteIndicator = False

    if len(timeList)>0:
        for data in timeList:
            if (data[0]==False):
                localTime.append(data[1])
            elif (data[0]==True):
                remoteTime.append(data[1])
        if len(localTime)>0:
            math=sum(localTime)/len(localTime)
            print args + " Local"
            print "--------------------------------------"


            if args == keyLists[0]:
                HKSheet1.write(row,col,'Pairing',styleHeader)
            elif args == keyLists[1]:
                HKSheet1.write(row,col,'APIRead',styleHeader)
            elif args == keyLists[2]:
                HKSheet1.write(row,col,'APIWrite',styleHeader)
            elif args == keyLists[3]:
                HKSheet1.write(row,col,'Siri Request',styleHeader)
            elif args == keyLists[4]:
                HKSheet1.write(row,col,'Multi Read',styleHeader)
            elif args == keyLists[5]:
                HKSheet1.write(row,col,'Multi Write',styleHeader)
            elif args == keyLists[6]:
                HKSheet1.write(row,col,'Notification',styleHeader)


            i = 0
            while i<len(localTime):
                row += 1
                HKSheet1.write(row,col,localTime[i], styleHeader)
                i+=1
            #            print("values(ms): " +str(localTime))
            print("Average Latency(s): " +str(round(float(math),3)))
            print("Count: " +str(len(localTime)))
            print("Max Value(s): " +str(round(max(localTime),3)))
            print("Min Value(s): " +str(round(min(localTime),3)))
            print("Median Value(s): " +str(round(numpy.median(localTime),3)))
            #print("StdDev Value(s): " +str(round(numpy.std(localTime),3)))
        if len(remoteTime)>0:
            math=sum(remoteTime)/len(remoteTime)
            print args + " Remote"
            print "--------------------------------------"
            if args == keyLists[0]:
                HKSheet2.write(row,col,'Pairing',styleHeader)
            elif args == keyLists[1]:
                HKSheet2.write(row,col,'APIRead',styleHeader)
            elif args == keyLists[2]:
                HKSheet2.write(row,col,'APIWrite',styleHeader)
            elif args == keyLists[3]:
                HKSheet2.write(row,col,'Siri Request',styleHeader)
            elif args == keyLists[4]:
                HKSheet2.write(row,col,'Multi Read',styleHeader)
            elif args == keyLists[5]:
                HKSheet2.write(row,col,'Multi Write',styleHeader)
            elif args == keyLists[6]:
                HKSheet2.write(row,col,'Notification',styleHeader)
            i = 0
            while i<len(localTime):
                row += 1
                HKSheet2.write(row,col,localTime[i], styleHeader)
                i+=1
            #            print("values(ms): " +str(remoteTime))
            print("Average Latency(s): " +str(round(float(math),3)))
            print("Count: " +str(len(remoteTime)))
            print("Max Value(s): " +str(round(max(remoteTime),3)))
            print("Min Value(s): " +str(round(min(remoteTime),3)))
            print("Median Value(s): " +str(round(numpy.median(remoteTime),3)))
            #print("StdDev Value(s): " +str(round(numpy.std(localTime),3)))





def execute():
    print("=========================Calculating===============================")
    print("Welcome to logParser v1.1")
    srcFilename = raw_input('Enter a filename: ')
    print("\n")
    keyLists=['kAddAccessoryRequestKey','kCharacteristicReadRequestKey','kCharacteristicWriteRequestKey','kSiriCommandRequestKey', 'kMultipleCharacteristicReadRequestKey','kMultipleCharacteristicWriteRequestKey','kCharacteristicEnableNotificationRequestKey']
    col = 0
    for key in keyLists:
        timeCalculator(key,srcFilename, col)
        col += 1
    HKBook.save('Homekit_Performance.csv')

if __name__ == '__main__':
    execute()






