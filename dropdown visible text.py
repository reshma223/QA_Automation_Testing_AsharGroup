# import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
driver.get("https://merolagani.com/")

#maximize the window()
driver.maximize_window()
time.sleep(5)

market=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(5)

#dropdown ma bhako particular name bata arko page ma jana
indices=driver.find_element(By.LINK_TEXT,"Indices")  #website ma jasto naam ma testaii lekhne so "Indices"
indices.click()
time.sleep(5)

print("Congrats!! the code dropdown is working fine")

#close.get the webdriver
driver.quit()