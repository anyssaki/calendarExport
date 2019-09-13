# -------------------------------------------------------------------------------------
#
#  Date: 2019-09-13
#  Author: Anyssa Iwamoto
#  Description: Exporting ASU's composite sports calendar to Google Calendar
#  Instructions:
#    1. Install Python (https://www.python.org/downloads/)
#    2. Install Scrapy (Run PowerShell as Administrator > pip install scrapy)
#    3. Install iPython (Run PowerShell as Administrator > pip install ipython)
#    4. Additional Tools: Visual Studios Code, GitHub, Git, Firefox Developer Edition
#
# -------------------------------------------------------------------------------------

# Import Required Modules
import scrapy
import json
from scrapy import Selector
# Identified URL (JSON File): https://thesundevils.com/services/responsive-calendar.ashx?type=month&sport=0&location=h&date=9%2F13%2F2019+12%3A00%3A00+AM
# Sport Name: https://thesundevils.com/services/sportnames.ashx
# Print version: https://thesundevils.com/calendar.aspx?date=9/19/2019&vtype=print&location=h&sport=0

# JSON Request (Inspect Element > Network > JSON File > Request URL)
class exportData(scrapy.Spider):
    name = "export" # name of this spider
    allowed_domains = ["thesundevils.com/"] # where the spider should start crawling
    start_urls = ['https://thesundevils.com/services/responsive-calendar.ashx?type=month&sport=0&location=h&date=9%2F13%2F2019+12%3A00%3A00+AM']

    def parse(self, response):
        pass