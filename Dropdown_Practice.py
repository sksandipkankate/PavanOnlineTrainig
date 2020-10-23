from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")

drp = Select(driver.find_element_by_id("select-demo"))
print("Number of options in dropdown are:", len(drp.options))
alloptions = drp.options
for option in alloptions:
    print(option.text)
drp.select_by_visible_text('Tuesday')

drpmulti = Select(driver.find_element_by_id("multi-select"))
print("Number of options in multiselect dropdown are:", len(drpmulti.options))
NoOfOptions = drpmulti.options
for option in NoOfOptions:
    print(option.text)
drpmulti.select_by_value("Florida")
drpmulti.select_by_value("New York")


