import time
from selenium import webdriver

####################################################################
#                   Proudly written by Vafa Abadi.
#           LinkedIn: https://www.linkedin.com/in/vafaabadi/
####################################################################

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
#to add 3 kg of carrots to cart
driver.find_element_by_xpath("//div[5]//div[2]//a[2]").click()
driver.find_element_by_xpath("//div[5]//div[2]//a[2]").click()
driver.find_element_by_xpath("//div[5]//div[3]//button[1]").click()
#to add 2 kg of capsicum to cart
driver.find_element_by_xpath("//div[9]//div[2]//a[2]").click()
driver.find_element_by_xpath("//div[9]//div[3]//button[1]").click()
#observe the items in basket
driver.find_element_by_xpath("//a[4]//img[1]").click()
#remove capsicum from the basket
driver.find_element_by_xpath("//header//li[2]//a[1]").click()
#proceed to check out
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
TotalBeforeDiscount = str(driver.find_element_by_xpath("//p[contains(text(),'168')]").text)
assert "168" in TotalBeforeDiscount
#driver.find_element_by_xpath("//input[@placeholder='Enter promo code']").send_keys("this is promo code")
#driver.find_element_by_xpath("//button[contains(text(),'Apply')]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
driver.find_element_by_tag_name("select").click()
driver.find_element_by_xpath("//option[contains(text(),'Iceland')]").click()
driver.find_element_by_class_name("chkAgree").click()
driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()

print("\nWell done! This automation test, VeggieKart, successfully passed.")


#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work



