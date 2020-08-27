import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
driver.get("http://automationpractice.com/index.php")

action = ActionChains(driver)
VisualizeButtons = driver.find_element_by_xpath("//ul[1]//li[7]//div[1]//div[1]//div[1]//a[1]//img[1]")
action.move_to_element(VisualizeButtons).perform()
time.sleep(1)
MoreButton = driver.find_element_by_xpath("//ul[1]//li[7]//div[1]//div[2]//div[2]//a[2]//span[1]")
MoreButton.click()
time.sleep(2)
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("view_scroll_right").click()
time.sleep(1)
driver.find_element_by_xpath("//a[2]//span[1]//i[1]").click()
driver.find_element_by_xpath("//select[@name='group_1']").click()
driver.find_element_by_xpath("//option[contains(text(),'L')]").click()
driver.find_element_by_xpath("//a[@name='Green']").click()
driver.find_element_by_xpath("//span[contains(text(),'Add to cart')]").click()
time.sleep(2)
Dressname = driver.find_element_by_xpath("//span[contains(text(),'Printed Chiffon Dress')]").text
assert "Printed Chiffon Dress" in Dressname
driver.find_element_by_xpath("//span[contains(text(),'Proceed to checkout')]").click()
InStock = driver.find_element_by_xpath("//span[contains(text(),'In stock')]").text
assert "In stock" in InStock
driver.find_element_by_xpath("//html//body//div//div//div//div//div//p//a//span[contains(text(),'Proceed to checkout')]").click()
time.sleep(2)
#username
driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//form//div//div//input[@name='email']").click()
driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//form//div//div//input[@name='email']").send_keys("zirkhaki12@yahoo.com")
#password
driver.find_element_by_xpath("//input[@name='passwd']").click()
driver.find_element_by_xpath("//input[@name='passwd']").send_keys("123456789123456789")
time.sleep(3)
driver.find_element_by_xpath("//body//form//p//span[1]").click()
time.sleep(3)
driver.find_element_by_xpath("//textarea[@name='message']").click()
driver.find_element_by_xpath("//textarea[@name='message']").send_keys("This is example automation test")
driver.find_element_by_xpath("//button[@name='processAddress']//span[contains(text(),'Proceed to checkout')]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='cgv']").click()
driver.find_element_by_xpath("//button[@name='processCarrier']//span[contains(text(),'Proceed to checkout')]").click()
time.sleep(2)
CorrectColorAndSize = driver.find_element_by_xpath("//a[contains(text(),'Color : Green, Size : L')]").text
assert "Color : Green, Size : L" in CorrectColorAndSize
#Total Price
TotalPrice = str(driver.find_element_by_id("total_price").text)
assert "$34.80" in TotalPrice
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Pay by bank wire')]").click()
time.sleep(2)
confirmTotal = str(driver.find_element_by_xpath("//p[contains(text(),'- The total amount of your order comes to:')]//span[contains(text(),'$34.80')]").text)
assert "$34.80" in confirmTotal
driver.find_element_by_xpath("//span[contains(text(),'I confirm my order')]").click()
CompletionOfOrder = driver.find_element_by_xpath("//strong[contains(text(),'Your order on My Store is complete.')]").text
assert "Your order on My Store is complete" in CompletionOfOrder

print("\nWell done! This automation test, YourLogo_Ecommerce, successfully passed.")


