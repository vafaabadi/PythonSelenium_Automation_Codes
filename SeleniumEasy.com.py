import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options

#  Wait until an item fully loaded to perform next task as follow:
#  search_box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='search']")))    reference: https://stackoverflow.com/questions/46455702/selenium-find-element-by-id-doesnt-work


driver = webdriver.Chrome(executable_path="C:\\Users\\Vafa\\AppData\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/")
time.sleep(3)
driver.find_element_by_id("details-button").click()
time.sleep(2)
driver.find_element_by_id("proceed-link").click()
time.sleep(5)
driver.find_element_by_xpath("//a[contains(text(),'No, thanks!')]").click()
time.sleep(2)
#Start Practising
driver.find_element_by_xpath("//a[contains(text(),'Start Practising')]").click()
#Simple Form Demo
time.sleep(2)
driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//div//div//a[contains(text(),'Simple Form Demo')]").click()
#enter message
driver.find_element_by_xpath("//input[@placeholder='Please enter your Message']").send_keys("This is Selenium test automation")
#show message button
driver.find_element_by_xpath("//button[contains(text(),'Show Message')]").click()
#your message
Message = driver.find_element_by_xpath("//span[contains(text(),'Selenium test')]").text
assert "Selenium test" in Message
#Enter a
driver.find_element_by_xpath("//body//div//div//div//div[2]//div[2]//div[1]//input[1]").send_keys("7")
#Enter b
driver.find_element_by_xpath("//div//div//div//div//div//div[2]//input[1]").send_keys("7")
#get total button
driver.find_element_by_xpath("//button[contains(text(),'Get Total')]").click()
#total value
total = str(driver.find_element_by_xpath("//span[contains(text(),'14')]").text)
assert "14" in total
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
#checkbox demo
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Checkbox Demo')]").click()
time.sleep(2)
#Single Checkbox Demo
driver.find_element_by_xpath("//label[text()='Click on this check box']//input").click()
time.sleep(1)
SingleCheckBox = driver.find_element_by_xpath("//div[contains(text(),'Success - Check box is checked')]").text
time.sleep(2)
assert "Success" in SingleCheckBox
#Multiple Checkbox Demo
driver.find_element_by_xpath("//body/div/div/div/div/div/input[1]").click()             #to check all boxes
driver.find_element_by_xpath("//label[text()='Option 1']//input").is_selected()         #to check box 1 selected
driver.find_element_by_xpath("//body/div/div/div/div/div/input[1]").click()             #to uncheck all boxes
driver.find_element_by_xpath("//label[text()='Option 2']//input").click()               #to check box 2
driver.find_element_by_xpath("//label[text()='Option 2']//input").is_selected()         #to check box 2 is selected
#Input Forms
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
#Radio buttons Demo
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Radio Buttons Demo')]").click()
time.sleep(2)
#radio button female checked
driver.find_element_by_xpath("//label[contains(text(),'Female')]//input[@name='optradio']").click()
#get checked value
driver.find_element_by_xpath("//button[contains(text(),'Get Checked value')]").click()
CheckedMessage = driver.find_element_by_class_name("radiobutton").text
assert "Female" in CheckedMessage
#Group Radio buttons demo
driver.find_element_by_xpath("//label[contains(text(),'Male')]//input[@name='gender']").click()
driver.find_element_by_xpath("//label[contains(text(),'15 to 50')]").click()
driver.find_element_by_xpath("//button[contains(text(),'Get values')]").click()
GroupRadioButtonsValue = str(driver.find_element_by_xpath("//body//div//div//div//div[2]//div[2]//p[2]").text)
assert "Male" in GroupRadioButtonsValue
assert "15 - 50" in GroupRadioButtonsValue
#input forms
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
#select dropdown list
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Select Dropdown List')]").click()
#select list bar
driver.find_element_by_xpath("//div//div//div[1]//div[2]//select[1]").click()
#select wednesday
driver.find_element_by_xpath("//option[contains(text(),'Wednesday')]").click()
SelectedDay = driver.find_element_by_xpath("//p[contains(text(),'Day selected :- Wednesday')]").text
assert "Wednesday" in SelectedDay

California = driver.find_element_by_xpath("//option[contains(text(),'California')]")
Florida = driver.find_element_by_xpath("//option[contains(text(),'Florida')]")
Washington = driver.find_element_by_xpath("//option[contains(text(),'Washington')]")

time.sleep(3)
ActionChains(driver).key_down(Keys.CONTROL).click(California).key_up(Keys.CONTROL).perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).click(Florida).key_up(Keys.CONTROL).perform()
time.sleep(2)
ActionChains(driver).key_down(Keys.CONTROL).click(Washington).key_up(Keys.CONTROL).perform()
time.sleep(2)

#get all selected button
driver.find_element_by_xpath("//button[contains(text(),'Get All Selected')]").click()
time.sleep(1)
SelectedCities = driver.find_element_by_xpath("//p[contains(text(),'Options selected are : Florida,Washingt')]").text
assert "Florida,Wash" in SelectedCities
#ATTENTION: THE WEB PAGE HAS BUG. IT DOES NOT RETURN CALIFORNIA AS ONE OF THE SELECTED CITIES!!!
#inpot forms
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
#input form submit
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Input Form Submit')]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@placeholder='First Name']").send_keys("Test")
driver.find_element_by_xpath("//input[@placeholder='Last Name']").send_keys("automation")
driver.find_element_by_xpath("//input[@placeholder='E-Mail Address']").send_keys("test@automation.com")
driver.find_element_by_xpath("//input[@placeholder='(845)555-1212']").send_keys("0123456789")
driver.find_element_by_xpath("//input[@placeholder='Address']").send_keys("01 test road")
driver.find_element_by_xpath("//input[@placeholder='city']").send_keys("automation")
driver.find_element_by_xpath("//select[@name='state']").click()
driver.find_element_by_xpath("//option[contains(text(),'Maryland')]").click()
driver.find_element_by_xpath("//input[@placeholder='Zip Code']").send_keys("AA0 0AA")
driver.find_element_by_xpath("//input[@placeholder='Website or domain name']").send_keys("www.testautomation.com/")
driver.find_element_by_xpath("//div//div//div//div[2]//label[1]//input[1]").click()
driver.find_element_by_xpath("//textarea[@placeholder='Project Description']").send_keys("test automating Input Form page")
driver.find_element_by_xpath("//button[contains(text(),'Send')]").click()
time.sleep(3)
#input forms
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
time.sleep(2)
#Ajax form submit
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Ajax Form Submit')]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='title']").click()
driver.find_element_by_xpath("//input[@name='title']").send_keys("Mr Test Automation")
time.sleep(2)
#comment
driver.find_element_by_xpath("//textarea[@name='description']").send_keys("Here to comment about this selenium test automation case")
driver.find_element_by_xpath("//input[@name='btn-submit']").click()
time.sleep(5)
assert "Successfully!" in driver.find_element_by_id("submit-control").text

#input forms
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Input Forms')]").click()
#JQuery select dropdown
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'JQuery Select dropdown')]").click()
#drop down with search box
driver.find_element_by_xpath("//body/div/div/div/div[1]/div[1]/div[2]/span[1]/span[1]/span[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//body/span/span/span/input[1]").send_keys("Ind")
time.sleep(2)
driver.find_element_by_xpath("//li[contains(text(),'India')]").click()
driver.find_element_by_xpath("//input[@placeholder='Select state(s)']").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Select state(s)']").send_keys("lo")
time.sleep(1)
driver.find_element_by_xpath("//option[contains(text(),'Louisiana')]").click()
driver.find_element_by_xpath("//span[contains(text(),'American Samoa')]").click()
time.sleep(1)
driver.find_element_by_xpath("//option[contains(text(),'Puerto Rico')]").click()
driver.find_element_by_xpath("//select[@name='files']").click()
driver.find_element_by_xpath("//option[contains(text(),'Java')]").click()
#Date pickers
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Date pickers')]").click()
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Bootstrap Date Picker')]").click()
time.sleep(2)
#select date bar
driver.find_element_by_xpath("//input[@placeholder='dd/mm/yyyy']").click()
time.sleep(2)
#to change year from 2020 to 2019
driver.find_element_by_xpath("//th[contains(text(),'August 2020')]").click()
driver.find_element_by_xpath("//div[2]//table[1]//thead[1]//tr[2]//th[2]").click()
driver.find_element_by_xpath("//span[contains(text(),'2019')]").click()
driver.find_element_by_xpath("//span[contains(text(),'Jun')]").click()
driver.find_element_by_xpath("//td[contains(text(),'10')]").click()
#start date
driver.find_element_by_xpath("//input[@placeholder='Start date']").click()
driver.find_element_by_xpath("//td[contains(text(),'10')]").click()
#end date
driver.find_element_by_xpath("//input[@placeholder='End date']").click()
driver.find_element_by_xpath("//td[contains(text(),'24')]").click()
driver.find_element_by_xpath("//li[contains(text(),'Future Dates Disabled')]").click()
#date pickers
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Date pickers')]").click()
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'JQuery Date Picker')]").click()
time.sleep(2)
driver.find_element_by_xpath("//input[@name='from']").click()
driver.find_element_by_xpath("//html//body//div//div//div//select").click()
driver.find_element_by_xpath("//option[contains(text(),'Jul')]").click()
driver.find_element_by_xpath("//tr[2]//td[3]//a[1]").click()
driver.find_element_by_xpath("//input[@name='to']").click()
driver.find_element_by_xpath("//a[contains(text(),'25')]").click()
time.sleep(2)
#Table
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[3]").click()
#Table pagination
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Table Pagination')]").click()
#next page button
driver.find_element_by_xpath("//a[contains(text(),'»')]").click()
driver.find_element_by_xpath("//a[contains(text(),'«')]").click()
#Table
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[3]").click()
#table data search
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Table Data Search')]").click()
#filter by task
driver.find_element_by_xpath("//input[@id='task-table-filter']").send_keys("bug")
BugFixing = driver.find_element_by_xpath("//td[contains(text(),'Bug fixing')]").text
assert "Bug" in BugFixing
driver.find_element_by_xpath("//input[@id='task-table-filter']").clear()
time.sleep(1)
driver.find_element_by_xpath("//input[@id='task-table-filter']").send_keys("emily")
BootStrap3 = driver.find_element_by_xpath("//td[contains(text(),'Bootstrap 3')]").text
assert "stra" in BootStrap3
driver.find_element_by_xpath("//button[contains(text(),'Filter')]").click()
time.sleep(1)
driver.find_element_by_xpath("//input[@placeholder='Username']").send_keys("jac")
time.sleep(2)
Karano = driver.find_element_by_xpath("//td[contains(text(),'Karano')]").text
assert "Kar" in Karano
#Table
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[3]").click()
#table filter
driver.find_element_by_xpath("//ul[@id='treemenu']//ul//li//ul//li//a[contains(text(),'Table Filter')]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[contains(text(),'Green')]").click()
#is second listed item checked
driver.find_element_by_xpath("//tr[4]//td[1]//div[1]//label[1]").is_selected()
#is the first listed item Green
assert "Green" in driver.find_element_by_xpath("//tr[1]//td[3]//div[1]//div[1]//h4[1]//span[1]").text
time.sleep(2)
#click on Red
driver.find_element_by_xpath("//button[contains(text(),'Red')]").click()
time.sleep(2)
#checkbox Red
driver.find_element_by_xpath("//tr[3]//td[1]//div[1]").click()
time.sleep(2)
#click to view All
driver.find_element_by_xpath("//button[@class='btn btn-default btn-filter']").click()
#check Red is still checked
driver.find_element_by_xpath("//tr[3]//td[1]//div[1]").is_selected()
#Table
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[3]").click()
time.sleep(2)
#table sort and search
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Table Sort & Search')]").click()
time.sleep(2)
#2nd page
driver.find_element_by_xpath("//a[contains(text(),'2')]").click()
time.sleep(2)
#show entries drop down
driver.find_element_by_xpath("//select[@name='example_length']").click()
time.sleep(2)
#select 25 entries
driver.find_element_by_xpath("//option[contains(text(),'25')]").click()
time.sleep(2)
#Search bar
driver.find_element_by_xpath("//label[contains(text(),'Search:')]//input").send_keys("chief mark")
time.sleep(2)
#find Chief Marketing Officer
assert "CMO" in driver.find_element_by_xpath("//td[contains(text(),'Chief Marketing Officer (CMO)')]").text
#Table
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[3]").click()
time.sleep(2)
#table data download
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Table Data Download')]").click()
time.sleep(2)
#THE TABLE DOESNT DO ANYTHING. UNABLE TO DOWNLOAD OR TO PRINT IT.
#progress bars and sliders
driver.find_element_by_xpath("//a[contains(text(),'Progress Bars & Sliders')]").click()
time.sleep(2)
#JQuery download and progress bars
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'JQuery Download Progress bars')]").click()
time.sleep(2)
#Start Download
driver.find_element_by_xpath("//button[contains(text(),'Start Download')]").click()
time.sleep(15)
assert "Complete" in driver.find_element_by_xpath("//div[contains(text(),'Complete!')]").text
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'Close')]").click()
time.sleep(2)
#progress bars and sliders
driver.find_element_by_xpath("//a[contains(text(),'Progress Bars & Sliders')]").click()
time.sleep(2)
#bootstrap progress bar
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Bootstrap Progress bar')]").click()
time.sleep(2)
#download
driver.find_element_by_xpath("//button[contains(text(),'Download')]").click()
time.sleep(35)
assert "100" in driver.find_element_by_xpath("//div[contains(text(),'100%')]").text
time.sleep(2)
#progress bars and sliders
driver.find_element_by_xpath("//a[contains(text(),'Progress Bars & Sliders')]").click()
time.sleep(2)
#drag and drop sliders
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Drag & Drop Sliders')]").click()
time.sleep(4)
#Default Value 10
slider = driver.find_element_by_xpath('//div[@id="slider1"]//input')
ActionChains(driver).drag_and_drop_by_offset(slider, 250, 0).perform()
time.sleep(2)
#Default Value 50 - blue
slider = driver.find_element_by_xpath('//div[@id="slider2"]//input')
ActionChains(driver).drag_and_drop_by_offset(slider, 50, 0).perform()
time.sleep(2)
#Default value 30 - green
slider = driver.find_element_by_xpath('//div[@id="slider3"]//input')
ActionChains(driver).drag_and_drop_by_offset(slider, 100, 0).perform()
time.sleep(2)
#Alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#bootstrap alerts
driver.find_element_by_xpath("//li[@class='tree-branch']//ul//li//a[contains(text(),'Bootstrap Alerts')]").click()
time.sleep(2)
#autoclosable success
driver.find_element_by_xpath("//button[@id='autoclosable-btn-success']").click()
time.sleep(1)
assert "autocloseable success" in driver.find_element_by_xpath("//div[@class='alert alert-success alert-autocloseable-success']").text
time.sleep(5)
#normal success
driver.find_element_by_xpath("//button[@id='normal-btn-success']").click()
assert "normal success" in driver.find_element_by_xpath("//div[@class='alert alert-success alert-normal-success']").text
time.sleep(2)
#autoclosable warning
driver.find_element_by_xpath("//button[@id='autoclosable-btn-warning']").click()
time.sleep(1)
assert "autocloseable warning" in driver.find_element_by_xpath("//div[@class='alert alert-warning alert-autocloseable-warning']").text
time.sleep(2)
#Alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#Bootstrap Modals
driver.find_element_by_xpath("//li[@class='tree-branch']//ul//li//a[contains(text(),'Bootstrap Modals')]").click()
time.sleep(2)
#single modal
driver.find_element_by_xpath("//body/div/div/div/div[1]/div[1]/div[1]/div[2]/a[1]").click()
time.sleep(2)
assert "content for the modal dialog displays" in driver.find_element_by_xpath("//div[@class='modal fade in']//div[@class='modal-body'][contains(text(),'This is the place where the content for the modal')]").text
time.sleep(2)
driver.find_element_by_xpath("//div[@class='modal fade in']//a[@class='btn btn-primary'][contains(text(),'Save changes')]").click()
time.sleep(2)
#multiple modal
driver.find_element_by_xpath("//body/div/div/div/div[2]/div[1]/div[1]/div[2]/a[1]").click()
time.sleep(2)
#Launch modal on modal
driver.find_element_by_xpath("//div//div//div//div//div//div//div//div//a[contains(text(),'Launch modal')]").click()
time.sleep(2)
assert "Modal 2" in driver.find_element_by_xpath("//h4[contains(text(),'Modal 2')]").text
time.sleep(2)
driver.find_element_by_xpath("//div[6]//a[2]").click()
time.sleep(2)
#Alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#windows popup modal
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Window Popup Modal')]").click()
time.sleep(2)
#follow on twitter
driver.find_element_by_xpath("//a[contains(text(),'Follow On Twitter')]").click()
time.sleep(2)
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
driver.maximize_window()
time.sleep(2)
#No Thanks
driver.find_element_by_xpath("//span[contains(text(),'No, thanks')]").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)
#alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#progress bar modal
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Progress Bar Modal')]").click()
time.sleep(2)
#yellow show dialog
driver.find_element_by_xpath("//body//button[3]").click()
time.sleep(1)
#progress bar
assert "Hello Mr. Alert !" in driver.find_element_by_xpath("//h3[contains(text(),'Hello Mr. Alert !')]").text
time.sleep(4)
#alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#javascript alerts
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Javascript Alerts')]").click()
time.sleep(2)
#javascript alert box
driver.find_element_by_xpath("//div//div//div[1]//div[2]//button[1]").click()
time.sleep(2)
alert = driver.switch_to.alert
alertMessage = alert.text
assert "alert box" in alertMessage
alert.accept()
time.sleep(2)
#javascript confirm box
driver.find_element_by_xpath("//body//div//div//div//div[2]//div[2]//button[1]").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.dismiss()
time.sleep(2)
#javascript with text box box
driver.find_element_by_xpath("//button[contains(text(),'Click for Prompt Box')]").click()
time.sleep(2)
alert = driver.switch_to.alert
alert.send_keys("JavaScript Alert box! Promt Box! My text!")
alert.accept()
time.sleep(2)
#alerts and modals
driver.find_element_by_xpath("//li[@class='tree-branch']//a[contains(text(),'Alerts & Modals')]").click()
time.sleep(2)
#file download
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'File Download')]").click()
time.sleep(2)
#enter data box
driver.find_elements_by_css_selector("//html//body//div//div//div//div//div//div//textarea").click()
time.sleep(1)
driver.find_element_by_xpath("//html//body//div//div//div//div//div//div//textarea").send_keys("test automation for file downlaod")
driver.find_element_by_xpath("//button[contains(text(),'Generate File')]").click()
time.sleep(1)
#downliad link
driver.find_element_by_xpath("//body/div/div/div/div/div[2]/a[1]").click()
time.sleep(2)
#List box
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[6]/a[1]").click()
time.sleep(2)
#bootstrap list box
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Bootstrap List Box')]").click()
time.sleep(2)
#select Morbi and shift it to right
driver.find_element_by_xpath("//body//div//div//div//div//div[1]//div[1]//li[3]").click()
time.sleep(1)
#shift right button
driver.find_element_by_xpath("//button[2]//span[1]").click()
time.sleep(1)
#shift cras to left
driver.find_element_by_xpath("//li[contains(text(),'Cras justo odio')]").click()
time.sleep(1)
driver.find_element_by_xpath("//div//div//div//div//div//button[1]//span[1]").click()
#select all on left
driver.find_element_by_xpath("//div//div//div//div[2]//div[1]//a[1]//i[1]").click()
time.sleep(2)
driver.find_element_by_xpath("//button[2]//span[1]").click()
time.sleep(2)
#List box
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[6]/a[1]").click()
time.sleep(2)
#JQuery List Box
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'JQuery List Box')]").click()
time.sleep(2)
#select Isis
driver.find_element_by_xpath("//option[contains(text(),'Isis')]").click()
time.sleep(1)
driver.find_element_by_xpath("//body//div//div//div//div//div//button[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'Add All')]").click()
time.sleep(1)
driver.find_element_by_xpath("//option[contains(text(),'Isabella')]").click()
time.sleep(1)
driver.find_element_by_xpath("//body//button[3]").click()
time.sleep(1)
driver.find_element_by_xpath("//button[contains(text(),'Remove All')]").click()
time.sleep(2)
#List box
driver.find_element_by_xpath("//body/div/div/div/div/div/ul/li/ul/li[6]/a[1]").click()
time.sleep(2)
#data list filler
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Data List Filter')]").click()
time.sleep(2)
#search attendees
driver.find_element_by_xpath("//input[@placeholder='Search Attendees...']").click()
driver.find_element_by_xpath("//input[@placeholder='Search Attendees...']").send_keys("Arman")
time.sleep(2)
#others
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//a[contains(text(),'Others')]").click()
time.sleep(2)
#drag and drop
driver.find_element_by_xpath("//html//body//div//div//div//div//div//ul//li//ul//li//ul//li//a[contains(text(),'Drag and Drop')]").click()
time.sleep(2)
drag = driver.find_element_by_xpath("//span[contains(text(),'Draggable 1')]")
drop = driver.find_element_by_id("mydropzone")
ActionChains(driver).click_and_hold(drag).move_to_element(drop).release(drop).perform()







