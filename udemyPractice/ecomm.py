import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

list = []
list2 = []
driver = webdriver.Chrome(executable_path= "C:\\browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element_by_css_selector("input[class='search-keyword']").send_keys("on")
time.sleep(3)
products = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for product in products:
    list.append(product.find_element_by_xpath("parent::div/parent::div/h4").text)
    product.click()

print(list)

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "input[class='promoCode']")))
veggies = driver.find_elements_by_css_selector("p.product-name")

for veg in veggies:
    list2.append(veg.text)
print(list2)
assert list == list2

amounts = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)

originalamount = driver.find_element_by_css_selector(".discountAmt").text

driver.find_element_by_css_selector("input[class='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
total = int(driver.find_element_by_css_selector(".totAmt").text)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element_by_css_selector(".promoInfo").text)
discountlamount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discountlamount) < int(originalamount)
print(discountlamount)

assert sum == total

driver.close()