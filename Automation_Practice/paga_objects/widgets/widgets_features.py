import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from paga_objects.base import Base


class Widgets(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    accordian = (By.XPATH, "//span[normalize-space()='Accordian']")
    auto_complete = (By.XPATH, "//span[normalize-space()='Auto Complete']")
    date_picker = (By.XPATH, "//span[normalize-space()='Date Picker']")
    slider = (By.XPATH,"//span[normalize-space()='Slider']")
    progress_bar = (By.XPATH, "//span[normalize-space()='Progress Bar']")
    tabs = (By.XPATH, "//span[normalize-space()='Tabs']")
    tool_tip = (By.XPATH, "//span[normalize-space()='Tool Tips']")
    normalise_space = (By.XPATH, "//span[normalize-space()='Menu']")
    select_menu = (By.XPATH, "//span[normalize-space()='Select Menu']")
    accordian_1 = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/div[1]")
    accordian_2 = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]")
    accordian_3 = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[1]")
    input_1 = (By.XPATH, "//input[@id='autoCompleteMultipleInput']")
    input_2 = (By.XPATH, "//input[@id='autoCompleteSingleInput']")
    select_date = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    date_and_time = (By.XPATH, "//input[@id='datePickerMonthYearInput']")
    date_picker_1 = (By.XPATH, "//div[@class='react-datepicker__header']")
    calendar = (By.XPATH, "//div[@class='react-datepicker__month-container']")
    next_button = (By.XPATH, "//button[normalize-space()='Next Month']")
    previous_button = (By.XPATH, "//button[normalize-space()='Previous Month'")
    calendar_2 = (By.XPATH,"//div[@class='react-datepicker__month-container']")
    month_picker = (By.XPATH, "//div[@class='react-datepicker__header']")
    month = (By.XPATH, "//div[@class='react-datepicker__month-option react-datepicker__month-option--selected_month']")
    time_picker = (By.XPATH, "//div[@class='react-datepicker__time']")
    time = (By.XPATH, "//li[normalize-space()='22:00']")
    range = (By.XPATH, "//input[@type='range']")
    tool_tip_arrow = (By.XPATH, "//div[@class='range-slider__tooltip__arrow']")
    start_stop = (By.XPATH, "//button[@id='startStopButton']")
    tab_1 = (By.XPATH, "//a[@id='demo-tab-what']")
    tab_2 = (By.XPATH, "//a[@id='demo-tab-origin']")
    tab_3 = (By.XPATH, "//a[@id='demo-tab-use']")
    tab_4 = (By.XPATH, "//a[@id='demo-tab-more']")
    tool_tip_button = (By.XPATH, "//button[@id='toolTipButton']")
    text_field = (By.XPATH, "//input[@id='toolTipTextField']")
    contrary_button = (By.XPATH, "//a[normalize-space()='Contrary']")
    number = (By.XPATH, "//a[normalize-space()='1.10.32']")
    main_item_1 = (By.XPATH, "//a[normalize-space()='Main Item 1']")
    main_item_2 = (By.XPATH, "//a[normalize-space()='Main Item 2']")
    main_item_3 = (By.XPATH, "//a[normalize-space()='Main Item 3']")
    select_value = (By.XPATH, "//div[@id='withOptGroup']")
    select_option = (By.XPATH, "//div[contains(text(),'Select Option')]")
    select_title = (By.XPATH, "//div[contains(text(),'Select Title')]")
    old_select_menu = (By.XPATH, "//select[@id='oldSelectMenu']")
    multy_select = (By.XPATH, "//div[contains(text(),'Select...')]")
    select_cars = (By.XPATH, "//select[@id='cars']")
    volvo = (By.XPATH, "//option[@value='volvo']")
    saab = (By.XPATH, "//option[@value='saab']")
    opel = (By.XPATH, "//option[@value='opel']")
    audi = (By.XPATH, "//option[@value='audi']")

    def check_accordian(self):
        self.click_on_widgets()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(2)
        self.EF.find_element(self.accordian).click()
        time.sleep(2)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        self.EF.find_element(self.accordian_1).click()
        time.sleep(2)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        self.EF.find_element(self.accordian_2).click()
        time.sleep(2)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        self.EF.find_element(self.accordian_3).click()
        time.sleep(3)
        actions.scroll_by_amount(10,400).perform()
        time.sleep(2)
        self.EF.find_element(self.accordian_3).click()

    def check_auto_complete(self):
        self.click_on_widgets()
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(2)
        self.EF.find_element(self.auto_complete).click()
        time.sleep(2)
        actions.scroll_by_amount(10,200).perform()
        time.sleep(2)
        input_box = self.EF.find_element(self.input_1)
        input_box.send_keys("red")
        input_box.send_keys(Keys.ARROW_DOWN)
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)
        input_box.send_keys("blu")
        input_box.send_keys(Keys.ARROW_DOWN)
        input_box.send_keys(Keys.ENTER)
        time.sleep(3)
        input_box_2 = self.EF.find_element(self.input_2)
        input_box_2.send_keys("blu")
        time.sleep(2)
        suggestions = self.WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(By.CSS_SELECTOR, "auto-complete__single-value css-1uccc91-singleValue"))
        for suggestion in suggestions:
            if "Blue" in suggestion.text:
                suggestion.click()
                break





















