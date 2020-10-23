from selenium import webdriver
driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
print("Title of the page is:", driver.title)
print("Current url of the page is:", driver.current_url)
driver.find_element_by_id("txtUsername").send_keys("Admin")
driver.find_element_by_id("txtPassword").send_keys("admin123")
driver.find_element_by_id("btnLogin").click()
# Capture the title of the Dashboard page(Actual title)
act_title = driver.title
exp_title = "OrangeHRM"
# verify title of the page : OrangeHRM (Expected)
if act_title == exp_title:
    print("Login Test Passed...")
else:
    print("Login Test Failed...")
driver.close()



