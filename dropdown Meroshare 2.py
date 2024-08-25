from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

website_url = "https://meroshare.cdsc.com.np/#/login"
driver.get(website_url)
time.sleep(4)

driver.maximize_window()
time.sleep(3)

button_down = driver.find_element(By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]")
button_down.click()

options_xpath = "//li[contains(text(), 'AAKASH CAPITAL LIMITED (19000)')]"

options = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, options_xpath)))
options.click()
time.sleep(5)

driver.quit()
print("Congrats!!!Drop-down menu options is working successfully")