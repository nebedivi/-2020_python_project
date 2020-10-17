from common.webdriver_factory import create_driver_instance
from page_objects.home_page import HomePage

driver = create_driver_instance('chrome')
home = HomePage(driver)
home.open()
home.wait_until_loaded()
home.click_logo()
home.wait_until_loaded()
job_page = home.search_for_a_job()
job_page.wait_until_loaded()
job_page.search('Software Engineer', 'Zapopan, Jalisco')
driver.quit()

