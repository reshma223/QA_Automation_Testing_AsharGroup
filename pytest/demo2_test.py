# import the neccessary module as
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import pytest
import time

@pytest.fixture()
def driver():
    driver=webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    #yield the driver
    yield driver
    #close the driver instance
    driver.quit()
def test_google_search(driver):
    driver.get("https://google.com")
    search_box=driver.find_element(*(By.XPATH,"//textarea[@id='APjFqb']"))
    search_box.send_keys("mindrisers.com.np")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    #click on the link available
    first_link=driver.find_element(*(By.XPATH,"//h3[contains(text(),'Best IT Training Institute in kathmandu, Nepal | M')]"))
    first_link.click()
    driver.maximize_window()
    time.sleep(5)
    print("Congrats!! First pytest execute successfully!!!!!!!!")


