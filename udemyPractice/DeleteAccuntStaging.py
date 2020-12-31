from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe", options=chrome_options)

driver.maximize_window()
driver.get("http://35.192.176.45/")
driver.find_element_by_xpath("//span[text()=' Account ']").click()
driver.find_element_by_xpath("//span[text()='Sign in']").click()
driver.implicitly_wait(4)
driver.find_element_by_css_selector("input#username").send_keys("admin@localhost")
driver.find_element_by_css_selector("input#password").send_keys("sbx-adm@Mar2020!a55")
driver.find_element_by_css_selector("button[class*='btn-primary']").click()
driver.find_element_by_xpath("//span[text()='Administration']").click()
driver.find_element_by_xpath("//span[text()='API']").click()
driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@class='border-0']"))
driver.find_element_by_xpath("//a[@href='#!/sb45account45resource']").click()
driver.find_element_by_link_text("/api/v1/account/delete/{emailId}").click()
driver.find_element_by_css_selector("ul#resour  ces li:nth-of-type(4) ul li:nth-of-type(6) ul li div:nth-of-type(2) form table tbody tr td:nth-of-type(2) input").send_keys("testing1@searchblox.com")
driver.find_element_by_xpath("//div[@id='sb45account45resource_deleteAccountUsingDELETE_content']/form[1]/div[3]/input").click()
print(driver.find_element_by_xpath("//div[@id='sb45account45resource_deleteAccountUsingDELETE_content']/div[2]/div[3]/pre/code/span[4]").get_attribute("value"))

#assert "Successfully" in success_message
