#parameterization
import time
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    # yield the driver
    yield driver
    # close the driver insatnce
    driver.quit()

# @pytest.mark.parametrize("username,password",[
#     ("TestQA","password"),         #valid username & password
#     ("InvalidUser","InvalidPassword"),
#     ("1","a"),
#     ("User4","pass4"),
#
# ])
#
# def test_login(driver,username,password):
#     driver.get("https://sagar-test-qa.vercel.app/")
#     username_field=driver.find_element(*(By.XPATH,"//input[@id='username']"))
#     password_field=driver.find_element(*(By.XPATH,"//input[@id='password']"))
#     #login_button=driver.find_element(*(By.XPATH,"//button[normalize-space()='Login']"))
#     login_button = driver.find_element(*(By.XPATH, "//button[normalize-space(text())='Login']"))
#
#     username_field.send_keys(username)
#     password_field.send_keys(password)
#     login_button.click()
#     time.sleep(1)
#
#     try:
#         #check the alert is present or not
#         alert=driver.switch_to.alert
#         alert_text=alert.text
#         alert.accept()
#         assert "Invalid username or password" in alert_text
#         print(f"invalid username or password for {username}")
#     except:
#         #if no alert then:
#         time.sleep(2)
#         page_source=driver.page_source
#
#         if "Welcome to the Dashboard" in page_source:
#             print(f"Login successful for {username}")
#         else:
#             print(f"Unexpected error or login failed for {username}")