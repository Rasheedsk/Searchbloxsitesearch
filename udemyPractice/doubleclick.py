from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)


action.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
assert not driver.find_element_by_id("button").is_displayed()