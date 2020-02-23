bat = open("callspiders.bat", "w", encoding="utf-8")
#bat.write("@ECHO OFF\n")
urls = open("urls.txt")
while True:
    line = urls.readline()
    if not line:
        break
    bat.write('scrapy runspider spider.py -s LOG_ENABLED=False -a domain="' + line + '"')
urls.close()
bat.close()