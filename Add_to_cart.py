from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
driver.find_element("id", "twotabsearchtextbox").send_keys('iphone 13' + Keys.ENTER)
time.sleep(3)
driver.find_element("xpath", "//span[@class='a-size-medium a-color-base a-text-normal'][normalize-space()='Apple iPhone 13, 128GB, Blue - Unlocked (Renewed)']").click()
time.sleep(3)
driver.find_element("id", "color_name_2").click()
time.sleep(3)
driver.find_element("id", "service_provider_3").click()
time.sleep(3)
driver.find_element("id", "size_name_0").click()
time.sleep(3)
driver.find_element("id", "contextualIngressPtLabel_deliveryShortLine").click()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#GLUXCountryListDropdown .a-button-text").click()
time.sleep(3)
driver.find_element("id", "GLUXCountryList_107").click()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "button[name='glowDoneButton']").click()
time.sleep(3)
driver.find_element("xpath", "/html/body/div[1]/div[2]/div[10]/div[6]/div[1]/div[4]/div/div/div/div[1]/div/div/div[1]/div/div[2]/div/form/div/div/div[5]/div/div/span/div/div/span/span/span/span").click()
time.sleep(3)
driver.find_element("id", "quantity_0").click()
time.sleep(3)
driver.find_element("id", "add-to-cart-button").click()
time.sleep(10)


driver.close()
driver.quit()
print("Test Complete")