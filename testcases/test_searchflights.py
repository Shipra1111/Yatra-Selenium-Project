import pytest
from selenium.webdriver.support.ui import WebDriverWait
from pages.search_flight_results_page import SearchFlightResults
from pages.yatra_launch_page import LaunchPage
from utilites.utils import Utils
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestSearchAndVerifyFilter:
    def test_search_flights(self):
        wait = WebDriverWait(self.driver, 10)
        # Launching browser and opening the url
        # Providing going from location
        print("Searching for flights...")  # Example of indented code

        # Add your code to launch the browser, open the URL, and search for flights here
        lp = LaunchPage(self.driver)

        # providing depart from location.
        lp.departfrom("New Delhi")

        # providing going to location.
        lp.goingto("New York")

        # select date
        lp.selectdate()

        # click on flight search button
        lp.clicksearch()

        #to handle dynamic scroll.
        lp.page_scroll()

        #select the filter
        sf = SearchFlightResults(self.driver)

        all_stops= lp.wait_for_presence_of_all_elements(By.XPATH,"//span[contains(text(),'Non Stop')]")
        print(len(all_stops))

        ut = Utils()
        ut.assertlistitemtext(all_stops,"Non Stop")


















