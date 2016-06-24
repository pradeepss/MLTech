import os
import subprocess


def get_filepaths(directory):
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            if "metriclog.log" in filename:
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.
                cmd = "AWDDisplay " + filepath + " > /users/ltecoex/Desktop/AWD/" + filename  +".txt"
                subprocess.call(cmd, shell=True)
    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
# full_file_paths = get_filepaths("/Users/ltecoex/Library/Logs/CrashReporter")
full_file_paths = get_filepaths("/Volumes/buildbot/Logs/AWDLogs")
print full_file_paths
# print len(full_file_paths)
# i = 0
# for i to len(full_file_paths):
#     print


