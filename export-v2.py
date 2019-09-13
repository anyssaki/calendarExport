# Prerequisite Installations
# 1. Python (https://www.python.org/downloads/)
# 2. Scrapy (Run PowerShell as Administrator > pip install scrapy)
# 3. Enthought Canopy (https://assets.enthought.com/downloads/)

# Additional Tools
# 1. Visual Studio Code (https://code.visualstudio.com/)
# 2. Firefox Developer Editions (https://www.mozilla.org/en-US/firefox/developer/?utm_source=firebug&utm_medium=lp&utm_campaign=switch&utm_content=landingpage)
# 3. GitHub (https://github.com/)
# 4. Git (https://git-scm.com/)

# Import Rquired Modules
import scrapy
import json

# Inspect Element > Network > JSON File > Request URL
# Identified URL (JSON File): https://thesundevils.com/services/responsive-calendar.ashx?type=month&sport=0&location=h&date=9%2F13%2F2019+12%3A00%3A00+AM
# Sport Name: https://thesundevils.com/services/sportnames.ashx
class exportData(scrapy.Spider) : 
    name = ''