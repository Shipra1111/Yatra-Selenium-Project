import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.base_driver import BaseDriver

class LaunchPage(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def departfrom(self, departlocation):
        depart_from = self.wait_until_element_is_clickable(By.XPATH, "//p[@title='New Delhi']")
        depart_from.click()
        enter_location = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='input-with-icon-adornment']")
        enter_location.send_keys(departlocation)
        select_from_dropdown = self.wait_until_element_is_clickable(By.XPATH, "(//div[@class='fw-600 mb-0'])[1]")
        select_from_dropdown.click()

    def goingto(self, goingtolocation):
        going_to = self.wait_until_element_is_clickable(By.XPATH, "//p[@title='Mumbai']")
        going_to.click()
        enter_location = self.wait_until_element_is_clickable(By.XPATH, "//input[@id='input-with-icon-adornment']")
        enter_location.send_keys(goingtolocation)
        time.sleep(4)
        select_from_dropdown = self.wait_until_element_is_clickable(By.XPATH, "(//div[@class='fw-600 mb-0'])[1]")
        select_from_dropdown.click()

    def selectdate(self):
        self.wait_until_element_is_clickable(By.XPATH, "//div[@class='css-rd021u']").click()
        select_date = self.wait_until_element_is_clickable(By.XPATH,
                                              "//div[contains(@aria-label,'2024-10')]//div[contains(@aria-label,'Choose Wednesday, October 30th, 2024')]")
        select_date.click()

    def clicksearch(self):
        self.wait_until_element_is_clickable(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(4)




