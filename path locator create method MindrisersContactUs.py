# #import the neccessary module as

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# #set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
driver.get("https://www.mindrisers.com.np/contact-us")

#maximize the window()
driver.maximize_window()

#find or locate th element by their xpath method
name=driver.find_element(By.XPATH," //input[@name='name']")
email_field=driver.find_element(By.XPATH,"//input[@name='email']")
phone_number=driver.find_element(By.XPATH,"//input[@name='mobile_no']")
subject=driver.find_element(By.XPATH,"//input[@name='subject']")
any_queries=driver.find_element(By.XPATH,"//textarea[@name='message']")

# fill the form as
name.send_keys("Reshma Shrestha")
email_field.send_keys("reshma@gmail.com")
phone_number.send_keys("9779844563214")
subject.send_keys("QA")
any_queries.send_keys("Is the mentor industry experts? Is the class recording available?")

# robert=driver.find_element(*(By.XPATH,"//div[@class='recaptcha-checkbox-checkmark']"))
# robert.click()

# robert1=driver.find_element(By.XPATH,"span[@class='recaptcha-checkbox goog-inline-block recaptcha-checkbox-unchecked rc-anchor-checkbox recaptcha-checkbox-expired']")
# robert1.click()
#
# submit=driver.find_element(*(By.XPATH,"//button[normalize-space()='Submit']"))
# submit.click()

time.sleep(5)

#close the webdriver instances as
driver.quit()
print("finally code success!!")
