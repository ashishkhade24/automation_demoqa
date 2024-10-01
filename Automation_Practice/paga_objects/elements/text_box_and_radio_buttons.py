import time
from selenium.webdriver.common.by import By
from paga_objects.base import Base
from selenium.webdriver.common.action_chains import ActionChains

class Textbox_and_buttons(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    textbox=(By.XPATH,"//span[normalize-space()='Text Box']")
    full_name = (By.XPATH,"//input[@id='userName']")
    email = (By.XPATH,"//input[@id='userEmail']")
    current_add = (By.XPATH,"//textarea[@id='currentAddress']")
    permanent_add = (By.XPATH,"//textarea[@id='permanentAddress']")
    submit = (By.XPATH,"//button[@id='submit']")
    check_box=(By.XPATH,"//span[normalize-space()='Check Box']")
    expand_all=(By.XPATH,"//button[@title='Expand all']")
    home=(By.XPATH,"//label[@for='tree-node-home']//span[@class='rct-checkbox']")
    docs=(By.XPATH,"//label[@for='tree-node-documents']//span[@class='rct-checkbox']")
    radio_button=(By.XPATH,"//span[normalize-space()='Radio Button']")
    yes=(By.XPATH,"//label[normalize-space()='Yes']")
    impressive=(By.XPATH,"//label[normalize-space()='Impressive']")

    def text_box(self):
        self.click_on_elements()
        time.sleep(3)
        self.EF.find_element(self.textbox).click()
        time.sleep(2)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(3)
        self.EF.find_element(self.full_name).send_keys("Ashish Khade")
        time.sleep(3)
        self.EF.find_element(self.email).send_keys("ashishkhade11@gmail.com")
        time.sleep(3)
        self.EF.find_element(self.current_add).send_keys("Nanda Nagar Indore")
        time.sleep(3)
        self.EF.find_element(self.permanent_add).send_keys("Indira Gandhi Ward multai")
        time.sleep(3)
        self.EF.find_element(self.submit).click()

    def click_on_checkbox(self):
        self.click_on_elements()
        time.sleep(3)
        self.EF.find_element(self.check_box).click()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 400).perform()
        time.sleep(3)
        self.EF.find_element(self.expand_all).click()
        time.sleep(3)
        self.EF.find_element(self.home).click()
        time.sleep(3)
        self.EF.find_element(self.docs).click()
        time.sleep(3)

    def click_on_radio_buttons(self):
        self.click_on_elements()
        time.sleep(2)
        self.EF.find_element(self.radio_button).click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 500).perform()
        time.sleep(3)
        self.EF.find_element(self.yes).click()
        time.sleep(3)
        self.EF.find_element(self.impressive).click()
        time.sleep(3)



