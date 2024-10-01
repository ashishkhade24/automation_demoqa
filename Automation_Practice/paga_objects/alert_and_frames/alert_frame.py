import time

from paga_objects.base import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class AlarmFramesWindows(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    browser_window_button = (By.XPATH,"//span[normalize-space()='Browser Windows']")
    alert_button = (By.XPATH,"//span[normalize-space()='Alerts']")
    frames_button = (By.XPATH,"//span[normalize-space()='Frames']")
    nested_frame = (By.XPATH,"//span[normalize-space()='Nested Frames']")
    modal_button = (By.XPATH,"//span[normalize-space()='Modal Dialogs']")
    new_tab = (By.XPATH,"//button[@id='tabButton']")
    window_button = (By.XPATH,"//button[@id='windowButton']")
    new_window_msg = (By.XPATH,"//button[@id='messageWindowButton']")
    alert_click= (By.XPATH,"//button[@id='alertButton']")
    timer_alert = (By.XPATH,"//button[@id='timerAlertButton']")
    confirm_button = (By.XPATH,"//button[@id='confirmButton']")
    prompt_button = (By.XPATH,"//button[@id='promtButton']")
    iframe_1 = (By.XPATH, "//iframe[@id='frame1']")
    iframe_2 = (By.XPATH, "//iframe[@id='frame2']")
    sample_heading= (By.XPATH,"//h1[@id='sampleHeading']")
    child_frame_path = (By.XPATH,"//iframe[@srcdoc='<p>Child Iframe</p>']")
    parent_frame_path = (By.XPATH,"//iframe[@id='frame1']")
    small_modal = (By.XPATH,"//button[@id='showSmallModal']")
    large_modal = (By.XPATH,"//button[@id='showLargeModal']")
    close_button_1 = (By.XPATH,"//button[@id='closeSmallModal']")
    close_button_2 = (By.XPATH,"//button[@id='closeLargeModal']")

    def check_browser_windows(self):
        self.click_on_alert_frame()
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(3)
        self.EF.find_element(self.browser_window_button).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 300).perform()
        time.sleep(3)
        self.EF.find_element(self.new_tab).click()
        time.sleep(3)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(3)
        self.driver.switch_to.window(parent_handle)
        time.sleep(3)
        self.EF.find_element(self.window_button).click()
        time.sleep(3)
        parent_handle = self.driver.current_window_handle
        print(parent_handle)
        all_handles = self.driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_handle:
                self.driver.switch_to.window(handle)
                time.sleep(1)
        self.driver.maximize_window()
        time.sleep(2)
        self.driver.switch_to.window(parent_handle)
        time.sleep(3)
        self.EF.find_element(self.new_window_msg).click()
        time.sleep(2)
        self.driver.maximize_window()
        time.sleep(1)
        self.driver.back()

    def alerts_handle(self):
        self.click_on_alert_frame()
        time.sleep(2)
        action=ActionChains(self.driver)
        action.scroll_by_amount(10,600).perform()
        time.sleep(2)
        self.EF.find_element(self.alert_button).click()
        time.sleep(2)
        action.scroll_by_amount(10, 500).perform()
        time.sleep(2)
        self.EF.find_element(self.alert_click).click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        time.sleep(1)
        alert.accept()
        time.sleep(2)
        # alert.dismiss()
        self.EF.find_element(self.timer_alert).click()
        time.sleep(6)
        alert_2 = self.driver.switch_to.alert
        time.sleep(2)
        alert_2.accept()
        time.sleep(2)
        self.EF.find_element(self.confirm_button).click()
        time.sleep(2)
        alert_3 = self.driver.switch_to.alert
        time.sleep(2)
        # alert_3.accept()
        alert_3.dismiss()
        time.sleep(2)
        self.EF.find_element(self.prompt_button).click()
        time.sleep(2)
        alert_4 = self.driver.switch_to.alert
        time.sleep(2)
        alert_4.send_keys("Ashish Khade")
        time.sleep(2)
        alert_4.accept()

    def check_frames(self):
        self.click_on_alert_frame()
        time.sleep(1)
        actions=ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(2)
        self.EF.find_element(self.frames_button).click()
        time.sleep(2)
        actions.scroll_by_amount(10, 500).perform()
        time.sleep(2)
        frame_1 = self.EF.find_element(self.iframe_1)
        self.driver.switch_to.frame(frame_1)
        time.sleep(2)
        print("Frame one")
        actions.scroll_by_amount(10, 200).perform()
        time.sleep(2)
        frame_2 = self.EF.find_element(self.iframe_2)
        self.driver.switch_to.frame(frame_2)
        time.sleep(2)
        self.EF.find_element(self.sample_heading).click()
        time.sleep(2)
        print("frame_two")

    def check_nested_frames(self):
        self.click_on_alert_frame()
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10, 500).perform()
        time.sleep(2)
        self.EF.find_element(self.nested_frame).click()
        time.sleep(2)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        parent_frame = self.EF.find_element(self.parent_frame_path)
        self.driver.switch_to.frame(parent_frame)
        time.sleep(3)
        print("moved_to_parent_frame")
        child_frame = self.EF.find_element(self.child_frame_path)
        self.driver.switch_to.frame(child_frame)
        time.sleep(3)
        # actions.double_click(child_frame).perform()
        # time.sleep(2)
        print("child_frame")
        self.driver.switch_to.parent_frame()
        time.sleep(2)
        print("parent_frame")

    def check_modal_dialogs(self):
        self.click_on_alert_frame()
        time.sleep(2)
        actions = ActionChains(self.driver)
        actions.scroll_by_amount(10,500).perform()
        time.sleep(2)
        self.EF.find_element(self.modal_button).click()
        time.sleep(2)
        actions.scroll_by_amount(10,300).perform()
        time.sleep(2)
        self.EF.find_element(self.small_modal).click()
        time.sleep(2)
        self.EF.find_element(self.close_button_1).click()
        time.sleep(2)
        self.EF.find_element(self.large_modal).click()
        time.sleep(2)
        self.EF.find_element(self.close_button_2).click()




















