# #import the neccessary module as
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# #set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# #get the website url as
website_url="https://mindrisers.com.np"
#open the website
driver.get(website_url)
#maximize the window size
driver.maximize_window()
time.sleep(5)

#calcualate the height if page using is
page_height=driver.execute_script("return document.body.scrollHeight")

#for scroll down the web page
scroll_speed=100
scroll_iteration=int(page_height/scroll_speed)

#loop to perform some increments
for _ in range (scroll_iteration):
 driver.execute_script(f"window.scrollBy(0,{scroll_speed});")
 time.sleep(1)


#extract the website title;
web_site_title=driver.title
print(f"website title is:,{web_site_title}")

# #open the website
driver.get(website_url)

# #close.get the webdriver
driver.quit()
