import scrapy

class spider(scrapy.Spider):
    name = "Spider"
    vname = ""
    vlink = ""

    def __init__(self, domain='', *args, **kwargs):
        super(spider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]
        
    def parse(self, response):
        print("Spider [] working...")
        videolist = open("videolist.txt", "w", encoding="utf-8")
        SET_SELECTOR = ".branded-page-header-title-link"
        for video in response.css(SET_SELECTOR):
            NAME_SELECTOR = "a ::text"
            videolist.write("<h2>" + video.css(NAME_SELECTOR).extract_first() + "</h2>")
            break
        SET_SELECTOR = ".yt-uix-tile-link"
        for video in response.css(SET_SELECTOR):
            NAME_SELECTOR = "a ::text"
            LINK_SELECTOR = "a ::attr(href)"
            vname = video.css(NAME_SELECTOR).extract_first()
            vlink = video.css(LINK_SELECTOR).extract_first()
            videolist.write('<a href="http://youtube.com' + vlink + '">' + vname + '</a><br />\n')
        videolist.close()
        