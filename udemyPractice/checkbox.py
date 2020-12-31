from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2" :
        checkbox.click()
        assert checkbox.is_selected()

radiobutton = driver.find_elements_by_xpath("//input[@name='radioButton']")
radiobutton[0].click()
assert radiobutton[0].is_selected()

assert driver.find_element_by_id("displayed-text").is_displayed()

driver.find_element_by_id("hide-textbox").click()