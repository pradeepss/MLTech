import os
import subprocess


def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if "metriclog" in filename:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
                cmd = "AWDDisplay " + filepath + " > /Volumes/CarryMac/Users/pradeepsharma/Desktop/AWD/" + filename  +".txt"
                subprocess.call(cmd, shell=True)
    return file_paths  # Self-explanatory.


def extractMetrics(directory, metricsName, fname):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if "metriclog" in filename:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
                cmd = "AWDDisplay " + filepath + " |grep -i '" + metricsName + "' >> " + fname
                subprocess.call(cmd, shell=True)
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
# full_file_paths = get_filepaths("/Volumes/CarryMac/Users/pradeepsharma/Downloads/AWD/")
extractMetrics("/Volumes/CarryMac/Users/pradeepsharma/Downloads/AWD/", "timestamp:\|sys_mode:\|elapsed_ms\|triggerId: 0xca108\|triggerId: 0xca162\|rat_info:\|triggerId: 0x220001\|triggerId: 0xca100\|duration_ms:" , "/Volumes/CarryMac/Users/pradeepsharma/Desktop/OOS_filter.txt")
# full_file_paths = get_filepaths("/Volumes/buildbot/Logs/AWDLogs")
# full_file_paths = get_filepaths("/Users/pradeepsharma/Downloads/AWD/")
# print full_file_paths





