# #import the neccessary module as
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# #set the chrome web driver
driver=webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# #get the website url as
website_url="https://mindrisers.com.np"
#open the website
driver.get(website_url)
#maximize the window size
driver.maximize_window()
time.sleep(5)

#extract the website title;
web_site_title=driver.title
print(f"website title is:,{web_site_title}")

# #open the website
driver.get(website_url)

# #close.get the webdriver
driver.quit()
