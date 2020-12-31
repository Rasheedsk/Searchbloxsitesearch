from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
driver.maximize_window()

driver.get("https://rahulshettyacademy.com/angularpractice/")

#driver.find_element_by_name("name").send_keys("Rasheed")
driver.find_element_by_xpath("//input[@name='name']").send_keys("Rasheed")
driver.find_element_by_css_selector("input[name='email']").send_keys("rasheedsk4d7@gmail.com")
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element_by_css_selector("input[id='exampleCheck1']").click()
driver.find_element_by_css_selector("input[class*='btn-success']").click()
print(driver.find_element_by_css_selector("div[class*='alert-success']").text)

