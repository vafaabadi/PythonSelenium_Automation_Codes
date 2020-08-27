import time
from selenium import webdriver

#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.phptravels.net/admin")

driver.find_element_by_xpath(
    "//form[@class='form-signin form-horizontal wow fadeIn animated animated']//input[@placeholder='Email']").send_keys(
    "admin@phptravels.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("demoadmin")
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block ladda-button fadeIn animated btn-lg']").click()
time.sleep(7)
driver.find_element_by_xpath("//body/div/nav/div/ul/li[8]/a[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'Routes')]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Add')]").click()
time.sleep(5)
driver.maximize_window()
time.sleep(2)
# price for adults
driver.find_element_by_xpath("//td[2]//input[1]").click()
driver.find_element_by_xpath("//td[2]//input[1]").click()
driver.find_element_by_xpath("//td[2]//input[1]").send_keys("1000")
# price for child
driver.find_element_by_xpath("//td[3]//input[1]").click()
driver.find_element_by_xpath("//td[3]//input[1]").click()
driver.find_element_by_xpath("//td[3]//input[1]").send_keys("500")
# price for infant
driver.find_element_by_xpath("//td[4]//input[1]").click()
driver.find_element_by_xpath("//td[4]//input[1]").click()
driver.find_element_by_xpath("//td[4]//input[1]").send_keys("200")
time.sleep(2)
# departure city - airport
driver.find_element_by_xpath("//tr[1]//th[2]//div[1]//a[1]//span[1]").click()
driver.find_element_by_xpath("//body/div/div/input[1]").send_keys("bar")
time.sleep(2)
driver.find_element_by_xpath("//body/div/ul/li[12]").click()
time.sleep(1)
# departure airline
driver.find_element_by_xpath("//tr[1]//th[3]//div[1]//a[1]//span[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[13]//input[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//div[13]//input[1]").send_keys("sou")
time.sleep(2)
driver.find_element_by_xpath("//body/div/ul/li[6]").click()
time.sleep(2)
# flight number
driver.find_element_by_xpath("//tr[1]//th[4]//input[1]").click()
driver.find_element_by_xpath("//tr[1]//th[4]//input[1]").send_keys("12345")
# departure date
driver.find_element_by_xpath("//tr[1]//th[5]//input[1]").click()
driver.find_element_by_xpath("//tr[1]//th[5]//input[1]").send_keys("12/12/2020")
driver.find_element_by_xpath("//tr[1]//th[6]//input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[6]//div[3]//a[1]").click()
driver.find_element_by_xpath("//div[6]//div[4]//div[2]//div[1]").click()
driver.find_element_by_xpath("//div[6]//div[5]//div[1]//div[2]").click()
driver.find_element_by_xpath("//tr[1]//th[7]//input[1]").click()
driver.find_element_by_xpath("//a[contains(text(),'AM')]").click()
driver.find_element_by_xpath("//div[7]//div[4]//div[1]//div[2]").click()
driver.find_element_by_xpath("//div[7]//div[2]//div[1]//div[1]").click()
driver.find_element_by_xpath("//span[contains(text(),'Enter City Or Airport')]").click()
driver.find_element_by_xpath("//div[14]//input[1]").click()
driver.find_element_by_xpath("//div[14]//input[1]").send_keys("lon")
time.sleep(2)
driver.find_element_by_xpath("//div[contains(text(),'don (BQH)')]").click()
driver.find_element_by_xpath("//tr[2]//th[3]//div[1]//a[1]//span[1]").click()
driver.find_element_by_xpath("//div[15]//input[1]").send_keys("bar")
time.sleep(2)
driver.find_element_by_xpath("//li[3]//div[1]").click()
driver.find_element_by_xpath("//tr[2]//th[4]//input[1]").click()
driver.find_element_by_xpath("//tr[2]//th[4]//input[1]").send_keys("987654")
driver.find_element_by_xpath("//tr[2]//th[5]//input[1]").click()
driver.find_element_by_xpath("//tr[2]//th[5]//input[1]").send_keys("13/12/2020")
driver.find_element_by_xpath("//tr[2]//th[6]//input[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//a[contains(text(),'AM')]").click()
driver.find_element_by_xpath("//div[8]//div[4]//div[1]//div[2]").click()
driver.find_element_by_xpath("//div[8]//div[3]//div[1]//div[1]").click()
driver.find_element_by_xpath("//tr[2]//th[7]//input[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//div[9]//a[1]").click()
driver.find_element_by_xpath("//div[9]//div[2]//div[1]//div[2]").click()
driver.find_element_by_xpath("//div[9]//div[2]//div[1]//div[1]").click()
time.sleep(2)
iframe = driver.find_element_by_xpath(
    "//html//body//div//div//form//div//div//div//div//div//div//div//div//div//div//iframe")
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//html//body").click()
driver.find_element_by_xpath("//html//body").send_keys("This is back-end automation testing example!")
driver.switch_to.default_content()
# Main settings (side box)
driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[1]/input[1]").click()
driver.find_element_by_xpath("//body/div/div/form/div/div/div/div[2]/div[1]/div[1]/input[1]").send_keys("20")
# VAT tax
driver.find_element_by_xpath("//div//div[3]//div[1]//div[1]//input[1]").click()
driver.find_element_by_xpath("//div//div[3]//div[1]//div[1]//input[1]").send_keys("20")
# Deposit
driver.find_element_by_xpath("//div[4]//div[1]//div[1]//input[1]").click()
driver.find_element_by_xpath("//div[4]//div[1]//div[1]//input[1]").send_keys("10")
# Flight type
driver.find_element_by_xpath("//span[contains(text(),'Economy')]").click()
driver.find_element_by_xpath("//div[contains(text(),'Business')]").click()
# refundable
driver.find_element_by_xpath("//span[contains(text(),'Non Refundable')]").click()
driver.find_element_by_xpath("//li[1]//div[1]").click()
# submit
driver.find_element_by_xpath("//button[contains(text(),'Submit')]").click()
time.sleep(3)
From = driver.find_element_by_xpath("//td[contains(text(),'Barbuda')]").text
assert "Barbuda" in From
To = driver.find_element_by_xpath("//td[contains(text(),'London')]").text
assert "London" in To
print("\nWell done! This automation test, phptravels_backend_flights, successfully passed.")
