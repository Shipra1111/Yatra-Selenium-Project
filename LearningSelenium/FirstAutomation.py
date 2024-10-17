from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome()
driver = webdriver.Chrome()
driver.get("https://www.google.com")
print(driver.title)
driver.maximize_window()
driver.close()