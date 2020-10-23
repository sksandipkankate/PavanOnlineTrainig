from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get("https://www.orangehrm.com/open-source/demo/")
driver.maximize_window()
driver.implicitly_wait(5)
print(driver.title)
print(driver.current_url)
driver.find_element_by_name("FirstName").send_keys("Sandip")
driver.find_element_by_name("LastName").send_keys("Kankate")
driver.find_element_by_name("CompanyName").send_keys("SPSoftware")
element = driver.find_element_by_xpath("//select[@name=Industry]").click()
drop_down = Select(element)
#drop_down_options = list(element.get_attribute())
drop_down.select_by_index(6)
driver.close()
