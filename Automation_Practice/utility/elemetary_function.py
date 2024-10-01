from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EleFunc():

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
                EC.element_to_be_clickable(locator))
            return element
        except:

            screenshot = self.driver.save_screenshot('./reports/screenshots/failed_cases/failed_test.png')
            return screenshot

    def find_elements(self, locator):
        try:
            elements = WebDriverWait(self.driver, timeout=10, poll_frequency=1).until(
                EC.visibility_of_all_elements_located(locator))
            return elements
        except:
            screenshot = self.driver.save_screenshot('./reports/screenshots/failed_cases/failed_test.png')
            return screenshot
