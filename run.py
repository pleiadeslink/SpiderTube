import os
import generatebat
import glob
import neocities
import sys

# Remove current .web files
for f in glob.glob("*.web"):
    os.remove(f)

# Call spiders from batch file
urls = open("callspiders.bat")
while True:
    line = urls.readline()
    if not line:
        break
    os.system(line)
urls.close()

# Generates html
import generator

# Uploads to Neocities
print("Uploading to Neocities...")
nc = neocities.NeoCities(sys.argv[1], sys.argv[2])
nc.upload(('index.html', 'index.html'), ('style.css','style.css'))