import time
from selenium.webdriver.common.by import By
from base.base_driver import BaseDriver

class SearchFlightResults(BaseDriver):
    def __init__(self , driver):
        super().__init__(driver)
        self.driver = driver

    def filter_flight(self):
        self.wait_until_element_is_clickable(By.XPATH,"//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
        time.sleep(10)

    def closewidgeticon(self):
        time.sleep(2)
        self.wait_until_element_is_clickable(By.XPATH, "//span[@class='wewidgeticon we_close']").click()
