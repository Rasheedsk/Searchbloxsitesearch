from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome("C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
menu = driver.find_element_by_css_selector("#mousehover")
action.move_to_element(menu).perform()

submenu = driver.find_element_by_link_text("Reload")

action.move_to_element(submenu).click().perform()