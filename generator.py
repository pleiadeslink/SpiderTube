import os
import json
import pathlib
from datetime import datetime
now = datetime.now()

print("Generating html...") 
index = open("index.html", "w", encoding="utf-8")

# Load variables from json
with open('config.json') as file:
    data = json.load(file, encoding="utf-8")

    # Write html
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
            <title>{0}</title>
        </head>
        <body>
            <div class="global-container">
                <div class="main-container">
                    <div class="header">{0}</div>
                    <div class="content-container">
                        <p>{1}</p>
                        <div class="list-container">

    """.format(data["Name"], data["Description"]))

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
        f.close()
    
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