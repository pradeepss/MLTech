import pyrui
# import ResultQuery
import datetime
import os
import argparse
import subprocess
import zipfile


tmpDir = '/Users/ltecoex/Data/Download/'
metricDir = '/Users/ltecoex/Data/Logs/'

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
        # name = '%d_%s_%s' % (result.started_epoch, result.test_id, attach.filename)
        name = attach.filename



        if os.path.exists(os.path.join(path, name)):
            continue
        if attach.filename.endswith('.%s' % filter):
            p = '%s/%s' % (result.result_source, name)
            print '%s%s' % (p.ljust(85), result.simple_status)
            print 'size: %s' % attach.size

            if not os.path.isdir(path):
                os.makedirs(path)

            try:
                archive = path+ '/' + name
                attach.download(path)
                extractMetricLogsFromArchive(archive)
            except Exception, e:
                print 'Error: %s' % e
                continue


def extractMetricLogsFromArchive(zippath):
    print zippath
    zip = zipfile.ZipFile(zippath)
    zip.extractall(tmpDir)
    full_file_paths = get_filepaths(tmpDir)
    cmd = 'rm -r ' + tmpDir
    subprocess.call(cmd, shell=True)

def downloadLogs(results, path='Log', filter='log'):
    print '%s Start downloading %s logs %s' % ('='*25, len(results), '='*25)
    for result in results:
        downloadLog(result, path, filter)
    print '%s Finish download %s\n' % ('='*25, '='*35)


def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.
            if "metriclog" in filename:
                print('converting file')
                cmd = "AWDDisplay " + filepath + " > " +metricDir+''+ filename  +".txt"
                subprocess.call(cmd, shell=True)
                print ('Deleting file' + filepath)
                cmd = "rm -f " + filepath
                subprocess.call(cmd, shell=True)
            else:
                print('Deleting file' + filepath)
                cmd = "rm -f " + filepath
                subprocess.call(cmd, shell=True)
    return file_paths  # Self-explanatory.


if __name__=='__main__':
    # predicates = getPredicates(days=1, hostname='C09', failed=None)
    # results = rui.resultsForPredicates(predicates)
    # showStats(results)
    # downloadLogs(results,path=tmpDir,filter='zip')
    parseMetric(mFilePath)
























































