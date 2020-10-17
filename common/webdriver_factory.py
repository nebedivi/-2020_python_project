import os
from selenium import webdriver

__COMMON_DIR = os.path.dirname(os.path.realpath(__file__))
__CHROME_PATH = os.path.join(__COMMON_DIR, 'chromedriver.exe')
__FIREFOX_PATH = os.path.join(__COMMON_DIR, 'geckodriver.exe')


def create_driver_instance(browser_name):
    if browser_name.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(executable_path=__CHROME_PATH, chrome_options=options)
    elif browser_name.lower() == 'firefox':
        firefox_driver = webdriver.Firefox(executable_path=__FIREFOX_PATH)
        firefox_driver.maximize_window()
        return firefox_driver
    else:
        raise ValueError('Invalid browser selected!')
