from selenium import webdriver

    #driver = webdriver.Chrome(executable_path="C:\\browser\chromedriver.exe")

driver = webdriver.Firefox(executable_path="C:\\browser\geckodriver.exe")
driver.maximize_window()
driver.get("https://staging.searchblox.com/")

print(driver.title)
print(driver.current_url)
driver.get("https://staging.searchblox.com/signup")
print(driver.current_url)
driver.back()
driver.refresh()
driver.close()