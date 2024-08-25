# #import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# #set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#open website as
driver.get("https://demoqa.com/text-box")

#maximize the window()
driver.maximize_window()

#find or locate th element by their xpath method
full_name=driver.find_element(By.XPATH," //input[@id='userName']")
email_field=driver.find_element(By.XPATH,"//input[@id='userEmail']")
current_address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
permanent_address=driver.find_element(By.XPATH,"//textarea[@id='permanentAddress']")
#submit=driver.find_element(By.XPATH,"//button[@id='submit']")


# fill the form as
full_name.send_keys("Binita")
email_field.send_keys("binita@gmail.com")
current_address.send_keys("bagbazar")
permanent_address.send_keys("pulchowk")

#click the submit button
#submit.click()

time.sleep(5)

#close the webdriver instances as
driver.quit()
print("finally code success!!")
