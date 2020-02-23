import os
import generatebat

urls = open("callspiders.bat")
while True:
    line = urls.readline()
    if not line:
        break
    os.system(line)
urls.close()

import generator