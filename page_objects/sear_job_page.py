from selenium.webdriver.android import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page_object import BasePageObject
from selenium.webdriver.support import expected_conditions as EC


class SearchJobPage(BasePageObject):
    def __init__(self, driver: webdriver, timeout: int = 10):
        super().__init__(driver, timeout)
        self.__titles_locator = (By.XPATH, "//*[@name='keywords' and @aria-label='Search job titles or companies']")
        self.__location_locator = (By.XPATH, "//*[@name='location' and @aria-label='Location']")
        self.__search_Locator = (
        By.XPATH, "//*[@data-tracking-control-name='public_jobs_jobs-search-bar_base-search-bar-search-submit']")

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.__titles_locator))
        self.wait.until(EC.visibility_of_element_located(self.__location_locator))
        self.wait.until(EC.visibility_of_element_located(self.__search_Locator))

    def search(self, title: str, location: str):
        title_input = self.wait.until(EC.visibility_of_element_located(self.__titles_locator))
        title_input.clear()
        title_input.send_keys(title)
        location_input = self.wait.until(EC.visibility_of_element_located(self.__location_locator))
        location_input.clear()
        location_input.send_keys(location)
        btn = self.wait.until(EC.visibility_of_element_located(self.__search_Locator))
        btn.click()
