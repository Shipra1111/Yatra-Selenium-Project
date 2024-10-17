from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight); return document.body.scrollHeight")
        match = False
        while not match:
            lastCount = pageLength
            time.sleep(2)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight); return document.body.scrollHeight")
            if lastCount == pageLength:
                match = True
        time.sleep(4)


    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element
