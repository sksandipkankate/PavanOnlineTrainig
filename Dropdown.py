
"""Dropdown single and multi element select(list box)-> Dropdown also called combo box-> Operations on dropdown as
1) In dropdown , count number of options their.
2) Extract or capture all the options in the console window
3) select one of the options from dropdown"""

from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get("http://www.practiceselenium.com/practice-form.html")
# driver.maximize_window()
# driver.implicitly_wait(5)

# Dropdown
continent_dropdown = Select(driver.find_element_by_id("continents"))
# 1) Number of options count
NoOfOptions = len(continent_dropdown.options)
print("Number of options in dropdown:", NoOfOptions)

# 2)Extract all the options
all_options = continent_dropdown.options
for option in all_options:
    # print(option.get_attribute('text')) # here option is webelement and from that we have to extract text
    print(option.text, end=' ') # it will give the same result as above

# 3) select option from the dropdown using select by index, value , visible text
continent_dropdown.select_by_visible_text('North America')
continent_dropdown.select_by_index(3)
#continent_dropdown.select_by_value("4") --> Here value is not their in webelements so cant use it.

# list box i.e, select multiple elements from dropdown
listbox = Select(driver.find_element_by_id("selenium_commands"))
print("Numbers of options:", len(listbox.options))
all_listoptions = listbox.options

# read / capture all the options from the listbox
for option in all_listoptions:
    print(option.text) # print(option.get_attribute("text")

# select multiple options
listbox.select_by_visible_text("Switch Commands")
listbox.select_by_visible_text("WebElement Commands")
# here we didn't use select by values becoz values isn't associated with the options
driver.find_element_by_id('submit').click()

driver.quit()

""" Browser Commands
close() --> Closes single browser window
quit() --> closes multiple browser windows
"""

