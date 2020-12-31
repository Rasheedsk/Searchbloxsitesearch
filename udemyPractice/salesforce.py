from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("input#username").send_keys("Rasheed")
driver.find_element_by_css_selector("input.password").send_keys("aaaaa")
driver.find_element_by_css_selector("input.password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.close()