# Prerequisite Installations
# 1. Python (https://www.python.org/downloads/)
# 2. Selenium (Run PowerShell as Administrator > pip install selenium)
# 3. Install ChromeDriver (https://sites.google.com/a/chromium.org/chromedriver/downloads)

# Import Required Modules
from selenium import webdriver # allows you to launch a browser
from selenium.webdriver.common.by import By # allows you to search for things using specific parameters
from selenium.webdriver.support.ui import WebDriverWait # allows you to wait for a page to load
from selenium.webdriver.support import expected_conditions as EC # specify what you are looking for on a specific page in order to determine taht the webpage has loaded
from selenium.common.exceptions import TimeoutException # handling timeout situation
from selenium.webdriver.chrome.options import Options

# Create new instance of Chrome in Incognito mode
option = webdriver.ChromeOptions()
option.add_argument(" - incognito")

# Run chrome in silent mode
chrome_options = Options()  
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-print-preview")

# Using chrome to access web
driver = webdriver.Chrome("C:/Users/ANY2147015/Documents/installations/chromedriver.exe")
driver.maximize_window()

# Open website
# driver.get('https://thesundevils.com/calendar.aspx')

# Select id for "filter game location" dropdown
# gameLocation = driver.find_element_by_id('selected_location').send_keys("Home")

# Locate home games
# dateSelector = driver.find_element_by_class_name("sidearm-calendar-chooser-datepicker")
# print(homeGames.text)

# Restarting

# Extract information from simplified print version of the calendar
driver.get('https://thesundevils.com/calendar.aspx?date=9/19/2019&vtype=print&location=h&sport=0')


# driver.close()
