from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\Driver\\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.find_element_by_link_text("REGISTER").click()
driver.find_element_by_partial_link_text("REG")

# find how many links present in the webpage
links = driver.find_elements_by_tag_name("a")  # driver.find_elements_by_xpath("//a")
print("Number of links present on a webpage:", len(links))

link_texts = []  # empty list to store all link text

# Reading all the link texts and storing them in list
for link in links:
    print(link.text)  # just extract all the link text on a webpage
    link_texts.append(link.text)
print(link_texts)
