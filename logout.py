from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://amazon.com")
time.sleep(1)
driver.find_element("xpath", "//div[@id='nav-signin-tooltip']//span[@class='nav-action-inner'][normalize-space()='Sign in']").click()
time.sleep(3)
driver.find_element("id", "ap_email").send_keys('lavasneakers@gmail.com')
time.sleep(2)
driver.find_element("xpath", "//input[@id='continue']").click()
time.sleep(2)
driver.find_element("id", "ap_password").send_keys('juni1234')
time.sleep(2)
driver.find_element("xpath", "//input[@id='signInSubmit']").click()
time.sleep(2)
pointer=driver.find_element("xpath", "//span[@id='nav-link-accountList-nav-line-1']")
act=ActionChains(driver)
act.move_to_element(pointer).pause(3).click(driver.find_element("xpath", "//span[normalize-space()='Sign Out']")).perform()
time.sleep(3)


driver.close()
driver.quit()
print("Test Complete")