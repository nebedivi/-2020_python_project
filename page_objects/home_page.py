from selenium.webdriver.android import webdriver
from selenium.webdriver.common.by import By
from page_objects.base_page_object import BasePageObject
from selenium.webdriver.support import expected_conditions as EC

from page_objects.sear_job_page import SearchJobPage

_HOME_PAGE_URL = 'https://www.linkedin.com/?trk=guest_homepage-basic_nav-header-logo'


class HomePage(BasePageObject):
    def __init__(self, driver: webdriver, timeout: int = 10):
        super().__init__(driver, timeout, _HOME_PAGE_URL)
        self.__logo_locator = (By.CLASS_NAME, 'nav__logo-link')
        self.__search_job_locator = (By.PARTIAL_LINK_TEXT, 'Buscar un empleo')
        self.__find_person_locator = (By.PARTIAL_LINK_TEXT, 'Encontrar a personas que conoces')
        self.__learn_skill_locator = (By.PARTIAL_LINK_TEXT, 'Aprender una nueva aptitud')

    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.__logo_locator))

    def click_logo(self):
        logo = self.wait.until(EC.visibility_of_element_located(self.__logo_locator))
        logo.click()

    def search_for_a_job(self):
        link = self.wait.until(EC.visibility_of_element_located(self.__search_job_locator))
        link.click()
        return SearchJobPage(self.driver, self.timeout)

    def find_a_person(self):
        link = self.wait.until(EC.visibility_of_element_located(self.__find_person_locator))
        link.click()

    def learn_new_skills(self):
        link = self.wait.until(EC.visibility_of_element_located(self.__learn_skill_locator))
        link.click()

