import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.yatra.com/")
    driver.maximize_window()
    driver.refresh()
    request.cls.driver = driver
    yield
    driver.close()
