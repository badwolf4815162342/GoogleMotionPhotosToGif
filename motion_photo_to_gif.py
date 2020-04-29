import os, sys
import ffmpeg
import time

""" 
The goal is to convert all the extracted videos (extracted by https://takeout.google.com/)
from the Google Motion Pictures into GIF format
"""

directory = os.path.dirname(os.path.realpath(sys.argv[0])) #get the directory of your script
for subdir, dirs, files in os.walk(directory):
    for filename in files:
        if filename.find('(1).jpg') > 0:
            subdirectoryPath = os.path.relpath(subdir, directory) #get the path to your subdirectory
            filePath = os.path.join(subdirectoryPath, filename) #get the path to your file
            newFilePath = filePath.replace("(1).jpg",".mp4") #create the new name
            os.rename(filePath, newFilePath) #rename your file
            # ffmpeg to gif -> stream 0.0
            convert_str = 'ffmpeg -i ' + newFilePath + ' -map 0:0 ' + newFilePath  + '.gif'
            os.system(convert_str)
            # Extract date stamp from google.jpg filename
            filename_without_signs = filePath.replace("(1).jpg","").replace("_","")
            timestr = filename_without_signs[-14:]
            timestr_for_touch = timestr[0:12] + '.' + timestr[-2:]
            # set new date to gif
            set_date_str = 'touch -t ' + timestr_for_touch + ' ' + newFilePath + '.gif'
            os.system(set_date_str)
            # Delete mp4 version
            os.remove(newFilePath)