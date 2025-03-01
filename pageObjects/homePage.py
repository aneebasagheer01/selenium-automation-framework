from selenium.webdriver.common.by import By

from base.baseDriver import BaseDriver
from pageObjects.dashboardPage import DashboardPage
from utilities.utils import Logger


class HomePage(BaseDriver):
    customLogger = Logger.sample_logger()
    input_username_xpath = (By.XPATH,"//input[contains(@placeholder,'name')]")# "//input[@placeholder='Username']")
    input_password_xpath = (By.XPATH, "//input[contains(@placeholder,'ssword')]")#"//input[@placeholder='Password']")
    button_login_xpath = (By.XPATH, "//button[normalize-space()='Login']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_username(self):
        return self.wait_for_element_to_be_visible(self.input_username_xpath)

    def get_password(self):
        return self.wait_for_element_to_be_visible(self.input_password_xpath)

    def get_login(self):
        return self.wait_for_element_to_be_clickable(self.button_login_xpath)

    def enter_username(self, user_name):
        element = self.get_username()
        if element:

            self.send_input(element, user_name)
            self.customLogger.info("***** User Name Sent *****")
        else:
            self.customLogger.error("**** Unable to send User Name *****")

    def enter_password(self, password):
        element = self.get_password()
        if element:
            self.send_input(element, password)
            self.customLogger.info("***** Password Sent *****")
        else:
            self.customLogger.error("***** Unable to send Password *****")
    def click_login_button(self):
        button = self.get_login()
        if button:
            self.click_element(button)
            self.customLogger.info("***** Login Button Clicked *****")
            dashboardPage=DashboardPage(self.driver)
            return dashboardPage
        else:
            self.customLogger.error("***** Unable to click Login Button *****")