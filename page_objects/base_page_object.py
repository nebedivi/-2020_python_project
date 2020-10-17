from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePageObject:
    def __init__(self, driver: webdriver, timeout: int = 10, url: str = None):
        self.driver = driver
        self.timeout = timeout
        self.url = url
        self.wait = None
        self.set_timeout(timeout)

    def open(self):
        self.driver.get(self.url)

    def wait_until_loaded(self):
        raise NotImplemented

    def refresh(self):
        self.driver.refresh()

    def set_timeout(self, timeout: int):
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, self.timeout)
