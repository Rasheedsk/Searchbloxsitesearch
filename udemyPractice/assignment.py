import time

from selenium import webdriver

vegetables = ['Onion - 1 Kg', 'Musk Melon - 1 Kg', 'Water Melon - 1 Kg', 'Almonds - 1/4 Kg']
veggies = []

driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[type='search']").send_keys("on")
time.sleep(3)
vegs = driver.find_elements_by_css_selector("h4[class='product-name']")

for veg in vegs:
    veggies.append(veg.text)

print(veggies)

assert veggies == vegetables