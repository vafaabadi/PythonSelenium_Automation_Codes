import time
from selenium import webdriver

####################################################################
#                   Proudly written by Vafa Abadi.
#           LinkedIn: https://www.linkedin.com/in/vafaabadi/
####################################################################

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
#search for the fruits that have "ber" in their names
driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ber")
time.sleep(2)
#highlighting all 3 "Add To Chart" buttons
buttons = driver.find_elements_by_xpath("//div[@class='product']//div[3]//button")
assert "3" in str(len(driver.find_elements_by_xpath("//div[@class='product']//div[3]//button")))

#the full XPath address is //div[@class='product']//div[3]//button/parent::div/parent::div/h4
list_one = []
#adding all 3 fruits to the cart
for button in buttons:
    list_one.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)    #pick name of fruits and add them to the list
    time.sleep(1)
    button.click()

#backet image
driver.find_element_by_xpath("//a[@class='cart-icon']//img[contains(@class,'')]").click()
time.sleep(2)
#makeing sure 3 items listed in basket
items_added = driver.find_elements_by_xpath("//li[@class='cart-item']//img")
assert "6" in str(len(driver.find_elements_by_xpath("//li[@class='cart-item']//img")))
#Proceed to Check Out
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(3)
#Check Out page
#to check number of listed items
No_of_Items = driver.find_elements_by_xpath("//table/tr")     #3 items listed but Selenium will return 4 because it is also counting the title
assert "3" in str(len(driver.find_elements_by_xpath("//table/tr"))-1)

list_two = []
fruits_names = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[2]/p")
for fruits_name in fruits_names:
    list_two.append(fruits_name.text)

assert list_one == list_two             #to check the contents of both lists are same.

#to observe the sum of the individual fruits is equal to the total amount shown on check out page.
sum = 0
amounts = driver.find_elements_by_xpath("//table[@class='cartTable']/tr/td[5]/p")
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)
assert sum == int(driver.find_element_by_xpath("//span[@class='totAmt']").text)

#to check total amount is 388
assert "388" in str(driver.find_element_by_xpath("//span[@class='totAmt']").text)
#applying discount code
driver.find_element_by_xpath("//input[@placeholder='Enter promo code']").send_keys("rahulshettyacademy")
#Apply button
driver.find_element_by_xpath("//button[@class='promoBtn']").click()
time.sleep(5)
assert "Code applied" in driver.find_element_by_xpath("//span[@class='promoInfo']").text
#discount percentage
discount_percent = str(driver.find_element_by_xpath("//span[@class='discountPerc']").text)
assert "10%" in discount_percent
#discounted total
assert "349.2" in str(driver.find_element_by_xpath("//span[@class='discountAmt']").text)
#place order
driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
time.sleep(3)
#final page
driver.find_element_by_tag_name("select").click()
driver.find_element_by_xpath("//option[contains(text(),'Iceland')]").click()
driver.find_element_by_class_name("chkAgree").click()
driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()

print("\nWell done! This automation test, VeggieKart_Alternative, successfully passed.")



#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work












##to add 3 kg of carrots to cart
#driver.find_element_by_xpath("//div[5]//div[2]//a[2]").click()
#driver.find_element_by_xpath("//div[5]//div[2]//a[2]").click()
#driver.find_element_by_xpath("//div[5]//div[3]//button[1]").click()
##to add 2 kg of capsicum to cart
#driver.find_element_by_xpath("//div[9]//div[2]//a[2]").click()
#driver.find_element_by_xpath("//div[9]//div[3]//button[1]").click()
##observe the items in basket
#driver.find_element_by_xpath("//a[4]//img[1]").click()
##remove capsicum from the basket
#driver.find_element_by_xpath("//header//li[2]//a[1]").click()
##proceed to check out
#driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
#TotalBeforeDiscount = str(driver.find_element_by_xpath("//p[contains(text(),'168')]").text)
#assert "168" in TotalBeforeDiscount
##driver.find_element_by_xpath("//input[@placeholder='Enter promo code']").send_keys("this is promo code")
##driver.find_element_by_xpath("//button[contains(text(),'Apply')]").click()
#time.sleep(1)
#driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
#driver.find_element_by_tag_name("select").click()
#driver.find_element_by_xpath("//option[contains(text(),'Iceland')]").click()
#driver.find_element_by_class_name("chkAgree").click()
#driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()

#print("\nWell done! This automation test, VeggieKart, successfully passed.")





