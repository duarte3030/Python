from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\Documents\Selenium\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")
print(driver.title)
print(driver.page_source)
print(driver.current_url)
driver.close()