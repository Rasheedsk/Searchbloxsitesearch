import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.makemytrip.com/")
driver.find_element_by_css_selector("input#fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(3)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")

for city in cities:
    if city.text == "Deline, Canada":
        city.click()
        break

driver.find_element_by_xpath("//p[text()='Hyderabad, India']").click()



