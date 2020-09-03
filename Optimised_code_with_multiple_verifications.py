import time
from selenium import webdriver

####################################################################
#                   cd ..Proudly written by Vafa Abadi.
#           LinkedIn: https://www.linkedin.com/in/vafaabadi/
####################################################################

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(2)
#search for the fruits that have "ber" in their names
driver.find_element_by_xpath("//input[@placeholder='Search for Vegetables and Fruits']").send_keys("b")
time.sleep(2)


#pick names of the fruits
names = driver.find_elements_by_xpath("//div[@class='product']/h4")
# //div[@class='product']/h4/parent::div/p     XPATH from names to prices. child (name) to parent (cart) and then to another child (price)
# parent::div/p/parent::div/div[3]/button      XPATH from prices to buttons. child (price) to parent (cart) and then to child (button)
list_names = []
list_prices = []
for name in names:
    list_names.append(name.text)                    #adding fruit names to list_names list.
    list_prices.append(name.find_element_by_xpath("parent::div/p").text)            #adding prices to list_prices list
    name.find_element_by_xpath("parent::div/p").find_element_by_xpath("parent::div/div[3]/button").click()      #clicking on Add To Chart


#basket image
driver.find_element_by_xpath("//a[@class='cart-icon']//img[contains(@class,'')]").click()
time.sleep(2)
#Proceed to Check Out
driver.find_element_by_xpath("//button[contains(text(),'PROCEED TO CHECKOUT')]").click()
time.sleep(3)


#Check Out page
#picking name of the fruits and adding them to a unique list
fruits = driver.find_elements_by_xpath("//table[@class='cartTable']//tr/td[2]/p")
list_fruits = []
list_totals = []
sum = 0
#//table[@class='cartTable']//tr/td[2]/p/parent::td/parent::tr/td[5]/p XPATH for parent and child.
for fruit in fruits:
    list_fruits.append(fruit.text)
    list_totals.append(fruit.find_element_by_xpath("parent::td/parent::tr/td[5]/p").text)
    sum = sum + int(fruit.find_element_by_xpath("parent::td/parent::tr/td[5]/p").text)

assert list_names == list_fruits
assert list_prices == list_totals
assert sum == int(driver.find_element_by_xpath("//span[@class='totAmt']").text)


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
assert "631.8" in str(driver.find_element_by_xpath("//span[@class='discountAmt']").text)
#place order
driver.find_element_by_xpath("//button[contains(text(),'Place Order')]").click()
time.sleep(3)
#final page
driver.find_element_by_tag_name("select").click()
driver.find_element_by_xpath("//option[contains(text(),'Iceland')]").click()
driver.find_element_by_class_name("chkAgree").click()
driver.find_element_by_xpath("//button[contains(text(),'Proceed')]").click()

print("\nWell done! This automation test, VeggieKart_Alternative, successfully passed.")



