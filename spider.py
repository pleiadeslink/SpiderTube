import scrapy
import os
import glob
import pathlib

class spider(scrapy.Spider):
    name = "Spider"
    vname = ""
    vlink = ""

    def __init__(self, domain='', *args, **kwargs):
        super(spider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]
        
    def parse(self, response):
        print("A spider is knitting her web...")

        # Get channel name
        channelName = "Unknown"
        SET_SELECTOR = ".branded-page-header-title-link"
        for video in response.css(SET_SELECTOR):
            NAME_SELECTOR = "a ::text"
            channelName = video.css(NAME_SELECTOR).extract_first()
            break

        # Create new .web file
        webCounter = len(glob.glob1(pathlib.Path().absolute(),"*.web"))
        webCounter = webCounter + 1
        videolist = open(str(webCounter) + ".web", "w", encoding="utf-8")

        # Write header
        videolist.write("<h2>🎥 " + channelName + "</h2>")

        # Get video data
        SET_SELECTOR = ".yt-uix-tile-link"
        for video in response.css(SET_SELECTOR):
            NAME_SELECTOR = "a ::text"
            LINK_SELECTOR = "a ::attr(href)"
            META_SELECTOR = ""
            vname = video.css(NAME_SELECTOR).extract_first()
            vlink = video.css(LINK_SELECTOR).extract_first()
            videolist.write('> <a href="http://youtube.com' + vlink + '">' + vname + '</a><br />\n')
        videolist.close()
        