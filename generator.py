import os
import pathlib
from datetime import datetime
now = datetime.now()

print("Generating html...") 
index = open("index.html", "w", encoding="utf-8")
index.write("""
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <meta name="description" content="Scambait updates">
        <meta name="keywords" content="scambait">
        <meta name="author" content="SpiderTube">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>😬 Scambait channels 🤯</title>
    </head>
    <body>
        <div class="global-container">
            <div class="main-container">
                <div class="header">😬 Scambait channels 🤯</div>
                <div class="content-container">
                    <p>Scambaiting is a form of Internet vigilantism, where the vigilante poses as a potential victim to the scammer in order to waste their time and resources, gather information that will be of use to authorities, and publicly expose the scammer.</p><p>This website provides updates from the best scambaiting channels.</p>
                    <div class="list-container">

""")

# Iterates through each .web file
files = []
for i in os.listdir(pathlib.Path().absolute()):
    if i.endswith('.web'):
        files.append(open(i))
for file in files:
    f = open(file.name, encoding="utf-8")
    c = 0
    while True:
        line = f.readline()
        if not line or c > 9:
            break
        c = c + 1
        index.write(line)
   
index.write("""
                    </div>
                </div>
                <div class="footer">Last refresh: 
""")
index.write(str(now.strftime("%d/%m/%Y %H:%M:%S")))
index.write("""<br />Website generated with <a href="https://github.com/FractalMonkey/SpiderTube"><b>🕷SpiderTube</b></a>.
                </div>
            </div>
        </div>
    </body>
</html>
""")
index.close()