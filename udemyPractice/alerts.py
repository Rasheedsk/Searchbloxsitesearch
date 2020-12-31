from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
driver.maximize_window()
validateText = "Rasheed"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_css_selector("input#name").send_keys(validateText)
driver.find_element_by_css_selector("input#alertbtn").click()
alert = driver.switch_to.alert
alertText =alert.text
assert validateText in alertText
alert.accept()