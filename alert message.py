#use the selector hub
# #import the neccessary module as
#application command
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.support.expected_conditions import alert_is_present
from webdriver_manager.chrome import ChromeDriverManager
import time

#from main import website_title

# #set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
website_url="https://demoqa.com/alerts"
driver.get(website_url)

#maximize the window as
driver.maximize_window()
time.sleep(2)

#locate the path-- selectorshub.com
click_me=driver.find_element(*(By.XPATH,"//button[@id='alertButton']"))
click_me.click()
time.sleep(5)

#----------switch to alert
alert=driver.switch_to.alert

#-----------close the alert
alert.accept()

#application command

#1.Extract the website title
website_title=driver.title
print(f"Website title is:",website_title)

#2.Get the current url
current_url=driver.current_url
print(f"Current url is:",current_url)

#3.Get the page source
page_source=driver.page_source
print(f"Page Source:",page_source[:500])

#close the webdriver instance
driver.quit()

print("Congrats!!!")

