from sys import argv
import re
import datetime
# datafile = file.read('/Users/ltecoex/Downloads/26407800/Write_A2DP_WiFi-hci.pklg.txt')
#
# for line in datafile:
#     if '[200D]' in line:
#         print line
#     if 'LE Connection Complete' in line:
#         print line
startTime = 0
stopTime = 0
with open('/Users/pradeepsharma/Desktop/Read_A2DP_WiFi_KB-hci.pklg.txt', 'r') as inF:
    for line in inF:
        if '[200D]' in line:
            print line
            startTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{3}', line)
            print startTime
        if 'LE Connection Complete' in line:
            print line
            stopTime=re.findall(r'\d{2}:\d{2}:\d{2}.\d{3}', line)
if startTime != 0:
    delta=(datetime.datetime.strptime("".join(stopTime), "%H:%M:%S.%f")-datetime.datetime.strptime("".join(startTime),"%H:%M:%S.%f")) #Join command to convert list to string.
    print delta
else:
    print "No LE connection found"
inF.close()