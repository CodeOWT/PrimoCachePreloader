# Preloads files into PrimoCache's L2 cache.
# Inspired by RobF's post on https://forum.romexsoftware.com/en-us/viewtopic.php?p=11033#p11033
# 
# How to use:
# First argument is the starting directory you want to preload. 
# Second argument is the file pattern to read.
# C:\> python primocache_preloader.py C:\Path\to\Folder *.*

import os
import fnmatch
import sys
import threading
import datetime

def find_files(directory, pattern):
    file_list = []
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                file_list.append(os.path.join(root, basename))
    return file_list

def load_file(filename, bufsize, semaphore, print_lock):
    with semaphore:
        output = f'Loading: {filename} '
        with open(filename, 'rb') as fh:
            while True:
                data = fh.read(bufsize)
                output += '.'
                if not data:
                    break
        
        output += " done"
        with print_lock:
            print(output)

bufsize = 1024 * 1024 * 256
max_threads = 4
semaphore = threading.Semaphore(max_threads)
print_lock = threading.Lock()
threads = []

# Get the list of files to be processed
file_list = find_files(sys.argv[1], sys.argv[2])

# Output the number of files
print(f"Number of files to be scanned: {len(file_list)}")

# Record start time
start_time = datetime.datetime.now()

for filename in file_list:
    thread = threading.Thread(target=load_file, args=(filename, bufsize, semaphore, print_lock))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# Record end time
end_time = datetime.datetime.now()

# Calculate total processing time
total_time = end_time - start_time

# Print total processing time
print(f"Total processing time: {total_time}")