# import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
driver.get("https://formy-project.herokuapp.com/form")

#maximize the window()
driver.maximize_window()
time.sleep(5)

#locate the form fill locator
first_name=driver.find_element(By.XPATH,"//input[@id='first-name']")
last_name=driver.find_element(By.XPATH,"//input[@id='last-name']")
job_title=driver.find_element(By.XPATH,"//input[@id='job-title']")

#fill the content
first_name.send_keys("Reshma")
last_name.send_keys("Shrestha")
job_title.send_keys("QA Learner")

#handle the radio button as
high_level_of_education=driver.find_element(By.XPATH,"//input[@id='radio-button-1']")
high_level_of_education.click()

#handle checkbox
sex=driver.find_element(By.XPATH,"//input[@id='checkbox-2']")
sex.click()

#handle the drop down element as
select_option=driver.find_element(By.XPATH,"//select[@id='select-menu']")
select_option.click()
first_option=driver.find_element(By.XPATH,"//option[@value='1']")
first_option.click()

#handle the date picker as
datepicker=driver.find_element(*(By.XPATH,"//input[@id='datepicker']"))
#datepicker.click()
datepicker.send_keys("08/28/2024")

#select the date
# date_today=driver.find_element(By.XPATH,"//td[@class='today day']")
# date_today.click()
# time.sleep(1)

#handel the submit
submit=driver.find_element(*(By.XPATH,"//a[normalize-space()='Submit']"))
submit.click()
time.sleep(3)

#extract the title as
website_title=driver.title
print(f"website title:{website_title}")

time.sleep(5)

#close.get the webdriver
driver.quit()