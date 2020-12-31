from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")

driver.get("https://staging.searchblox.com/signup")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_css_selector("input[name='firstName']").send_keys("Rasheed")
driver.find_element_by_css_selector("input[name='lastName']").send_keys("Shaik")
driver.find_element_by_xpath("//input[@name='email']").send_keys("testing1@searchblox.com")
driver.switch_to.frame("__privateStripeFrame5")
driver.find_element_by_css_selector("input[name='cardnumber']").send_keys("4242424242424242")
driver.find_element_by_css_selector("input[autocomplete='cc-exp']").send_keys("02/22")
driver.find_element_by_css_selector("input[autocomplete='cc-csc']").send_keys("333")
driver.switch_to.default_content()
driver.find_element_by_css_selector("input[title='Password']").send_keys("admin")
driver.find_element_by_css_selector("input[title='Confirm Password']").send_keys("admin")
driver.find_element_by_css_selector("input[class*='form-check-input']").click()
driver.find_element_by_xpath("//div[@class='form-group']/button").click()

print(driver.find_element_by_link_text("Add Collection").text)




