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
act.move_to_element(pointer).pause(3).click(driver.find_element("xpath", "//span[normalize-space()='Account']")).perform()
time.sleep(3)
driver.find_element("xpath", "//a[normalize-space()='Your addresses']").click()
time.sleep(3)
driver.find_element("id", "ya-myab-plus-address-icon").click()
time.sleep(3)
driver.find_element("xpath", "//span[@id='address-ui-widgets-countryCode']//span[@role='button']").click()
time.sleep(2)
driver.find_element("id", "address-ui-widgets-countryCode-dropdown-nativeId_103").click()
time.sleep(2)
driver.find_element("id", "address-ui-widgets-enterAddressFullName").send_keys('Naufal Rizky')
time.sleep(2)
driver.find_element("id", "address-ui-widgets-enterAddressLine1").send_keys('Jalan Karya Timur, Gang Wonosari - Malang, Jawa Timur')
time.sleep(3)
driver.find_element("id", "address-ui-widgets-enterAddressCity").send_keys('Malang')
time.sleep(2)
driver.find_element("id", "address-ui-widgets-enterAddressStateOrRegion").send_keys('Jawa Timur')
time.sleep(2)
driver.find_element("id", "address-ui-widgets-enterAddressPostalCode").send_keys('65121')
time.sleep(2)
driver.find_element("id", "address-ui-widgets-enterAddressPhoneNumber").send_keys('085850836103')
time.sleep(2)
driver.find_element("xpath", "//input[@aria-labelledby='address-ui-widgets-form-submit-button-announce']").click()
time.sleep(2)
driver.find_element("xpath", "//label[@for='kyc-xborder-radio-skip']//i[@class='a-icon a-icon-radio']").click()
time.sleep(2)
driver.find_element("xpath", "//input[@aria-labelledby='kyc-xborder-continue-button-announce']").click()
time.sleep(3)


driver.close()
driver.quit()
print("Test Complete")