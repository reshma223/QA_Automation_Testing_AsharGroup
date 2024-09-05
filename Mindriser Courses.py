#import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

#set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#maximize the window()
driver.maximize_window()
time.sleep(1)

#open website as
driver.get("https://www.mindrisers.com.np/")

Courses=driver.find_element(*(By.XPATH,"//a[contains(text(),'our courses')]"))
Courses.click()
time.sleep(1)

quality_assurance=driver.find_element(*(By.XPATH,"//h3[contains(@class,'sub-header title-space-md text-expanded')][normalize-space()='Quality Assurance Training in Nepal']"))
quality_assurance.click()
time.sleep(1)

get_admission=driver.find_element(*(By.XPATH,"//a[normalize-space()='Get Admission']"))
get_admission.click()
time.sleep(5)