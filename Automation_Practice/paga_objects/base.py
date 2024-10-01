from selenium.webdriver.common.by import By
from utility.elemetary_function import EleFunc
from selenium.webdriver.common.action_chains import ActionChains
import time


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.EF = EleFunc(self.driver)

    element = (By.XPATH, "//h5[normalize-space()='Elements']")
    forms = (By.XPATH, "//h5[normalize-space()='Forms']")
    alert_frame = (By.XPATH, "//h5[normalize-space()='Alerts, Frame & Windows']")
    widgets = (By.XPATH, "//h5[normalize-space()='Widgets']")

    def click_on_elements(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.element).click()

    def click_on_forms(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.forms).click()

    def click_on_alert_frame(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.alert_frame).click()

    def click_on_widgets(self):
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.widgets).click()

