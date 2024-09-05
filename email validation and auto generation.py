#import the neccessary module as
import re
import time
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# #set the chrome web driver
driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

#define the fun for valid email pattern
def is_valid_email(email):
    try:
        #check the formate using re
        email_pattern=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

        if re.search(email_pattern,email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def is_valid_phone(phone):
    return bool(re.match(r'^\d{10}$',phone))

#open website as
driver.get("https://www.mindrisers.com.np/contact-us")
driver.maximize_window()

#set the scroll parameter
target_y=6000
scroll_distance=1000
current_y=0

#loop the scrolling
while current_y<target_y:
    driver.execute_script(f"window.scrollBy(0,{scroll_distance});")
    current_y +=scroll_distance
    time.sleep(0.25)

#interact with the path loacator
name_field=driver.find_element(By.XPATH," //input[@name='name']")
email_field=driver.find_element(By.XPATH,"//input[@name='email']")
phone_field=driver.find_element(By.XPATH,"//input[@name='mobile_no']")
time.sleep(3)

#define the function for random data
def generate_random_email():
    domain="test.com"
    email_length=5
    random_string=''.join(random.choice(string.ascii_lowercase) for _ in range(email_length))
    email=random_string + "@" + domain
    return email
def generate_random_name():
    return ''.join(random.choices(string.ascii_letters,k=8))

def generate_random_phone_number():
    phone_number="98" + "".join(random.choices(string.digits,k=8))
    return  phone_number

#generate random data
name=generate_random_name()
email=generate_random_email()
phone=generate_random_phone_number()

time.sleep(2)

#check the first name is empty
if not name:
    print("name cannot be empty")

#clear the field and give the input
name_field.clear()
name_field.send_keys(name)
time.sleep(0.75)

#check the valid email address
if is_valid_email(email):
    print("Valid email address:")
else:
    print("Invalid email address:")

#clear the phone field
if not phone:
    print("Phone number cannot be empty:")

#clear the phone and add the data
phone_field.clear()
phone_field.send_keys(phone)
time.sleep(0.75)

#close the webdriver instance
driver.quit()
print("Code successfully executed!!!")


