import time
from selenium import webdriver

####################################################################
#                   Proudly written by Vafa Abadi.
#           LinkedIn: https://www.linkedin.com/in/vafaabadi/
####################################################################

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\chromedriver.exe")
driver.get("http://www.practiceselenium.com/welcome.html")

driver.find_element_by_xpath("//div[21]//div[1]//div[1]//a[1]//img[1]").click()
driver.find_element_by_xpath("//div[27]//div[1]//a[1]//span[1]").click()
driver.find_element_by_xpath("//body//div//div//div//div//div//div//div//div[1]//div[1]//input[1]").send_keys("test@automation.com")
driver.find_element_by_xpath("//fieldset[1]//div[2]//div[1]//input[1]").send_keys("Mr Test Automation")
driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//form//fieldset//div//div//textarea").send_keys("99 automation road, test avenue")
driver.find_element_by_css_selector("#card_type").click()
driver.find_element_by_xpath("//option[contains(text(),'American Express')]").click()
driver.find_element_by_id("card_number").click()
driver.find_element_by_id("card_number").send_keys("1234567891234567")
driver.find_element_by_css_selector("#cardholder_name").send_keys("Test Automation")
driver.find_element_by_id("verification_code").send_keys("000")
driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()

print("\nWell done! This automation test, PassionTea, successfully passed.")




#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work
