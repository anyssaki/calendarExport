import selenium
import webdriver

# Using Chrome to access web
driver = webdriver.Chrome()

# Open website
driver.get('https://thesundevils.com/calendar.aspx')

# Select id for "filter game location" dropdown
gameLocation = driver.find_element_by_id('selected_location').send_keys("Home")
gameLocation.click()
