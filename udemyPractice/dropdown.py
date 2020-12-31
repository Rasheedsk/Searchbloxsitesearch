import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")

driver.maximize_window()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_css_selector("input#autosuggest").send_keys("can")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
driver.implicitly_wait(5)

print(len(countries))

for country in countries:
    if country.text == "Canada":
        country.click()
        break
assert driver.find_element_by_css_selector("input#autosuggest").get_attribute("value") == "Canada"

driver.get_screenshot_as_file("screen.png")


