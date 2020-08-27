import time
from selenium import webdriver

#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.phptravels.net/admin")

driver.find_element_by_xpath("//form[@class='form-signin form-horizontal wow fadeIn animated animated']//input[@placeholder='Email']").send_keys("admin@phptravels.com")
driver.find_element_by_xpath("//input[@placeholder='Password']").send_keys("demoadmin")
driver.find_element_by_xpath("//button[@class='btn btn-primary btn-block ladda-button fadeIn animated btn-lg']").click()
time.sleep(5)
driver.find_element_by_xpath("//button[@class='btn btn-danger btn-block']").click()
time.sleep(2)
driver.find_element_by_name("applytax").click()
driver.find_element_by_xpath("//option[contains(text(),'Yes')]").click()
time.sleep(2)
driver.find_element_by_id("servicetype").click()
driver.find_element_by_xpath("//option[contains(text(),'Hotels')]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[@class='btn btn-primary']").click()
driver.find_element_by_id("selusertype").click()
driver.find_element_by_xpath("//option[contains(text(),'Guest')]").click()
driver.find_element_by_id("fname").send_keys("Charlie")
driver.find_element_by_name("lastname").send_keys("Chaplin")
driver.find_element_by_id("mobile").send_keys("01234567890")
driver.find_element_by_xpath("//input[@id='email']").send_keys("charlie_chapling@automation.com")
driver.find_element_by_xpath("//input[@id='Hotels']").send_keys("12/12/2020")
driver.find_element_by_xpath("//td[contains(@class,'active')][contains(text(),'12')]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[5]//tr[4]//td[7]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[4]//div[1]//div[1]//a[1]//span[1]").click()
driver.find_element_by_xpath("//div[4]//div[1]//div[1]//a[1]//span[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(text(),'Hyatt Regency Perth')]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[@id='s2id_poprooms']").click()
time.sleep(1)
driver.find_element_by_xpath("//div[contains(text(),'Standard Room')]").click()
driver.find_element_by_xpath("//select[@name='roomscount']").click()
time.sleep(3)
driver.find_element_by_xpath("//option[contains(text(),'1')]").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='extras_4']").click()
driver.find_element_by_xpath("//input[@id='extras_3']").click()
driver.find_element_by_xpath("//input[@id='extras_2']").click()
driver.find_element_by_xpath("//input[@id='extras_1']").click()
driver.find_element_by_xpath("//div[@class='panel panel-default rprice paytype']//div[@class='col-md-4']").click()
driver.find_element_by_xpath("//div[@class='panel panel-default rprice paytype']//option[6]").click()
driver.find_element_by_xpath("//input[@class='btn btn-primary btn-lg']").click()
CustomerName = driver.find_element_by_xpath("//td[contains(text(),'Charlie')]").text
assert "Charlie" in CustomerName
Total = str(driver.find_element_by_xpath("//tr[1]//td[8]").text)
assert "2483.25" in Total
#click on view invoice button
driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//tr[1]//td[12]//a[1]").click()
time.sleep(2)
child_window = driver.window_handles[1]
time.sleep(1)
driver.switch_to.window(child_window)
time.sleep(4)
#to confirm the name of the client for the reservation
FirstNameConfirmation = str(driver.find_element_by_xpath("//span[contains(text(),'Charlie Chaplin')]").text)
assert "Charlie Chaplin" in FirstNameConfirmation
HotelConfirmation = str(driver.find_element_by_xpath("//h6[contains(text(),'Hyatt Regency Perth')]").text)
assert "Hyatt Regency Perth" in HotelConfirmation
CorrectTotal = str(driver.find_element_by_xpath("//span[contains(text(),'USD $2,483.25')]").text)
assert "USD $2,483.25" in CorrectTotal
driver.find_element_by_xpath("//button[contains(text(),'Pay on Arrival')]").click()
alert = driver.switch_to.alert
alertMessage = alert.text
assert "to pay at arrival?" in alertMessage
alert.accept()
time.sleep(2)
ReservationConfirmed = str(driver.find_element_by_xpath("//h4[contains(text(),'Your booking status is Reserved')]").text)
assert "is Reserved" in ReservationConfirmed
print("\nWell done! This automation test, phptravels_backend, successfully passed.")
