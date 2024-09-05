#import the necessary module as:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# set the chrome webdriver
driver = webdriver.Chrome(service=ChromeServices(ChromeDriverManager().install()))
driver.maximize_window()
time.sleep(3)

# get the website url as:
website_url = "https://demoqa.com/automation-practice-form"
# open the website
driver.get(website_url)
time.sleep(10)

# Fill out the form
first_name = driver.find_element(By.XPATH,"//input[@id='firstName']")
first_name.send_keys("Prem")
last_name = driver.find_element(By.XPATH,"//input[@id='lastName']")
last_name.send_keys("Poudel")
user_email = driver.find_element(By.XPATH,"//input[@id='userEmail']")
user_email.send_keys("prem12345@gmail.com")
time.sleep(10)


# handle radio button
gender_male = driver.find_element(By.XPATH, "//label[normalize-space()='Male']")
driver.execute_script("arguments[0].click();", gender_male)


mobile_no = driver.find_element(By.XPATH,"//input[@id='userNumber']")
mobile_no.send_keys("9867373777")

# handling datepicker
date_of_birth = driver.find_element(By.XPATH,"//input[@id='dateOfBirthInput']")
driver.execute_script("arguments[0].click();", date_of_birth)
time.sleep(10)

month_select = driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
month_select.click()
time.sleep(3)
month_select_january = driver.find_element(By.XPATH,"//option[@value='1']")
month_select_january.click()

year_select = driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']")
select_year = Select(year_select)
select_year.select_by_value('1997')
time.sleep(3)
day_select = driver.find_element(By.XPATH,"//div[@aria-label='Choose Friday, February 7th, 1997']")
driver.execute_script("arguments[0].click();", day_select)
time.sleep(3)

subjects = driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)
time.sleep(2)
subjects.send_keys("Social Studies")
subjects.send_keys(Keys.ENTER)
time.sleep(2)
subjects.send_keys("Computer Science")
subjects.send_keys(Keys.ENTER)
time.sleep(2)
subjects.send_keys("Arts")
subjects.send_keys(Keys.ENTER)
time.sleep(2)


# handling checkbox
hobbies_sports = driver.find_element(By.XPATH,"//label[normalize-space()='Sports']")
driver.execute_script("arguments[0].click();", hobbies_sports)
time.sleep(2)

# upload a file
file_path = "C:/Users/Administrator/OneDrive/Desktop/TEST.docx"
file_upload = driver.find_element(By.XPATH,"//input[@id='uploadPicture']")
file_upload.send_keys(file_path)

time.sleep(4)

current_address = driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
current_address.send_keys("address-13")
time.sleep(5)

# state = driver.find_element(By.XPATH,"//div[contains(text(),'Select State')]")
# driver.execute_script("arguments[0].click();", state)
# state.send_keys("Rajasthan")
# state.send_keys(Keys.ENTER)
#
# city = driver.find_element(By.XPATH,"//div[@class=' css-1wa3eu0-placeholder']")
# driver.execute_script("arguments[0].click();", city)
# city.send_keys("Jaipur")
# city.send_keys(Keys.ENTER)

# Submit the form
submit = driver.find_element(By.XPATH,"//button[@id='submit']")
driver.execute_script("arguments[0].click();", submit)
time.sleep(2)

# close the webdriver
driver.quit()
print("Finally Form Filled")