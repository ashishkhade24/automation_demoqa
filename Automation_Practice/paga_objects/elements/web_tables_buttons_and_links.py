import time
from selenium.webdriver.common.by import By
from paga_objects.base import Base
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

class Web_tables_and_links(Base):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

    web_tables=(By.XPATH,"//span[normalize-space()='Web Tables']")
    add_button=(By.XPATH,"//button[@id='addNewRecordButton']")
    first_name=(By.XPATH,"//input[@id='firstName']")
    last_name=(By.XPATH,"//input[@id='lastName']")
    email=(By.XPATH,"//input[@id='userEmail']")
    age=(By.XPATH,"//input[@id='age']")
    salary=(By.XPATH,"//input[@id='salary']")
    department=(By.XPATH,"//input[@id='department']")
    submit=(By.XPATH,"//button[@id='submit']")
    delete_button=(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[2]/*[name()='svg'][1]/*[name()='path'][1]")
    edit_button=(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/div[1]/div[2]/div[1]/div[1]/div[7]/div[1]/span[1]/*[name()='svg'][1]/*[name()='path'][1]")
    search_option=(By.XPATH,"//input[@id='searchBox']")
    buttons=(By.XPATH,"//span[normalize-space()='Buttons']")
    double_click=(By.XPATH,"//button[@id='doubleClickBtn']")
    right_click=(By.XPATH,"//button[@id='rightClickBtn']")
    click_me=(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[3]/button[1]")
    links=(By.XPATH,"//span[normalize-space()='Links']")
    home_link=(By.XPATH,"//a[@id='simpleLink']")
    home_fc=(By.XPATH,"//a[@id='dynamicLink']")
    created=(By.XPATH,"//a[@id='created']")
    no_content=(By.XPATH,"//a[@id='no-content']")
    moved=(By.XPATH,"//a[@id='moved']")
    bad_request=(By.XPATH,"//a[@id='bad-request']")
    unauthorized=(By.XPATH,"//a[@id='unauthorized']")
    forbidden=(By.XPATH,"//a[@id='forbidden']")
    not_found=(By.XPATH,"//a[@id='invalid-url']")
    broken_link_images=(By.XPATH,"//span[normalize-space()='Broken Links - Images']")
    valid_link=(By.XPATH,"//a[normalize-space()='Click Here for Valid Link']")
    broken_link=(By.XPATH,"//a[normalize-space()='Click Here for Broken Link']")
    download_upload_button=(By.XPATH,"//span[normalize-space()='Upload and Download']")
    download_button=(By.XPATH,"//a[@id='downloadButton']")
    select_file=(By.XPATH,"//label[normalize-space()='Select a file']")
    dynamic_properties=(By.XPATH,"//input[@id='uploadFile']")
    enable_button=(By.XPATH,"//button[@id='enableAfter']")
    change_color=(By.XPATH,"//button[@id='colorChange']")
    visible_after_5_sec=(By.XPATH,"//button[@id='visibleAfter']")

    def create_web_table(self):
        self.click_on_elements()
        time.sleep(3)
        self.EF.find_element(self.web_tables).click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.add_button).click()
        time.sleep(2)
        self.EF.find_element(self.first_name).send_keys("Ashish")
        self.EF.find_element(self.last_name).send_keys("Khade")
        self.EF.find_element(self.email).send_keys("ashishkhade11@gmail.com")
        self.EF.find_element(self.age).send_keys("29")
        self.EF.find_element(self.salary).send_keys("25000")
        self.EF.find_element(self.department).send_keys("Quality")
        self.EF.find_element(self.submit).click()

    def edit_web_tables(self):
        self.click_on_elements()
        time.sleep(3)
        self.EF.find_element(self.web_tables).click()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.edit_button).click()
        time.sleep(3)
        edit_first_name=self.EF.find_element(self.first_name)
        edit_first_name.send_keys(Keys.BACKSPACE*10)
        edit_first_name.send_keys("King")
        edit_last_name=self.EF.find_element(self.last_name)
        edit_last_name.send_keys(Keys.BACKSPACE*10)
        edit_last_name.send_keys("Vishnu")
        edit_email=self.EF.find_element(self.email)
        edit_email.send_keys(Keys.BACKSPACE*20)
        edit_email.send_keys("ashu123@gmai.com")
        edit_age=self.EF.find_element(self.age)
        edit_age.send_keys(Keys.BACKSPACE*5)
        edit_age.send_keys("28")
        self.EF.find_element(self.submit).click()

    def delete_user(self):
        self.click_on_elements()
        time.sleep(3)
        self.EF.find_element(self.web_tables).click()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.search_option).send_keys("Kie")
        time.sleep(3)
        self.EF.find_element(self.delete_button).click()

    def click_on_buttons(self):
        self.click_on_elements()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.buttons).click()
        actions.scroll_by_amount(10, 400).perform()
        time.sleep(3)
        double_click_button=self.EF.find_element(self.double_click)
        actions.double_click(double_click_button).perform()
        time.sleep(1)
        right_click_button=self.EF.find_element(self.right_click)
        actions.context_click(right_click_button).perform()
        time.sleep(1)
        self.EF.find_element(self.click_me).click()

    def click_on_links(self):
        self.click_on_elements()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(3)
        self.EF.find_element(self.links).click()
        time.sleep(3)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        current_window = self.driver.current_window_handle
        self.EF.find_element(self.home_link).click()
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(current_window)
        time.sleep(1)
        self.EF.find_element(self.home_fc).click()
        new_window = [window for window in self.driver.window_handles if window != current_window][0]
        self.driver.switch_to.window(new_window)
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(current_window)
        time.sleep(1)
        self.EF.find_element(self.created).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 100).perform()
        time.sleep(3)
        self.EF.find_element(self.no_content).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 100).perform()
        time.sleep(3)
        self.EF.find_element(self.moved).click()
        time.sleep(2)
        self.EF.find_element(self.bad_request).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 100).perform()
        time.sleep(3)
        self.EF.find_element(self.unauthorized).click()
        time.sleep(2)
        self.EF.find_element(self.forbidden).click()
        time.sleep(2)
        self.EF.find_element(self.not_found).click()

    def click_on_broken_links(self):
        self.click_on_elements()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.broken_link_images).click()
        time.sleep(3)
        actions.scroll_by_amount(10, 500).perform()
        time.sleep(3)
        self.EF.find_element(self.valid_link).click()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        actions.scroll_by_amount(10, 500).perform()
        time.sleep(3)
        self.EF.find_element(self.broken_link).click()
        time.sleep(1)
        self.driver.back()

    def check_download_upload(self):
        self.click_on_elements()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.download_upload_button).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 400).perform()
        time.sleep(3)
        self.EF.find_element(self.download_button).click()
        time.sleep(2)
        upload_file=self.EF.find_element(self.select_file)
        upload_file.click()
        time.sleep(3)
        image_path = r'C:/home/mayank/Desktop/yellow-trouser.jpg'
        pyautogui.write(image_path)
        pyautogui.press('enter')
        time.sleep(3)































