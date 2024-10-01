import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from paga_objects.base import Base
import pyautogui


class PracticeForm(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    practice_form_button=(By.XPATH,"//span[normalize-space()='Practice Form']")
    first_name = (By.XPATH, "//input[@id='firstName']")
    last_name = (By.XPATH, "//input[@id='lastName']")
    email = (By.XPATH, "//input[@id='userEmail']")
    male = (By.XPATH, "//label[normalize-space()='Male']")
    female = (By.XPATH, "//label[normalize-space()='Female']")
    mobile_number = (By.XPATH, "//input[@id='userNumber']")
    DOB_input = (By.XPATH, "//input[@id='dateOfBirthInput']")
    date_picker = (By.XPATH, "//div[@class='react-datepicker__month-container']")
    next_month = (By.XPATH, "//button[normalize-space()='Next Month']")
    date = (By.XPATH, "//div[@aria-label='Choose Monday, September 23rd, 2024']")
    sports = (By.XPATH, "//label[normalize-space()='Sports']")
    reading = (By.XPATH, "//label[normalize-space()='Reading']")
    music = (By.XPATH, "//label[normalize-space()='Music']")
    select_picture = (By.XPATH, "//label[normalize-space()='Select picture']")
    current_address = (By.XPATH, "//textarea[@id='currentAddress']")
    select_state = (By.XPATH, "//div[contains(text(),'Select State')]")
    select_city = (By.XPATH, "//div[@id='city']")
    submit_button = (By.XPATH, "//button[@id='submit']")

    def practice_form(self):
        self.click_on_forms()
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 400).perform()
        time.sleep(1)
        self.EF.find_element(self.practice_form_button).click()
        actions.scroll_by_amount(10, 400).perform()
        time.sleep(2)
        self.EF.find_element(self.first_name).send_keys("Ashish")
        time.sleep(2)
        self.EF.find_element(self.last_name).send_keys("Khade")
        time.sleep(2)
        self.EF.find_element(self.email).send_keys("ashishkhade11@gmail.com")
        time.sleep(2)
        self.EF.find_element(self.female).click()
        time.sleep(2)
        self.EF.find_element(self.male).click()
        time.sleep(2)
        self.EF.find_element(self.mobile_number).send_keys("9893038093")
        time.sleep(2)
        self.EF.find_element(self.DOB_input).click()
        time.sleep(2)
        self.EF.find_element(self.date_picker)
        time.sleep(2)
        self.EF.find_element(self.date).click()
        time.sleep(2)
        self.EF.find_element(self.sports).click()
        time.sleep(2)
        self.EF.find_element(self.reading).click()
        time.sleep(2)
        self.EF.find_element(self.music).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(2)
        select_image=self.EF.find_element(self.select_picture)
        select_image.click()
        image_path = r'C:/home/mayank/Desktop/yellow-trouser.jpg'
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)
        self.EF.find_element(self.current_address).send_keys("Nanda Nagar Indore")
        time.sleep(3)
        self.EF.find_element(self.submit_button).click()



