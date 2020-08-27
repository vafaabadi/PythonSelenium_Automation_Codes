import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work

driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_id("checkBoxOption1").click()
driver.find_element_by_id("checkBoxOption2").click()
driver.find_element_by_id("checkBoxOption3").click()
dropdown = Select(driver.find_element_by_id("dropdown-class-example"))
dropdown.select_by_value("option2")
driver.find_element_by_id("autocomplete").click()
driver.find_element_by_id("autocomplete").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_css_selector("ul[id='ui-id-1'] li")
for country in countries:
    if country.text == "India":
        country.click()
        break
radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()
time.sleep(3)
driver.find_element_by_id("opentab").click()
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
time.sleep(4)
driver.find_element_by_link_text("Courses").click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_id("openwindow").click()
new_tab = driver.window_handles[2]
driver.switch_to.window(new_tab)
#driver.find_element_by_link_text("NO THANKS").click()
driver.switch_to.window(driver.window_handles[0])
driver.find_element_by_css_selector("#name").send_keys("testing alert")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alertMessage = alert.text
assert "testing alert" in alertMessage
alert.accept()
driver.find_element_by_css_selector("#name").send_keys("testing confirm")
driver.find_element_by_css_selector("#confirmbtn").click()
alert = driver.switch_to.alert
alertMessage = alert.text
assert "testing confirm" in alertMessage
alert.dismiss()
driver.find_element_by_css_selector("#hide-textbox").click()
driver.find_element_by_css_selector("#show-textbox").click()
driver.find_element_by_css_selector("#displayed-text").send_keys("testing element display box")
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(firstLevelMenu).perform()
time.sleep(2)
secondLevelMenu = driver.find_element_by_link_text("Top")
secondLevelMenu.click()
time.sleep(2)
action = ActionChains(driver)
firstLevelMenu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(firstLevelMenu).perform()
time.sleep(2)
secondLevelMenu = driver.find_element_by_link_text("Reload")
secondLevelMenu.click()
time.sleep(2)
#driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
#driver.find_element_by_partial_link_text("Articles").click()
##driver.switch_to.default_content()
driver.find_element_by_xpath("//a[@class='blinkingText']").click()

print("\nWell done! This automation test, PracticePage, successfully passed.")
