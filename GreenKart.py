import time
from selenium import webdriver

####################################################################
#                   Proudly written by Vafa Abadi.
#           LinkedIn: https://www.linkedin.com/in/vafaabadi/
####################################################################

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_link_text("Shop").click()
time.sleep(2)
products = driver.find_elements_by_xpath("//div[@class='card h-100']")  # parent
for product in products:  # //div[@class='card h-100']/div/h4/a
    productName = product.find_element_by_xpath("div/h4/a").text  # child
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_class_name("navbar-toggler-icon").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
selected_product = driver.find_element_by_xpath("//a[contains(text(),'Blackberry')]")
assert selected_product.text == "Blackberry"
driver.find_element_by_css_selector("button[class*='btn-default']").click()

products = driver.find_elements_by_css_selector("div[class='card h-100']")  # parent
for product in products:  # div[class='card h-100']
    productName = product.find_element_by_xpath("div/h4/a").text  # child
    if productName == "Nokia Edge" or productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()
time.sleep(2)
driver.find_element_by_css_selector("a[class*='btn-primary']").click()

time.sleep(2)
driver.find_element_by_xpath("//tr[1]//td[5]//button[1]").click()
driver.find_element_by_id("exampleInputEmail1").send_keys("2")
total = driver.find_element_by_xpath("//td[@class='text-right']//strong[contains(text(),'. 600000')]").text
assert "600000" in total
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ir")
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'Iran')]").click()
time.sleep(2)
driver.find_element_by_css_selector("div[class*='checkbox-primary']").click()
time.sleep(2)
driver.find_element_by_css_selector("input[type='submit']").click()
success = driver.find_element_by_xpath("//strong[contains(text(),'Success!')]").text
assert "Success!" in success

print("\nWell done! This automation test, GreenKart, successfully passed.")



#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work
