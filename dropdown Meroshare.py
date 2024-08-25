# import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
driver.get("https://meroshare.cdsc.com.np/#/login")

#maximize the window()
driver.maximize_window()
time.sleep(1)

select_your_dp=driver.find_element(*(By.XPATH,"//span[@class='select2-selection__rendered']"))
select_your_dp.click()
time.sleep(1)

option=driver.find_element(By.XPATH,"//li[@class='select2-results__option']")
#option=driver.find_element(*(By.XPATH,"//body"))
option.click()
#time.sleep(1)

# option=driver.find_element(By.XPATH,"//ul[@class='select2-results__options']")
# option.click()
# time.sleep(5)

# option=driver.find_element(By.XPATH,"//li[@class='select2-results__option']")
# option.send_keys("AAKASH CAPITAL LIMITED (19000) ")
# time.sleep(5)

username=driver.find_element(*(By.XPATH,"//input[@id='username']"))
username.send_keys("1700179")
#time.sleep(1)

password=driver.find_element(*(By.XPATH,"//input[@id='password']"))
password.send_keys("haha14!")
#time.sleep(1)

login=driver.find_element(*(By.XPATH,"//button[@type='submit']"))
login.click()
time.sleep(1)

forget_password=driver.find_element(*(By.XPATH,"//button[normalize-space()='Forgot your password?']"))
forget_password.click()
time.sleep(1)

select_your_dp=driver.find_element(*(By.XPATH,"//span[@class='select2-selection__rendered']"))
select_your_dp.click()
time.sleep(1)

option=driver.find_element(By.XPATH,"//li[@class='select2-results__option']")
option.click()
#time.sleep(1)

username=driver.find_element(*(By.XPATH,"//input[@id='username']"))
username.send_keys("1700179")
#time.sleep(1)

email=driver.find_element(*(By.XPATH,"//input[@id='email']"))
email.send_keys("a2gmail.com")
#time.sleep(1)

dob=driver.find_element(*(By.XPATH,"//input[@id='dateOfBirth']"))
dob.click()
dob.send_keys("10/5/2002")
#time.sleep(1)

# option_dob_1=driver.find_element(*(By.XPATH,"//span[@class='is-highlighted']"))
# option_dob_1.click()
# time.sleep(1)

send=driver.find_element(By.XPATH,"//button[@type='submit']")
send.submit()
time.sleep(5)

#close.get the webdriver
driver.quit()