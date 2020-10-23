from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get('http://www.practiceselenium.com/practice-form.html')
driver.maximize_window()
# driver.implicitly_wait(5)

print("Current URL of the page is:", driver.current_url)
print("Title of the page is:", driver.title)


firstname = driver.find_element_by_name('firstname')
print("Display status of first name is:", firstname.is_displayed())
# sometimes input box is disabled so we have to check status before providing the values
print("Enabled status of first name is:", firstname.is_enabled())

#
# is_selected,is_enabled,is_displayed ,.clear() are the methods of input box and any other web elements
# /conditional commands in webdriver...
# is_selected method is specifically used for radio buttons and checkboxes.....
firstname.send_keys("Sandip")
Lastname = driver.find_element_by_name("lastname")
Lastname.send_keys("Kankate")
# .clear() method will clear the values in input box provided before...
firstname.clear()

"""For radio button 4 methods available: 1) is_displayed , 2)is_enabled , 3)is_selected , 4) .click()
At a time we can select only one radio button """

radio_button = driver.find_element_by_css_selector("input[value=Male]")
print("Display status of Male radio button:", radio_button.is_displayed())  # it will check element is present on webpage or not
print("Enabled status of Male radio button:", radio_button.is_enabled()) # it will check element is allowed any value or not
print("Select status of Male radio button:", radio_button.is_selected())  # True becoz bydefault it is selected Male

radio_button1 = driver.find_element_by_css_selector("input[value=Female]").click() # .click() will select radio button
print("Select status of Male radio button:", radio_button.is_selected()) # becoz it's earlier status True and now its False

'''yoCD_radio = driver.find_element_by_css_selector("input[value=1]")
print("Display status of yoCD_radio button is:", yoCD_radio.is_displayed())
print("Enabled status of yoCD_radio button is:", yoCD_radio.is_enabled())
print("Select status of yoCD_radio button is:", yoCD_radio.is_selected())

yoCD_radio1 = driver.find_element_by_css_selector("input[value=5]")
yoCD_radio1.click()
print("Select status of yoCD_radio button is:", yoCD_radio.is_selected())
'''
# for checkboxes methods are is_displayed(), is_enabled(), is_selected()
favchai_checkbox = driver.find_element_by_xpath("//input[@name='BlackTea']")
print("Display status of the checkbox is:", favchai_checkbox.is_displayed())
print("Enable status of the checkbox is:", favchai_checkbox.is_enabled())
print("Select status of the checkbox is:", favchai_checkbox.is_selected())
favchai_checkbox.click()
print("Select status of the checkbox is:", favchai_checkbox.is_selected())

driver.close()